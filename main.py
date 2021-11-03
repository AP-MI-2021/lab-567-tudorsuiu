from Logic.CRUD import add_obiect
from Tests.test_all import run_all_tests
from UI.console import run_menu


def main():
    run_all_tests()
    inventar = []
    run_menu(inventar)


if __name__ == "__main__":
    main()
