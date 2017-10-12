from treelib import Tree

tree = Tree()


tree.create_node("a", "a", data={"v": 0})
tree.create_node("b", "b", data={"v": 7}, parent="a")
tree.create_node("c", "c", data={"v": 4}, parent="b")
tree.create_node("d", "d", data={"v": 3}, parent="b")
tree.create_node("f", "f", data={"v": 0}, parent="b")
tree.create_node("e", "e", data={"v": 3}, parent="a")

print(tree)


def func_1(node):
    v = 0
    children = tree.children(node.identifier)
    for child in children:
        if child.data["v"] == 0 and len(tree.children(child.identifier)) != 0:
            child.data["v"] = func_1(child)
        v += child.data["v"]

    return v

for node in tree.all_nodes():
    if node.data["v"] == 0 and len(tree.children(node.identifier)) != 0:
        node.data["v"] = func_1(node)


for node in tree.all_nodes():
    print("node: " + node.tag + " value: {}".format(node.data["v"]))