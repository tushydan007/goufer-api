# Generated by Django 5.0.6 on 2024-07-16 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_initial'),
        ('user', '0004_messageposter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='message_poster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_rooms', to='user.messageposter'),
        ),
    ]
