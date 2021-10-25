from Tests.test_CRUD import test_add_obiect, test_get_by_id, test_delete_obiect, test_modify_obiect
from Tests.test_domain import test_obiect
from Tests.test_functionalities import test_move_all_obiecte_to_another_locatie


def run_all_tests():
    test_obiect()
    test_add_obiect()
    test_get_by_id()
    test_modify_obiect()
    test_delete_obiect()
    test_move_all_obiecte_to_another_locatie()