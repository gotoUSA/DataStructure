class Node:
    def __init__(self, data):
        self.data = data  # 값
        self.next = None  # 다음 노드 가리키는 변수


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1

    def __str__(self):
        if self.head is None:
            return "Linked list is empty"
        res = "Head"
        node = self.head
        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        return res

    def __contains__(self, target):
        if self.head is None:
            return False
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            node = node.next
        return False

    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        while node.next is not None:
            prev = node
            node = node.next
        if node == self.head:
            self.head = None
        else:
            prev.next = None
        self.length -= 1
        return node.data

    def remove(self, target):
        node = self.head
        while node is not None and node.data != target:
            prev = node
            node = node.next
        if node is None:
            return False
        if node == self.head:
            self.head = self.head.next
        else:
            prev.next = node.next
        self.length -= 1
        return True

    def insert(self, i, data):
        if i <= 0:
            self.appendleft(data)
        elif i >= self.length:
            self.append(data)
        else:
            node = self.head
            for _ in range(i - 1):
                node = node.next
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.length += 1

    def reverse(self):
        if self.length < 2:
            return
        prev = None
        ahead = self.head.next
        while ahead:
            self.head.next = prev
            prev = self.head
            self.head = ahead
            ahead = ahead.next
        self.head.next = prev


if __name__ == "__main__":

    def get_data(msg):
        data = input(msg)
        if data.isdigit():
            return int(data)
        return None

    menu = """
1: appendleft  2: append  3: popleft  4: pop  5: search  6: insert  7: remove  8: reverse
9: Exit
"""
    my_list = LinkedList()
    while True:
        print("\n-------\nCurrent List: ", my_list)
        command = int(input(f"{menu}\nEnter your choice: "))
        print()

        if command == 1:
            data = get_data("Input number to append at start: ")
            my_list.appendleft(data)
        elif command == 2:
            data = get_data("Input number to append: ")
            my_list.append(data)
        elif command == 3:
            data = my_list.popleft()
            if data is not None:
                print(f"Poped from start: {data}")
            else:
                print("Linked list is empty!")
        elif command == 4:
            data = my_list.pop()
            if data is not None:
                print(f"Poped from end: {data}")
            else:
                print("Linked list is empty!")
        elif command == 5:
            data = get_data("Input number to search: ")
            if data in my_list:
                print(f"{data} is exists.")
            else:
                print(f"{data} is not exists.")
        elif command == 6:
            data = get_data("Input number to insert: ")
            index = int(get_data("Input index to insert at: "))
            my_list.insert(index, data)
        elif command == 7:
            data = get_data("Input number to remove: ")
            if my_list.remove(data):
                print(f"Removed {data}.")
            else:
                print(f"{data} is not exists.")
        elif command == 8:
            my_list.reverse()
            print(f"Reversed the linked list.")
        elif command == 9:
            break
