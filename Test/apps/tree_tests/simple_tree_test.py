from treelib import Tree

tree = Tree()
tree.create_node("Root", "Root", data={"Name": "Anthony"})
tree.create_node("Child1", "Child1", data={"Name": "Breta"}, parent="Root")
tree.create_node("Grand_Child1", "Grand_Child1", data={"Name": "Brica"}, parent="Child1")
tree.create_node("Great_Grand_Child1", "Great_Grand_Child1", data={"Name": "Bruce"}, parent="Grand_Child1")

tree.create_node("Child2", "Child2", data={"Name": "Brian"}, parent="Root")

tree.create_node("Child3", "Child3", data={"Name": "Bridget"}, parent="Root")
tree.create_node("Grand_Child2", "Grand_Child2", data={"Name": "Brima"}, parent="Child3")

print(tree)

# def func1(x):
#     return True if x.data["Name"] != "Bruce" else False

# for node in tree.expand_tree(filter=func1):
#     print(tree.get_node(node).data)

# for node in tree.expand_tree(filter=lambda x: x.identifier != "Child1"):
#     print(node)

root_childrens_list = tree.children(tree.root)
print(tree.depth())
for tag in tree.expand_tree(mode=Tree.DEPTH, reverse=False):
    print(tag)

# for cn in root_childrens_list:
#     print("##################################################")
#     sub_tree = tree.subtree(cn.identifier)
#     depth = sub_tree.depth()
#     print(sub_tree)
#     print("{}".format(depth))
#     for tag in sub_tree.expand_tree("Great_Grand_Child1", reverse=True):
#         print(tag)
