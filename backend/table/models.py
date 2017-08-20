# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import models

from channels import Group


# Create your models here.
class Table(models.Model):

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    # class Meta:

    def __unicode__(self):
        return self.name

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("table-%s" % self.id)

    def send_message(self, message, user):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message, 'username': user.username}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )