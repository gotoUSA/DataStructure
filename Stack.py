class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


# 스트링 뒤집기
def reverse_word(word: str) -> str:
    answer: str = ""
    s = Stack()
    for w in word:
        s.push(w)
    while not s.is_empty():
        answer += s.pop()
    return answer


# 괄호 확인
def check_bracket(expression: str) -> bool:
    brackets: dict[str, str] = {")": "(", "}": "{", "]": "["}
    s = Stack()
    for exp in expression:
        if exp in brackets.values():
            s.push(exp)
        elif exp in brackets:
            pop_bracket = s.pop()
            if not pop_bracket or pop_bracket != brackets[exp]:
                return False
    return True if s.is_empty() else False


# 후위 표기법
def to_postfix(expression: str) -> str:
    op: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2}
    res: str = ""
    s = Stack()
    for exp in expression:
        if exp.isnumeric():
            res += exp
        elif exp in op:
            if not s.is_empty() and (op[exp] <= op[s.peek()]):
                res += s.pop()
            s.push(exp)
    while not s.is_empty():
        res += s.pop()
    return res


def find_nge(arr: list[int]) -> list[int]:
    n: int = len(arr)
    s: list[int] = []
    res: list[int] = [-1] * n
    for i in range(n - 1, -1, -1):
        while s:
            if s[-1] > arr[i]:
                res[i] = s[-1]
                break
            else:
                s.pop()
        s.append(arr[i])
    for i in range(n):
        print(f"{arr[i]} --> {res[i]}")


if __name__ == "__main__":

    find_nge([5, 2, 7, 4, 22])
