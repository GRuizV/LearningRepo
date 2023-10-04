from Hash_Table_Implementation_RP import HashTable
import pytest


# Command for running test: python -m pytest

def test_should_always_pass():

    assert 2 + 2 == 4, "This is just a dummy test"


def test_should_create_hashtable_with_size():
    
    assert HashTable(capacity=100) is not None


def test_should_report_capacity():

    assert len(HashTable(capacity=100)) == 100


def test_should_create_empty_value_slots():

    #Given
    expected_pairs = [None, None, None]
    hash_table = HashTable(capacity=3)

    #When
    actual_pairs = hash_table.pairs

    #then
    assert actual_pairs == expected_pairs


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

    assert len(hash_table) == 100


@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass


def test_should_not_contain_none_value_when_created():
    hash_table = HashTable(capacity=100)
    values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in values


def test_should_insert_none_value():

    hash_table = HashTable(capacity=10)
    
    hash_table['Key'] = None

    assert None in hash_table.pairs


@pytest.fixture
def hash_table():

    sample_data = HashTable(capacity=100)
    sample_data['Hola'] = 'Hello'
    sample_data[98.6] = 37
    sample_data[False] = True

    return sample_data


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
    assert len(hash_table) == 100

    del hash_table['Hola']

    # assert 'Hola' not in hash_table
    assert ('Hola','Hello') not in hash_table.pairs
    assert len(hash_table) == 100


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
    assert len(hash_table) == 100


def test_should_return_pairs(hash_table):

    assert ('Hola', 'Hello') in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs






# Route on current work: 'C:\Users\USUARIO\GR\Software Development\Learning\Data Structures\Hash Table'
# Command for running test: python -m pytest









