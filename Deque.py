
class DoubleNode():
    def __init__(self, _data):
        self.data = _data
        self.prev = None # 이전 노드를 가리키는 변수
        self.next = None # 다음 노드를 가리키는 변수

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None:
            return "Empty!"
        res = ""
        node = self.head
        while node.next is not None:
            res += str(node.data) + " ↔ "
            node = node.next
        return res + str(node.data)

    def __contains__(self, target):
        if self.head is None:
            return False
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            node = node.next
        return False
    
    def appendleft(self, data):
        if self.head is None:
            self.head = self.tail = DoubleNode(data)
        else:
            new_node = DoubleNode(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def append(self, data):
        if self.head is None:
            self.head = self.tail = DoubleNode(data)
        else:
            new_node = DoubleNode(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return node.data

    def pop(self):
        if self.tail is None:
            return None
        node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return node.data
    
    def insert(self, idx, data):
        if idx <= 0:
            self.appendleft(data)
        elif idx >= self.length:
            self.append(data)
        else:
            node = self.head
            for _ in range(idx - 1):
                node = node.next
            new_node = DoubleNode(data)
            new_node.prev = node
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
            self.length += 1
   
    def remove(self, target):
        node = self.head
        while node is not None and node.data != target:
            node = node.next
        if node is None:
            return False
        if node == self.head:
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        self.length -= 1
        return True
    
    def reverse(self):
        if self.length < 2:
            return
        prev = None
        self.tail = self.head
        ahead = self.head.next
        while ahead:
            self.head.next = prev
            self.head.prev = ahead
            prev = self.head
            self.head = ahead
            ahead = ahead.next
        self.head.next = prev
        self.head.prev = None
    

def preorder(tree):
    if not tree:
        return []
    res = []
    stack = Deque()
    stack.append(0)

    while stack:
        index = stack.pop()
        res.append(tree[index])
        index = 2 * index + 2
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index -= 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
    return res

graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]}
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}

def bfs(graph, node):
    res = []
    queue = Deque()
    queue.append(node)
    visited = set([node])
    while queue:
        u = queue.popleft()
        res.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return res



print("무방향 그래프의 너비 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", bfs(graph1, 1))
print("노드 2에서 시작: ", bfs(graph1, 2))
print()
print("방향 그래프의 너비 우선 탐색")
print("========================")
print("노드 1에서 시작: ", bfs(graph2, 1))
print("노드 2에서 시작: ", bfs(graph2, 2))