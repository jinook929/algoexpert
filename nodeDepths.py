def nodeDepths(root):
    print(root)
    return

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node

nodes = [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "4", "left": "8", "right": "9", "value": 4},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8},
    {"id": "9", "left": None, "right": None, "value": 9}
]
root = "1"
