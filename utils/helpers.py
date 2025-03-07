import os
import json
import platform

from rich.table import Table

rich_table = Table()


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


def clear_terminal():
    """Clear the terminal window based on the used platform"""
    platform_name = platform.system()
    if platform_name in ["Darwin", "Linux"]:
        os.system("clear")
    elif platform_name == "Windows":
        os.system("cls")


def updated_status_table(life, score, max_score, time_left):
    """ Create a table with updated stats. """

    table = Table(title="Game Status")
    table.add_column("Lives", style="green", justify="center")
    table.add_column("Score", style="blue", justify="center")
    table.add_column("Remaining Time", style="red", justify="center")
    table.add_row(str(life), f"{score}/{max_score}", f"{time_left}s")

    return table


def load_translations():
    translations_path = os.path.join(os.path.dirname(__file__), 'translations.json')
    with open(translations_path, encoding="utf-8") as translation_file:
        return json.load(translation_file)
