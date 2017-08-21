from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

import serializers as CoreSerializers


class SessionViewSet(viewsets.ViewSet):

    queryset = User.objects.none()

    def list(self, request):

        serializer = CoreSerializers.SessionSerializer(request)
        return Response(serializer.data)
