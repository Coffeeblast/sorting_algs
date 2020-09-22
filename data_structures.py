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