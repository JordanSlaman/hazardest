import json

from channels import Channel
from channels.auth import channel_session_user_from_http, channel_session_user

from .models import Table
from .utils import get_table_or_error, catch_client_error
from .exceptions import ClientError


@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    message.channel_session['tables'] = []

@channel_session_user
def ws_disconnect(message):
    # Unsubscribe from any connected rooms
    for slug in message.channel_session.get("tables", set()):
        try:
            table = Table.objects.get(slug=slug)
            # Removes us from the room's send group. If this doesn't get run,
            # we'll get removed once our first reply message expires.
            table.websocket_group.discard(message.reply_channel)
        except Table.DoesNotExist:
            pass

# Unpacks the JSON in the received WebSocket frame and puts it onto a channel
# of its own with a few attributes extra so we can route it
# This doesn't need @channel_session_user as the next consumer will have that,
# and we preserve message.reply_channel (which that's based on)
def ws_receive(message):
    # All WebSocket frames have either a text or binary payload; we decode the
    # text part here assuming it's JSON.
    # You could easily build up a basic framework that did this encoding/decoding
    # for you as well as handling common errors.
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("chat.receive").send(payload)



# Channel_session_user loads the user out from the channel session and presents
# it as message.user. There's also a http_session_user if you want to do this on
# a low-level HTTP handler, or just channel_session if all you want is the
# message.channel_session object without the auth fetching overhead.
@channel_session_user
@catch_client_error
def chat_join(message):
    # Find the room they requested (by ID) and add ourselves to the send group
    # Note that, because of channel_session_user, we have a message.user
    # object that works just like request.user would. Security!
    table = get_table_or_error(message["table"], message.user)

    # Send a "enter message" to the room if available
    # if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
    #     room.send_message(None, message.user, MSG_TYPE_ENTER)

    # OK, add them in. The websocket_group is what we'll send messages
    # to so that everyone in the chat room gets them.
    table.websocket_group.add(message.reply_channel)
    message.channel_session['tables'] = list(set(message.channel_session['tables']).union([table.id]))
    # Send a message back that will prompt them to open the room
    # Done server-side so that we could, for example, make people
    # join rooms automatically.
    message.reply_channel.send({
        "text": json.dumps({
            "join": str(table.id),
            "title": table.name,
        }),
    })


@channel_session_user
@catch_client_error
def chat_leave(message):
    # Reverse of join - remove them from everything.
    table = get_table_or_error(message["table"], message.user)

    # Send a "leave message" to the table if available
    # if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
    #     table.send_message(None, message.user, MSG_TYPE_LEAVE)

    table.websocket_group.discard(message.reply_channel)
    message.channel_session['tables'] = list(set(message.channel_session['tables']).difference([table.id]))
    # Send a message back that will prompt them to close the table
    message.reply_channel.send({
        "text": json.dumps({
            "leave": str(table.id),
        }),
    })


@channel_session_user
@catch_client_error
def chat_send(message):
    if int(message['table']) not in message.channel_session['tables']:
        raise ClientError("ROOM_ACCESS_DENIED")
    table = get_table_or_error(message["table"], message.user)
    table.send_message(message["message"], message.user)