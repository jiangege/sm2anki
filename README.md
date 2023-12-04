# SuperMemo to Anki Importer

## Overview

This script facilitates the import of SuperMemo (SM) XML data into Anki, a popular flashcard application for spaced repetition learning. It parses SuperMemo XML files, extracts question and answer pairs, and generates an Anki-compatible APKG file containing the imported flashcards.

## Features

- Supports importing SuperMemo elements marked as 'Topic' and 'Item'.
- Converts HTML-escaped text to readable format in Anki.
- Organizes imported notes into decks based on SuperMemo's concept hierarchy.

## Prerequisites

- Python 3
- Anki
- Genanki library (for Anki deck generation)
- Tkinter (for file dialog functionality)

## Installation

1. Ensure Python 3 is installed on your system.
2. Install the required Python libraries:
   ```sh
   pip install genanki
   ```

## Usage

1. Run the script:
   ```sh
   python sm2anki.py
   ```
2. A file dialog will open. Select your SuperMemo XML file.
3. After selecting the file, the script will process the data and create an APKG file in the script's directory.
4. Import the generated `.apkg` file into Anki.

## How It Works

- The script uses Tkinter to open a file dialog for XML file selection.
- It then parses the XML file, extracting relevant data from 'Topic' and 'Item' elements.
- Questions and answers are unescaped from HTML format and added to a new Anki deck.
- Each SuperMemo 'Concept' element defines a new deck in Anki, maintaining the hierarchical structure.
- Finally, it compiles all decks into a single APKG file.

## Limitations

- Currently, only 'Topic' and 'Item' types from SuperMemo are supported.
- The script does not handle media files or advanced formatting from SuperMemo.

## Contributing

Feedback and contributions to the script are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License

[MIT]
