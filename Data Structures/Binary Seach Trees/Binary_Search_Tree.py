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

    def display_tree(self):


        '''
        After checking if the inserting operation was working as expected, next thing is
        to make a function that collects the nodes and its childs by level to pass it over to
        this display_tree function.
        '''
        
        bst = self.preorder_traversal()

        #This stands for the index of the first node of each level
        first = lambda h: 2**h - 1      # H stands for level height

        #This stands for the index of the last node of each level
        last = lambda h: first(h + 1)

        level = lambda tree, h: tree[first(h):last(h)]
        prepare = lambda e, field: str(e).center(field)

        width = max(len(str(e)) for e in bst)

        height = int(log(len(bst), 2)) + 1    
        gap = ' ' * width

        for h in range(height):

            #This below calculation brought me confusion, but my conclusion is that it represents the number of nodes
            #at the end of the heap if the curren level where the lvl 0, i.e. each node in the level act as the root
            #from there, that the in lvl 0: is 8, in lvl 1: is 4, ... lvl 4: is 1
            below = 2 ** (height - h - 1)
            field = (2 * below - 1) * width
            print(gap.join(prepare(e, field) for e in level(bst, h)))




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

        
















