from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

class SessionSerializer(serializers.Serializer):

    user = serializers.SerializerMethodField()

    class Meta:
        fields = ('user')

    def get_user(self, obj):
        user = self.context['request'].user
        if user.pk is None:
            return None
        return UserSerializer(user, required=False).data