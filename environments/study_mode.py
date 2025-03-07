from rich.console import Console

import environments
import game_modes
from utils import helpers, deck_manager

console = Console()
translations = helpers.load_translations()


def env_study_mode():
    helpers.clear_terminal()
    console.print(translations["titles"]["study_mode"])
    print(translations["env_study_mode"]["welcome_message"])
    console.print(translations["env_study_mode"]["study_mode_instructions"])

    deck_list = deck_manager.scan_decks()

    if not deck_list:
        environments.menu()  # Exit to the main menu if no decks are found
        return

    deck_manager.create_decks_table(deck_list)
    number_of_decks = len(deck_list)

    user_choice = helpers.choice_validator(range(number_of_decks + 1))

    if user_choice == 0:
        environments.menu()
    else:
        helpers.clear_terminal()
        deck_index = user_choice - 1
        filename = deck_list[deck_index] + ".csv"
        game_deck = deck_manager.open_deck_by_id(filename)  # Deck picked for the game
        game_modes.study_mode(game_deck, filename)
