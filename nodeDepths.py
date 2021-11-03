def nodeDepths(root):
    print(root)
    return

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTree(value)

    def insert_right(self, value):
        self.right = BinaryTree(value)

    def print_tree(self):
        print(self.value)

case1 = {
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": "6", "right": "7", "value": 3},
      {"id": "4", "left": "8", "right": "9", "value": 4},
      {"id": "5", "left": None, "right": None, "value": 5},
      {"id": "6", "left": None, "right": None, "value": 6},
      {"id": "7", "left": None, "right": None, "value": 7},
      {"id": "8", "left": None, "right": None, "value": 8},
      {"id": "9", "left": None, "right": None, "value": 9}
    ],
    "root": "1"
  }
}

# print(case1["tree"]["nodes"])
nodes = case1["tree"]["nodes"]
root = case1["tree"]["root"]
# rootNode = list(filter(lambda item: item["id"] == root, nodes))[0]
# print((rootNode))

def findNode(id):
    return list(filter(lambda item: item["id"] == id, case1["tree"]["nodes"]))[0]
# print(findNode("9"))

# for node in case1["tree"]["nodes"]:
#     if node["id"] == rootNode["id"]:
#         root = BinaryTree(node["value"])
#         # if root.left:
#         #     root.insert_left(findNode(root.left))
#         # if root.right:
#         #     root.insert_right(findNode(root.right))
# # root.print_tree()

def createTree(root, nodes):
    rootNode = list(filter(lambda node: node["id"] == root, nodes))[0]
    trav = rootNode
    # while not None:
    while trav.left || trav.right:
        if trav.left:


    return rootNode

print(createTree(root, nodes))