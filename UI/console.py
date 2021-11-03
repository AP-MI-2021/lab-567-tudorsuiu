from typing import List

from Domain.object import to_string, get_nume, get_descriere, get_pret_achizitie, get_locatie
from Logic.CRUD import add_obiect, delete_obiect, modify_obiect, get_by_id
from Logic.functionalities import move_all_obiecte_to_another_locatie, concatenation_to_all_obiecte_above_price, \
    ascending_sorting_by_price, determine_maximum_price_for_every_locatie


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


def ui_add_obiect(inventar: List[dict], undo_operations: List, redo_operations: List) -> List[dict]:
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret_achizitie = float(input("Dati pretul de achizitie: "))
        locatie = input("Dati locatia: ")
        result = add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
        undo_operations.append([
            lambda: delete_obiect(id, result),
            lambda: add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
        ])
        redo_operations.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_delete_obiect(inventar: List[dict], undo_operations: List, redo_operations: List) -> List[dict]:
    try:
        id = input("Dati id-ul obiectului de sters: ")
        obiect_deleted = get_by_id(id, inventar)
        result = delete_obiect(id, inventar)
        undo_operations.append([
            lambda: add_obiect(
                id,
                get_nume(obiect_deleted),
                get_descriere(obiect_deleted),
                get_pret_achizitie(obiect_deleted),
                get_locatie(obiect_deleted),
                result),
            lambda: delete_obiect(id, inventar)
        ])
        redo_operations.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_modify_obiect(inventar: List[dict], undo_operations: List, redo_operations: List) -> List[dict]:
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret_achizitie = float(input("Dati noul pret de achizitie: "))
        locatie = input("Dati noua locatie: ")
        obiect_modified = get_by_id(id, inventar)
        result = modify_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
        undo_operations.append([
            lambda: modify_obiect(
                id,
                get_nume(obiect_modified),
                get_descriere(obiect_modified),
                get_pret_achizitie(obiect_modified),
                get_locatie(obiect_modified),
                result),
            lambda: modify_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
        ])
        redo_operations.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def show_all(inventar: List[dict]):
    for obiect in inventar:
        print(to_string(obiect))


def ui_move_all_obiecte_to_another_locatie(inventar: List[dict]) -> List[dict]:
    try:
        location = input("Dati locatia: ")
        return move_all_obiecte_to_another_locatie(inventar, location)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_concatenation_to_all_obiecte_above_price(inventar: List[dict]) -> List[dict]:
    try:
        concat_description = input("Dati descrierea care se va adauga: ")
        price = float(input("Dati pretul de comparare: "))
        return concatenation_to_all_obiecte_above_price(inventar, concat_description, price)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_determine_maximum_price_for_every_locatie(inventar: List[dict]) -> dict:
    return determine_maximum_price_for_every_locatie(inventar)


def ui_ascending_sorting_by_price(inventar: List[dict]) -> List[dict]:
    try:
        return ascending_sorting_by_price(inventar)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return inventar


def ui_sum_for_every_location(inventar: List[dict]) -> dict:
    return ui_sum_for_every_location(inventar)


def run_menu(inventar: List[dict]):
    undo_operations = []
    redo_operations = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            inventar = ui_add_obiect(inventar, undo_operations, redo_operations)
        elif optiune == "2":
            inventar = ui_delete_obiect(inventar, undo_operations, redo_operations)
        elif optiune == "3":
            inventar = ui_modify_obiect(inventar, undo_operations, redo_operations)
        elif optiune == "4":
            inventar = ui_move_all_obiecte_to_another_locatie(inventar)
        elif optiune == "5":
            inventar = ui_concatenation_to_all_obiecte_above_price(inventar)
        elif optiune == "6":
            print(ui_determine_maximum_price_for_every_locatie(inventar))
        elif optiune == "7":
            inventar = ui_ascending_sorting_by_price(inventar)
        elif optiune == "8":
            print(ui_sum_for_every_location(inventar))
        elif optiune == "U":
            if len(undo_operations) > 0:
                operations = undo_operations.pop()
                redo_operations.append(operations)
                inventar = operations[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "R":
            if len(redo_operations) > 0:
                operations = redo_operations.pop()
                undo_operations.append(operations)
                inventar = operations[1]()
            else:
                print("Nu se poate face redo!")
        elif optiune == "A":
            show_all(inventar)
        elif optiune == "X":
            break
        else:
            print("Optiune gresita! Reincercati!")
