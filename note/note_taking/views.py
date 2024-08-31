from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.
def home(request):
    context = {}
    return render(request, 'note_taking/home.html', context)


def note_list(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'note_taking/note_list.html', context)


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-list')  
    else:
        form = NoteForm()
    
    context = {'form': form}
    return render(request, 'note_taking/create_note.html', context)
