from Tests.test_all import run_all_tests
from UI.command_line_console import run_command_line_console
from UI.console import run_menu


def main():
    run_all_tests()
    inventar = []
    type_of_menu = input("Ce de tip de consola doriti sa se foloseasca? (C/CLC) ")
    if type_of_menu == "C" or type_of_menu == "c":
        run_menu(inventar)
    elif type_of_menu == "CLC" or type_of_menu == "clc":
        run_command_line_console(inventar)
    else:
        print("Acest tip de consola nu exista! Alegeti dintre C - Console sau CLC - Command Line Console")


if __name__ == "__main__":
    main()
