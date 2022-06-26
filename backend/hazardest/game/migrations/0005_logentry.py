# Generated by Django 4.0.5 on 2022-06-23 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_rename_tricks_played_game_hands_played'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('log_text', models.CharField(max_length=200)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='game.game')),
            ],
        ),
    ]
