''' Decorator   '''

# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def add(a, b):
#     print(a + b)
#
# add(10, 20)
#

##############################################################################

# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def test_login():
#     print("login executing")
#
# @outer
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED

############################################################################################################

'''
Fixture :   @pytest.fixture()  is a inbuilt decorator
            It is a function which is used to perform setup and teardown operations
            setup       :   The set of operations which executes before the execution of the test_function
            teardown    :   The set of operations which executes after the execution of the test_function

            SYNTAX      :   @pytest.fixture()
                            def func():
                                pass            ## setup
                                yield
                                pass            ## teardown

                            def test_func(func):
                                pass

                            We should pass the name of the fixture as a parameter for the test_functions. Pytest willl automatically execute it.

                            *   autouse :   autouse is a argument of fixture. It is an optional argument.
                                            When we give autouse=True, by default the fixture will be applied for all the test_functions/test_methods present in that module

                            *   scope   :   It is an argument of a fixture. It is also an optional parameter.
                                            scope defines the scope of a fixture.

                                            When we give scope="class", the fixture will be applied on a class level.
                                            Before the execution of the entire class, setup operation will be performed
                                            After the execution of the entire class, teardown operation will be performed

                                            When we give scope="module", the fixture will be applied on a module(file) level.
                                            Before the execution of the entire module, setup operation will be performed
                                            After the execution of the entire module, teardown operation will be performed

                                            Be default, scope="function"

'''



import time

import pytest

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 2 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED

##################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_reg():
#     print("reg executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_reg                          reg executing       PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED

'''
Since we are not passing greet to the test_reg, the fixture will not be applied for test_reg
'''

# ##################################################################################################
#
# @pytest.fixture()
# def greet():
#     time.sleep(2)
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_reg():
#     print("reg executing")
#
# def test_logout(greet):
#     print("logout executing")
#

##################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# def test_login(greet):
#     print("login executing")
#
# def test_reg(greet):
#     print("reg executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::test_reg      Good morning        reg executing       PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSEDGood evening

'''
NOTE    :   The operations before yield will execute before the execution of the test_function
            The operations after yield will execute after the execution of the test_function
'''

##################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# @pytest.fixture()
# def display():
#     yield
#     print("Good evening")
#
# def test_login(greet):
#     print("login executing")
#
# def test_logout(display):
#     print("logout executing")
#
# ## collected 2 items
# ## test_fixtures.py::test_login        Good morning        login executing     PASSED
# ## test_fixtures.py::test_logout                           logout executing    PASSEDGood evening

##################################################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_login():
#     print("login executing")
#
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login        Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::test_reg          Good morning        reg executing       PASSEDGood evening
# ## test_fixtures.py::test_logout       Good morning        logout executing    PASSEDGood evening

##################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self, greet):
#         print("login executing")
#
#     def test_reg(self, greet):
#         print("reg executing")
#
#     def test_logout(self, greet):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::TestSample::test_reg      Good morning        reg executing       PASSEDGood evening
# ## test_fixtures.py::TestSample::test_logout   Good morning        logout executing    PASSEDGood evening

##################################################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::TestSample::test_reg      Good morning        reg executing       PASSEDGood evening
# ## test_fixtures.py::TestSample::test_logout   Good morning        logout executing    PASSEDGood evening

##################################################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::TestSample::test_reg                          reg executing       PASSED
# ## test_fixtures.py::TestSample::test_logout                       logout executing    PASSEDGood evening

##################################################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
#
# class TestDisplay:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_google(self):
#         print("google executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")
#
# ## collected 6 items
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSED
# ## test_fixtures.py::TestSample::test_reg                      reg executing       PASSED
# ## test_fixtures.py::TestSample::test_logout                   logout executing    PASSEDGood evening
# ## test_fixtures.py::TestDisplay::test_gmail   Good morning    gmail executing     PASSED
# ## test_fixtures.py::TestDisplay::test_google                  google executing    PASSED
# ## test_fixtures.py::TestDisplay::test_yahoo                   yahoo executing     PASSEDGood evening


##################################################################################################

# @pytest.fixture(autouse=True, scope='module')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
#
# class TestDisplay:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_google(self):
#         print("google executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")
#
#
# ## collected 6 items
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSED
# ## test_fixtures.py::TestSample::test_reg                      reg executing       PASSED
# ## test_fixtures.py::TestSample::test_logout                   logout executing    PASSED
# ## test_fixtures.py::TestDisplay::test_gmail                   gmail executing     PASSED
# ## test_fixtures.py::TestDisplay::test_google                  google executing    PASSED
# ## test_fixtures.py::TestDisplay::test_yahoo                   yahoo executing     PASSEDGood evening

##################################################################################################

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(opts)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()

## setup --> webdriver.Chrome(opts)

class TestRegister:

    def test_register_link(self, setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender_btn(self, setup):
        setup.find_element('id', 'gender-male').click()

    def test_firstname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('Lolla')

    def test_lastname(self, setup):
        setup.find_element('id', 'LastName').send_keys('Venkat')

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('venkat@gmail.com')

    def test_reg_password(self, setup):
        setup.find_element('id', 'Password').send_keys('venkat@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('venkat@12345')
        time.sleep(2)


class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('venkat@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('venkat@12345')

















































































