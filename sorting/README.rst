Sorting algorithms
==================

Implementations of sorting algorithms. Ranged according to `wiki sorting algorithms page <https://en.wikipedia.org/wiki/Sorting_algorithm>`__.

01. Insertion sort
~~~~~~~~~~~~~~~~~~

In-place sorting algorithm.
At each array-position, it checks the value there against the largest value in the sorted list (which happens to be next to it, in the previous array-position checked).
If larger, it leaves the element in place and moves to the next.
If smaller, it finds the correct position within the sorted list, shifts all the larger values up to make a space, and inserts into that correct position
(`wiki page <https://en.wikipedia.org/wiki/Insertion_sort>`__).

Two version exist:

- Non optimized - swap elements if one larger than another.
- Optimized - swap only larger elements to the right, at the end of the loop insert handled element at required position.
