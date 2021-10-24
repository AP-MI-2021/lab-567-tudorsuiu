from Logic.CRUD import add_obiect
from Tests.test_all import run_all_tests
from UI.console import run_menu


def main():
    run_all_tests()
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C2", inventar)
    inventar = add_obiect("2", "Telefon", "Tehnologie", 1000.0, "E1C1", inventar)
    run_menu(inventar)


if __name__ == "__main__":
    main()
