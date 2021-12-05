# Generated by Django 3.2.8 on 2021-12-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_app', '0007_meeting_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='media',
        ),
        migrations.AddField(
            model_name='meeting',
            name='behance',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='facebook',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='linkedin',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='twitter',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
