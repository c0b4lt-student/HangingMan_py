from tests.is_word_found_test import is_word_found_test
from tests.tabcnt_test import tabcnt_test


def run_tests():
    if not tabcnt_test():
        return False
    if not is_word_found_test():
        return False
    return True
