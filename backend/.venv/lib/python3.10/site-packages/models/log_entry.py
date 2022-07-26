from django.db import models


class LogEntry(models.Model):

    def __str__(self):
        return f'{self.timestamp.isoformat()} - {self.log_text}'

    timestamp = models.DateTimeField(auto_now=True)
    game = models.ForeignKey('Game', on_delete=models.RESTRICT)
    log_text = models.CharField(max_length=200)

