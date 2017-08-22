from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response

import serializers as CoreSerializers


class SessionViewSet(viewsets.GenericViewSet):

    queryset = User.objects.none()
    serializer_class = CoreSerializers.SessionSerializer

    def list(self, request):

        serializer = CoreSerializers.SessionSerializer(data=dict(), context=self.get_serializer_context())
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
