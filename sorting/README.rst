Sorting algorithms
==================

Implementations of sorting algorithms. Ranged according to `wiki sorting algorithms page <https://en.wikipedia.org/wiki/Sorting_algorithm>`__.

01. Insertion sort
~~~~~~~~~~~~~~~~~~

At each array-position, it checks the value there against the largest value in the sorted list (which happens to be next to it, in the previous array-position checked).
If larger, it leaves the element in place and moves to the next.
If smaller, it finds the correct position within the sorted list, shifts all the larger values up to make a space, and inserts into that correct position
(`wiki page <https://en.wikipedia.org/wiki/Insertion_sort>`__).

Pros:

- Adaptive(efficient for data sets that are already substantially sorted)
- Stable
- In-place
- Online

Cons:

- More number of writes compare to the Selection Sort

Optimization:

- Swap only larger elements to the right, at the end of the loop insert handled element at required position.

.. image:: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif

02. Selection sort
~~~~~~~~~~~~~~~~~~

The algorithm proceeds by finding the smallest element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right(`wiki page <https://en.wikipedia.org/wiki/Selection_sort>`__).

Pros:

- In-place
- Less number of writes compare to Insertion Sort

Cons:

- Not stable by default

.. image:: https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif

03. Merge Sort
~~~~~~~~~~~~~~

- Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
- Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.

Pros:

- *O(n log(n))* complexity
- Stable
- Parallelizes well

Cons:

- By default use *O(n)* additional space

.. image:: https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif

Python uses `Timsort <https://en.wikipedia.org/wiki/Timsort>`__, tuned hybrid of merge sort and insertion sort.

04. Heap Sort
~~~~~~~~~~~~~

Heapsort can be thought of as an improved selection sort. This algorithm:

- build heap structure based on data
- N times take a root(*O(log(n))*) and rearrange the heap

Pros:

- Can be performed in place

Cons:

- Not stable

Optimization:

- Use ternary heap

.. image:: https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif

05. Quick sort
~~~~~~~~~~~~~~

Relies on a partition operation: to partition an array an element called a pivot is selected. All elements smaller than the pivot are moved before it and all greater elements are moved after it.
The lesser and greater sublists are then recursively sorted. 

Pros:

- Can be performed in place
- Amenable to parallelization

Cons:

- O(n^2) worst-case complexity
- Not stable

Optimization:

- Use random or median pivot
- Middle index form medians can be rewritten from ``(lo + hi)/2`` to ``lo + (hi - lo) / 2``
- Return also array of values equal to pivot
- To make sure at most *O(log n)* space is used, recurse first into the smaller side of the partition


.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Quicksort-diagram.svg/300px-Quicksort-diagram.svg.png


06. Bubble sort
~~~~~~~~~~~~~~~
The algorithm starts at the beginning of the data set. It compares the first two elements, and if the first is greater than the second, it swaps them. It continues doing this for each pair of adjacent elements to the end of the data set. It then starts again with the first two elements, repeating until no swaps have occurred on the last pass.

Pros:

- Useful for sorted or nearly sorted arrays

.. image:: https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif
