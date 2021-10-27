from Domain.object import get_locatie, get_descriere, get_id
from Logic.CRUD import add_obiect, get_by_id
from Logic.functionalities import move_all_obiecte_to_another_locatie, concatenation_to_all_obiecte_above_price, \
    ascending_sorting_by_price, determine_maximum_price_for_every_locatie, sum_for_every_location


def test_move_all_obiecte_to_another_locatie():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C2", inventar)
    inventar = add_obiect("2", "Telefon", "Tehnologie", 1000.0, "E1C1", inventar)
    inventar_nou = move_all_obiecte_to_another_locatie(inventar, "P")
    assert get_locatie(inventar_nou[0]) == "P"
    assert get_locatie(inventar_nou[1]) == "P"


def test_concatenation_to_all_obiecte_above_price():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C1", inventar)
    inventar = add_obiect("2", "Telefon", "Tehnologie", 1000.0, "E1C2", inventar)
    inventar = add_obiect("3", "Televizor", "Tehnologie", 2500.0, "E1C3", inventar)
    inventar = add_obiect("4", "Mixer", "Tehnologie", 150.0, "E1C4", inventar)
    inventar_nou = concatenation_to_all_obiecte_above_price(inventar, " >", 1200.0)
    assert get_descriere(get_by_id("1", inventar_nou)) == "Tehnologie >"
    assert get_descriere(get_by_id("3", inventar_nou)) == "Tehnologie >"


def test_determine_maximum_price_for_every_locatie():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C1", inventar)
    inventar = add_obiect("2", "Televizor", "Tehnologie", 2500.0, "E1C2", inventar)
    inventar = add_obiect("3", "Mixer", "Tehnologie", 150.0, "E1C2", inventar)
    inventar = add_obiect("4", "Telefon", "Tehnologie", 1000.0, "E1C1", inventar)
    inventar = add_obiect("5", "Tableta", "Tehnologie", 1700.0, "E1C2", inventar)
    inventar = add_obiect("6", "Masina", "Tehnologie", 15000.0, "E1C2", inventar)
    dict_with_max = determine_maximum_price_for_every_locatie(inventar)
    assert len(dict_with_max) == 2
    assert dict_with_max["E1C1"] == 1400.0
    assert dict_with_max["E1C2"] == 15000.0


def test_ascending_sorting_by_price():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C1", inventar)
    inventar = add_obiect("2", "Telefon", "Tehnologie", 1000.0, "E1C2", inventar)
    inventar = add_obiect("3", "Televizor", "Tehnologie", 2500.0, "E1C3", inventar)
    inventar = add_obiect("4", "Mixer", "Tehnologie", 150.0, "E1C4", inventar)
    inventar_ascending = ascending_sorting_by_price(inventar)
    assert get_id(inventar_ascending[0]) == "4"
    assert get_id(inventar_ascending[1]) == "2"
    assert get_id(inventar_ascending[2]) == "1"
    assert get_id(inventar_ascending[3]) == "3"


def test_sum_for_every_location():
    inventar = []
    inventar = add_obiect("1", "Laptop", "Tehnologie", 1400.0, "E1C1", inventar)
    inventar = add_obiect("2", "Televizor", "Tehnologie", 2500.0, "E1C2", inventar)
    inventar = add_obiect("3", "Mixer", "Tehnologie", 150.0, "E1C2", inventar)
    inventar = add_obiect("4", "Telefon", "Tehnologie", 1000.0, "E1C1", inventar)
    inventar = add_obiect("5", "Tableta", "Tehnologie", 1700.0, "E1C2", inventar)
    inventar = add_obiect("6", "Masina", "Tehnologie", 15000.0, "E1C2", inventar)
    dict_with_sum = sum_for_every_location(inventar)
    assert len(dict_with_sum) == 2
    assert dict_with_sum["E1C1"] == 2400.0
    assert dict_with_sum["E1C2"] == 19350.0
