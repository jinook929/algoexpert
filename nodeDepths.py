def nodeDepths(root):
    print(root)
    return

class BinaryTree:
    def __init__(self, node_id, value):
        self.id = node_id
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

tmp = []

for i in range(len(nodes)):
    tmp.append(BinaryTree(str(i + 1), nodes[i]["value"]))

def findNode(id):
    return list(filter(lambda node: node.id == id, tmp))[0]

print(findNode("1"))
print("=====")
for i in reversed(range(len(tmp))):
    print(nodes[i]["left"])
    # if findNode(nodes[i]["left"]):
    #     print(findNode(nodes[i]["left"]))
    # if nodes[i]["left"]:
    #     print(findNode(nodes[i]["left"]))
        # tmp[i].left = findNode(nodes[i]["left"])
    # if nodes[i]["right"]:
    #     tmp[i].right = findNode(nodes[i]["right"])

# print(tmp[0].value)
        

# def findNode(id):
#     return list(filter(lambda item: item["id"] == id, case1["tree"]["nodes"]))[0]

# def createTree(root_id, nodes):
#     root_obj = list(filter(lambda item: item["id"] == root_id, nodes))[0]
#     root = BinaryTree(root_obj["value"])
#     for obj in range(len(nodes)):
#         if "left" in root_obj:
#             findNode(root_obj["left"])
        

