from Domain.object import get_id, get_nume, get_descriere, get_pret_achizitie, get_locatie
from Logic.CRUD import add_obiect, get_by_id, delete_obiect, modify_obiect


def test_add_obiect():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C2", inventar)
    assert len(inventar) == 1
    assert get_id(get_by_id("1", inventar)) == "1"
    assert get_nume(get_by_id("1", inventar)) == "Laptop"
    assert get_descriere(get_by_id("1", inventar)) == "Tehnologie"
    assert get_pret_achizitie(get_by_id("1", inventar)) == 1400.0
    assert get_locatie(get_by_id("1", inventar)) == "E1C2"


def test_get_by_id():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C2", inventar)
    inventar = add_obiect("2", "Telefon", "Tehnologie", 1000.0, "E1C1", inventar)
    assert get_by_id("2", inventar) is not None
    assert get_by_id("6", inventar) is None


def test_modify_obiect():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C2", inventar)
    inventar = add_obiect("2", "Telefon", "Tehnologie", 1000.0, "E1C1", inventar)
    inventar_nou = modify_obiect("2", "Telefon", "Tehnologie", 450.0, "P", inventar)
    assert get_by_id("2", inventar_nou) == {
        "id": "2",
        "nume": "Telefon",
        "descriere": "Tehnologie",
        "pret_achizitie": 450.0,
        "locatie": "P"
    }


def test_delete_obiect():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C2", inventar)
    inventar = add_obiect("2", "Telefon", "Tehnologie", 1000.0, "E1C1", inventar)
    inventar = delete_obiect("2", inventar)
    assert len(inventar) == 1
    assert get_by_id("2", inventar) is None
    assert get_by_id("1", inventar) is not None
