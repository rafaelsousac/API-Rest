# Generated by Django 5.0.1 on 2024-01-23 02:04

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=150)),
                ('event_type', models.CharField(choices=[('atividade física', 'Atividade Física'), ('festa', 'Festa'), ('horário livre', 'Horário Livre'), ('hackathon', 'Hackathon'), ('lazer', 'Lazer'), ('reunião', 'Reunião')], max_length=20)),
                ('start_time', models.DateTimeField(default=datetime.datetime.today)),
                ('end_time', models.DateTimeField(default=datetime.datetime.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event',
                'ordering': ['start_time'],
            },
        ),
    ]