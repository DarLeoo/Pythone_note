import datetime

from file_operation import load_notes, save_notes


def create_note():
    notes = load_notes()
    note_id = int(str(max(notes.keys()))) + 1
    title = input('Enter note title: ')
    body = input('Enter note body: ')
    date = str(datetime.datetime.now())
    notes[note_id] = {'title': title, 'body': body, 'date': date}
    save_notes(notes)
    print(f'Note created with id: {note_id}')


def read_note():
    notes = load_notes()
    note_id = input('Enter note id: ')
    note = notes.get(note_id)
    if note:
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Date: {note['date']}")
    else:
        print('Note not found')


def update_note():
    notes = load_notes()
    note_id = input('Enter note id: ')
    note = notes.get(note_id)
    if note:
        title = input(f"Enter new title ({note['title']}): ")
        body = input(f"Enter new body ({note['body']}): ")
        date = str(datetime.datetime.now())
        notes[note_id] = {'title': title or note['title'], 'body': body or note['body'], 'date': date}
        save_notes(notes)
        print(f'Note {note_id} updated')
    else:
        print('Note not found')


def delete_note():
    notes = load_notes()
    note_id = input('Enter note id: ')
    note = notes.get(note_id)
    if note:
        del notes[note_id]
        save_notes(notes)
        print(f'Note {note_id} deleted')
    else:
        print('Note not found')


def list_notes():
    notes = load_notes()
    if notes:
        print('ID\tTitle\t\tDate')
        print('--\t-----\t\t----')
        for note_id, note in notes.items():
            print(f"{note_id}\t{note['title']}\t{note['date']}")
    else:
        print('No notes found')