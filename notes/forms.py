"""Forms for creating and editing notes."""
from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating Note objects."""

    class Meta:
        """Tell the form which model and fields to use."""

        model = Note
        fields = ['title', 'content']
