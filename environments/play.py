from tabulate import tabulate
from rich.console import Console

from utils import helpers, deck_manager
import environments
import game_modes

console = Console()


def env_play():
    helpers.clear_terminal()
    console.print("[bold bright_blue]PLAY[/bold bright_blue]")
    console.print("Choose the game mode. Or [bold magenta][0] Return[/bold magenta] to the main menu.", end="\n")

    table = [["[1]", "Quiz", "*Guess the right definition*"], ["[2]", "Time Attack", "*Currently Unavailable*"]]
    print(tabulate(table, tablefmt="heavy_outline"))
    print(end="\n")

    choice_range = [0, 1, 2]
    user_choice = helpers.choice_validator(choice_range)
    if user_choice == 0:
        environments.menu()
    elif user_choice == 1:
        game_mode = "QUIZ"
        game_deck = deck_manager.prepare_deck_for_game(game_mode)
        game_modes.quiz(game_deck)
    elif user_choice == 2:
        console.print("[magenta]This game mode is not available in this version.[/magenta]")
        input("Press [Enter] to continue.")
        environments.env_play()
    #     game_mode = "TIME ATTACK"
    #     game_deck = deck_manager.prepare_deck_for_game(game_mode)
    #     game_modes.time_attack(game_deck)
