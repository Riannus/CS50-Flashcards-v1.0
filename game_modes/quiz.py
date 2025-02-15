import random
from rich.console import Console
from tabulate import tabulate

import environments
from utils import helpers

console = Console()


def quiz(game_deck):
    life = 3
    score = 0
    max_score = 15

    helpers.clear_terminal()
    print("Your goal is to match 15 cards correctly. You have only 3 chances, so be careful.")
    console.print("If you want to exit the game at any time, type [magenta]\\[exit_game][/magenta].")
    print("\n")
    input("To continue press [Enter]")
    helpers.clear_terminal()

    while life > 0:
        print("\n")
        random.shuffle(game_deck)  # Will pick random card from the deck.
        random_card = game_deck[0]
        console.print(f"What matches [bold magenta]{random_card['Term']}[/bold magenta]? ")
        answer_before_validation = input("Your Answer: ")
        answer = helpers.str_validation(answer_before_validation)  # Ensure that the answer is in lowercase.

        if answer == random_card["Definition"]:
            helpers.clear_terminal()
            score += 1
            print(tabulate([["Correct!"], [f"{score} out of {max_score} flashcards are correct."]],
                           tablefmt="heavy_outline"))
            print(end="\n")

            random.shuffle(game_deck)
            if score == max_score:
                helpers.clear_terminal()
                print(tabulate([["Congratulations!"], ["You did it—you won!"]], tablefmt="heavy_outline"))
                console.print("[bold magenta]To return to the main menu, press enter.[/bold magenta]")
                input()
                helpers.clear_terminal()
                environments.menu()

        elif answer == "exit_game":
            environments.menu()

        else:
            helpers.clear_terminal()
            life -= 1
            print(tabulate([["Incorrect. Try again!"], [f"Remaining chances: {life}"],
                            [f"{score} out of {max_score} flashcards are correct."]], tablefmt="heavy_outline"))

            if life == 0:
                helpers.clear_terminal()
                table = [["GAME OVER"], ["Give it another shot!"]]
                print(tabulate(table, tablefmt="heavy_outline"))
                console.print("[bold magenta]To return to the main menu, press enter.[/bold magenta]")
                input()
                helpers.clear_terminal()
                environments.menu()
