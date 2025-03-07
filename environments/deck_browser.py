from rich.console import Console

import environments
from utils import helpers, deck_manager

console = Console()
translations = helpers.load_translations()


def env_deck_browser():
    helpers.clear_terminal()
    console.print(translations["titles"]["deck_browser"])
    console.print(translations["env_deck_browser"]["welcome_message"])

    deck_list = deck_manager.scan_decks()

    if not deck_list:
        console.print(translations["env_deck_browser"]["no_deck_found"])
        input()
        environments.menu()  # Exit to the main menu if no decks are found
        return

    deck_manager.create_decks_table(deck_list)
    print(end="\n")
    number_of_decks = len(deck_list)

    user_choice = helpers.choice_validator(range(number_of_decks + 1))

    if user_choice == 0:
        environments.menu()
    else:
        helpers.clear_terminal()
        deck_index = user_choice - 1
        filename = deck_list[deck_index] + ".csv"

        console.print(f"This is your deck [bold bright_blue]\"{filename}\"[/bold bright_blue]")
        console.print(translations["env_deck_browser"]["selected_deck"])
        picked_deck = deck_manager.open_deck_by_id(filename)
        deck_manager.create_cards_table(picked_deck)
        id_range = len(picked_deck)

        while True:
            second_choice = input(translations["log_messages"]["your_choice"])

            if second_choice == "delete":
                deck_manager.remove_deck(deck_list, deck_index)
                print("\n")
                print(translations["log_messages"]["successfully_deleted_deck"])
                console.print(translations["log_messages"]["return_to_the_deck_browser"])
                input()
                env_deck_browser()
                break
            elif second_choice == "edit": #TODO: Při zadání prázdného stringu (enter) při výběru ID, program spadne. Bude třeba přidat validaci.
                card_id = int(input(translations["log_messages"]["choose_id"]))
                deck_manager.edit_deck(card_id - 1, filename)
                console.print(translations["log_messages"]["return_to_the_deck_browser"])
                input()
                env_deck_browser()
                break
            elif second_choice == "0":
                env_deck_browser()
                break
            else:
                print(translations["log_messages"]["invalid_command"])
