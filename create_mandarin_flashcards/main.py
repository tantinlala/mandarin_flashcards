from . import genanki_helpers
from .mandarin_assistant import MandarinAssistant
import argparse

def main():

    # Parse arguments
    parser = argparse.ArgumentParser(description='Generate Anki flashcards using OpenAI')

    # Get the provided text file
    parser.add_argument('text_file', type=str, help='The text file to convert to flashcards')

    # Parse arguments
    args = parser.parse_args()

    # Get the text from the file
    with open(args.text_file, 'r') as file:
        text = file.read()

    mandarin_assistant = MandarinAssistant()
    flashcards_json = mandarin_assistant.convert_to_flashcards(text)

    # Create a new deck with new mandarin flashcards
    deck = genanki_helpers.create_deck("New mandarin flashcards")

    model = genanki_helpers.create_model()

    # Create a new note with genanki_helpers
    # Loop through all flashcards in json and create a note for each one
    for flashcard in flashcards_json["flashcards"]:
        note = genanki_helpers.create_note(model, [flashcard["mandarin"], flashcard["english"] + " (" + flashcard["pinyin"] + ")"])
        genanki_helpers.add_note_to_deck(deck, note)
        note = genanki_helpers.create_note(model, [flashcard["english"], flashcard["mandarin"] + " (" + flashcard["pinyin"] + ")"])
        genanki_helpers.add_note_to_deck(deck, note)

    # Generate the .apkg file
    genanki_helpers.generate_anki_file(deck, "new_mandarin_flashcards.apkg")

if __name__ == "__main__":
    main()