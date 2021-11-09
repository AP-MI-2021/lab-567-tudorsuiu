from typing import List

from Domain.object import to_string
from Logic.CRUD import add_obiect, delete_obiect, modify_obiect
from Logic.functionalities import undo, redo


def ui_add_obiect(id: str, nume: str, descriere: str, pret_achizitie: float, locatie: str, inventar: List[dict],
                  undo_list: List, redo_list: List) -> List[dict]:
    try:
        result = add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
        undo_list.append(inventar)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_modify_obiect(id: str, nume: str, descriere: str, pret_achizitie: float, locatie: str, inventar: List[dict],
                     undo_list: List, redo_list: List) -> List[dict]:
    try:
        result = modify_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
        undo_list.append(inventar)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_delete_obiect(id: str, inventar: List[dict], undo_list: List, redo_list: List) -> List[dict]:
    try:
        result = delete_obiect(id, inventar)
        undo_list.append(inventar)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def print_description():
    print("Lista de comenzi va fi separata prin ','")
    print("Comenzile pot fi: help, add, update, delete, showall, exit.")
    print("Parametrii fiecarei comenzi vor fi separati tot prin ','")


def print_help():
    print("Comenzile pot fi: help, add, update, delete, showall, undo, redo, exit.")
    print("Comenzile au urmatorii parametri:")
    print("add,id,nume,descriere,pret_achizitie,locatie;")
    print("update,id,noul_nume,noua_descriere,noul_pret_achizitie,noua_locatie;")
    print("delete,id;")
    print("undo")
    print("redo")
    print("exit")


def show_all(inventar: List[dict]):
    for obiect in inventar:
        print(to_string(obiect))


def run_command_line_console(inventar: List[dict]):
    print_description()
    should_run = True
    undo_list = []
    redo_list = []
    while should_run:
        list_input = input("Dati lista de comenzi: ")
        list_with_commands = list_input.split(",")
        for i in range(len(list_with_commands)):
            if list_with_commands[i] == "exit":
                should_run = False
                break
            elif list_with_commands[i] == "add":
                inventar = ui_add_obiect(list_with_commands[i + 1], list_with_commands[i + 2],
                                         list_with_commands[i + 3], float(list_with_commands[i + 4]),
                                         list_with_commands[i + 5], inventar, undo_list, redo_list)
            elif list_with_commands[i] == "delete":
                inventar = ui_delete_obiect(list_with_commands[i + 1], inventar, undo_list, redo_list)
            elif list_with_commands[i] == "update":
                inventar = ui_modify_obiect(list_with_commands[i + 1], list_with_commands[i + 2],
                                            list_with_commands[i + 3], float(list_with_commands[i + 4]),
                                            list_with_commands[i + 5], inventar, undo_list, redo_list)
            elif list_with_commands[i] == "help":
                print_help()
            elif list_with_commands[i] == "showall":
                if len(inventar) == 0:
                    print("Nu exista niciun obiect in inventar!")
                else:
                    show_all(inventar)
            elif list_with_commands[i] == "undo":
                if len(undo_list) > 0:
                    inventar = undo(inventar, undo_list, redo_list)
                else:
                    print("Nu se poate face undo!")
            elif list_with_commands[i] == "redo":
                if len(redo_list) > 0:
                    inventar = redo(inventar, undo_list, redo_list)
                else:
                    print("Nu se poate face redo!")
