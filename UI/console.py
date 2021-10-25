from typing import List

from Domain.object import to_string
from Logic.CRUD import add_obiect, delete_obiect, modify_obiect
from Logic.functionalities import move_all_obiecte_to_another_locatie


def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locatie in alta locatie data")
    print("A. Afisarea tuturor obiectelor")
    print("X. Iesire")


def ui_add_obiect(inventar: List[dict]) -> List[dict]:
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret_achizitie = float(input("Dati pretul de achizitie: "))
    locatie = input("Dati locatia: ")
    return add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)


def ui_delete_obiect(inventar: List[dict]) -> List[dict]:
    id = input("Dati id-ul obiectului de sters: ")
    return delete_obiect(id, inventar)

def ui_modify_obiect(inventar):
    id = input("Dati id-ul obiectului de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret_achizitie = float(input("Dati noul pret de achizitie: "))
    locatie = input("Dati noua locatie: ")
    return modify_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)


def show_all(inventar: List[dict]):
    for obiect in inventar:
        print(to_string(obiect))


def run_menu(inventar: List[dict]):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            inventar = ui_add_obiect(inventar)
        elif optiune == "2":
            inventar = ui_delete_obiect(inventar)
        elif optiune == "3":
            inventar = ui_modify_obiect(inventar)
        elif optiune == "4":
            location = input("Dati locatia: ")
            print(move_all_obiecte_to_another_locatie(inventar, location))
        elif optiune == "A":
            show_all(inventar)
        elif optiune == "X":
            break
        else:
            print("Optiune gresita! Reincercati!")