import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import html
import genanki
import random
import os


def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if not file_path:
        print("No file selected.")
        return None
    return file_path


def get_note_details(element_type, content):
    if content is None:
        return None

    if element_type == 'Topic':
        question = content.find('Question')
        fields = [html.unescape(question.text)
                  if question is not None else '', '']
    elif element_type == 'Item':
        question = content.find('Question')
        answer = content.find('Answer')
        fields = [
            html.unescape(question.text) if question is not None else '',
            html.unescape(answer.text) if answer is not None else ''
        ]
    return fields


def create_deck(deck_name):
    return genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        deck_name
    )


def import_to_anki(file_path):
    if not file_path:
        return

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    my_model = genanki.Model(
        random.randrange(1 << 30, 1 << 31),
        'SM Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    decks = {}

    for element in root.findall('.//SuperMemoElement'):
        element_type = element.find('Type').text
        deck_name = get_parent_concept_deck_name(element)
        content = element.find(
            './/Content') if element_type in ['Topic', 'Item'] else None

        if content:
            deck_full_name = "SM::" + deck_name
            if deck_full_name not in decks:
                decks[deck_full_name] = create_deck(deck_full_name)
            deck = decks[deck_full_name]

            fields = get_note_details(element_type, content)
            if fields is None:
                continue

            note = genanki.Note(model=my_model, fields=fields)
            deck.add_note(note)

    output_file = 'output.apkg'
    package = genanki.Package(decks.values())
    package.write_to_file(output_file)
    print(f"APKG file created: {os.path.abspath(output_file)}")


def get_parent_concept_deck_name(element):
    names = []
    while element is not None:
        if element.find('.//Type').text == 'Concept':
            names.insert(0, html.unescape(element.find('.//Title').text))
        element = element.find('..')
    return "::".join(names)


def main():
    file_path = select_file()
    import_to_anki(file_path)


if __name__ == "__main__":
    main()
