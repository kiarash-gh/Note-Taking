from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200)
    note_type = models.ForeignKey('NoteType', on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(User)
    note = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} - {self.created}'



class NoteType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name