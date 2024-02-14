import pytest


'Fixtures demo'

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1




'First Test Examples'

# def test_always_pass():
#     assert True

# def test_always_fail():
#     assert False




'Test Assert Examples'
    
# def test_uppercase():
#     assert "loud noises".upper() == "LOUD NOISES"

# def test_reversed():
#     assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

# def test_some_primes():
#     assert 37 in {
#         num for num in range(2, 50) 
#         if not any(num % div == 0 for div in range(2, num))
#     }



# path: 'C:\Users\USUARIO\GR\Software Development\Learning\Testing\Pytest'