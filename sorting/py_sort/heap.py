from __future__ import division


class MaxHeap:
    _heap = []

    def __init__(self, arr):
        for idx, entry in enumerate(arr):
            self._heap.append(entry)
            self._max_heapify_bottom_to_top(idx)

    def _max_heapify_bottom_to_top(self, idx):
        if idx == 0:
            return
        root = (idx - 1) // 2
        if self._heap[root] < self._heap[idx]:
            self._heap[root], self._heap[idx] = self._heap[idx], self._heap[root]
            self._max_heapify_bottom_to_top(root)

    def _max_heapify_top_to_bottom(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx
        arr = self._heap

        if left < len(arr) and arr[left] > arr[largest]:
            largest = left
        if right < len(arr) and arr[right] > arr[largest]:
            largest = right

        if largest != idx:
            self._heap[largest], self._heap[idx] = self._heap[idx], self._heap[largest]
            self._max_heapify_top_to_bottom(largest)

    def pop_root(self):
        if len(self.heap) == 1:
            return self._heap.pop(0)
        # swap root with last element, pop last element, normalize heap
        # less efficient version
        # self._heap[0], self._heap[self.last_idx] = self._heap[self.last_idx], self._heap[0]
        # prev_root = self._heap.pop()

        # more efficient version, only one assignment
        prev_root = self._heap.pop(0)
        self._heap.insert(0, self._heap.pop(self.last_idx))
        self._max_heapify_top_to_bottom(0)
        return prev_root

    def sorted(self):
        result = []
        while self.not_empty:
            result.append(self.pop_root())
        return result[::-1]

    @property
    def heap(self):
        return self._heap

    @property
    def last_idx(self):
        return len(self._heap) - 1

    @property
    def not_empty(self):
        return len(self._heap)


def heap_sort(data):
    return MaxHeap(data).sorted()
