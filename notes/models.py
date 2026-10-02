"""Database models for the sticky notes app."""
from django.db import models


class Note(models.Model):
    """A single sticky note.

    :param title: short heading for the note.
    :param content: the main text of the note.
    :param created_at: date and time the note was first saved.
    """

    # short heading for the note
    title = models.CharField(max_length=100)
    # the main text, TextField because it can be long
    content = models.TextField()
    # filled in automatically when the note is first saved
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the note title as its string representation."""
        return self.title
