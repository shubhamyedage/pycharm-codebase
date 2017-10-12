from apps.tree_tests.tree_node import TreeNode
from treelib import Tree


key_list = ['A', 'B']
tag = True
node_type = 'Add'
tree = Tree()
tree.create_node("root", "root", data=TreeNode(key_list, node_type, [2,2]))
tree.create_node("Child1", "Child1", data=TreeNode(key_list, node_type, [2,2]), parent="root")
tree.create_node("Child2", "Child2", data=TreeNode(key_list, node_type, [2,3]), parent="root")
tree.create_node("Child3", "Child3", data=TreeNode(key_list, node_type, [3,2]), parent="Child1")
tree.create_node("Child4", "Child4", data=TreeNode(key_list, node_type, [3,3]), parent="Child1")
tree.create_node("Child5", "Child5", data=TreeNode(key_list, node_type, [4,4]), parent="Child4")

print(tree)

l = tree.expand_tree(mode=Tree.WIDTH, filter=lambda x: x.data.get_change() == 0)
print(next(l))
print(next(l))
print(next(l))
print(next(l))

#
# for node in tree.all_nodes():
#     print(node.tag)
#     tree_node = node.data
#     print(tree_node.node_type)
#     tree_node.values = ['1', '2']
# print("#########################################")
# for node in tree.all_nodes():
    # print(node.tag)
    # print(node.data.values)
# print("+++++++++++++++++++++++++++++++++++++++++++++++++")