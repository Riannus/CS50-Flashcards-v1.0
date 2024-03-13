
class flashCard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def information(self):
        print(f"'termín je: {card.term}, definice je: {card.definition}")


print("Nazdar, vytvoř si svojí flash kartu")

term = input("termín: ")
definition = input("definice: ")

card = flashCard(term, definition)
card.information()


# vytvořit flash kartu s parametry: term a definition
# uložit jí do skupiny karet: deck
# vybírat pomocí inputu konkrétní kartu z decku -> zobrazí se jak její termín, tak i definice