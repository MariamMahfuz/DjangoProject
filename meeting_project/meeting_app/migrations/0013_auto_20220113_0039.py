# Generated by Django 3.2.8 on 2022-01-12 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_app', '0012_statename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statename',
            old_name='State',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='employeeform',
            name='state',
        ),
    ]