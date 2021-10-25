def create_obiect(id: str, nume: str, descriere: str, pret_achizitie: float, locatie: str) -> dict:
    """
    creeaza un dictionar ce retine un obiect
    :param id: id-ul obiectului - string
    :param nume: numele obiectului - string
    :param descriere: descrierea obiectului - string
    :param pret_achizitie: pretul achizitiei obiectului - float
    :param locatie: locatia obiectului - string
    :return: un dictionar ce retine un obiect
    """
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret_achizitie": pret_achizitie,
        "locatie": locatie
    }


def get_id(obiect: dict) -> str:
    """
    Determina id-ul unui obiect
    :param obiect: un dictionar de tip obiect
    :return: id-ul unui obiect
    """
    return obiect["id"]


def get_nume(obiect: dict) -> str:
    """
    Determina numele unui obiect
    :param obiect: un dictionar de tip obiect
    :return: numele unui obiect
    """
    return obiect["nume"]


def get_descriere(obiect: dict) -> str:
    """
    Determina descrierea unui obiect
    :param obiect: un dictionar de tip obiect
    :return: descrierea unui obiect
    """
    return obiect["descriere"]


def get_pret_achizitie(obiect: dict) -> float:
    """
    Determina pretul de achizitie al unui obiect
    :param obiect: un dictionar de tip obiect
    :return: pretul de achizitie al unui obiect
    """
    return obiect["pret_achizitie"]


def get_locatie(obiect: dict) -> str:
    """
    Determina locatia unui obiect
    :param obiect: un dictionar de tip obiect
    :return: locatia unui obiect
    """
    return obiect["locatie"]


def to_string(obiect: dict) -> str:
    """
    Transforma un dictionar intr-un string
    :param obiect: un dictionar de tip obiect
    :return: dictionarul obiect sub forma de string
    """
    return "id: {}, nume: {}, descriere: {}, pret achizitie: {}, locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret_achizitie(obiect),
        get_locatie(obiect)
    )
