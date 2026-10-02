"""Unit tests for the sticky notes app."""
from django.test import TestCase
from django.urls import reverse

from .forms import NoteForm
from .models import Note


class NoteModelTests(TestCase):
    """Tests for the Note model."""

    def test_str_returns_title(self):
        """The string form of a note is its title."""
        note = Note.objects.create(title='Shopping', content='Milk')
        self.assertEqual(str(note), 'Shopping')

    def test_created_at_is_set_automatically(self):
        """A new note gets a created_at date without it being given."""
        note = Note.objects.create(title='Shopping', content='Milk')
        self.assertIsNotNone(note.created_at)


class NoteFormTests(TestCase):
    """Tests for the NoteForm validation."""

    def test_form_is_valid_with_title_and_content(self):
        """The form accepts a title and content."""
        form = NoteForm(data={'title': 'Idea', 'content': 'Learn Django'})
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_title(self):
        """The form rejects an empty title."""
        form = NoteForm(data={'title': '', 'content': 'Learn Django'})
        self.assertFalse(form.is_valid())

    def test_form_is_invalid_without_content(self):
        """The form rejects empty content."""
        form = NoteForm(data={'title': 'Idea', 'content': ''})
        self.assertFalse(form.is_valid())


class NoteViewTests(TestCase):
    """Tests for the CRUD views."""

    def setUp(self):
        """Create one note for the tests that need an existing note."""
        self.note = Note.objects.create(title='Test note', content='Body')

    # READ
    def test_list_page_shows_notes(self):
        """The list page loads and shows the saved notes."""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test note')

    def test_detail_page_shows_note(self):
        """The detail page loads and shows the note content."""
        response = self.client.get(
            reverse('note_detail', kwargs={'pk': self.note.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Body')

    def test_detail_page_returns_404_for_missing_note(self):
        """Asking for a note that does not exist gives a 404."""
        response = self.client.get(reverse('note_detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)

    # CREATE
    def test_create_page_loads(self):
        """The create page loads with a blank form."""
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_adds_note_and_redirects(self):
        """A valid form saves a new note and goes back to the list."""
        response = self.client.post(
            reverse('note_create'),
            {'title': 'New note', 'content': 'New body'},
        )
        self.assertRedirects(response, reverse('note_list'))
        self.assertTrue(Note.objects.filter(title='New note').exists())

    def test_create_with_empty_title_does_not_save(self):
        """An empty title keeps the user on the form and saves nothing."""
        response = self.client.post(
            reverse('note_create'), {'title': '', 'content': 'No title'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), 1)

    # UPDATE
    def test_edit_page_is_filled_with_existing_note(self):
        """The edit page shows the current values of the note."""
        response = self.client.get(
            reverse('note_update', kwargs={'pk': self.note.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test note')

    def test_edit_changes_the_note(self):
        """A valid edit changes the note and goes back to the list."""
        response = self.client.post(
            reverse('note_update', kwargs={'pk': self.note.pk}),
            {'title': 'Changed', 'content': 'Changed body'},
        )
        self.assertRedirects(response, reverse('note_list'))
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Changed')
        self.assertEqual(self.note.content, 'Changed body')

    # DELETE
    def test_delete_page_asks_for_confirmation(self):
        """Opening the delete page shows a confirmation and keeps the note."""
        response = self.client.get(
            reverse('note_delete', kwargs={'pk': self.note.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure')
        self.assertEqual(Note.objects.count(), 1)

    def test_delete_removes_note_after_confirmation(self):
        """Confirming the delete removes the note and goes to the list."""
        response = self.client.post(
            reverse('note_delete', kwargs={'pk': self.note.pk})
        )
        self.assertRedirects(response, reverse('note_list'))
        self.assertEqual(Note.objects.count(), 0)

    def test_delete_returns_404_for_missing_note(self):
        """Deleting a note that does not exist gives a 404."""
        response = self.client.get(reverse('note_delete', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)


class NoteEmptyListTests(TestCase):
    """Tests for the list page when there are no notes."""

    def test_list_page_works_with_no_notes(self):
        """The list page still loads when the database is empty."""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notes']), 0)
