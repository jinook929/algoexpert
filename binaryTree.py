class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = Node(value)

    def insert_right(self, value):
        self.right = Node(value)

    def has_left(self):
        if self.left != None:
            return True
        return False

    def has_right(self):
        if self.right != None:
            return True
        return False

    def insert(self, current, value):
        if current.value == value:
            return
        elif current.value < value:
            if current.has_right():
                current.right.insert(current.right, value)
            else:
                current.insert_right(value)
        else:
            if current.has_left():
                current.left.insert(current.left, value)
            else:
                current.insert_left(value)

array = [200, 3, 64, 23, 64, 603, 65, 742, 399, 1]
root = Node(array[0])
for i in range(len(array)):
    root.insert(root, array[i])
print(root.left.left.value)