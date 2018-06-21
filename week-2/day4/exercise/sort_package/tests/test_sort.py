from unittest import TestCase

import bubble_sort


class TestSort(TestCase):
    def test_is_string(self):
        a_list = [5, 1, 90, 54, 72, 39, 20]
        self.assertEqual(bubble_sort(a_list), [1, 5, 20, 39, 54, 72, 90])
