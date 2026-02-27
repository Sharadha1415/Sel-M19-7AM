'''
assert  :   It is a keyword.
            It is used to validate the expected output with the actual output.
            assert will take a condition

            SYNTAX  :   assert condition

            If the condition is True, the test case passes and the execution will continue
            If the condition is False, then it will always give AssertionError
'''

assert 10%2==0
## assert True  --> True.
## Nothing will happen. No output from the assert statement

#-----------------------------------------------------------------------

assert 11%2==0
## assert False --> AssertionError

## AssertionError

##-----------------------------------------------------------------------

# assert 11%2==0, "condition is wrong"
# ## assert False --> AssertionError
#
# ## AssertionError: condition is wrong

##-----------------------------------------------------------------------

# ## assert condition
#
# a = 10
# assert a>5, f"{a} is not greater than 5"
# ## assert 10>5  --> assert True --> True


# ## assert not condition
#
# a = 10
# assert not a>5, f"{a} is not greater than 5"
# ## assert not 10>5  --> assert not True --> assert False --> AssertionError

##-----------------------------------------------------------------------

## assert actual == expected

# a = 10
# b = 10
# assert a == b
# ## assert 10==10 --> assert True --> True


# a = 10
# b = 20
# assert a == b       ## assert 10 == 20  --> assert False --> AssertionError
#
# ## AssertionError

##-----------------------------------------------------------------------

# ## assert actual != expected
#
# a = 10
# b = 10
# assert a != b       ## assert 10 != 10  --> assert False --> AssertionError


# a = 10
# b = 20
# assert a != b       ## assert 10 != 20  --> assert True --> True

##-----------------------------------------------------------------------

## assert value is None

# assert None     ## assert bool(None) --> assert False --> AssertionError

assert not None     ## assert not bool(None) --> assert not False --> assert True --> True


















































