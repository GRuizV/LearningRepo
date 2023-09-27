from Hash_Table_Implementation import HashTable


# Command for running test: python -m pytest

def test_should_always_pass():
    assert 2 + 2 == 4, "This is just a dummy test"


# # This first test was used to check wether pytest catch the creation of a non empty object
# def test_should_create_hashtable():
#     assert HashTable() is not None


def test_should_create_hashtable_with_size():
    assert HashTable(capacity=100) is not None



def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100