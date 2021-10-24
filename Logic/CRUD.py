from typing import List
from Domain.object import create_obiect, get_id


def add_obiect(id: str, nume: str, descriere: str, pret_achizitie: float, locatie: str, inventar: List[dict]) -> List[dict]:
    """
    Adauga un obiect in dictionar
    :param id: id-ul obiectului - string
    :param nume: numele obiectului - string
    :param descriere: descrierea obiectului - string
    :param pret_achizitie: pretul achizitiei obiectului - float
    :param locatie: locatia obiectului - string
    :param inventar: lista care contine toate obiectele - list
    :return: adauga un obiect in dictionar
    """
    obiect = create_obiect(id, nume, descriere, pret_achizitie, locatie)
    return inventar + [obiect]


def get_by_id(id: str, inventar: List[dict]) -> dict or None:
    """
    Ia obiectul cu id-ul dat din inventar
    :param id: string
    :param inventar: lista de obiecte
    :return: obiectul cu id-ul dat sau None, daca nu exista nicio prajitura cu id-ul dat
    """
    for obiect in inventar:
        if get_id(obiect) == id:
            return obiect
    return None


def delete_obiect(id: str, inventar: List[dict]) -> List[dict]:
    """
    Sterge un obiect din inventar dupa id
    :param id: string
    :param inventar: lista de obiecte
    :return: lista de obiecte din care se sterge obiectul cu id-ul dat
    """
    return [obiect for obiect in inventar if get_id(obiect) != id]


def modify_obiect(id: str, nume: str, descriere: str, pret_achizitie: float, locatie: str, inventar: List[dict]) -> List[dict]:
    """
    Modifica un obiect din lista
    :param id: id-ul obiectului care se modifica - string
    :param nume: noul nume al obiectului - string
    :param descriere: noua descriere a obiectului - string
    :param pret_achizitie: noul pret de achizitie al obiectului - float
    :param locatie: noua locatie a obiectului - string
    :param inventar: lista care contine toate obiectele - list
    :return: obiectul modificat in lista
    """
    inventar_modificat = []
    for obiect in inventar:
        if get_id(obiect) == id:
            obiect_nou = create_obiect(id, nume, descriere, pret_achizitie, locatie)
            inventar_modificat.append(obiect_nou)
        else:
            inventar_modificat.append(obiect)
    return inventar_modificat
