# Flashcards  

#### Video Demo: [Watch Here](https://youtu.be/4CTJjVHR3PM)  

## Overview  

**Flashcards** is a Python-based application developed as the final project for *CS50’s Introduction to Programming with Python*. The app enables users to create, manage, and interact with flashcard decks, designed for learning and reviewing information effectively.  

## Features  
- **Custom Decks**: Create flashcard decks by defining terms and corresponding definitions.  
- **Deck Browser**: View, edit, or delete existing flashcard decks.  
- **Game Modes**: Play several games to memorize your custom flashcards.
  - **Quiz Mode**: Match the term with its definition.
  - **Guess the Definition**: Multiple-choice mode (A, B, C, D).
  - **Survival Mode**: An endless quiz mode.
- **Study Mode**: A relaxed mode where users can go through their flashcards without penalties. Cards can also be edited directly in this mode.
- **CSV-Based Storage**: Flashcard decks are stored in easily accessible CSV files for management and sharing.  
- **Default Decks**: Includes a preloaded decks for immediate gameplay.

## Design Decisions  
- **CSV for Data Storage**: Chosen for its simplicity and ease of use, given the small scale of the project.  
- **Command-Line Interface**: A terminal-based menu system ensures a straightforward user experience without requiring additional dependencies for graphical interfaces.  
- **Error Handling**: User inputs are validated to ensure a smooth experience, including standardized inputs for terms and definitions to avoid case-sensitivity issues.
- **Dynamic Text System**: All in-game texts are stored in a JSON file, making it easy to modify or expand without altering the source code.

## Future Features  
Planned enhancements include:  
1. **Database Integration**: Replace CSV storage with a more robust database system.  
2. **Graphical User Interface (GUI)**: Add a user-friendly graphical interface.  
3. **Deck Enhancements**:  
   - Rename decks.  
   - Mark decks as favorites.  
   - Delete individual cards from decks.  
4. **Game Mode Settings**:  
   - Match either terms or definitions.  
   - Add a time limit for answers.  
   - Enable or disable case-sensitivity.  
5. **New Game Modes**: Implement a memory game (e.g., matching pairs).  

## Project Structure  
- `card_decks/`: Folder containing game decks saved as CSV files.
- `environments/`: Contains environment files for menu, gameplay, deck browser, etc.
- `game_modes/`: Contains different game modes like Study Mode, Time Attack, etc.
- `models/`: Contains classes that define flashcards, decks, etc.
- `utils/`: Helper functions for various operations like deck management, validation, etc.
- `README.md`: Documentation for the project.
- `requirements.txt`: List of dependencies (if any).
- `test_flashcards.py`: Unit tests for key functionality.
- `translations.json`: translation keys.

## How to Use  

### Installation
Ensure that Python is installed on the system. The program is developed in Python, so having Python installed is essential.

1. Clone the repository to your local machine:  
   ```bash
   git clone https://github.com/your-username/CS50-Flashcards-v1.0.git
   cd flashcards
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
3. Run the application using Python:
   ```bash
   python flashcards.py

## Licensing
This project is open source and distributed under the MIT License. Feel free to use, modify, and distribute it as long as the original license is included.

