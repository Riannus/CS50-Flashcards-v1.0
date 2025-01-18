from flashcards import str_validation, FlashCard, CardDeck, create_default_deck
import pytest
import os


def test_str_validation():
    assert str_validation("FlaSHcArD") == "flashcard"
    assert str_validation("?Sp3c1aL-Ch4r4ct3r!") == "?sp3c1al-ch4r4ct3r!"


def test_create_default_deck():
    create_default_deck()
    assert os.path.exists("Math_match.csv") == True
    os.remove("Math_match.csv")  # To clean the folder


def test_create_flashcard():
    card = FlashCard("term", "definition")
    assert card.term == "term"
    assert card.definition == "definition"


def test_add_card():
    deck = CardDeck()
    deck.add_card("black", "white")
    assert len(deck.card_deck) == 1
    deck.card_deck[0].term == "black"
    deck.card_deck[0].definition == "white"


def test_edit_card():
    deck = CardDeck()
    deck.add_card("black", "white")
    deck.edit_card(0, "dark", "light")
    assert deck.card_deck[0].term == "dark"
    assert deck.card_deck[0].definition == "light"
