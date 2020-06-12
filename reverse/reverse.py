class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # 5 - 4 - 3 - 2 - 1
    # 1 - 2 - 3 - 4 - 5

    def reverse_list(self, node, prev):
        list1 = []
        while node != None:
            list1.append(node.value)
            node = node.next_node

        print(list1)        

        for node in list1:
            node.add_to_head(node.value)

        # start = None
        # while node != start:
        #     temp = node.get_next()
        #     node.next_node = start
        #     start = node
        #     node = temp
