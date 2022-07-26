from rest_framework import serializers

from ..models.log_entry import LogEntry


class GameLogSerializer(serializers.HyperlinkedModelSerializer):

    log_text = serializers.CharField(max_length=200, read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)

    class Meta:
        model = LogEntry
        fields = ['timestamp', 'log_text']

# latest_question_list = Question.objects.order_by('-pub_date')[:5]