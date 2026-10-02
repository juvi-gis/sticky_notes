"""Admin site setup for the notes app."""
from django.contrib import admin

from .models import Note

# so I can add notes from /admin
admin.site.register(Note)
