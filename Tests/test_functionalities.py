from Domain.object import get_locatie
from Logic.CRUD import add_obiect
from Logic.functionalities import move_all_obiecte_to_another_locatie


def test_move_all_obiecte_to_another_locatie():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C2", inventar)
    inventar = add_obiect("2", "Telefon", "Tehnologie", 1000.0, "E1C1", inventar)
    inventar_nou = move_all_obiecte_to_another_locatie(inventar, "P")
    assert get_locatie(inventar_nou[0]) == "P"
    assert get_locatie(inventar_nou[1]) == "P"
