# Generated by Django 5.0.7 on 2024-07-20 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_schedule_pro_gofer'),
    ]

    operations = [
        migrations.AddField(
            model_name='errandboy',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='gofer',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
