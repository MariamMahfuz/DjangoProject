# Generated by Django 3.2.8 on 2021-12-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_app', '0008_auto_20211203_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='up_events',
            name='heading',
        ),
        migrations.AddField(
            model_name='meeting',
            name='place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]