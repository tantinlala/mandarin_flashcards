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
    mandarin_assistant.convert_to_flashcards(text)

    # Create a new deck with new mandarin flashcards
    deck = genanki_helpers.create_deck("New mandarin flashcards")

    model = genanki_helpers.create_model()

    # Create a new note with genanki_helpers
    note = genanki_helpers.create_note(model, ["Front of card", "Back of card"])

    # Add the note to the deck
    deck.add_note(note)

    # Generate the .apkg file
    genanki_helpers.generate_anki_file(deck, "new_mandarin_flashcards.apkg")

if __name__ == "__main__":
    main()