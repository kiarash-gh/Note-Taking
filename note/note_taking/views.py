from django.shortcuts import render, redirect,get_object_or_404
from django.http import FileResponse, Http404
from reportlab.pdfgen import canvas
from django.template import RequestContext
from io import BytesIO
from .models import Note, NoteType
from .forms import NoteForm,NoteTypeForm
from note import renderers


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
    context= {'form': form, 'note': note}
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


def generate_pdf(request, pk):
    note = get_object_or_404(Note, id=pk)
    context = {
        "note": note
    }
    response = renderers.render_to_pdf("pdf/note_pdf.html", context)
    if response.status_code == 404:
        raise HTTP404("Note not found")

    filename = f"{note.title}.pdf"
    """
    Tell browser to view inline (default)
    """
    content = f"inline; filename={filename}"
    download = request.GET.get("download")
    if download:
        """
        Tells browser to initiate download
        """
        content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response



# list, create, edit and delete Note Types
def note_type_list(request):
    note_types = NoteType.objects.all()
    context ={'note_types': note_types}
    return render(request, 'note_taking/note_type_list.html', context)


def create_note_type(request):
    form = NoteTypeForm()
    if request.method == 'POST':
        form = NoteTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-type-list')
        
    context = {'form': form}

    return render(request, 'note_taking/create_note_type.html', context)



def note_type_detail(request, pk):
    note_type = get_object_or_404(NoteType, id=pk)
    form = NoteTypeForm(instance=note_type)
    context= {'form': form, 'note_type': note_type}
    return render(request, 'note_taking/note_type_detail.html', context)


def update_note_type(request, pk):
    note_type = get_object_or_404(NoteType, id=pk)
    form = NoteTypeForm(instance=note_type)  
    if request.method == 'POST':
        form = NoteTypeForm(request.POST, instance=note_type)
        if form.is_valid():
            form.save()
            return redirect('note-type-list')
    context= {'form': form}
    return render(request, 'note_taking/edit_note_type.html', context)


def delete_note_type(request, pk):
    note_type = get_object_or_404(NoteType, id=pk)
    context = {'obj': note_type.name}
    if request.method == 'POST':        
        note_type.delete()
        return redirect('note-type-list')
    
    return render(request, 'note_taking/delete.html', context)

