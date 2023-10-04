from Hash_Table_Implementation_RP import HashTable
import pytest
from pytest_unordered import unordered


# Command for running test: python -m pytest

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


def test_should_report_lenght_of_empty_hash_table():

    assert len(HashTable(capacity=100)) == 0


def test_should_create_empty_value_slots():
   
    assert HashTable(capacity=3)._slots == [None, None, None]


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


@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass


def test_should_not_contain_none_value_when_created():
    
    assert None not in HashTable(capacity=100).values


def test_should_insert_none_value():

    hash_table = HashTable(capacity=10)
    
    hash_table['Key'] = None

    assert None in hash_table._slots


def test_should_find_value_by_key(hash_table):

    assert hash_table['Hola'] == 'Hello'
    assert hash_table[98.6] == 37
    assert hash_table[False] == True


def test_should_raise_error_on_missing_key():

    hash_table = HashTable(capacity=100)

    with pytest.raises(KeyError) as exception_info:
        hash_table['missing_key']

    assert exception_info.value.args[0] == 'missing_key'


def test_should_find_key(hash_table):
    assert 'Hola' in hash_table


def test_should_not_find_key(hash_table):
    assert 'missing_key' not in hash_table


def test_should_get_value(hash_table):
    assert hash_table.get('Hola') == 'Hello'


def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get('missing_key') is None


def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get('missing_key', 'default') == 'default'


def test_should_get_value_with_default(hash_table):
    assert hash_table.get('Hola', 'default') == 'Hello'


def test_should_delete_key_value_pair(hash_table):

    assert 'Hola' in hash_table
    assert ('Hola','Hello') in hash_table.pairs
    assert len(hash_table) == 3

    del hash_table['Hola']

    assert 'Hola' not in hash_table
    assert ('Hola','Hello') not in hash_table.pairs
    assert len(hash_table) == 2


def test_should_raise_key_error_when_deleting(hash_table):

    with pytest.raises(KeyError) as exception_info:

        del hash_table['missing_key']
    
    assert exception_info.value.args[0] == 'missing_key'


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


def test_should_get_pairs_of_empty_hash_table():

    assert HashTable(capacity=100).pairs == set()


def test_should_return_copy_of_pairs(hash_table):
    
    assert hash_table.pairs is not hash_table.pairs


def test_should_not_include_blank_pairs(hash_table):

    assert None not in hash_table.pairs


def test_should_return_duplicate_values():

    hash_table = HashTable(capacity = 100)
    hash_table['Alice'] = 24
    hash_table['Bob'] = 42
    hash_table['Joe'] = 42

    assert [24, 42, 42] == sorted(hash_table.values)


def test_should_get_values(hash_table):
    
    assert unordered(hash_table.values) == ['Hello', 37, True]


def test_should_get_values_of_empty_hash_table():

    assert HashTable(capacity=100).values == []


def test_should_return_copy_of_values(hash_table):

    assert hash_table.values is not hash_table.values


def test_should_get_keys(hash_table):

    assert hash_table.keys == {'Hola', 98.6, False}


def test_shuold_get_keys_of_empty_hash_table():

    assert HashTable(capacity=100).keys == set()


def test_should_return_copy_of_keys(hash_table):

    assert hash_table.keys is not hash_table.keys


def test_should_convert_to_dict(hash_table):

    dictionary = dict(hash_table.pairs)

    # the built-in set data type is used to disregard the order of the keys and items pairs 
    # to be compared to one another
    assert set(dictionary.keys()) == hash_table.keys
    assert set(dictionary.items()) == hash_table.pairs
    assert list(dictionary.values()) == hash_table.values


def test_should_not_creat_hash_table_with_zero_capacity():

    with pytest.raises(ValueError):
        HashTable(capacity=0)


def test_should_not_create_hash_table_with_negative_capacity():

    with pytest.raises(ValueError):
        HashTable(capacity=-100)


def test_should_report_length(hash_table):

    assert len(hash_table) == 3


def test_should_report_capacity_of_empty_hash_table():

    assert HashTable(capacity=100).capacity == 100


def test_should_report_capacity(hash_table):

    assert hash_table.capacity == 100





# Route on current work: 'C:\Users\USUARIO\GR\Software Development\Learning\Data Structures\Hash Table'
# Command for running test: python -m pytest









