from Tests.test_CRUD import test_add_obiect, test_get_by_id, test_delete_obiect, test_modify_obiect
from Tests.test_domain import test_obiect
from Tests.test_functionalities import test_move_all_obiecte_to_another_locatie, \
    test_concatenation_to_all_obiecte_above_price, test_determine_maximum_price_for_every_locatie, \
    test_ascending_sorting_by_price, test_sum_for_every_location
from Tests.test_undo_redo import test_undo_redo, test_undo_redo_move_all_obiecte_to_another_locatie, \
    test_undo_redo_concatenation_to_all_obiecte_above_price, test_undo_redo_ascending_sorting_by_price


def run_all_tests():
    test_obiect()
    test_add_obiect()
    test_get_by_id()
    test_modify_obiect()
    test_delete_obiect()
    test_move_all_obiecte_to_another_locatie()
    test_concatenation_to_all_obiecte_above_price()
    test_determine_maximum_price_for_every_locatie()
    test_ascending_sorting_by_price()
    test_sum_for_every_location()
    test_undo_redo()
    test_undo_redo_move_all_obiecte_to_another_locatie()
    test_undo_redo_concatenation_to_all_obiecte_above_price()
    test_undo_redo_ascending_sorting_by_price()