from random import randint
from datetime import datetime


class Heap:

    def __init__(self, num_arr):
        self.size = len(num_arr)
        self.arr = self.size * [None]
        for i in range(self.size - 1, -1, -1):
            self.arr[i] = num_arr[i]
            self.bubble_down(i)

    def bubble_down(self, i):
        lf, rt = 2*i + 1, 2*i +2
        if lf >= self.size:
            return
        if rt == self.size or self.arr[lf] >= self.arr[rt]:
            larger = lf
        else:
            larger = rt
        if self.arr[i] < self.arr[larger]:
            self.arr[i], self.arr[larger] = self.arr[larger], self.arr[i]
            self.bubble_down(larger)

    def bubble_up(self, i):
        if i == 0:
            return
        parent = (i - 1) // 2
        if self.arr[parent] < self.arr[i]:
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            self.bubble_up(parent)

    def is_empty(self):
        return self.size == 0

    def pop_max(self):
        return self.remove(0)

    def remove(self, i):
        result = self.arr[i]
        if i == self.size -1:
            del self.arr[i]
            self.size -= 1
        else:
            self.arr[i] = self.arr.pop(-1)
            self.size -= 1
            self.bubble_down(i)
            self.bubble_up(i)
        return result


def get_max(num_arr):
    if len(num_arr) == 0:
        return None
    else:
        max_num = num_arr[0]
        for num in num_arr:
            if num > max_num:
                max_num = num
        return max_num


def get_min(num_arr):
    if len(num_arr) == 0:
        return None
    else:
        min_num = num_arr[0]
        for num in num_arr:
            if num < min_num:
                min_num = num
        return min_num


def bubble_sort(num_arr):
    size = len(num_arr)
    arr = [num_arr[i] for i in range(size)]
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(num_arr):
    size = len(num_arr)
    arr = [num_arr[i] for i in range(size)]
    for i in range(size - 1):
        k = 0
        c = arr[i + 1]
        for j in range(i, -1, -1):
            if c >= arr[j]:
                k = j + 1
                break
        del arr[i + 1]
        arr.insert(k, c)
    return arr


def merge_sort(num_arr):
    size = len(num_arr)
    if size <= 1:
        arr = [num_arr[i] for i in range(size)]
        return arr
    k = size // 2
    arr1 = merge_sort(num_arr[:k])
    arr2 = merge_sort(num_arr[k:])
    sz1, sz2 = len(arr1), len(arr2)
    p1 = p2 = 0
    arr = []
    while True:
        if arr1[p1] <= arr2[p2]:
            arr.append(arr1[p1])
            p1 += 1
            if p1 == sz1:
                break
        else:
            arr.append(arr2[p2])
            p2 += 1
            if p2 == sz2:
                break
    if p2 == sz2:
        arr += arr1[p1:]
    else:
        arr += arr2[p2:]
    return arr


def heap_sort(num_arr):
    hp = Heap(num_arr)
    result = []
    while not hp.is_empty():
        result.insert(0, hp.pop_max())
    return result


def quick_sort(num_arr):
    size = len(num_arr)
    arr=[num_arr[i] for i in range(size)]
    if size <= 1:
        return arr
    divider = arr[0]
    first, last = 1, size - 1
    while True:
        while first < size:
            if arr[first] > divider:
                break
            else:
                first += 1
        while last > 0:
            if arr[last] < divider:
                break
            else:
                last -= 1
        if last > first:
            arr[first], arr[last] = arr[last], arr[first]
            last -= 1
            first += 1
        else:
            arr[0], arr[last] = arr[last], arr[0]
            break
    return quick_sort(arr[0: last]) + [divider] + quick_sort(arr[last + 1:])


def counting_sort(num_arr):
    if len(num_arr) == 0:
        return []
    mn, mx = get_min(num_arr), get_max(num_arr)
    sz = mx - mn + 1
    count_arr = sz * [0]
    for num in num_arr:
        count_arr[num - mn] += 1
    arr = []
    for i in range(sz):
        arr += count_arr[i] * [mn + i]
    return arr


def bucket_sort(num_arr, bucket_num=100):
    if len(num_arr) == 0:
        return []
    mn, mx = get_min(num_arr), get_max(num_arr)
    if mn == mx:
        return [num_arr[i] for i in range(len(num_arr))]
    buckets = bucket_num * [None]
    for num in num_arr:
        k = bucket_num - 1 if num == mx else int(((num - mn)/(mx - mn)) * bucket_num)
        if buckets[k] is None:
            buckets[k] = [num]
        else:
            buckets[k].append(num)
    arr = []
    for i in range(bucket_num):
        if not(buckets[i] is None):
            if len(buckets[i]) == 1:
                arr.append(buckets[i][0])
            else:
                arr += insertion_sort(buckets[i])

    return arr


def internal_radix_sort(num_arr, base):
    sz = len(num_arr)
    arr = [num_arr[i] for i in range(sz)]
    if sz <= 1:
        return arr
    mx = get_max(num_arr)
    max_order = -1
    num = mx
    while num != 0:
        max_order += 1
        num = num // base
    divider = 1
    for _ in range(max_order + 1):
        aux = [[] for i in range(base)]
        for i in range(sz):
            k = (arr[i] // divider) % base
            aux[k].append(arr[i])
        arr = []
        for i in range(base):
            arr += aux[i]
        divider *= base
    return arr


def radix_sort(num_arr, base=10):
    plus, minus = [], []
    for num in num_arr:
        if num >= 0:
            plus.append(num)
        else:
            minus.append(-num)
    plus, minus = internal_radix_sort(plus, base=base), internal_radix_sort(minus, base=base)
    minus = [-minus[i] for i in range(len(minus))]
    return minus[:: -1] + plus


class Tests:

    @staticmethod
    def random_array(size,num_min,num_max):
        return [randint(num_min,num_max) for _ in range(size)]

    @staticmethod
    def is_sorted(arr):
        return arr == sorted(arr)

    @staticmethod
    def test(method):
        a = [3, 8, 7, 1, -6]
        print(method(a))
        print(method([5]))
        print(method([]))

    @staticmethod
    def test2(method):
        success = True
        for _ in range(100):
            b = Tests.random_array(10000, -10000000, 10000000)
            c = method(b)
            success = success and Tests.is_sorted(c)
        print(success)

    @staticmethod
    def test_heap():
        a = list(range(10))
        hp = Heap(a)
        print(hp.arr)

    @staticmethod
    def test_time():
        methods = [bubble_sort, insertion_sort, merge_sort, heap_sort]
        N_list = [1000, 10000]
        nmin, nmax = -100, 100
        for N in N_list:
            print(f'N = {N}')
            a = Tests.random_array(N, nmin, nmax)
            for method in methods:
                start = datetime.now()
                b = method(a)
                end = datetime.now()
                print(f'{method} : {end - start}')
            print()

if __name__ == '__main__':
    Tests.test2(radix_sort)
    #Tests.test_heap()
    #Tests.test_time()
