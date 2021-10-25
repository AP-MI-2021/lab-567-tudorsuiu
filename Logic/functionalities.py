from typing import List

from Domain.object import get_id, get_nume, get_pret_achizitie, get_descriere
from Logic.CRUD import modify_obiect


def move_all_obiecte_to_another_locatie(inventar: List[dict], location: str) -> List[dict]:
    """
    Muta toata obiectele din locatia initiala, intr-o locatie data
    :param inventar: lista de obiecte
    :param location: unde se vor muta obiectele - string
    :return: lista de obiecte, toate obiectele fiind mutate intr-o locatie data
    """
    inventar_modified = []
    for obiect in inventar:
        if inventar_modified == []:
            inventar_modified = modify_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect),
                                              get_pret_achizitie(obiect), location, inventar)
        else:
            inventar_modified = modify_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect),
                                              get_pret_achizitie(obiect), location, inventar_modified)
    return inventar_modified

