import unittest

from data_structures import Heap
import numpy as np

class MyTestCase(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)

    def test_create(self):
        num_list = [1, 4, 7, 5, -3, 2, 8, 9]
        h = Heap(num_list)
        result = [9, 5, 8, 4, -3, 2, 7, 1]
        self.assertTrue(h.arr == result, f"Heap construction failed {h.arr}")

    def test_create_many(self):
        def is_invariant_node(i, my_heap):
            if i < 0 or i >= my_heap.size:
                raise IndexError(f"Index i should be between [0 and {my_heap.size})")
            if i != 0:
                pt = (i - 1) // 2
                if my_heap.arr[pt] < my_heap.arr[i]:
                    return False
            lf, rt = 2*i + 1, 2*i + 2
            if lf >= my_heap.size:
                return True
            elif rt == my_heap.size:
                if my_heap.arr[lf] > my_heap.arr[i]:
                    return False
            else:
                if my_heap.arr[i] < max(my_heap.arr[lf], my_heap.arr[rt]):
                    return False
            return True

        def check_heap_inv(my_heap):
            is_invariant = True
            for i in range(my_heap.size):
                is_invariant = is_invariant and is_invariant_node(i, my_heap)
            return is_invariant

        n_cases = 100
        n_nums = 50
        for _ in range(n_cases):
            num_list = list(np.random.rand(n_nums))
            h = Heap(num_list)
            self.assertTrue(check_heap_inv(h), "Heap invariant check failed")

if __name__ == '__main__':
    unittest.main()
