from treelib import Tree
from apps.tree_tests.tree_node import TreeNode

tree = Tree()

tree.create_node('a', 'a', data=TreeNode('a', 'a', [5, 5]))
tree.create_node('b', 'b', parent='a', data=TreeNode('b', 'b', [5, 5]))
tree.create_node('c', 'c', parent='a', data=TreeNode('c', 'c', [5, 6]))
tree.create_node('d', 'd', parent='c', data=TreeNode('d', 'd'))
tree.create_node('e', 'e', parent='d', data=TreeNode('e', 'e'))

print(tree)

for child in tree.children('b'):
    print(child.tag)
