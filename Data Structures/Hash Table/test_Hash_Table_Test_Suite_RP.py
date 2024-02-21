from Hash_Table_Implementation_RP import HashTable
import pytest
from pytest_unordered import unordered


def test_should_always_pass():

    assert 2 + 2 == 4, "This is just a dummy test"




@pytest.fixture
def hash_table():

    sample_data = HashTable(capacity=100)
    sample_data['Hola'] = 'Hello'
    sample_data[98.6] = 37
    sample_data[False] = True

    return sample_data




def test_should_create_hashtable_with_size():
    
    assert HashTable(capacity=100) is not None

def test_should_create_empty_value_slots():
   
    assert HashTable(capacity=3)._slots == [None, None, None]

def test_should_create_hash_table_from_dict():

    dictionary = {'Hola': 'Hello', 98.6: 37, False: True}

    hash_table = HashTable.from_dict(dictionary)

    assert hash_table.capacity == len(dictionary) * 10
    assert hash_table.keys == set(dictionary.keys())
    assert hash_table.pairs == set(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())

def test_should_create_hash_table_from_dict_with_custom_capacity():

    dictionary = {'Hola': 'Hello', 98.6: 37, False: True}

    hash_table = HashTable.from_dict(dictionary, capacity = 100)

    assert hash_table.capacity == 100
    assert hash_table.keys == set(dictionary.keys())
    assert hash_table.pairs == set(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())

def test_should_not_create_hash_table_with_zero_capacity():

    with pytest.raises(ValueError):
        HashTable(capacity=0)

def test_should_not_create_hash_table_with_negative_capacity():

    with pytest.raises(ValueError):
        HashTable(capacity=-100)




def test_should_report_lenght_of_empty_hash_table():

    assert len(HashTable(capacity=100)) == 0

def test_should_report_length(hash_table):

    assert len(hash_table) == 3

def test_should_report_capacity_of_empty_hash_table():

    assert HashTable(capacity=100).capacity == 100

def test_should_report_capacity(hash_table):

    assert hash_table.capacity == 100



def test_should_insert_key_value_pairs():

    #Given
    hash_table = HashTable(capacity=100)

    #When
    hash_table['Hola'] = 'Hello'
    hash_table[98.6] = 37
    hash_table[False] = True
    
    #then
    assert ('Hola', 'Hello') in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs

    assert len(hash_table) == 3

def test_should_insert_none_value():

    hash_table = HashTable(capacity=10)
    
    hash_table['Key'] = None

    assert None in hash_table._slots




@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass




def test_should_not_contain_blank_pairs(hash_table):

    assert None not in hash_table.pairs

def test_should_not_contain_none_value_when_created():
    
    assert None not in HashTable(capacity=100).values




def test_should_find_value_by_key(hash_table):

    assert hash_table['Hola'] == 'Hello'
    assert hash_table[98.6] == 37
    assert hash_table[False] == True

def test_should_find_key(hash_table):
    assert 'Hola' in hash_table

def test_should_not_find_key(hash_table):
    assert 'missing_key' not in hash_table




def test_should_raise_error_on_missing_key():

    hash_table = HashTable(capacity=100)

    with pytest.raises(KeyError) as exception_info:
        hash_table['missing_key']

    assert exception_info.value.args[0] == 'missing_key'

def test_should_raise_key_error_when_deleting(hash_table):

    with pytest.raises(KeyError) as exception_info:

        del hash_table['missing_key']
    
    assert exception_info.value.args[0] == 'missing_key'




def test_should_get_value(hash_table):
    assert hash_table.get('Hola') == 'Hello'

def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get('missing_key') is None

def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get('missing_key', 'default') == 'default'

def test_should_get_value_with_default(hash_table):
    assert hash_table.get('Hola', 'default') == 'Hello'

def test_should_get_pairs_of_empty_hash_table():

    assert HashTable(capacity=100).pairs == set()

def test_should_get_values(hash_table):
    
    assert unordered(hash_table.values) == ['Hello', 37, True]

def test_should_get_values_of_empty_hash_table():

    assert HashTable(capacity=100).values == []

def test_should_get_keys(hash_table):

    assert hash_table.keys == {'Hola', 98.6, False}

def test_should_get_keys_of_empty_hash_table():

    assert HashTable(capacity=100).keys == set()




def test_should_delete_key_value_pair(hash_table):

    assert 'Hola' in hash_table
    assert ('Hola','Hello') in hash_table.pairs
    assert len(hash_table) == 3

    del hash_table['Hola']

    assert 'Hola' not in hash_table
    assert ('Hola','Hello') not in hash_table.pairs
    assert len(hash_table) == 2




def test_should_update_value(hash_table):

    assert hash_table['Hola'] == 'Hello'

    hash_table['Hola'] = 'Hi'

    assert hash_table['Hola'] == 'Hi'
    assert hash_table[98.6] == 37
    assert hash_table[False] == True
    assert len(hash_table) == 3




def test_should_return_pairs(hash_table):

    assert hash_table.pairs == {
        ('Hola', 'Hello'), 
        (98.6, 37),
        (False, True)
    }

def test_should_return_copy_of_pairs(hash_table):
    
    assert hash_table.pairs is not hash_table.pairs

def test_should_return_duplicate_values():

    hash_table = HashTable(capacity = 100)
    hash_table['Alice'] = 24
    hash_table['Bob'] = 42
    hash_table['Joe'] = 42

    assert [24, 42, 42] == sorted(hash_table.values)

def test_should_return_copy_of_values(hash_table):

    assert hash_table.values is not hash_table.values

def test_should_return_copy_of_keys(hash_table):

    assert hash_table.keys is not hash_table.keys




def test_should_convert_to_dict(hash_table):

    dictionary = dict(hash_table.pairs)

    # the built-in set data type is used to disregard the order of the keys and items pairs 
    # to be compared to one another
    assert set(dictionary.keys()) == hash_table.keys
    assert set(dictionary.items()) == hash_table.pairs
    assert list(dictionary.values()) == hash_table.values




def test_should_iterate_over_keys(hash_table):

    for key in hash_table.keys:
        assert key in ('Hola', 98.6, False)

def test_should_iterate_over_values(hash_table):

    for value in hash_table.values:
        assert value in ('Hello', 37, True)

def test_should_iterate_over_pairs(hash_table):

    for key, value in hash_table.pairs:
        assert key in hash_table.keys
        assert value in hash_table.values

def test_should_iterate_over_instance(hash_table):
    
    for key in hash_table:
        assert key in ('Hola', 98.6, False)




def test_should_use_dict_literal_for_str(hash_table):

    assert str(hash_table) in {
        "{'Hola': 'Hello', 98.6: 37, False: True}",
        "{'Hola': 'Hello', False: True, 98.6: 37}",
        "{98.6: 37, 'Hola': 'Hello', False: True}",
        "{98.6: 37, False: True, 'Hola': 'Hello'}",
        "{False: True, 'Hola': 'Hello', 98.6: 37}",
        "{False: True, 98.6: 37, 'Hola': 'Hello'}",
    }




def test_should_have_canonical_string_representation(hash_table):

    assert repr(hash_table) in {
        "HashTable.from_dict({'Hola': 'Hello', 98.6: 37, False: True})",
        "HashTable.from_dict({'Hola': 'Hello', False: True, 98.6: 37})",
        "HashTable.from_dict({98.6: 37, 'Hola': 'Hello', False: True})",
        "HashTable.from_dict({98.6: 37, False: True, 'Hola': 'Hello'})",
        "HashTable.from_dict({False: True, 'Hola': 'Hello', 98.6: 37})",
        "HashTable.from_dict({False: True, 98.6: 37, 'Hola': 'Hello'})",
    }




def test_should_compare_equal_to_itsel(hash_table):

    assert hash_table == hash_table

def test_should_compare_equal_to_copy(hash_table):

    assert hash_table is not hash_table.copy()
    assert hash_table == hash_table.copy()

def test_should_compare_equal_diffent_key_value_order(hash_table):

    h1 = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    h2 = HashTable.from_dict({"b": 2, "a": 1, "c": 3})

    assert h1 == h2

def test_should_compare_unequal(hash_table):

    other = HashTable.from_dict({'different': 'value'})

    assert hash_table != other

def test_should_compare_unequal_another_data_type(hash_table):

    assert hash_table != 42

def test_should_compare_equal_different_capacity():

    data = {'a': 1, 'b': 2, 'c': 3}
    h1 = HashTable.from_dict(data, capacity=50)
    h2 = HashTable.from_dict(data, capacity=100)

    assert h1 == h2




def test_should_copy_keys_values_pairs_capacity(hash_table):

    copy = hash_table.copy()

    assert copy is not hash_table
    assert set(hash_table.keys) == set(copy.keys)
    assert unordered(hash_table.values) == copy.values
    assert set(hash_table.pairs) ==set(copy.pairs)
    assert hash_table.capacity == copy.capacity













# Route on current work: 'C:\Users\USUARIO\GR\Software Development\Learning\Data Structures\Hash Table'








# a = HashTable(capacity=100)
# a['Hola'] = 'Hello'
# a[98.6] = 37
# a[False] = True

# b = HashTable(capacity=100)
# b['Hola'] = 'Hello'
# b[98.6] = 37
# b[False] = True

# print(a != 5)


