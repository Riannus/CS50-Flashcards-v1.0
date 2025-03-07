from tabulate import tabulate
from rich.console import Console

import environments
from utils import helpers, deck_manager

console = Console()
translations = helpers.load_translations()


def env_deck_creation():
    helpers.clear_terminal()
    console.print(translations["titles"]["deck_creator"])
    print(translations["env_deck_creator"]["welcome_message"])
    table = [["[1]", "Create Your Deck"], ["[2]", "Return to the Main Menu"]]
    print(tabulate(table, tablefmt="heavy_outline"))
    print(end="\n")

    choice_range = [1, 2]
    user_choice = helpers.choice_validator(choice_range)
    if user_choice == 1:
        helpers.clear_terminal()
        deck_name = input(translations["log_messages"]["enter_deck_name"])
        deck_manager.create_deck(deck_name)
    elif user_choice == 2:
        environments.menu()
