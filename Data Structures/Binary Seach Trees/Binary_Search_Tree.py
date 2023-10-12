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
        return self._search(self.root, key)

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

    def find_min(self, node):

        current = node

        while current.left is not None:
            current = current.left
        
        return current.key

    def find_max(self, node):

        current = node

        while current.right is not None:
            current = current.right

        return current.key

    def delete(self, key):

        self.root = self._delete(self.root, key)




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
            return self._search(root.left, key)
        
        return self._search(root.right, key)

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

    def _delete(self, root, key):

        if root is None:
            return root
        
        if key < root.key:
            root.left = self._delete(root.left, key)
        
        elif key > root.key:
            root.right = self._delete(root.right, key)

        else:

            # Case 1 & 2: Node with only one child or no child

            if root.left is None:
                return root.right
            
            elif root.right is None:
                return root.left
            

            # Case 3: Node with two children: Get the in-order successor (Min value or the right subtree)
            root.key = self.find_min(root.right)

            # Finally, delete the in-order successor

            root.right = self._delete(root.right, root.key)

        return root














