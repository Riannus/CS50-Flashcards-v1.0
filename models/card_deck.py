import os
import csv

from rich.console import Console

import config
import environments
from .flashcard import FlashCard

console = Console()


class CardDeck:
    def __init__(self):
        self.card_deck = []

    def add_card(self, term, definition):
        """Adds a flashcard to the deck."""
        flash_card = FlashCard(term, definition)
        self.card_deck.append(flash_card)

    def save_deck(self, filename):
        """Save the card deck to the CSV file."""

        file_path = os.path.join(config.DECKS_DIR, filename)

        with open(file_path, "w", newline='', encoding="utf-8") as csv_deck:
            fields = ["Term", "Definition"]
            writer = csv.DictWriter(csv_deck, fieldnames=fields)
            writer.writeheader()
            for card in self.card_deck:
                writer.writerow({'Term': card.term, 'Definition': card.definition})

    def load_deck(self, filename):
        """Load the card deck from the CSV file."""
        self.card_deck = []
        file_path = os.path.join(config.DECKS_DIR, filename)
        with open(file_path, newline='', encoding="utf-8") as csv_deck:
            reader = csv.DictReader(csv_deck)
            for row in reader:
                term, definition = row['Term'], row['Definition']
                self.card_deck.append(FlashCard(term, definition))

        if len(self.card_deck) == 0:
            console.print("[bold magenta]The Deck is empty! To return to the main menu, press enter.[/bold magenta]")
            input()
            environments.menu()

    def edit_card(self, card_id, new_term, new_definition):
        """Edit a specific card in the deck."""
        if 0 <= card_id < len(self.card_deck):
            self.card_deck[card_id].term = new_term
            self.card_deck[card_id].definition = new_definition
        else:
            print("Invalid card ID.")

    def __str__(self):
        print(self.card_deck)
