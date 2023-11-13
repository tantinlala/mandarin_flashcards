# mandarin_flashcards
This is a Python package that simplifies the process of creating Mandarin Anki flashcards using the genanki library and OpenAI.

## Installation
You can install this package using pip:
```bash
pip install mandarin_flashcards

## Usage

This package provides a console script that you can use to create Mandarin Anki flashcards. Here's how to use it:

1. First, install the package using pip

2. Then, you can run the `create_mandarin_flashcards` script from the command line. You'll need to provide the path to a text file that contains the Mandarin passage from which you want to create flash cards.

```bash
create_mandarin_flashcards mandarin_text.txt
```

This will create an Anki package file (`.apkg`) in the current directory.

3. You can import the `.apkg` file into Anki to add the flashcards to your collection.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License.