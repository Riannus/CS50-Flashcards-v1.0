import environments
from utils import deck_manager

def main():
    deck_manager.create_default_deck()
    environments.menu()


if __name__ == "__main__":
    main()
