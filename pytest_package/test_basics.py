# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()
# logout()
#
# ## works fine
# ## To execute the function, we should give the function call

##----------------------------------------------------------------------

# class Sample:
#
#     def login(self):
#         print("login executing")
#
#     def logout(self):
#         print("logout executing")
#
# s_obj = Sample()
# s_obj.login()
# s_obj.logout()
#

########################################################################################################

'''
PYTEST  :   Pytest is a unit testing framework
            Testing the small unit/small portion of the entire program, we call it as unit testing
            To perform unit testing in selenium, we use pytest

            To install pytest
            Go to command prompt -->    pip install pytest

            RULES
            *   filename should always start with test_ or end with _test
                EG  :   test_filename.py            OR          filename_test.py
            *   function name should always start with test_
                EG  :   def test_funcname():
                            pass
            *   class name should always start with Test
                EG  :   class TestClassName:
                            pass

            Pytest will automatically recognize the files, functions and the classes which are following
            the pytest rules.
            So, without calling the function, we can execute the function and without creating the object
            and without calling the attributes we can execute the class

            To execute
            Right click --> Open in --> Terminal --> pytest test_filename.py -vs
            -v --> Verbosity.   This gives the detailed explanation of the code
            -s --> Scripting.   This will print all the print statements

'''
import time

# def test_login():
#     print("login executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing     PASSED
# ## test_basics.py::test_logout     logout executing    PASSED

#########################################################################################################

# def test_login():
#     print("login executing")
#
# def signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing     PASSED
# ## test_basics.py::test_logout     logout executing    PASSED

'''
signup will not execute because it is not following the pytest rules.
Pytest cannot recognize the functions which are not following the rules
'''

#########################################################################################################

# def test_login():
#     print("login executing")
#     def test_signup():
#         print("signup executing")
#
# ## collected 1 item
# ## test_basics.py::test_login login executing      PASSED

'''
NOTE    :   Incase of nested test_functions, pytest can recognize only the outer test_function.
            pytest cannot recognize the inner test_function
'''

#########################################################################################################

# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# test_login()
# test_signup()
# test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::test_login      login executing     PASSED
# ## test_basics.py::test_signup     signup executing    PASSED
# ## test_basics.py::test_logout     logout executing    PASSED

'''
When we call the test_functions explicitly, the execution will happen twice
'''

#########################################################################################################

# def test_login():
#     raise Exception
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::test_login                          FAILED
# ## test_basics.py::test_signup     signup executing    PASSED
# ## test_basics.py::test_logout     logout executing    PASSED

'''
NOTE    :   Error in one testcase will not affect the execution of the other testcases
'''

#########################################################################################################

# def test_add(a, b):
#     print(a + b)
#
# test_add(1, 2)
#
# ## collecting ... 3
# ## collected 1 item
# ## test_basics.py::test_add        ERROR

'''
NOTE    :   test_functions donot take any parameters
'''

#########################################################################################################

# def test_login():
#     print("Good morning")
#
# def test_login():
#     print("Good evening")
#
# ## collected 1 item
# ## test_basics.py::test_login      Good evening     PASSED

'''
NOTE    :   Whenever there are multiple test_functions with the same test_function name, pytest will always consider
            the latest occurance
'''

#########################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing     PASSED
# ## test_basics.py::TestSample::test_signup     signup executing    PASSED
# ## test_basics.py::TestSample::test_logout     logout executing    PASSED

#########################################################################################################

# class Sample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 0 items

'''
classname is not following the pytest rules
'''

#########################################################################################################

# class TestSample:
#
#     def login(self):
#         print("login executing")
#
#     def signup(self):
#         print("signup executing")
#
#     def logout(self):
#         print("logout executing")
#
# ## collected 0 items

'''
attributes are not following the rules
'''

#########################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# s = TestSample()
# s.test_login()
# s.test_signup()
# s.test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing     PASSED
# ## test_basics.py::TestSample::test_signup     signup executing    PASSED
# ## test_basics.py::TestSample::test_logout     logout executing    PASSED


#########################################################################################################

# class TestSample:
#
#     def test_login(self, name):
#         print("login executing")
#
# ## collected 1 item
# ## test_basics.py::TestSample::test_login      ERROR

'''
NOTE    :   test_attributes donot take any parameter
'''

#########################################################################################################

# class TestSample:
#
#     def __init__(self):
#         pass
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 0 items
# ## PytestCollectionWarning: cannot collect test class 'TestSample' because it has a __init__ constructor

#########################################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

class TestRegister:

    def test_register_link(self):
        driver.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender_btn(self):
        driver.find_element('id', 'gender-male').click()

    def test_firstname(self):
        driver.find_element('id', 'FirstName').send_keys('Lolla')

    def test_lastname(self):
        driver.find_element('id', 'LastName').send_keys('Venkat')

    def test_reg_email(self):
        driver.find_element('id', 'Email').send_keys('venkat@gmail.com')

    def test_reg_password(self):
        driver.find_element('id', 'Password').send_keys('venkat@12345')

    def test_confirm_pwd(self):
        driver.find_element('id', 'ConfirmPassword').send_keys('venkat@12345')
        time.sleep(2)

class TestLogin:

    def test_login_link(self):
        driver.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self):
        driver.find_element('id', 'Email').send_keys('venkat@gmail.com')

    def test_login_pwd(self):
        driver.find_element('id', 'Password').send_keys('venkat@12345')





























































































