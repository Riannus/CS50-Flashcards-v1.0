from rich.console import Console

import environments
from utils import helpers, deck_manager

console = Console()


def env_deck_browser():
    helpers.clear_terminal()
    console.print("[bold bright_blue]YOUR DECKS[/bold bright_blue]")
    console.print(
        "Here you can see a list of your saved decks. To interact with a specific deck, select its [magenta][ID][/magenta]. Or [magenta][0] Return[/magenta] to the main menu.")

    deck_list = deck_manager.scan_decks()

    if not deck_list:
        console.print("[bold magenta]No Deck found. To return to the main menu, press enter.[/bold magenta]")
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

        console.print(
            f"This is your deck [bold bright_blue]\"{filename}\"[/bold bright_blue]. You can [magenta][0] Return[/magenta] to the Deck Browser, [magenta]\\[delete][/magenta] the deck, or [magenta]\\[edit][/magenta] the deck.")
        picked_deck = deck_manager.open_deck_by_id(filename)
        deck_manager.create_cards_table(picked_deck)
        id_range = len(picked_deck)

        while True:
            second_choice = input("Your Choice: ")

            if second_choice == "delete":
                deck_manager.remove_deck(deck_list, deck_index)
                print("\n")
                print("Deck was successfuly removed.")
                console.print("[bold magenta]To return to the Deck Browser, press enter.[/bold magenta]")
                input()
                env_deck_browser()
                break
            elif second_choice == "edit":
                card_id = int(input("Choose an card ID: "))
                deck_manager.edit_deck(card_id - 1, filename)
                console.print("[bold magenta]To return to the Deck Browser, press enter.[/bold magenta]")
                input()
                env_deck_browser()
                break
            elif second_choice == "0":
                env_deck_browser()
                break
            else:
                print("Invalid command. Please try again.")
