def nodeDepths(root):
    BinaryTree.printTree(BinaryTree, root)
    depth_sum = 0
    nodes = [{"node": root, "depth": 0}]
    while nodes:
        current = nodes.pop()
        depth_sum += current["depth"]
        if current["node"].left:
            nodes.append({"node": current["node"].left, "depth": current["depth"] + 1})
        if current["node"].right:
            nodes.append({"node": current["node"].right, "depth": current["depth"] + 1})
    return depth_sum

from _createBinaryTree import createBinaryTree, BinaryTree

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
print("Depth Sum = ", str(nodeDepths(treeRoot)))

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
print("Depth Sum = ", str(nodeDepths(treeRoot)))