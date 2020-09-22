class Heap:
    """
    Heap data structure: this is a max heap
    Heap is a COMPLETE BINARY TREE of numbers, that satisfies the heap invariant.
    Heap invariant: for each parent P, and its children L and R, there holds L < P and R < P.
    Heap implements two methods __bubble_down() and __bubble_up() to enforce the heap invariant.
    Note that the maximum number is always at the root of the heap.
    We implement heap as a list of its elements, the elements being put in the heap left to right, row by row.
    e.g. for a heap N0 (N1, N2); N1 (N3, N4), N2 (N5, N6) in the notation P (L, R) the array would be
    [N0, N1, N2, N3, N4, N5, N6]
    e.g. the heap invariant is satisfied for values [26, 17, 13, 16, 15, -1, 7]
    """

    def __init__(self, num_list):
        """
        Initializes a heap from a list of numbers:
        num_list: list of numbers to be put in the heap
        This is an efficient algorithm for heap construction that starts creating the heap from bottom upwards and
        bubbling down, as opposed to starting at root and bubbling up. The latter case would involve MANY bubble-ups
        from leaves, which would slow down the algorithm.
        """
        self.size = len(num_list)
        self.arr = self.size * [None]
        for i in reversed(range(self.size)):
            self.arr[i] = num_list[i]
            # __bubble_up() is not needed since all of the above nodes are None so far
            self.__bubble_down(i)

    def __bubble_down(self, i):
        """
        Recursively bubbles down the element i, if the heap invariant is not satisfied
        """
        # finds indices of left and right child
        lf, rt = 2*i + 1, 2*i + 2
        if lf >= self.size:
            # if i is a leaf node, just return
            return
        elif rt == self.size or self.arr[lf] >= self.arr[rt]:
            # if the node either doesn't have right child or the right child is smaller than left
            larger = lf
        else:
            # if right child is larger than left
            larger = rt
        if self.arr[i] < self.arr[larger]:
            # if the i-th node is smaller than the larger child, we swap them and recursively call the method on
            # this child node
            self.arr[i], self.arr[larger] = self.arr[larger], self.arr[i]
            self.__bubble_down(larger)

    def __bubble_up(self, i):
        """
        Recursively bubbles up the element i, if the heap invariant is not satisfied
        """
        if i == 0:
            # if i is the root node, there is nothing to bubble up
            return
        # find the parent of the i-th node
        parent = (i - 1) // 2
        if self.arr[parent] < self.arr[i]:
            # if the parent is smaller than the current node, swap them and call __bubble_up() recursively on the parent
            # index
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            self.__bubble_up(parent)

    def is_empty(self):
        """Returns True if heap is empty, False if heap is non-empty"""
        return self.size == 0

    def pop_max(self):
        """Pops the number at the top of the heap, i.e. removes it from the heap and returns it"""
        return self.__remove(0)

    def __remove(self, i):
        """Removes i-th element of the heap and readjusts the heap to satisfy the heap invariant"""
        result = self.arr[i]
        if i == self.size - 1:
            # if we are removing the last element, we can just delete it
            del self.arr[i]
            self.size -= 1
        else:
            # if we are removing non-last element, we first place the last element on the i-th index
            self.arr[i] = self.arr.pop(-1)
            self.size -= 1
            # subsequently we need to either bubble up or down to resatisfy the heap invariant
            self.__bubble_down(i)
            self.__bubble_up(i)
        return result
