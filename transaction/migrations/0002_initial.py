# Generated by Django 5.0.6 on 2024-07-06 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_initial'),
        ('transaction', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='custom_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_recipient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='message_poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='main.messageposter'),
        ),
        migrations.AddField(
            model_name='booking',
            name='pro_gofer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='user.progofer'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='pro_gofer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='user.progofer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='transaction.schedule'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='custom_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='transaction.wallet'),
        ),
    ]
