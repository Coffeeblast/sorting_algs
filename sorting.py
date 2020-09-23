from data_structures import Heap


def __get_max(num_arr):
    """
    Returns maximum of list of numbers num_arr or None if the list is empty
    """
    if len(num_arr) == 0:
        return None
    else:
        max_num = num_arr[0]
        for num in num_arr:
            if num > max_num:
                max_num = num
        return max_num


def __get_min(num_arr):
    """
    Returns minimum of list of numbers num_arr or None if the list is empty
    """
    if len(num_arr) == 0:
        return None
    else:
        min_num = num_arr[0]
        for num in num_arr:
            if num < min_num:
                min_num = num
        return min_num


def bubble_sort(num_arr):
    """
    Returns num_arr sorted in ascending fashion. The original array is not modified.
    Sorting is implemented using bubble sort algorithm.
    The algorithm has O(n ** 2) complexity.
    How it works: for every element of the array, two neighbouring elements are swapped if they are sorted incorrectly
        relative to each other (they "bubble over" each other). This is repeated n-times for an array of size n. i-th
        iteration of bubbling over requires only first n - i - 1 elements to be bubbled, as the rest of the array will
        already be sorted.
    This implementation conserves the order of equal elements ("stable sort").
    """
    size = len(num_arr)
    arr = [num_arr[i] for i in range(size)]
    for i in range(size - 1):
        # size - 1 iterations of the bubbling procedure
        for j in range(size - 1 - i):
            # each iteration is ended at j = size - i - 2
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(num_arr):
    """
    Returns num_arr sorted in ascending fashion. The original array is not modified.
    Sorting is implemented using insertion sort algorithm.
    The algorithm has O(n ** 2) complexity.
    How it works: we iteratively sort the the array, after i-th iterations first i + 1 elements of the array will be
        sorted. In each iteration we take the last element and scan over the previous elements (which are already
        sorted) to find the proper place for it. The scanning is done from current last element working our way
        backwards.
    This implementation conserves the order of equal elements ("stable sort").
    """
    size = len(num_arr)
    arr = [num_arr[i] for i in range(size)]
    for i in range(size - 1):
        # remember the number "c" we wish to add to the "sorted part" in the current iteration
        c = arr[i + 1]
        # we will eventually insert "c" at index k, set it as 0 in case "c" is current minimum and the following if
        # statement is never True
        k = 0
        for j in range(i, -1, -1):
            # scan over the sorted part from last element j = i to first element j = 0 to find the point where "c"
            # becomes larger or equal to the current element
            if c >= arr[j]:
                k = j + 1
                break
        # delete the element "c" from its original place and insert it to position k
        del arr[i + 1]
        arr.insert(k, c)
    return arr


def merge_sort(num_arr):
    """
    Returns num_arr sorted in ascending fashion. The original array is not modified.
    Sorting is implemented using merge sort algorithm.
    The algorithm has O(n * log(n)) complexity.
    How it works: The algorithm works by splitting array in two, sorting each half by itself, and "sewing" them back
        together" appropriately. Sorting of the halves is done recursively. Trivial case of recursion occurs when the
        array is either empty or contains just one number. The sewing step is performed by traversing arr1 with index p1
        and arr2 with index p2. Values at current indices are compared, the lesser one is picked and writen into the
        result. The corresponding index is then incremented by 1.
    This implementation conserves the order of equal elements ("stable sort").
    """
    size = len(num_arr)
    if size <= 1:
        # trivial case of the induction
        arr = [num_arr[i] for i in range(size)]
        return arr
    k = size // 2
    # splitting of the array and performing recursive step
    arr1 = merge_sort(num_arr[:k])
    arr2 = merge_sort(num_arr[k:])
    sz1, sz2 = len(arr1), len(arr2)
    p1 = p2 = 0
    arr = []
    while True:
        # traversing arr1 with index p1 and arr2 with index p2
        if arr1[p1] <= arr2[p2]:
            # writing element from arr1 to arr and incrementing index p1
            arr.append(arr1[p1])
            p1 += 1
            if p1 == sz1:
                # break the loop if whole arr1 was traversed
                break
        else:
            # writing element from arr2 to arr and incrementing index p2
            arr.append(arr2[p2])
            p2 += 1
            if p2 == sz2:
                # break the loop if whole arr2 was traversed
                break
    # write the rest of the elements of the array whose traversion was left unfinished into arr
    if p2 == sz2:
        arr += arr1[p1:]
    else:
        arr += arr2[p2:]
    return arr


def heap_sort(num_arr):
    """
    Returns num_arr sorted in ascending fashion. The original array is not modified.
    Sorting is implemented using heap sort algorithm.
    The algorithm has O(n * log(n)) complexity.
    How it works: The array is put into max heap. The root of max heap is always the largest number. The sorting is done
        by repeated popping of the root.
    This implementation does not conserve the order of equal elements ("unstable sort").
    """
    hp = Heap(num_arr)
    result = []
    while not hp.is_empty():
        result.insert(0, hp.pop_max())
    return result


def quick_sort(num_arr):
    """
    Returns num_arr sorted in ascending fashion. The original array is not modified.
    Sorting is implemented using quick sort algorithm.
    The algorithm has average O(n * log(n)) complexity but worst-case O(n ** 2) complexity.
    How it works: The zero-th element of the array is designated "divider", it divides rest of the array into numbers
        greater than divider and smaller than divider. The equals can be placed in either group. The division into
        groups is performed by traversing array from index 1 forwards (we denote this index "first") and from the last
        index backwards (we denote this index "last"). When elements are find such that (i) arr[first] > divider and
        (ii) arr[last] < divider, one of two situations has happened:
        1. first < last: we swap the elements
        2. first > last: all elements between 1 and last are less or equal to divider and all elements after last are
            greater or equal to divider. When situation 2. occurs we can break the loop, call recursively quick sort
            on both of the groups and then "sew" the result back together.
    This implementation does not conserve the order of equal elements ("unstable sort").
    """
    size = len(num_arr)
    arr = [num_arr[i] for i in range(size)]
    if size <= 1:
        # trivial case of the recursion
        return arr
    divider = arr[0]
    # initialize two index variables at the beginning after divider and end of the array
    first, last = 1, size - 1
    while True:
        while first < size:
            # progress with first index forward, until you encounter a number larger than divider
            if arr[first] > divider:
                break
            else:
                first += 1
        while last > 0:
            # progress with the last index backward, until you encounter a number smaller than a divider
            if arr[last] < divider:
                break
            else:
                last -= 1
        if last > first:
            # if indices haven't crossed each other, swap the corresponding numbers
            arr[first], arr[last] = arr[last], arr[first]
            last -= 1
            first += 1
        else:
            # if indices have crossed each other, swap the number corresponding to the last index with the divider
            # and break the loop
            arr[0], arr[last] = arr[last], arr[0]
            break
    # recursively sort the group that is smaller than the divider, as well as the group that is larger than the divider
    # and sew the sorted groups back together
    return quick_sort(arr[0: last]) + [divider] + quick_sort(arr[last + 1:])


def counting_sort(num_arr):
    """
    Returns num_arr sorted in ascending fashion. The original array is not modified.
    Sorting is implemented using counting sort algorithm.
    The algorithm has O(n + m) complexity, where n is number of elements in the array and m is difference between max
    and min element.
    How it works: a counting array of size (max - min + 1) is created, each slot in the counting array corresponding
        to the number of occurrences of the corresponding integer between max and min. At first, the original array is
        traversed and slot corresponding to each element is incremented by 1. Then, the counting array is traverse, and
        the sorted version of the original values is recreated according to number of occurrences of each value stored
        in the counting array.
    This implementation does not conserve the order of equal elements ("unstable sort").
    Note: this algorithm can be used only for sorting of integers.
    Note: this algorithm can be slow if the range of values is much larger than size of the array.
    """
    if len(num_arr) == 0:
        return []
    mn, mx = __get_min(num_arr), __get_max(num_arr)
    sz = mx - mn + 1
    # initialize the counting array with zeros
    count_arr = sz * [0]
    for num in num_arr:
        # traverse the original array and increment the counter at corresponding position in the counting array
        count_arr[num - mn] += 1
    arr = []
    for i in range(sz):
        # reassemble the sorted version of num_arr
        arr += count_arr[i] * [mn + i]
    return arr


def bucket_sort(num_arr, bucket_num=100):
    """
    Returns num_arr sorted in ascending fashion. The original array is not modified.
    Sorting is implemented using bucket sort algorithm.
    The algorithm has O(m * individual_bucket_sorting_complexity) complexity, where m is number of buckets. In our
        implementation, individual_bucket_sorting_complexity is n ** 2, since we used insertion sort as the sorting
        method for individual buckets.
    How it works: in the first step, we divide the interval between maximum and minimum of the array to N equal
        intervals, called "buckets", and traverse the array, stuffing each number into its corresponding bucket. Next
        we sort elements in each bucket individually and subsequently glue the sorted arrays together. For sorting of
        individual buckets, some other algorithm shall be chosen, e.g. insertion sort in our case.
    This implementation does not conserve the order of equal elements ("unstable sort").
    Note: the "bucket improvement" is most efficient if the numbers we want to sort are distributed rather
        homogeneously. In worst case, when all numbers fall into the same bucket and we actually get a worse
        performance.
    """
    if len(num_arr) == 0:
        return []
    mn, mx = __get_min(num_arr), __get_max(num_arr)
    if mn == mx:
        # special case, when we get an array of equal numbers
        return [num_arr[i] for i in range(len(num_arr))]
    # buckets is list of lists, each inner list corresponding to a different bucket
    buckets = bucket_num * [None]
    for num in num_arr:
        # find out into which bucket num belongs
        k = bucket_num - 1 if num == mx else int(((num - mn)/(mx - mn)) * bucket_num)
        # add num into the corresponding bucket
        if buckets[k] is None:
            buckets[k] = [num]
        else:
            buckets[k].append(num)
    arr = []
    for i in range(bucket_num):
        # sort numbers in each individual bucket and glue the buckets back together
        if buckets[i] is not None:
            if len(buckets[i]) == 1:
                arr.append(buckets[i][0])
            else:
                # insertion sort is used as a method for sorting individual buckets. This can be replaced by any other
                # sorting method
                arr += insertion_sort(buckets[i])
    return arr


def __internal_radix_sort(num_arr, base):
    """
    Sorts array of num_arr of non-negative integers.
    Arguments:
        num_arr --> array of non-negative integers
        base --> base into which the numbers are decomposed, integer >= 2
    How it works: the integers are written in a specific base, e.g. base 10. Then the numbers are sorted according to
        the digits (in this order !!!) base ** 0, base ** 1 ... base ** max_order. The result is an array sorted in
        ascending order.
    This implementation conserves the order of equal elements (stable sort).
    Note: this method can sort only INTEGERS, and only NON-NEGATIVE ones.
    """
    sz = len(num_arr)
    arr = [num_arr[i] for i in range(sz)]
    if sz <= 1:
        # trivial case
        return arr
    mx = __get_max(num_arr)
    max_order = -1
    num = mx
    # determine order of maximum non-zero digit, base ** max_order is the maximum base element that occurs with non-zero
    # component
    while num != 0:
        max_order += 1
        num = num // base
    # divisor describes current order against which we are sorting. It is always power of base, starting with
    # base ** 0 = 1
    divisor = 1
    for _ in range(max_order + 1):
        # set up array of buckets corresponding to different digits 0, 1 ... base - 1
        aux = [[] for _ in range(base)]
        for i in range(sz):
            # k is digit standing before divisor in the current number
            k = (arr[i] // divisor) % base
            # put the number into k-th bucket
            aux[k].append(arr[i])
        arr = []
        # reassemble the array with digits of current order sorted
        for i in range(base):
            arr += aux[i]
        # move to the next digit to the left
        divisor *= base
    return arr


def radix_sort(num_arr, base=10):
    """
    Returns num_arr sorted in ascending fashion. The original array is not modified.
    Sorting is implemented using radix sort algorithm.
    Arguments:
        num_arr --> array of non-negative integers
        base --> base into which the numbers are decomposed, integer >= 2, default: 10
    The algorithm has O(n * max_order) complexity, n is number of sorted elements and max_order order corresponding to
        the maximum non-zero digit in the array.
    How it works: the numbers are separated to non-negative ("plus") and negative ("minus"). Negative numbers are
        converted to positive by multiplying with -1, and both groups are sorted using the hierarchy provided by their
        decomposition into base "base" (this is known as radix sort and we implemented it in the method
        __internal_radix_sort()).
    This implementation conserves the order of equal elements ("stable sort").
    """
    # divide the numbers to non-negative and negative
    plus, minus = [], []
    for num in num_arr:
        if num >= 0:
            plus.append(num)
        else:
            # convert negative numbers to positive
            minus.append(-num)
    # sort each group using __internal_radix_sort
    plus, minus = __internal_radix_sort(plus, base=base), __internal_radix_sort(minus, base=base)
    # convert negative numbers back to negative
    minus = [-minus[i] for i in range(len(minus))]
    # glue the result together
    return minus[:: -1] + plus
