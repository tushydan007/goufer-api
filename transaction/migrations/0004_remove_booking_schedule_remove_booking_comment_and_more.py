# Generated by Django 5.0.6 on 2024-07-17 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_booking_message_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
