from Binary_Search_Tree import TreeNode, BinarySearchTree
import random


bst = BinarySearchTree()

[bst.insert(i) for i in [22,30,12,8,20,25,40]]


print(bst.root.key)
print(f'{bst.root.left.key}  {bst.root.right.key}')
print()
print(f'Left Node: {bst.root.left.key}')
print(f'{bst.root.left.left.key}  {bst.root.left.right.key}')
print()
print(f'Right Node: {bst.root.right.key}')
print(f'{bst.root.right.left.key}  {bst.root.right.right.key}')




# def printPreOrder(node):

#     if node is None:
#         return
    
#     # Visit Node
#     print(node.key, end = " ")
 
#     # Traverse left subtree
#     printPreOrder(node.left)
 
#     # Traverse right subtree
#     printPreOrder(node.right)




# printPreOrder(bst.root)
# print()

# bst.display_tree()


