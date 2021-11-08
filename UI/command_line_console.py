from typing import List

from Domain.object import to_string
from Logic.CRUD import add_obiect, delete_obiect


def ui_add_obiect(id: str, nume: str, descriere: str, pret_achizitie: float, locatie: str, inventar: List[dict]) -> List[dict]:
    try:
        return add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_delete_obiect(id: str, inventar: List[dict]) -> List[dict]:
    try:
        return delete_obiect(id, inventar)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def print_description():
    print("Lista de comenzi va fi separata prin ','")
    print("Comenzile pot fi: add, showall, delete, exit.")
    print("Parametrii fiecarei comenzi vor fi separati prin ','")


def show_all(inventar: List[dict]):
    for obiect in inventar:
        print(to_string(obiect))


def run_command_line_console(inventar: List[dict]):
    print_description()
    should_run = True
    while should_run:
        list_input = input("Dati lista de comenzi: ")
        list_with_commands = list_input.split(",")
        for i in range(len(list_with_commands)):
            if list_with_commands[i] == "exit":
                should_run = False
                break
            elif list_with_commands[i] == "add":
                inventar = ui_add_obiect(list_with_commands[i + 1], list_with_commands[i + 2], list_with_commands[i + 3],
                                      float(list_with_commands[i + 4]), list_with_commands[i + 5], inventar)
            elif list_with_commands[i] == "delete":
                inventar = ui_delete_obiect(list_with_commands[i + 1], inventar)
            elif list_with_commands[i] == "showall":
                show_all(inventar)
