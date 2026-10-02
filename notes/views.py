"""Views handling the create, read, update and delete (CRUD) actions."""
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """Display a list of all notes.

    :param request: HTTP request object.
    :return: rendered note list page.
    """
    # READ: get every note and send them to the template
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_detail(request, pk):
    """Display a single note.

    :param request: HTTP request object.
    :param pk: primary key (id) of the note.
    :return: rendered note detail page, or a 404 if the note is missing.
    """
    # READ: get one note by its id, 404 page if it doesn't exist
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request):
    """Show a blank form and save a new note when it is submitted.

    :param request: HTTP request object.
    :return: the form page, or a redirect to the list after saving.
    """
    # CREATE: POST means the form was submitted, otherwise show a blank form
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    """Show a form filled with the note and save the changes.

    :param request: HTTP request object.
    :param pk: primary key (id) of the note to edit.
    :return: the form page, or a redirect to the list after saving.
    """
    # UPDATE: same as create but instance=note fills in the old values
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    """Ask the user to confirm, then delete the note.

    :param request: HTTP request object.
    :param pk: primary key (id) of the note to delete.
    :return: the confirmation page, or a redirect to the list after deleting.
    """
    note = get_object_or_404(Note, pk=pk)
    # DELETE: only delete once the confirmation form is submitted (POST)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
