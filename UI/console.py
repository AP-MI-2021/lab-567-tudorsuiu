from typing import List

from Domain.object import to_string
from Logic.CRUD import add_obiect, delete_obiect, modify_obiect
from Logic.functionalities import move_all_obiecte_to_another_locatie, concatenation_to_all_obiecte_above_price, \
    ascending_sorting_by_price, determine_maximum_price_for_every_locatie, sum_for_every_location, undo, redo


def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locatie in alta locatie data")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu pretul mai mare decat o valoare citita")
    print("6. Determinarea celui mai mare pret pentru fiecare locatie")
    print("7. Ordonarea obiectelor crescator dupa pretul de achizitie")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație")
    print("U. Undo")
    print("R. Redo")
    print("A. Afisarea tuturor obiectelor")
    print("X. Iesire")


def ui_add_obiect(inventar: List[dict], undo_list: List, redo_list: List) -> List[dict]:
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret_achizitie = float(input("Dati pretul de achizitie: "))
        locatie = input("Dati locatia: ")

        result = add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
        undo_list.append(inventar)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_delete_obiect(inventar: List[dict], undo_list: List, redo_list: List) -> List[dict]:
    try:
        id = input("Dati id-ul obiectului de sters: ")

        result = delete_obiect(id, inventar)
        undo_list.append(inventar)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_modify_obiect(inventar: List[dict], undo_list: List, redo_list: List) -> List[dict]:
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret_achizitie = float(input("Dati noul pret de achizitie: "))
        locatie = input("Dati noua locatie: ")

        result = modify_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
        undo_list.append(inventar)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def show_all(inventar: List[dict]):
    for obiect in inventar:
        print(to_string(obiect))


def ui_move_all_obiecte_to_another_locatie(inventar: List[dict], undo_list: List, redo_list: List) -> List[dict]:
    try:
        location = input("Dati locatia: ")

        result = move_all_obiecte_to_another_locatie(inventar, location)
        undo_list.append(inventar)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_concatenation_to_all_obiecte_above_price(inventar: List[dict], undo_list: List, redo_list: List) -> List[dict]:
    try:
        concat_description = input("Dati descrierea care se va adauga: ")
        price = float(input("Dati pretul de comparare: "))

        result = concatenation_to_all_obiecte_above_price(inventar, concat_description, price)
        undo_list.append(inventar)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_determine_maximum_price_for_every_locatie(inventar: List[dict]) -> dict:
    return determine_maximum_price_for_every_locatie(inventar)


def ui_ascending_sorting_by_price(inventar: List[dict], undo_list: List, redo_list: List) -> List[dict]:
    try:
        result = ascending_sorting_by_price(inventar)
        undo_list.append(inventar)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_sum_for_every_location(inventar: List[dict]) -> dict:
    return sum_for_every_location(inventar)


def run_menu(inventar: List[dict]):
    undo_list = []
    redo_list = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            inventar = ui_add_obiect(inventar, undo_list, redo_list)
        elif optiune == "2":
            inventar = ui_delete_obiect(inventar, undo_list, redo_list)
        elif optiune == "3":
            inventar = ui_modify_obiect(inventar, undo_list, redo_list)
        elif optiune == "4":
            inventar = ui_move_all_obiecte_to_another_locatie(inventar, undo_list, redo_list)
        elif optiune == "5":
            inventar = ui_concatenation_to_all_obiecte_above_price(inventar, undo_list, redo_list)
        elif optiune == "6":
            print(ui_determine_maximum_price_for_every_locatie(inventar))
        elif optiune == "7":
            inventar = ui_ascending_sorting_by_price(inventar, undo_list, redo_list)
        elif optiune == "8":
            print(ui_sum_for_every_location(inventar))
        elif optiune == "U" or optiune == "u":
            if len(undo_list) > 0:
                inventar = undo(inventar, undo_list, redo_list)
            else:
                print("Nu se poate face undo!")
        elif optiune == "R" or optiune == "r":
            if len(redo_list) > 0:
                inventar = redo(inventar, undo_list, redo_list)
            else:
                print("Nu se poate face redo!")
        elif optiune == "A" or optiune == "a":
            if len(inventar) == 0:
                print("Nu exista niciun obiect in inventar!")
            else:
                show_all(inventar)
        elif optiune == "X" or optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")
