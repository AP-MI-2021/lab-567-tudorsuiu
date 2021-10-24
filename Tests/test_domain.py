from Domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret_achizitie, get_locatie


def test_obiect():
    obiect = creeaza_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C2")
    assert get_id(obiect) == "1"
    assert get_nume(obiect) == "Laptop"
    assert get_descriere(obiect) == "Tehnologie"
    assert get_pret_achizitie(obiect) == 1400.0
    assert get_locatie(obiect) == "E1C2"

