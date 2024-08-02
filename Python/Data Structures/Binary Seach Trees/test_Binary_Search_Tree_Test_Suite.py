import pytest
from Binary_Search_Tree import TreeNode, BinarySearchTree


def test_should_always_pass():
    assert 2+2 == 4, "Dummy test sould always pass"




@pytest.fixture
def binary_search_tree():

    bst = BinarySearchTree()
    [bst.insert(i) for i in [4,2,6,1,3,7,5]]
    
    #       ┌── 7
    #   ┌── 6
    #   │   └── 5
    #   4
    #   │   ┌── 3
    #   └── 2
    #       └── 1
    
    return bst




def test_should_create_an_empty_bst():
    
    bst = BinarySearchTree()

    assert bst.root is None
 
def test_should_create_a_non_empty_bst():

    bst = BinarySearchTree()
    bst.insert(TreeNode(10))

    assert bst.root is not None




def test_should_insert_a_new_value(binary_search_tree):

    binary_search_tree.insert(10)

    assert 10 in binary_search_tree.inorder_traversal()




def test_should_find_a_value_in_bst(binary_search_tree):

    searched_node = binary_search_tree.search(3)

    assert searched_node.key == 3

def test_should_find_the_min_value_in_bst(binary_search_tree):

    bst_root = binary_search_tree.root
    bst_min_inord_trav = binary_search_tree.inorder_traversal()[0]

    assert binary_search_tree.find_min(bst_root) == bst_min_inord_trav

def test_should_find_the_max_value_in_bst(binary_search_tree):

    bst_root = binary_search_tree.root
    bst_max_inord_trav = binary_search_tree.inorder_traversal()[-1]

    assert binary_search_tree.find_max(bst_root) == bst_max_inord_trav

def test_should_not_find_a_value_in_bst():

    bst = BinarySearchTree()

    assert bst.search(10) is None




def test_should_delete_a_value_from_bst(binary_search_tree):

   binary_search_tree.delete(3)

   assert 3 not in binary_search_tree.inorder_traversal()





# Route on current work: 'C:\Users\USUARIO\GR\Software Development\Learning\Data Structures\Binary Seach Trees'
# Command for running test: python -m pytest
