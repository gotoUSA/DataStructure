from collections import deque

"""tree = ["A", "B", "C", "D", "E", "F", None, "G"]

n = len(tree)
for i in range(n):
    if tree[i] is not None:
        print(f"Parent: {tree[i]}", end=", ")
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and tree[left] is not None:
            print(f"Left: {tree[left]}", end=", ")
        if right < n and tree[right] is not None:
            print(f"Right: {tree[right]}", end=", ")
        print()

for i in range(1, n):#루트제외
    if tree[i] is not None:
        print(f"Parent of {tree[i]}-> {tree[(i-1)//2]}")"""


def preorder(tree, i=0):
    if i < len(tree):
        print(tree[i], end=" ")
        left = 2 * i + 1
        right = left + 1
        if left < len(tree) and tree[left] is not None:
            preorder(tree, left)
        if right < len(tree) and tree[right] is not None:
            preorder(tree, right)


def inorder(tree):
    def _inorder(i=0):
        if i >= len(tree) or tree[i] is None:
            return
        _inorder(2 * i + 1)
        res.append(tree[i])
        _inorder(2 * i + 2)

    res = []
    _inorder()
    return res


def postorder(tree):
    def _postorder(i=0):
        if i >= len(tree) or tree[i] is None:
            return
        _postorder(2 * i + 1)
        _postorder(2 * i + 2)
        res.append(tree[i])

    res = []
    _postorder()
    return res


def preorder(tree):
    if not tree:
        return []
    res, stack = [], [0]

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


def inorder(tree):
    if not tree:
        return []
    index = 0
    res, stack = [], []

    while True:
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
            index = 2 * index + 1
        elif stack:
            index = stack.pop()
            res.append(tree[index])
            index = 2 * index + 2
        else:
            break
    return res


def postorder(tree):
    if not tree:
        return []
    res, stack = [], [0]

    while stack:
        index = stack.pop()
        res.append(tree[index])
        index = 2 * index + 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index += 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
    return res[::-1]  # 전위순회에서 순서만 뒤집으면 후위순회가 됨


def levelorder(tree):
    if not tree:
        return []
    res, queue = [], deque([0])

    while queue:
        index = queue.popleft()
        res.append(tree[index])
        index = 2 * index + 1
        if index < len(tree) and tree[index] is not None:
            queue.append(index)
        index += 1
        if index < len(tree) and tree[index] is not None:
            queue.append(index)
    return res


"""
tree = ["A", "B", "C", "D", "E", "F", None, "G"]
print(levelorder(tree))
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def preorder(self):
        def _preorder(node):
            if node is None:
                return
            res.append(node.data)
            _preorder(node.left)
            _preorder(node.right)

        res = []
        _preorder(self.root)
        return res

    def inorder(self):
        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            res.append(node.data)
            _inorder(node.right)

        res = []
        _inorder(self.root)
        return res

    def postorder(self):
        def _postorder(node):
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            res.append(node.data)

        res = []
        _postorder(self.root)
        return res

    def levelorder(self):
        res = []
        if not self.root:
            return res
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            res.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def make_tree(self, arr):
        if not arr:
            return
        self.root = Node(arr[0])
        q = [self.root]
        index = 1
        while q and index < len(arr):
            node = q.pop(0)
            if index < len(arr) and arr[index] is not None:
                node.left = Node(arr[index])
                q.append(node.left)
            index += 1
            if index < len(arr) and arr[index] is not None:
                node.right = Node(arr[index])
                q.append(node.right)
            index += 1


if __name__ == "__main__":
    tree = Tree()
    tree.make_tree(["A", "B", "C", "D", "E", "F", None, "G"])

    print("전위 순회 결과: ", tree.preorder())
    print("중위 순회 결과: ", tree.inorder())
    print("후위 순회 결과: ", tree.postorder())
    print("레벨 순서 순회 결과: ", tree.levelorder())
