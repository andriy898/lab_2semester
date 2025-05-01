class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None
        self.prev = None


class Priority:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value, priority):
        new_node = Node(value, priority)

        if self.head is None:
            self.head = self.tail = new_node
            return

        current = self.head
        while current and current.priority >= priority:
            current = current.next

        if current is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        elif current == self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node

    def pop(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return node.value

    def peek(self):
        if self.head:
            return self.head.value
        return None

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(f"({current.value}, {current.priority})")
            current = current.next
        return ' -> '.join(result)


if __name__ == "__main__":
    queue = Priority()
    queue.insert("A", 2)
    queue.insert("B", 1)
    queue.insert("C", 3)
    queue.insert("D", 2)

    print("Поточна черга:", queue)
    print("Найвищий пріоритет:", queue.peek())
    print("Видалення елементу з найвищим пріоритетом:", queue.pop())
    print("Черга після видалення:", queue)
