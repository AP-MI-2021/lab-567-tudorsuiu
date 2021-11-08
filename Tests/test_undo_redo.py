from Logic.CRUD import add_obiect
from Logic.functionalities import undo, redo, move_all_obiecte_to_another_locatie, \
    concatenation_to_all_obiecte_above_price, ascending_sorting_by_price


def test_undo_redo_move_all_obiecte_to_another_locatie():
    inventar = []
    undo_list = []
    redo_list = []
    inventar = add_obiect("1", "o1", "o1", 1, "o1", inventar)
    undo_list.append(inventar)
    redo_list.clear()
    inventar = move_all_obiecte_to_another_locatie(inventar, "P")
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "P"}]
    inventar = undo(inventar, undo_list, redo_list)
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]
    inventar = redo(inventar, undo_list, redo_list)
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "P"}]


def test_undo_redo_concatenation_to_all_obiecte_above_price():
    inventar = []
    undo_list = []
    redo_list = []
    inventar = add_obiect("1", "o1", "o1", 1, "o1", inventar)
    inventar = add_obiect("2", "o2", "o2", 2, "o2", inventar)
    inventar = add_obiect("3", "o3", "o3", 3, "o3", inventar)
    undo_list.append(inventar)
    redo_list.clear()
    inventar = concatenation_to_all_obiecte_above_price(inventar, "t", 1)
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2t", "pret_achizitie": 2, "locatie": "o2"},
                        {"id": "3", "nume": "o3", "descriere": "o3t", "pret_achizitie": 3, "locatie": "o3"}]
    inventar = undo(inventar, undo_list, redo_list)
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"},
                        {"id": "3", "nume": "o3", "descriere": "o3", "pret_achizitie": 3, "locatie": "o3"}]
    inventar = redo(inventar, undo_list, redo_list)
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2t", "pret_achizitie": 2, "locatie": "o2"},
                        {"id": "3", "nume": "o3", "descriere": "o3t", "pret_achizitie": 3, "locatie": "o3"}]


def test_undo_redo_ascending_sorting_by_price():
    inventar = []
    undo_list = []
    redo_list = []
    inventar = add_obiect("1", "o1", "o1", 3, "o1", inventar)
    inventar = add_obiect("2", "o2", "o2", 2, "o2", inventar)
    inventar = add_obiect("3", "o3", "o3", 1, "o3", inventar)
    undo_list.append(inventar)
    redo_list.clear()
    inventar = ascending_sorting_by_price(inventar)
    assert inventar == [{"id": "3", "nume": "o3", "descriere": "o3", "pret_achizitie": 1, "locatie": "o3"},
                        {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"},
                        {"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 3, "locatie": "o1"}]
    inventar = undo(inventar, undo_list, redo_list)
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 3, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"},
                        {"id": "3", "nume": "o3", "descriere": "o3", "pret_achizitie": 1, "locatie": "o3"}]
    inventar = redo(inventar, undo_list, redo_list)
    assert inventar == [{"id": "3", "nume": "o3", "descriere": "o3", "pret_achizitie": 1, "locatie": "o3"},
                       {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"},
                       {"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 3, "locatie": "o1"}]


def test_undo_redo():
    # PUNCTUL 1
    inventar = []
    undo_list = []
    redo_list = []

    # PUNCTUL 2
    undo_list.append(inventar)
    redo_list.clear()
    inventar = add_obiect("1", "o1", "o1", 1, "o1", inventar)
    assert len(undo_list) == 1
    last = len(undo_list) - 1
    assert undo_list[last] == []

    # PUNCTUL 3
    undo_list.append(inventar)
    redo_list.clear()
    inventar = add_obiect("2", "o2", "o2", 2, "o2", inventar)
    assert len(undo_list) == 2
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]

    # PUNCTUL 4
    undo_list.append(inventar)
    redo_list.clear()
    inventar = add_obiect("3", "o3", "o3", 3, "o3", inventar)
    assert len(undo_list) == 3
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]

    # PUNCTUL 5
    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 2
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]
    assert len(redo_list) == 1
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"},
                               {"id": "3", "nume": "o3", "descriere": "o3", "pret_achizitie": 3, "locatie": "o3"}]

    # PUNCTUL 6
    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 1
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]
    assert len(redo_list) == 2
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]

    # PUNCTUL 7
    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 0
    assert inventar == []
    assert len(redo_list) == 3
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]

    # PUNCTUL 8
    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 0
    assert inventar == []
    assert len(redo_list) == 3
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]

    # PUNCTUL 9
    undo_list.append(inventar)
    redo_list.clear()
    inventar = add_obiect("1", "o1", "o1", 1, "o1", inventar)
    assert len(undo_list) == 1
    last = len(undo_list) - 1
    assert undo_list[last] == []

    undo_list.append(inventar)
    redo_list.clear()
    inventar = add_obiect("2", "o2", "o2", 2, "o2", inventar)
    assert len(undo_list) == 2
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]

    undo_list.append(inventar)
    redo_list.clear()
    inventar = add_obiect("3", "o3", "o3", 3, "o3", inventar)
    assert len(undo_list) == 3
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]

    # PUNCTUL 10
    inventar = redo(inventar, undo_list, redo_list)
    assert len(inventar) == 3
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"},
                        {"id": "3", "nume": "o3", "descriere": "o3", "pret_achizitie": 3, "locatie": "o3"}]
    assert len(undo_list) == 3
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]

    # PUNCTUL 11
    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 2
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]
    assert len(redo_list) == 1
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"},
                               {"id": "3", "nume": "o3", "descriere": "o3", "pret_achizitie": 3, "locatie": "o3"}]

    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 1
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]
    assert len(redo_list) == 2
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]

    # PUNCTUL 12
    inventar = redo(inventar, undo_list, redo_list)
    assert len(inventar) == 2
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]
    assert len(undo_list) == 2
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]

    # PUNCTUL 13
    inventar = redo(inventar, undo_list, redo_list)
    assert len(inventar) == 3
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"},
                        {"id": "3", "nume": "o3", "descriere": "o3", "pret_achizitie": 3, "locatie": "o3"}]
    assert len(undo_list) == 3
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]

    # PUNCTUL 14
    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 2
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]
    assert len(redo_list) == 1
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"},
                               {"id": "3", "nume": "o3", "descriere": "o3", "pret_achizitie": 3, "locatie": "o3"}]

    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 1
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]
    assert len(redo_list) == 2
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "2", "nume": "o2", "descriere": "o2", "pret_achizitie": 2, "locatie": "o2"}]

    # PUNCTUL 15
    undo_list.append(inventar)
    redo_list.clear()
    inventar = add_obiect("4", "o4", "o4", 4, "o4", inventar)
    assert len(undo_list) == 2
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]

    # PUNCTUL 16
    inventar = redo(inventar, undo_list, redo_list)
    assert len(inventar) == 2
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "4", "nume": "o4", "descriere": "o4", "pret_achizitie": 4, "locatie": "o4"}]
    assert len(undo_list) == 2
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]

    # PUNCTUL 17
    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 1
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]
    assert len(redo_list) == 1
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                               {"id": "4", "nume": "o4", "descriere": "o4", "pret_achizitie": 4, "locatie": "o4"}]

    # PUNCTUL 18
    inventar = undo(inventar, undo_list, redo_list)
    assert len(inventar) == 0
    assert inventar == []
    assert len(redo_list) == 2
    last = len(redo_list) - 1
    assert redo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]

    # PUNCTUL 19
    inventar = redo(inventar, undo_list, redo_list)
    assert len(inventar) == 1
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]
    assert len(undo_list) == 1
    last = len(undo_list) - 1
    assert undo_list[last] == []

    inventar = redo(inventar, undo_list, redo_list)
    assert len(inventar) == 2
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "4", "nume": "o4", "descriere": "o4", "pret_achizitie": 4, "locatie": "o4"}]
    assert len(undo_list) == 2
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]

    # PRIMUL 20
    inventar = redo(inventar, undo_list, redo_list)
    assert len(inventar) == 2
    assert inventar == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"},
                        {"id": "4", "nume": "o4", "descriere": "o4", "pret_achizitie": 4, "locatie": "o4"}]
    assert len(undo_list) == 2
    last = len(undo_list) - 1
    assert undo_list[last] == [{"id": "1", "nume": "o1", "descriere": "o1", "pret_achizitie": 1, "locatie": "o1"}]
