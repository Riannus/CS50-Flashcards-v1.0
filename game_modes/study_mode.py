import random
from rich.table import Table
from rich.console import Console

from utils import helpers, deck_manager
import environments

console = Console()
rich_table = Table()


def study_mode(game_deck, filename):
    random.shuffle(game_deck)
    random_card = game_deck[0]
    card_side = True

    while True:
        helpers.clear_terminal()
        if card_side:
            card_content = random_card["Term"]
            title = "Term"
        else:
            card_content = random_card["Definition"]
            title = "Definition"

        console.print(
            "Use [bold magenta][Enter] to flip cards[/bold magenta] and memorize terms. Type [bold magenta][1] to switch cards[/bold magenta], [bold magenta][2] to edit card[/bold magenta] or type [bold magenta][0] to exit[/bold magenta].")
        nested_table = Table(title=f"{title}", title_style="italic dim", show_header=False, box=None,
                             title_justify="center", expand=True)
        nested_table.add_column(justify="center", vertical="middle")
        nested_table.add_row(f"{card_content}", style="bold cyan")
        outer_table = Table(show_header=False, min_width=40, padding=2)
        outer_table.add_row(nested_table)
        console.print(outer_table)

        print("\n")
        user_choice = input("Your Choice: ")

        if user_choice == "0":
            environments.menu()
        elif user_choice == "1":
            random.shuffle(game_deck)
            random_card = game_deck[0]
            card_side = True
        elif user_choice == "2":
            deck_manager.edit_deck(0, filename)
            console.print("[bold magenta]The change will only be visible after reloading the study mode."
                          "Press enter to continue.[/bold magenta]")
            input()

        elif user_choice == "":
            card_side = not card_side
        else:
            print("Invalid command. Please try again.")
