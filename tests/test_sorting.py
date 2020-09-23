import unittest
from sorting import *
import numpy as np


class MyTestCase(unittest.TestCase):
    def setUp(self):
        np.random.seed()

    def test_bubble(self):
        arr_size = 50
        n_tests = 100
        for _ in range(n_tests):
            arr = list(np.random.rand(arr_size))
            arr_bubble = bubble_sort(arr)
            arr_sorted = sorted(arr)
            self.assertTrue(arr_bubble == arr_sorted, "Array was bubble-sorted incorrectly")

    def test_insertion(self):
        arr_size = 50
        n_tests = 100
        for _ in range(n_tests):
            arr = list(np.random.rand(arr_size))
            arr_insertion = insertion_sort(arr)
            arr_sorted = sorted(arr)
            self.assertTrue(arr_insertion == arr_sorted, "Array was insertion-sorted incorrectly")

    def test_merge(self):
        arr_size = 50
        n_tests = 100
        for _ in range(n_tests):
            arr = list(np.random.rand(arr_size))
            arr_merge = merge_sort(arr)
            arr_sorted = sorted(arr)
            self.assertTrue(arr_merge == arr_sorted, "Array was merge-sorted incorrectly")

    def test_heap(self):
        arr_size = 50
        n_tests = 100
        for _ in range(n_tests):
            arr = list(np.random.rand(arr_size))
            arr_heap = heap_sort(arr)
            arr_sorted = sorted(arr)
            self.assertTrue(arr_heap == arr_sorted, "Array was heap-sorted incorrectly")

    def test_quick(self):
        arr_size = 50
        n_tests = 100
        for _ in range(n_tests):
            arr = list(np.random.rand(arr_size))
            arr_quick = quick_sort(arr)
            arr_sorted = sorted(arr)
            self.assertTrue(arr_quick == arr_sorted, "Array was quick-sorted incorrectly")

    def test_counting(self):
        arr_size = 50
        min_int = -100
        max_int = 100
        n_tests = 100
        for _ in range(n_tests):
            arr = list(np.random.randint(min_int, max_int, arr_size))
            arr_count = counting_sort(arr)
            arr_sorted = sorted(arr)
            self.assertTrue(arr_count == arr_sorted, "Array was counting-sorted incorrectly")

    def test_bucket(self):
        arr_size = 50
        n_tests = 100
        for _ in range(n_tests):
            arr = list(np.random.rand(arr_size))
            arr_bucket = bucket_sort(arr)
            arr_sorted = sorted(arr)
            self.assertTrue(arr_bucket == arr_sorted, "Array was bucket-sorted incorrectly")

    def test_radix(self):
        arr_size = 50
        min_int = -10000000
        max_int = 10000000
        n_tests = 100
        for _ in range(n_tests):
            arr = list(np.random.randint(min_int, max_int, arr_size))
            arr_radix = radix_sort(arr)
            arr_sorted = sorted(arr)
            self.assertTrue(arr_radix == arr_sorted, "Array was radix-sorted incorrectly")


if __name__ == '__main__':
    unittest.main()
