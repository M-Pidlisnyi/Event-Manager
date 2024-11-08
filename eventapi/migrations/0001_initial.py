# Generated by Django 5.1.3 on 2024-11-07 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', models.CharField(choices=[('PHYSICAL', 'Physical'), ('ONLINE', 'Online')], default='PHYSICAL', max_length=20)),
                ('address', models.CharField(blank=True, help_text='Address for physical locations', max_length=255, null=True)),
                ('url', models.URLField(blank=True, help_text='URL for online events', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organizer_type', models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('ORGANIZATION', 'Organization')], max_length=20, verbose_name='Organizer type')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapi.location')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapi.organizer')),
            ],
        ),
    ]
