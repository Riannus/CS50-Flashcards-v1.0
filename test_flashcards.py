import models
from models import FlashCard, CardDeck
from utils import helpers, deck_manager
import pytest
import os


def test_str_validation():
    assert helpers.str_validation("Flashcard") == "flashcard"
    assert helpers.str_validation("FLASHCARD") == "flashcard"
    assert helpers.str_validation("flaSHcard") == "flashcard"
    assert helpers.str_validation("FlaSHcArD") == "flashcard"
    assert helpers.str_validation("?Sp3c1aL-Ch4r4ct3r!") == "?sp3c1al-ch4r4ct3r!"


def test_create_default_deck():
    deck_manager.create_default_deck()
    assert os.path.exists(os.path.join("card_decks", "Math_match.csv")) == True
    os.remove(os.path.join("card_decks", "Math_match.csv"))  # To clean the folder


def test_create_flashcard():
    card = models.FlashCard("term", "definition")
    assert card.term == "term"
    assert card.definition == "definition"


def test_add_card():
    deck = models.CardDeck()
    deck.add_card("black", "white")
    assert len(deck.card_deck) == 1
    deck.card_deck[0].term == "black"
    deck.card_deck[0].definition == "white"


def test_edit_card():
    deck = models.CardDeck()
    deck.add_card("black", "white")
    deck.edit_card(0, "dark", "light")
    assert deck.card_deck[0].term == "dark"
    assert deck.card_deck[0].definition == "light"