from Logic.CRUD import add_obiect
from Tests.test_all import run_all_tests
from UI.console import run_menu


def main():
    run_all_tests()
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C1", inventar)
    inventar = add_obiect("2", "Televizor", "Tehnologie", 2500.0, "E1C2", inventar)
    inventar = add_obiect("3", "Mixer", "Tehnologie", 150.0, "E1C2", inventar)
    inventar = add_obiect("4", "Telefon", "Tehnologie", 1000.0, "E1C1", inventar)
    inventar = add_obiect("5", "Tableta", "Tehnologie", 1700.0, "E1C2", inventar)
    inventar = add_obiect("6", "Masina", "Tehnologie", 15000.0, "E1C2", inventar)
    run_menu(inventar)


if __name__ == "__main__":
    main()
