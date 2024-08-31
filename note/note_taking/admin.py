from django.contrib import admin
from .models import Note, NoteType


admin.site.register(Note)
admin.site.register(NoteType)
