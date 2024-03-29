# Generated by Django 4.0.5 on 2022-07-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_hand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit', models.IntegerField(choices=[(1, 'Diamonds'), (2, 'Clubs'), (3, 'Hearts'), (4, 'Spades')])),
                ('value', models.IntegerField(choices=[(1, 'Ace'), (2, 'King'), (3, 'Queen'), (4, 'Jack'), (5, 'Ten'), (6, 'Nine')])),
            ],
        ),
    ]
