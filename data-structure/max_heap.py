"""Heap

Max Heap
"""


class MaxHeap(obj):
    def __init__(self):
        self.queue = []

    def insert(self, n):
        self.queue.append(n)
        last_index = len(self.queue) - 1

        while last_index >= 0:
            parent_index = self.parent(last_index)
            if parent_index >= 0 and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return -1
        self.swap(0, last_index)
        maxv = self.queue.pop()
        self.maxHeapify(0)

        # ongoing
