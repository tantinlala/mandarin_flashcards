# my_anki_package

This is a Python package that simplifies the process of creating Anki flashcards using the genanki library.

## Installation

You can install this package using pip:

```bash
pip install my_anki_package
```

## Usage

First, import the package:

```python
import my_anki_package
```

Then, you can use the functions and classes provided by the package to generate Anki flashcards.

Here is a basic example:

```python
from my_anki_package import genanki_helpers

# Create a new deck
deck = genanki_helpers.create_deck("My Deck")

# Add a card to the deck
genanki_helpers.add_card(deck, "Front of card", "Back of card")

# Save the deck to a file
genanki_helpers.save_deck(deck, "my_deck.apkg")
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License.