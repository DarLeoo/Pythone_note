import json
import os


notes_file = 'notes.json'


def load_notes():
    if not os.path.exists(notes_file):
        return {}
    with open(notes_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_notes(notes):
    with open(notes_file, 'w', encoding='utf-8') as f:
        json.dump(notes, f)