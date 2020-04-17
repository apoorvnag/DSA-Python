class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


if __name__ == '__main__':
    # New Node
    new_node = Node()
    new_node.set_data(2)

    # Head Node
    head = new_node
    print(head.get_data())
