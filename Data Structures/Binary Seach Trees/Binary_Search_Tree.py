from math import log


class TreeNode:

    def __init__(self,key):

        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):

        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def search(self, key):
        return self.root._search(self.root, key)

    def inorder_traversal(self):
        
        result = list()
        self._inorder_traversal(self.root, result)
        return result
    
    def preorder_traversal(self):

        result = list()
        self._preorder_traversal(self.root, result)
        return result

    def pretty_print_bst(self, node, prefix="", is_left=True):
    
        if not node:
            node = self.root
        
        if not node:
            print('Empty Tree')
            return


        if node.right is not None:
            self.pretty_print_bst(node.right, prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.key))

        if node.left is not None:
            self.pretty_print_bst(node.left, prefix + ("    " if is_left else "│   "), True)






    def _insert(self, root, key):
        
        if root is None:
            return TreeNode(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        
        else:
            root.right = self._insert(root.right, key)
        
        return root
    
    def _search(self, root, key):

        if root is None or root.key == key:
            return root
        
        if key < root.key:
            return root.left._search(root.left, key)
        
        return root.right._search(root.right, key)

    def _inorder_traversal(self, root, result):

        if root is not None:

            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)
    
    def _preorder_traversal(self, root, result):

        if root is not None:

            result.append(root.key)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)















