# Generated by Django 3.2.8 on 2021-12-03 10:38

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_app', '0005_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='heading',
            name='meeting_detail_heading',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', froala_editor.fields.FroalaField()),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('booking_number', models.CharField(blank=True, max_length=30)),
                ('media', models.CharField(blank=True, max_length=30)),
                ('heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting_app.up_events')),
            ],
        ),
    ]
