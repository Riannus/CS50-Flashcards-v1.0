import sys

from tabulate import tabulate
from rich.console import Console

import environments
from utils import helpers

console = Console()


def menu():
    helpers.clear_terminal()
    console.print("[bold bright_blue]FLASH CARDS[/bold bright_blue]")
    print("Welcome! Please choose an option by typing the corresponding number.", end="\n")

    table = [["[1]", "Play"], ["[2]", "Study Mode"], ["[3]", "Create Deck"], ["[4]", "Browse Decks"], ["[5]", "Exit"]]
    print(tabulate(table, tablefmt="heavy_outline"))
    print(end="\n")

    choice_range = [1, 2, 3, 4, 5]
    user_choice = helpers.choice_validator(choice_range)
    if user_choice == 1:
        environments.env_play()
    elif user_choice == 2:
        environments.env_study_mode()
    elif user_choice == 3:
        environments.env_deck_creation()
    elif user_choice == 4:
        environments.env_deck_browser()
    elif user_choice == 5:
        helpers.clear_terminal()
        print("Exiting...")
        sys.exit()
