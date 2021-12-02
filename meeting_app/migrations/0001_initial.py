# Generated by Django 3.2.8 on 2021-11-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='card')),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cover')),
                ('address', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=200)),
                ('Success_percent', models.IntegerField(blank=True, null=True)),
                ('Succesed', models.CharField(max_length=30)),
                ('Member_Number', models.IntegerField(blank=True, null=True)),
                ('Member', models.CharField(max_length=30)),
                ('Mentor_number', models.IntegerField(blank=True, null=True)),
                ('Mentor', models.CharField(max_length=30)),
                ('Award_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='card')),
                ('heading', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Upcoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=80)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='card')),
                ('heading_tag', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]