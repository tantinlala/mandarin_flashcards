from . import genanki_helpers
from .mandarin_assistant import MandarinAssistant

def main():

    mandarin_assistant = MandarinAssistant()
    mandarin_assistant.convert_to_flashcards("小丽：手机、电脑、地图，一个也不能少。 小刚：这些我昨天下午就准备好了。 小丽：再多带几件衣服吧。 小刚：我们是去旅游，不是搬家，还是少带一些吧")

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