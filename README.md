# Flashcards

#### Video Demo: https://youtu.be/4CTJjVHR3PM

#### Description:

The Flashcard Application allow users to create, manage and play flashcard game designed for learning and reviewing
information through custom descks of flashcards. Each flashcard consists of term and definition that users must match
during gameplay.
Flashcards consists of several key features. The most important is the ability to create custom decks which allow users
to create flashcard deck by defining terms and their corresponding definitions. This function is followed by Deck
Browser where users can view all their saved decks, remove them or edit certain flashcards within them. Flashcards are
stored in CSV files that represent the entire deck. This system enables users to easily access the decks, manage and
share decks with others.
The game mode enables user to choose a deck they have created and start the "guessing game," where a random flashcard
term is displayed and user are prompted for its definition. Player starts with 3 lives which decrease with each
incorrect guess. The game ends once all 15 flashcards are answered correctly.

The Flashcard Application is a simple yet powerful tool for learning and reviewing information through custom flashcard
decks. Whether you are studying for exams, memorizing facts, learning foreign language or just having fun, this app
provides an intuitive way to manage and interact with your flashcards.

#### Design Decisions:

The decision to use CSV as the database instead of using full database system (TinyDB for example) was based on the
simplicity of CSV files, which are easy to manage and do not require complex database setup. Since the application is
designed to handle small number of decks (no more than 20), a database system would be unnecessary.
According to the scale of the project, the user interface is based on a simple terminal navigation system, with
different environments accessible from the main menu. Several helper functions were created to manage the dlow of the
application and to allow users to move between different environments without the need of restarting the app. One such
helper is "choice_validator()" ensuring that users can only input valid options, minimizing errors caused by invalid
inputs.
Despite "choice_validator()" minimizing value errors, it introduced a new challenge within the deck browser environment.
Initially, user prompts were string-based, causing frequent errors due to inconsistent input types. Standardizing
prompts to accept integers resolved these issues but created a conflict when interacting with decks or cards, as IDs
also required numeric input. To address this, additional string-based options like "exit" and "edit" were introduced,
allowing users to perform actions and select specific items without collisions.
Another challange was to ensure that no errors occur when users do not have any flashcard decks saved in the root
folder. This was achieved through simple if-statement validators and a function that creates a default card deck during
the application initialization, called "create_default_deck()." The advantage of this solution is that users can try the
game mode immidiately without being required to have a deck.
Additionaly, to ensure that correct user answers (definitions) always match the term side of the flashcard in the game
mode, both terms and definitions are converted to lowercase. This conversion occurs in two places: when the card itself
is created and when the user provides an "answer" during the game. This way, it is ensured that users are not penalized
for case-sensitve input errors.

#### Structure:

- `project.py`: The entry point for the application, where the user interacts with the menu system, creates/edit
  flashcard decks, and plays the game.
- `README.md`: This file provides detailed documentation about the project and its functionality.
- `requirements.txt`: Contains a list of third-party libraries that are required for the application to run.
- `test_flashcards.py`: Contains a set of unit tests.

