##Sorting algorithms - documentation

Provides for-practice implementation of basic sorting algorithms. algorithms
are placed in the file _sorting.py_. Apart from that there is also 
the file _data_structures.py_ which contains simple implementation 
of max-heap we use in heap sort. 

The details of how the sorting algorithms work can be found e.g. in a nice
course by Shai Simonson on [Youtube](https://www.youtube.com/watch?v=Z3J-PN2WrE8&ab_channel=ArjunSuresh). 

####_bubble_sort(num_arr)_

Returns _num_arr_ sorted in ascending fashion. The original array is not modified.
Sorting is implemented using bubble sort algorithm.
The algorithm has _O(n ** 2)_ complexity.

_How it works_: for every element of the array, two neighbouring elements are swapped if they are sorted incorrectly
relative to each other (they "bubble over" each other). This is repeated _n_-times for an array of size n. i-th
iteration of bubbling over requires only first _n - i - 1_ elements to be bubbled, as the rest of the array will
already be sorted.

This implementation conserves the order of equal elements ("stable sort").

####_insertion_sort(num_arr)_

Returns _num_arr_ sorted in ascending fashion. The original array is not modified.
Sorting is implemented using insertion sort algorithm.
The algorithm has _O(n ** 2)_ complexity.

_How it works:_ we iteratively sort the the array, after _i_-th iterations first _i + 1_ elements of the array will be
sorted. In each iteration we take the last element and scan over the previous elements (which are already
sorted) to find the proper place for it. The scanning is done from current last element working our way
backwards.

This implementation conserves the order of equal elements ("stable sort").

####_merge_sort(num_arr)_

Returns _num_arr_ sorted in ascending fashion. The original array is not modified.
Sorting is implemented using merge sort algorithm.
The algorithm has _O(n * log(n))_ complexity.

_How it works:_ The algorithm works by splitting array in two, sorting each half by itself, and "sewing" them back
together" appropriately. Sorting of the halves is done recursively. Trivial case of recursion occurs when the
array is either empty or contains just one number. The sewing step is performed by traversing _arr1_ with index _p1_
and _arr2_ with index _p2_. Values at current indices are compared, the lesser one is picked and writen into the
result. The corresponding index is then incremented by _1_.

This implementation conserves the order of equal elements ("stable sort").

####_heap_sort(num_arr)_

Returns _num_arr_ sorted in ascending fashion. The original array is not modified.
Sorting is implemented using heap sort algorithm.
The algorithm has _O(n * log(n))_ complexity.

_How it works:_ The array is put into max heap. The root of max heap is always the largest number. The sorting is done
by repeated popping of the root.

This implementation does not conserve the order of equal elements ("unstable sort").

####_quick_sort(num_arr)_

Returns _num_arr_ sorted in ascending fashion. The original array is not modified.
Sorting is implemented using quick sort algorithm.
The algorithm has average _O(n * log(n))_ complexity but worst-case _O(n ** 2)_ complexity.

_How it works:_ The zero-th element of the array is designated _divider_, it divides rest of the array into numbers
greater than _divider_ and smaller than _divider_. The equals can be placed in either group. The division into
groups is performed by traversing array from index _1_ forwards (we denote this index _first_) and from the last
index backwards (we denote this index _last_). When elements are find such that (i) _arr[first] > divider_ and
(ii) _arr[last] < divider_, one of two situations has happened:
1. _first < last_: we swap the elements
2. _first > last_: all elements between _1_ and _last_ are less or equal to _divider_ and all elements after _last_ are
greater or equal to _divider_. When situation _2_ occurs we can break the loop, call recursively quick sort
on both of the groups and then "sew" the result back together.

This implementation does not conserve the order of equal elements ("unstable sort").

####_counting_sort(num_arr)_

Returns _num_arr_ sorted in ascending fashion. The original array is not modified.
Sorting is implemented using counting sort algorithm.
The algorithm has _O(n + m)_ complexity, where _n_ is number of elements in the array and _m_ is difference between max
and min element.

_How it works:_ a counting array of size _(max - min + 1)_ is created, each slot in the counting array corresponding
to the number of occurrences of the corresponding integer between _max_ and _min_. At first, the original array is
traversed and slot corresponding to each element is incremented by _1_. Then, the counting array is traverse, and
the sorted version of the original values is recreated according to number of occurrences of each value stored
in the counting array.

This implementation does not conserve the order of equal elements ("unstable sort").

Note: this algorithm can be used only for sorting of integers.  
Note: this algorithm can be slow if the range of values is much larger than size of the array.

####_bucket_sort(num_arr, bucket_num=100)_

Returns _num_arr_ sorted in ascending fashion. The original array is not modified.
Sorting is implemented using bucket sort algorithm.
The algorithm has _O(m * individual_bucket_sorting_complexity)_ complexity, where m is number of buckets. In our
implementation, individual_bucket_sorting_complexity is _n ** 2_, since we used insertion sort as the sorting
method for individual buckets.

_How it works:_ in the first step, we divide the interval between maximum and minimum of the array to N equal
intervals, called "buckets", and traverse the array, stuffing each number into its corresponding bucket. Next
we sort elements in each bucket individually and subsequently glue the sorted arrays together. For sorting of
individual buckets, some other algorithm shall be chosen, e.g. insertion sort in our case.

This implementation does not conserve the order of equal elements ("unstable sort").

Note: the "bucket improvement" is most efficient if the numbers we want to sort are distributed rather
homogeneously. In worst case, when all numbers fall into the same bucket and we actually get a worse
performance.

####_radix_sort(num_arr, base=10)_

Returns _num_arr_ sorted in ascending fashion. The original array is not modified.
Sorting is implemented using radix sort algorithm.

Arguments:  
_num_arr_ --> array of non-negative integers  
_base_ --> base into which the numbers are decomposed, integer >= 2, default: 10  
The algorithm has _O(n * max_order)_ complexity, _n_ is number of sorted elements and max_order order corresponding to
the maximum non-zero digit in the array.

_How it works:_ the numbers are separated to non-negative ("plus") and negative ("minus"). Negative numbers are
converted to positive by multiplying with _-1_, and both groups are sorted using the hierarchy provided by their
decomposition into base "base" (this is known as radix sort and we implemented it in the method
___internal_radix_sort()_).

This implementation conserves the order of equal elements ("stable sort").
