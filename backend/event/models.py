from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    choice_event = (
        ('atividade física', 'Atividade Física'),
        ('festa', 'Festa'),
        ('horário livre', 'Horário Livre'),
        ('hackathon', 'Hackathon'),
        ('lazer', 'Lazer'),
        ('reunião', 'Reunião')
    )

    id = models.AutoField(auto_created=True, primary_key=True)
    description = models.CharField(max_length=150)
    event_type = models.CharField(max_length=20, choices=choice_event)
    start_time = models.DateTimeField(default=datetime.today)
    end_time = models.DateTimeField(default=datetime.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'
        ordering = ['start_time']

    def __str__(self):
        return self.description