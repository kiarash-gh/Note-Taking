from django import forms
from .models import Note, NoteType
    
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"


class NoteTypeForm(forms.ModelForm):
    class Meta:
        model = NoteType
        fields = "__all__"