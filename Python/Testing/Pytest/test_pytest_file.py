import pytest


'Fixtures Examples'

# @pytest.fixture
# def example_fixture():
#     return 1

# def test_with_fixture(example_fixture):
#     assert example_fixture == 1




'First Test Examples'

# def test_always_pass():
#     assert True

# @pytest.mark.xfail
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




'Test with markers Examples'

# @pytest.mark.slow   # This is the actual marking 'slow'
# def test_function():
#     assert True


# @pytest.mark.skip(reason='Outdate test, needs revision')
# def test_another_function():
#     assert True

# @pytest.mark.slow
# def test_sum():
#     assert 1 + 1 == sum([1,1])




'Parametrization Examples'

# import string

# # Let's say we have this
# def is_palindrome(s):

#     raw = ''.join( [ x for x in s if x not in string.punctuation and x != " " ] )
#     raw = raw.casefold() 

#     return raw == raw[::-1]




# # All these tests feel pretty similar

# def test_is_palindrome_empty_string():
#     assert is_palindrome('')

# def test_is_palindrome_single_character():
#     assert is_palindrome('a')

# def test_is_palindrome_mixed_casing():
#     assert is_palindrome('Bob')

# def test_is_palindrome_with_spaces():
#     assert is_palindrome("Never odd or even")

# def test_is_palindrome_with_punctuation():
#     assert is_palindrome("Do geese see God?")

# def test_is_palindrome_not_palindrome():
#     assert not is_palindrome("abc")

# def test_is_palindrome_not_quite():
#     assert not is_palindrome("abab")




# # Parametrizing them will look like this
    
# @pytest.mark.parametrize('palindrome',
#                          [
#                             '',
#                             'a',
#                             'Bob',
#                             'Never od or even',
#                             'Do geese see God?'                        
#                          ]
#                          )

# def test_is_palindrome(palindrome):
#     assert is_palindrome(palindrome)


# @pytest.mark.parametrize('non_palindrome',
#                          [
#                             'abc',
#                             'abab'
#                          ])

# def test_is_palindorme_not_palindrome(non_palindrome):
#     assert not is_palindrome(non_palindrome)




# # It could even be taken one step further

# @pytest.mark.parametrize('maybe_palindrome, expected_result', [
#                             ('', True),
#                             ('a', True),
#                             ('Bob', True),
#                             ('Never odd or even', True),
#                             ('Do geese see God?', True),
#                             ('abc', False),
#                             ('abab', False)                             
#                          ])


# def test_is_palindrome(maybe_palindrome, expected_result):
#     assert is_palindrome(maybe_palindrome) == expected_result







# path: 'C:\Users\USUARIO\GR\Software Development\Learning\Testing\Pytest'