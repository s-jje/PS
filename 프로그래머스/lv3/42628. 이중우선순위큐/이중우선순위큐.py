from collections import Counter
import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    min_heap_removed = []
    max_heap_removed = []

    for operation in operations:
        op, val = operation.split()
        val = int(val)

        if op == 'I':
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
        elif op == 'D':
            if val == -1 and min_heap:
                min_heap_removed.append(heapq.heappop(min_heap))
            elif val == 1 and max_heap:
                max_heap_removed.append(-heapq.heappop(max_heap))

            if not min_heap or not max_heap:
                min_heap.clear()
                max_heap.clear()
                min_heap_removed.clear()
                max_heap_removed.clear()

    min_heap = list(Counter(min_heap) - Counter(max_heap_removed))
    heapq.heapify(min_heap)
    max_heap = list(Counter(max_heap) - Counter(min_heap_removed))
    heapq.heapify(max_heap)

    min_val, max_val = 0, 0
    if min_heap:
        min_val = min_heap[0]

    if max_heap:
        max_val = -max_heap[0]

    return [max_val, min_val]