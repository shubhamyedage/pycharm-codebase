from treelib.tree import Tree


def create_tree():
    tree = Tree()
    tree.create_node('a', 'a', data="ABC")
    tree.create_node('b', 'b', parent='a', data="ACB")
    tree.create_node('c', 1, parent='b', data="CAB")
    tree.create_node('c', 2, parent='b', data="CAB")
    tree.create_node('c', 3, parent='b', data="CAB")
    tree.create_node(4, 4, parent='b', data="CAB")
    for c in tree.children('b'):
        print(c.identifier)

    # process_tree(tree.subtree('b'))
    # node = tree.get_node('c')
    # print(node.data)
    # print(tree.children(tree.root))
    # if tree.get_node('f'):
    #     print("b is there!")


def process_tree(tree):
    for node in tree.all_nodes():
        if node.identifier is 'c':
            node.data = "XYZ"

create_tree()