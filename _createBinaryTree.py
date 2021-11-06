# assumed id == value in nodes
def createBinaryTree(nodes, root):
    tmp = []
    for i in range(len(nodes)):
        tmp.append(BinaryTree(nodes[i]["value"]))

    def findNode(value):
        return list(filter(lambda node: node.value == int(value), tmp))[0]

    for i in reversed(range(len(tmp))):
        if nodes[i]["left"]:
            tmp[i].left = findNode(nodes[i]["left"])
        if nodes[i]["right"]:
            tmp[i].right = findNode(nodes[i]["right"])
            
    return tmp

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node
        
    def printTree(self, node, depth = 0):
        print("+---" * depth + str(node.value))
        if node.left:
            self.printTree(self, node.left, depth + 1)
        if node.right:
            self.printTree(self, node.right, depth + 1)
        return
        

# def createBinaryTree(nodes, root):
#     tmp = []
#     for i in range(len(nodes)):
#         tmp.append(BinaryTree(str(i + 1), nodes[i]["value"]))

#     def findNode(id):
#         return list(filter(lambda node: node.id == id, tmp))[0]

#     for i in reversed(range(len(tmp))):
#         if nodes[i]["left"]:
#             tmp[i].left = findNode(nodes[i]["left"])
#         if nodes[i]["right"]:
#             tmp[i].right = findNode(nodes[i]["right"])
            
#     return tmp

# class BinaryTree:
#     def __init__(self, node_id, value):
#         self.id = node_id
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert_left(self, node):
#         self.left = node

#     def insert_right(self, node):
#         self.right = node

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
treeRoot = createBinaryTree(nodes, root)[0]
# print(treeRoot.value)
# print(treeRoot.left.value)
# print(treeRoot.left.left.value)
# print(treeRoot.left.left.left.value)
# print(treeRoot.left.left.right.value)

nodes = [
    {"id": "1", "left": "2", "right": None, "value": 1},
    {"id": "2", "left": "3", "right": None, "value": 2},
    {"id": "3", "left": "4", "right": None, "value": 3},
    {"id": "4", "left": "5", "right": None, "value": 4},
    {"id": "5", "left": "6", "right": None, "value": 5},
    {"id": "6", "left": "7", "right": None, "value": 6},
    {"id": "7", "left": "8", "right": None, "value": 7},
    {"id": "8", "left": "9", "right": None, "value": 8},
    {"id": "9", "left": None, "right": None, "value": 9}
]
root = "1"
treeRoot = createBinaryTree(nodes, root)[0]
# print(treeRoot.value)
# print(treeRoot.left.value)
# print(treeRoot.left.left.value)
# print(treeRoot.left.left.left.value)
# print(treeRoot.left.left.left.left.value)
# print(treeRoot.left.left.left.left.left.value)
# print(treeRoot.left.left.left.left.left.left.value)
# print(treeRoot.left.left.left.left.left.left.left.value)
# print(treeRoot.left.left.left.left.left.left.left.left.value)

nodes = [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "4", "left": "8", "right": "9", "value": 4},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "6", "left": "10", "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8},
    {"id": "9", "left": None, "right": None, "value": 9},
    {"id": "10", "left": None, "right": "11", "value": 10},
    {"id": "11", "left": "12", "right": "13", "value": 11},
    {"id": "12", "left": "14", "right": None, "value": 12},
    {"id": "13", "left": "15", "right": "16", "value": 13},
    {"id": "14", "left": None, "right": None, "value": 14},
    {"id": "15", "left": None, "right": None, "value": 15},
    {"id": "16", "left": None, "right": None, "value": 16}
  ]
root = "1"
treeRoot = createBinaryTree(nodes, root)[0]
# print(treeRoot.value)
# print(treeRoot.right.value)
# print(treeRoot.right.left.value)
# print(treeRoot.right.left.left.value)
# print(treeRoot.right.left.left.right.value)
# print(treeRoot.right.left.left.right.left.value)
# print(treeRoot.right.left.left.right.left.left.value)
# print(treeRoot.right.left.left.right.right.value)
# print(treeRoot.right.left.left.right.right.right.value)