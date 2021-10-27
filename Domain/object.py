def create_obiect(id: str, nume: str, descriere: str, pret_achizitie: float, locatie: str) -> tuple:
    """
    creeaza un dictionar ce retine un obiect
    :param id: id-ul obiectului - string
    :param nume: numele obiectului - string
    :param descriere: descrierea obiectului - string
    :param pret_achizitie: pretul achizitiei obiectului - float
    :param locatie: locatia obiectului - string
    :return: un dictionar ce retine un obiect
    """
    return (id, nume, descriere, pret_achizitie, locatie)


def get_id(obiect: tuple) -> str:
    """
    Determina id-ul unui obiect
    :param obiect: tuple
    :return: id-ul unui obiect
    """
    return obiect[0]


def get_nume(obiect: tuple) -> str:
    """
    Determina numele unui obiect
    :param obiect: un dictionar de tip obiect
    :return: numele unui obiect
    """
    return obiect[1]


def get_descriere(obiect: tuple) -> str:
    """
    Determina descrierea unui obiect
    :param obiect: un dictionar de tip obiect
    :return: descrierea unui obiect
    """
    return obiect[2]


def get_pret_achizitie(obiect: tuple) -> float:
    """
    Determina pretul de achizitie al unui obiect
    :param obiect: un dictionar de tip obiect
    :return: pretul de achizitie al unui obiect
    """
    return obiect[3]


def get_locatie(obiect: tuple) -> str:
    """
    Determina locatia unui obiect
    :param obiect: un dictionar de tip obiect
    :return: locatia unui obiect
    """
    return obiect[4]


def to_string(obiect: tuple) -> str:
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
