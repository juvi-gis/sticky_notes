# Sticky Notes Design Diagrams

Mermaid source. Paste each block (without the backticks) into
https://mermaid.live and export a PNG.

## Use case diagram

```mermaid
flowchart LR
    user([User])
    subgraph Sticky Notes App
        uc1(View all notes)
        uc2(View a single note)
        uc3(Create a note)
        uc4(Edit a note)
        uc5(Delete a note)
        uc6(Confirm deletion)
    end
    user --- uc1
    user --- uc2
    user --- uc3
    user --- uc4
    user --- uc5
    uc5 -.->|includes| uc6
```

## Sequence diagram (all CRUD use cases)

```mermaid
sequenceDiagram
    actor User
    participant Browser
    participant Views as views.py
    participant DB as Database

    rect rgb(235, 245, 255)
    Note over User,DB: READ - view notes
    User->>Browser: Open home page
    Browser->>Views: GET /
    Views->>DB: Get all notes
    DB-->>Views: Notes
    Views-->>Browser: Show note list
    User->>Browser: Click a note
    Browser->>Views: GET /note/pk/
    Views->>DB: Get one note
    DB-->>Views: Note
    Views-->>Browser: Show note detail
    end

    rect rgb(235, 255, 240)
    Note over User,DB: CREATE - add a note
    User->>Browser: Click Add note
    Browser->>Views: GET /note/new/
    Views-->>Browser: Show blank form
    User->>Browser: Fill in form and submit
    Browser->>Views: POST /note/new/
    Views->>DB: Save new note
    Views-->>Browser: Redirect to note list
    end

    rect rgb(255, 250, 230)
    Note over User,DB: UPDATE - edit a note
    User->>Browser: Click Edit note
    Browser->>Views: GET /note/pk/edit/
    Views->>DB: Get the note
    Views-->>Browser: Show form with old values
    User->>Browser: Change text and submit
    Browser->>Views: POST /note/pk/edit/
    Views->>DB: Save changes
    Views-->>Browser: Redirect to note list
    end

    rect rgb(255, 238, 238)
    Note over User,DB: DELETE - remove a note
    User->>Browser: Click Delete note
    Browser->>Views: GET /note/pk/delete/
    Views-->>Browser: Show confirmation page
    alt user confirms
        User->>Browser: Click Yes, delete
        Browser->>Views: POST /note/pk/delete/
        Views->>DB: Delete note
        Views-->>Browser: Redirect to note list
    else user cancels
        User->>Browser: Click Cancel
        Browser->>Views: GET /note/pk/
        Views-->>Browser: Show note detail
    end
    end
```

## Class diagram

```mermaid
classDiagram
    class Model {
        <<Django base class>>
    }
    class ModelForm {
        <<Django base class>>
    }
    class Note {
        +id: int
        +title: str
        +content: str
        +created_at: datetime
        +__str__() str
    }
    class NoteForm {
        +is_valid() bool
        +save() Note
    }
    Model <|-- Note
    ModelForm <|-- NoteForm
    NoteForm --> Note : creates and updates
```
