from channels import route

import consumers as TableConsumers



websocket_routing = [
    route("websocket.connect", TableConsumers.ws_connect),
    route("websocket.receive", TableConsumers.ws_receive),
    route("websocket.disconnect", TableConsumers.ws_disconnect),
]

# You can have as many lists here as you like, and choose any name.
# Just refer to the individual names in the include() function.
custom_routing = [
    route("table.receive", TableConsumers.chat_join, command="^join$"),
    route("table.receive", TableConsumers.chat_leave, command="^leave$"),
    route("table.receive", TableConsumers.chat_send, command="^send$"),
]