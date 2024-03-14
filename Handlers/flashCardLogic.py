
class flashCard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def information(self):
        print(f"'termín je: {newCard.term}, definice je: {newCard.definition}")

def newCard():
    print("Vytvoř si další flash kartu")

    term = input("termín: ")
    definition = input("definice: ")


function_dict = {"nová" : newCard}
func = input('>')  #raw_input on python2.x
function_dict[func]()

cardDeck = []

print("Nazdar, vytvoř si svojí flash kartu")

term = input("termín: ")
definition = input("definice: ")

newCard = flashCard(term, definition)
cardDeck.append(newCard)

newCard.information()
print("pokud si přeješ přidat novou flash kartu, napiš: nová.")
command = input("> ")
function_dict[command]()

# vytvořit flash kartu s parametry: term a definition
# uložit jí do skupiny karet: deck
# vybírat pomocí inputu konkrétní kartu z decku -> zobrazí se jak její termín, tak i definice


# python manage.py runserver -> zapne lokální server (web)