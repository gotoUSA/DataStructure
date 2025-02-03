class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front is None:
            self.front = self.rear = Node(data)
        else:
            node = Node(data)
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        node = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return node.data

    def is_empty(self):
        return self.front is None


def reverse_queue(q: Queue) -> None:
    s = []
    while not q.is_empty():
        s.append(q.dequeue())
    while s:
        q.enqueue(s.pop())


def display(q: Queue) -> None:
    node = q.front
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def reverse_queue_recursive(q: Queue) -> None:
    if not q.is_empty():
        data = q.dequeue()
        reverse_queue_recursive(q)
        q.enqueue(data)


def josephus(n: int, k: int) -> list[int]:
    res: list[int] = []
    line: list[int] = [1 for _ in range(n)]
    i: int = -1
    for _ in range(n - 1):
        count: int = 0
        while count < k:
            i = (i + 1) % n
            if line[i]:
                count += 1
        line[i] = 0
        res.append(i + 1)

    res.append(line.index(1) + 1)
    return res


def josephus_q(n: int, k: int) -> list[int]:
    res: list[int] = []
    q = Queue()
    for i in range(n):
        q.enqueue(i + 1)
    while q.front.next:
        for _ in range(k - 1):
            q.enqueue(q.dequeue())
        res.append(q.dequeue())
    res.append(q.dequeue())
    return res


def generate_binary(n: int) -> None:
    for i in range(1, n + 1):
        print(bin(i)[2:])


def generate_binary2(n: int) -> None:
    q = Queue()
    q.enqueue("1")
    for _ in range(n):
        i = q.dequeue()
        q.enqueue(i + "0")
        q.enqueue(i + "1")
        print(i)


def solution(n: int) -> int:
    q: list[int] = [1]
    answer: int = 1
    i: int = 1
    total: int = 1
    mid: int = (n + 1) // 2
    while i < mid:
        i += 1
        total += i
        q.append(i)
        while total > n:
            total -= q.pop(0)
        if total == n:
            answer += 1
    return answer


if __name__ == "__main__":
    q = Queue()

    for i in range(3):
        q.enqueue(chr(ord("A") + i))
        print(f"Enqueue data = {q.rear.data}")
    print()

    while not q.is_empty():
        print(f"Dequeue data = {q.dequeue()}")

# print(josephus_q(10, 7))
# print(josephus(10, 7))
# generate_binary1(10)
# generate_binary(10)
# print(solution(15))
# print(solution(20))
