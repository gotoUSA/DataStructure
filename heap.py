"""
def heappush(heap, data):
    heap.append(data)
    shift_up(heap, len(heap) - 1)


def shift_up(heap, child):
    while child > 0:
        parent = (child - 1) // 2
        if heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
        else:
            break


def heappop(heap):
    if not heap:
        return "Empty Heap."
    elif len(heap) == 1:
        return heap.pop()

    pop_data, heap[0] = heap[0], heap.pop()
    shift_down(heap, 0, len(heap))
    return pop_data


def shift_down(heap, parent, last):
    while parent < last:
        child = parent * 2 + 1
        sibling = child + 1
        if sibling < last and heap[child] > heap[sibling]:
            child = sibling
        if child < last and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
        else:
            break


def heapify(arr):
    last = len(arr) // 2
    for current in range(last - 1, -1, -1):
        shift_down(arr, current, len(arr))


if __name__ == "__main__":
    h = []
    arr = [21, 33, 17, 27, 9, 11, 14]
    for i in arr:
        heappush(h, i)

    print(f"배열의 상태: {arr}\n")
    print(f"배열의 모든 원소를 힙에 push한 상태: {h}\n")
    print("힙에서 모든 원소를 pop한 결과:", end=" ")
    while h:
        print(heappop(h), end=" ")
    print(f"\n\n빈 힙에서 원소를 pop한 결과: {heappop(h)}")
    print()

    h1 = [5, 2, 4, 1, 3]
    h2 = [3, 4, 5, 1, 2]
    h3 = [1, 5, 6, 4, 3, 8, 7, 2]
    for h in (h1, h2, h3):
        print(f"{h}를 최소 힙 구조로 만든 결과:", end=" ")
        heapify(h)
        print(h)
        print()
"""

import heapq


def solution(scoville: list[int], K: int) -> int:
    answer: int = 0
    s: list[int] = scoville[:]
    heapq.heapify(s)
    while s and s[0] < K:
        try:
            new_food = heapq.heappop(s) + heapq.heappop(s) * 2
            heapq.heappush(s, new_food)
            answer += 1
        except:
            return -1
    return answer


a = [1, 2, 3, 9, 10, 12]
k = 7
solution(a, k)
