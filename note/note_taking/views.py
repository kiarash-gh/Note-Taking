from django.shortcuts import render, redirect,get_object_or_404
from django.template import RequestContext
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


def note_detail(request, pk):
    note = get_object_or_404(Note, id=pk)
    form = NoteForm(instance=note)
    context= {'form': form}
    return render(request, 'note_taking/note_detail.html', context)


def update_note(request, pk):
    note = get_object_or_404(Note, id=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note-list')
    else:
        form = NoteForm(instance=note)  

    context= {'form': form}
    return render(request, 'note_taking/edit_note.html', context)


def delete_note(request, pk):
    note = get_object_or_404(Note, id=pk)
    context = {'obj': note.title}
    if request.method == 'POST':        
        note.delete()
        return redirect('note-list')
    
    return render(request, 'note_taking/delete.html', context)
