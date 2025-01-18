import os
import sys
import csv
import random
from tabulate import tabulate


def main():
    create_default_deck()
    menu()


# CLASSES
class FlashCard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition


class CardDeck:
    def __init__(self):
        self.card_deck = []

    def add_card(self, term, definition):
        """Adds a flashcard to the deck."""
        flash_card = FlashCard(term, definition)
        self.card_deck.append(flash_card)

    def save_deck(self, filename):
        """Save the card deck to the CSV file."""
        with open(filename, "w", newline='') as csv_deck:
            fields = ["Term", "Definition"]
            writer = csv.DictWriter(csv_deck, fieldnames=fields)
            writer.writeheader()
            for card in self.card_deck:
                writer.writerow({'Term': card.term, 'Definition': card.definition})

    def load_deck(self, filename):
        """Load the card deck from the CSV file."""
        self.card_deck = []
        with open(filename, newline='') as csv_deck:
            reader = csv.DictReader(csv_deck)
            for row in reader:
                term, definition = row['Term'], row['Definition']
                self.card_deck.append(FlashCard(term, definition))

        if len(self.card_deck) == 0:
            print("The deck is empty. Returning to the main menu.")
            print("---------------------------")
            menu()

    def edit_card(self, card_id, new_term, new_definition):
        """Edit a specific card in the deck."""
        if 0 <= card_id < len(self.card_deck):
            self.card_deck[card_id].term = new_term
            self.card_deck[card_id].definition = new_definition
        else:
            print("Invalid card ID.")

    def __str__(self):
        print(self.card_deck)


# ENVIRONMENT FUNCTIONS
def menu():
    os.system("clear")
    print(end="\n")
    print("""FLASH CARDS""")
    print("Let's get started by picking an option. Type the number next to your choice:", end="\n")

    table = [["[1]", "Play"], ["[2]", "Create Deck"], ["[3]", "Browse Decks"], ["[4]", "Exit"]]
    print(tabulate(table, tablefmt="heavy_outline"))
    print(end="\n")

    choice_range = [1, 2, 3, 4]
    user_choice = choice_validator(choice_range)
    if user_choice == 1:
        env_play()
    elif user_choice == 2:
        env_deck_creation()
    elif user_choice == 3:
        env_deck_browser()
    elif user_choice == 4:
        os.system("clear")
        print("Exiting...")
        sys.exit()


def env_play():
    os.system("clear")
    print("\n")
    print("PLAY")
    print("Choose the deck by its number you would like to play with. To exit to the main menu type [0].")
    print(
        "To edit or remove certain deck, visit 'Browse Decks' in the main menu. To create new deck visit 'Create Deck' in the main menu.")

    deck_list = scan_decks()

    if not deck_list:
        menu()  # Exit to the main menu if no decks are found
        return

    create_decks_table(deck_list)
    number_of_decks = len(deck_list)

    user_choice = choice_validator(range(number_of_decks + 1))

    if user_choice == 0:
        menu()
    else:
        os.system("clear")
        print("Your goal is to match 15 cards correctly. You have only 3 chances, so be careful.")
        deck_index = user_choice - 1
        filename = deck_list[deck_index] + ".csv"
        game_deck = open_deck_by_id(filename)  # Deck picked for the game

        if not game_deck:
            menu()  # Return to the main menu if the deck has no cards
            return

        game(game_deck)  # Stard the game


def env_deck_creation():
    os.system("clear")
    print("\n")
    print("CARD DECK CREATION")
    table = [["[1]", "Create Your Deck"], ["[2]", "Exit to Main Menu"]]
    print(tabulate(table, tablefmt="heavy_outline"))
    print(end="\n")

    choice_range = [1, 2]
    user_choice = choice_validator(choice_range)
    if user_choice == 1:
        os.system("clear")
        deck_name = input("Enter the name of your deck: ")
        create_deck(deck_name)
    elif user_choice == 2:
        menu()


def env_deck_browser():
    os.system("clear")
    print("\n")
    print("YOUR DECKS")
    print("To interact with certain deck, choose its number. To exit to the main menu type [0].")

    deck_list = scan_decks()

    if not deck_list:
        print("No decks found. Returning to the main menu.")
        menu()  # Exit to the main menu if no decks are found
        return

    create_decks_table(deck_list)
    print(end="\n")
    number_of_decks = len(deck_list)

    user_choice = choice_validator(range(number_of_decks + 1))

    if user_choice == 0:
        menu()
    else:
        os.system("clear")
        deck_index = user_choice - 1
        filename = deck_list[deck_index] + ".csv"

        print("\n")
        print(f"This is your deck \"{filename}\". [0] Exit, [delete] to delete, [edit] to edit")
        picked_deck = open_deck_by_id(filename)
        create_cards_table(picked_deck)
        id_range = len(picked_deck)

        while True:
            second_choice = input("Your Choice: ")

            if second_choice == "delete":
                remove_deck(deck_list, deck_index)
                print("\n")
                print("Deck was successfuly removed.")
                input("To return to the Deck Browser, press any key.")
                env_deck_browser()
                break
            elif second_choice == "edit":
                card_id = int(input("Choose an card ID: "))
                edit_deck(card_id - 1, filename)
                break
            elif second_choice == "0":
                env_deck_browser()
                break
            else:
                print("Invalid command. Please try again.")


# GAME MODE
def game(game_deck):
    life = 3
    score = 0
    max_score = 15

    while life > 0:
        print("\n")
        random.shuffle(game_deck)  # Will pick random card from the deck.
        random_card = game_deck[0]
        answer_before_validation = input(f"What matches \"{random_card['Term']}\"? ")
        answer = str_validation(answer_before_validation)  # Ensure that the answer is in lowercase.

        if answer == random_card["Definition"]:
            os.system("clear")
            score += 1
            print(tabulate([["Correct!"], [f"{score} out of {max_score} flashcards are correct."]],
                           tablefmt="heavy_outline"))
            print(end="\n")

            random.shuffle(game_deck)
            if score == max_score:
                print(tabulate([["Congratulations!"], ["You did it—you won!"]], tablefmt="heavy_outline"))
                print("Returning to the main menu.")
                print("---------------------------")
                menu()

        else:
            os.system("clear")
            life -= 1
            print(tabulate([["Incorrect. Try again!"], [f"Remaining chances: {life}"],
                            [f"{score} out of {max_score} flashcards are correct."]], tablefmt="heavy_outline"))
            print(end="\n")

            if life == 0:
                os.system("clear")
                table = [["GAME OVER"], ["Give it another shot!"]]
                print(tabulate(table, tablefmt="heavy_outline"))
                input("To return to the main menu, press any key.")
                os.system("clear")
                menu()


# VALIDATION FUNCTIONS
def choice_validator(choice_range) -> int:
    """Handles user input and ensures valid integer choice."""
    while True:
        choice = input("Your Choice: ")
        try:
            if int(choice) not in choice_range:
                print("Invalid command. Please try again.")
                continue
            return int(choice)

        except ValueError:
            print("Invalid command. Please try again.")


def str_validation(str) -> str:
    """Ensure that term and definition are both case insensitive."""
    return str.casefold()


# DECK HANDLERS
def create_default_deck():
    """Will create one default flashcard deck, so the user can play immidiately."""
    card_deck = CardDeck()
    default_deck = [["1 + 1 =", "2"], ["44 - 4 =", "40"], ["12 * 2 =", "24"], ["81 / 9 =", "9"], ["15 + 10 =", "25"],
                    ["50 - 13 =", "37"], ["7 * 8 =", "56"], ["64 / 8 =", "8"], ["100 + 50 =", "150"],
                    ["200 - 75 =", "125"],
                    ["9 * 9 =", "81"], ["144 / 12 =", "12"], ["30 + 25 =", "55"], ["60 - 20 =", "40"],
                    ["6 * 7 =", "42"],
                    ["72 / 9 =", "8"], ["5 + 5 =", "10"], ["33 - 18 =", "15"], ["8 * 5 =", "40"], ["90 / 10 =", "9"],
                    ["25 + 30 =", "55"], ["150 - 50 =", "100"], ["12 * 11 =", "132"], ["48 / 6 =", "8"],
                    ["20 + 19 =", "39"],
                    ["70 - 32 =", "38"], ["4 * 9 =", "36"], ["81 / 3 =", "27"], ["100 + 20 =", "120"],
                    ["300 - 150 =", "150"]]

    for card in default_deck:
        term, definition = card
        card_deck.add_card(term, definition)

    card_deck.save_deck("Math_match.csv")


def create_deck(deck_name):
    """Process of defining the term and definition for each flashcard and saving them to the deck."""
    print(
        "Enter a term and its definition to create your flashcards. Press [Enter] on an empty term to finish your deck.")
    print("")
    card_deck = CardDeck()

    while True:
        try:
            term = input("Term: ").strip().casefold()

            if term == "":

                if len(card_deck.card_deck) == 0:
                    print("You cannot save an empty deck. Please add at least one card.")
                    continue

                print("\n")
                print("Would you like to save your deck [1] or return to the main menu [2]?")
                choice_range = [1, 2]
                user_choice = choice_validator(choice_range)
                if user_choice == 1:
                    filename = deck_name + ".csv"
                    card_deck.save_deck(filename)
                    print("\n")
                    print(f"Deck \"{deck_name}\" was succesfully saved.")
                    input("To return to the main menu press any key.")
                    menu()
                elif user_choice == 2:
                    menu()

            definition = input("Definition: ").strip().casefold()
            while not definition:
                print(
                    "Please provide a definition for your term. You can only save or exit during the 'term' input stage.")
                definition = input("Definition: ").strip().casefold()

            card_deck.add_card(term, definition)


        except ValueError:
            print("Value Error: Please enter a valid term, such as 'black.'")


def edit_deck(card_id, filename):
    """Edit an existing card deck."""
    card_deck = CardDeck()
    card_deck.load_deck(filename)

    if card_id < 0 or card_id >= len(card_deck.card_deck):
        menu()

    new_term = input("Enter the new term: ").strip().casefold()
    new_definition = input("Enter the new definition: ").strip().casefold()

    card_deck.edit_card(card_id, new_term, new_definition)
    card_deck.save_deck(filename)
    print("\n")
    print("The card has been successfully updated.")
    input("To go back to the Deck Browser pres any key.")
    env_deck_browser()


def scan_decks():
    """Scans the project folder for CSV files and returns the list of deck names (without ".csv")."""
    project_folder = os.path.dirname(os.path.abspath(__file__))
    deck_list = []

    with os.scandir(project_folder) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".csv"):
                file_path = entry.path
                splitted_path = file_path.split("/")
                deck_name = splitted_path[-1].replace(".csv", "")
                deck_list.append(deck_name)

    return deck_list


def open_deck_by_id(filename) -> list:
    """Will load a card deck by its ID. Each card is then displayed in a table with own ID."""
    card_deck = CardDeck()

    card_deck.load_deck(filename)
    picked_card_deck = [{"Term": card.term, "Definition": card.definition} for card in card_deck.card_deck]

    # return list of dictionaries
    return picked_card_deck


def remove_deck(deck_list, deck_id):
    """Will delete a card deck by its ID."""
    filename = deck_list[deck_id] + ".csv"
    os.remove(filename)


# DESIGN HANDLERS
def create_decks_table(deck_list):
    """Creates and prints a table of the available decks along with their IDs."""
    table_data = []
    for i, deck in enumerate(deck_list, 1):
        table_data.append([f"[{i}]", deck])

    print(tabulate(table_data, headers=["Deck ID", "Deck Name"], tablefmt="heavy_outline"))
    print(end="\n")


def create_cards_table(deck_list):
    """Creates and prints a table of the flashcards in the deck along with their IDs."""
    if not deck_list:
        print("The Deck is empty.")
        return

    table_data = [[i, card["Term"], card["Definition"]] for i, card in enumerate(deck_list, 1)]
    print(tabulate(table_data, headers=["ID", "Term", "Definition"], tablefmt="heavy_outline"))
    print(end="\n")


if __name__ == "__main__":
    main()
