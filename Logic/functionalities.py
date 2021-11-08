from typing import List

from Domain.object import get_id, get_nume, get_pret_achizitie, get_descriere, get_locatie
from Logic.CRUD import modify_obiect


def move_all_obiecte_to_another_locatie(inventar: List[dict], location: str) -> List[dict]:
    """
    Muta toata obiectele din locatia initiala, intr-o locatie data
    :param inventar: lista de obiecte
    :param location: unde se vor muta obiectele - string
    :return: lista de obiecte, toate obiectele fiind mutate intr-o locatie data
    """
    inventar_modified = inventar[:]
    for obiect in inventar:
        if not inventar_modified:
            inventar_modified = modify_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect),
                                              get_pret_achizitie(obiect), location, inventar_modified)
        else:
            inventar_modified = modify_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect),
                                              get_pret_achizitie(obiect), location, inventar_modified)
    return inventar_modified


def concatenation_to_all_obiecte_above_price(inventar: List[dict], concat_description: str, price: float) -> List[dict]:
    """
    Concateneaza un string citit la toate descrierile obiectelor cu pretul mai mare decat o valoare citita
    :param inventar: lista de obiecte
    :param concat_description: sirul de caractere ce se va adauga descrierii - string
    :param price: pretul care va fi adaugat - float
    :return: lista de obiecte modificata
    """
    inventar_modified = inventar[:]
    for obiect in inventar:
        if get_pret_achizitie(obiect) > price:
            inventar_modified = modify_obiect(get_id(obiect), get_nume(obiect),
                                              get_descriere(obiect) + concat_description, get_pret_achizitie(obiect),
                                              get_locatie(obiect), inventar_modified)
        else:
            inventar_modified = modify_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect),
                                              get_pret_achizitie(obiect), get_locatie(obiect), inventar_modified)
    return inventar_modified


def determine_maximum_price_for_every_locatie(inventar: List[dict]) -> dict:
    """
    Determina cel mai mare pret de achizitie din fiecare locatie
    :param inventar: lista de obiecte
    :return: lista cu locatiile si pretul de achizitie maxim din fiecare locatie
    """
    result = {}
    for obiect in inventar:
        locatie = get_locatie(obiect)
        pret = get_pret_achizitie(obiect)
        if locatie in result:
            if pret > result[locatie]:
                result[locatie] = pret
        else:
            result[locatie] = pret
    return result


def ascending_sorting_by_price(inventar: List[dict]) -> List[dict]:
    """
    Ordoneaza crescator obiectele dupa pretul de achizitie
    :param inventar: lista de obiecte
    :return: lista de obiecte modificata
    """
    inventar_ascending = inventar[:]
    inventar_ascending.sort(key=get_pret_achizitie)
    return inventar_ascending


def sum_for_every_location(inventar: List[dict]) -> dict:
    """
    Determina suma preturilor pentru fiecare locatie
    :param inventar: lista de obiecte
    :return: suma preturilor pentru fiecare locatie
    """
    result = {}
    for obiect in inventar:
        locatie = get_locatie(obiect)
        pret = get_pret_achizitie(obiect)
        if locatie in result:
            result[locatie] += pret
        else:
            result[locatie] = pret
    return result


def undo(inventar: List[dict], undo_list: List, redo_list: List) -> List:
    """
    Determina ultima forma a inventarului inainte de a se efectua ultima operatie
    :param inventar: lista de obiecte
    :param undo_list: lista care memoreaza inventarul dupa fiecare operatie
    :param redo_list: lista care memoreaza inventarul dupa fiecare undo
    :return: inventarul inainte de a se efectua ultima operatie
    """
    if len(undo_list) > 0:
        redo_list.append(inventar)
        return undo_list.pop()
    else:
        return inventar


def redo(inventar: List[dict], undo_list: List, redo_list: List) -> List:
    """
    Determina ultima forma a inventarului inainte de a se efectua ultimul undo
    :param inventar: lista de obiecte
    :param undo_list: lista care memoreaza inventarul dupa fiecare operatie
    :param redo_list: lista care memoreaza inventarul dupa fiecare undo
    :return: inventarul inainte de a se efectua ultimul undo
    """
    if len(redo_list) > 0:
        undo_list.append(inventar)
        return redo_list.pop()
    else:
        return inventar
