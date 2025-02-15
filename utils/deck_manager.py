import os
import platform

from tabulate import tabulate
from rich.console import Console

import config
import models
import environments
from config import PROJECT_DIR, DECKS_DIR
from .helpers import choice_validator, clear_terminal

console = Console()


def create_default_deck():
    """Will create one default flashcard deck, so the user can play immediately."""
    card_deck = models.CardDeck()
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
    console.print(
        "Enter a term and its definition to create your flashcards. Press [magenta][Enter][/magenta] on an empty term to finish your deck.")
    print("")
    card_deck = models.CardDeck()

    while True:
        try:
            term = input("Term: ").strip().casefold()

            if term == "":

                if len(card_deck.card_deck) == 0:
                    print("You cannot save an empty deck. Please add at least one card.")
                    continue

                print("\n")
                console.print(
                    "Would you like to [magenta][0] return[/magenta] to the main menu or [magenta][1] save[/magenta] your deck?")
                choice_range = [0, 1]
                user_choice = choice_validator(choice_range)
                if user_choice == 1:
                    filename = deck_name + ".csv"
                    card_deck.save_deck(filename)
                    print("\n")
                    print(f"Deck \"{deck_name}\" was succesfully saved.")
                    console.print("[bold magenta]To return to the main menu, press enter.[/bold magenta]")
                    input()
                    environments.menu()
                elif user_choice == 0:
                    environments.menu()

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
    card_deck = models.CardDeck()
    card_deck.load_deck(filename)

    if card_id < 0 or card_id >= len(card_deck.card_deck):
        environments.menu()

    new_term = input("Enter the new term: ").strip().casefold()
    new_definition = input("Enter the new definition: ").strip().casefold()

    card_deck.edit_card(card_id, new_term, new_definition)
    card_deck.save_deck(filename)
    print("\n")
    print("The card has been successfully updated.")


def scan_decks():
    """Scans the project folder for CSV files and returns the list of deck names (without ".csv")."""

    saved_decks_folder = config.DECKS_DIR
    deck_list = []
    platform_name = platform.system()

    with os.scandir(saved_decks_folder) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".csv"):
                file_path = entry.path

                if platform_name in ["Darwin", "Linux"]:
                    splitted_path = file_path.split("/")
                elif platform_name == "Windows":
                    splitted_path = file_path.split("\\")

                deck_name = splitted_path[-1].replace(".csv", "")
                deck_list.append(deck_name)

    return deck_list


def open_deck_by_id(filename) -> list:
    """Will load a card deck by its ID. Each card is then displayed in a table with own ID."""
    card_deck = models.CardDeck()

    card_deck.load_deck(filename)
    picked_card_deck = [{"Term": card.term, "Definition": card.definition} for card in card_deck.card_deck]

    # return list of dictionaries
    return picked_card_deck


def remove_deck(deck_list, deck_id):
    """Will delete a card deck by its ID."""
    filename = deck_list[deck_id] + ".csv"
    file_in_deck_folder = os.path.join(config.DECKS_DIR, filename)
    os.remove(file_in_deck_folder)


def prepare_deck_for_game(game_mode):
    clear_terminal()
    console.print(f"[bold bright_blue]{game_mode}[/bold bright_blue]")
    console.print(
        "To select the deck you'd like to play with, choose its [magenta][ID][/magenta]. Or [magenta][0] Return[/magenta] to the main menu.")

    deck_list = scan_decks()

    if not deck_list:
        environments.menu()  # Exit to the main menu if no decks are found
        return

    create_decks_table(deck_list)
    number_of_decks = len(deck_list)

    user_choice = choice_validator(range(number_of_decks + 1))

    if user_choice == 0:
        environments.menu()
    else:
        deck_index = user_choice - 1
        filename = deck_list[deck_index] + ".csv"
        game_deck = open_deck_by_id(filename)  # Deck picked for the game

        if not game_deck:
            environments.menu()  # Return to the main menu if the deck has no cards
            return

    return game_deck


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
