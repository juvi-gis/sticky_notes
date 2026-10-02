# Sticky Notes

A simple Django web app for keeping sticky notes. You can create, view, edit
and delete notes. Deleting asks for confirmation first so a note is not
removed by accident.

## Features

- View all notes on the home page
- View a single note
- Add a new note (title and content)
- Edit an existing note
- Delete a note, with a confirmation step

## Built with

- Python 3
- Django (see `requirements.txt` for the version)
- SQLite (Django's default database)

## Project structure

```
sticky_notes/
├── manage.py
├── requirements.txt
├── README.md
├── docs/                  # use case, sequence and class diagrams
├── sticky_notes/          # project settings and main urls.py
└── notes/                 # the app
    ├── models.py          # Note model
    ├── forms.py           # NoteForm
    ├── views.py           # CRUD views
    ├── urls.py            # url patterns
    ├── tests.py           # unit tests
    ├── templates/         # base.html and the note pages
    └── static/notes/      # styles.css
```

## How to run it

1. Open a terminal in the project folder (the one with `manage.py`).
2. Create and activate a virtual environment:

   ```bash
   py -m venv venv
   venv\Scripts\activate          # Windows
   source venv/bin/activate       # macOS / Linux
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create the database tables:

   ```bash
   python manage.py migrate
   ```

5. Collect the static files (CSS):

   ```bash
   python manage.py collectstatic
   ```

6. Start the development server and open http://127.0.0.1:8000/ :

   ```bash
   python manage.py runserver
   ```

## Running the tests

```bash
python manage.py test
```

## Design diagrams

The use case, sequence and class diagrams are in the `docs/` folder.
