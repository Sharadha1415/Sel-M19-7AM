'''
Markers :   To group the testcases, we go for markers
            There are 2 types
            *   inbuilt marker  :   There are 4 types
                                    *   skip
                                    *   skipif
                                    *   parametrize
                                    *   xfail
            *   custom marker

'''

import pytest

# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## In terminal -->  pytest test_markers.py -vs -m="sanity"
# ## collected 4 items / 2 deselected / 2 selected
# ## test_markers.py::test_reg       reg executing       PASSED
# ## test_markers.py::test_signup    signup executing    PASSED

###########################################################################################

# @pytest.mark.smoke
# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.regression
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"                   --> test_reg will execute
# ## pytest test_markers.py -vs -m="smoke"                    --> test_login will execute
# ## pytest test_markers.py -vs -m="regression"               --> test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"         --> None
# ## pytest test_markers.py -vs -m="sanity and regression"    --> None
# ## pytest test_markers.py -vs -m="regression and smoke"     --> None
# ## pytest test_markers.py -vs -m="sanity or smoke"          --> test_login and test_reg will execute
# ## pytest test_markers.py -vs -m="sanity or regression"     --> test_reg, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="regression or smoke"      --> test_login, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not sanity"               --> test_login, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not smoke"                --> test_reg, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not regression"           --> test_login and test_reg will execute

###########################################################################################

# @pytest.mark.sanity
# @pytest.mark.smoke
# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"                   --> test_login and test_reg will execute
# ## pytest test_markers.py -vs -m="smoke"                    --> test_login  and test_signup will execute
# ## pytest test_markers.py -vs -m="regression"               --> test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"         --> test_login will execute
# ## pytest test_markers.py -vs -m="sanity and regression"    --> None
# ## pytest test_markers.py -vs -m="regression and smoke"     --> test_signup will execute
# ## pytest test_markers.py -vs -m="sanity or smoke"          --> test_login test_reg, and test_signup will execute
# ## pytest test_markers.py -vs -m="sanity or regression"     --> all 4 will execute
# ## pytest test_markers.py -vs -m="regression or smoke"      --> test_login, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not sanity"               --> test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not smoke"                --> test_reg and test_logout will execute
# ## pytest test_markers.py -vs -m="not regression"           --> test_login and test_reg will execute

###########################################################################################

'''
skip    :   To skip the execution of the testcases, we use skip marker
            It is an unconditional skip. To skip the testcases we dont have to pass any reason or condition.
            Reason is optional parameter.
            It will skip the testcases which are decorated with @pytest.mark.skip
            
            SYNTAX  :   @pytest.mark.skip
                        def test_case():
                            pass 
'''


# def test_login():
#     print("login executing")
#
# @pytest.mark.skip
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login         login executing         PASSED
# ## test_markers.py::test_signup                                SKIPPED (unconditional skip)
# ## test_markers.py::test_reg                                   SKIPPED (unconditional skip)
# ## test_markers.py::test_logout        logout executing        PASSED

############################################################################################################

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip(reason="reg completed")
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login         login executing         PASSED
# ## test_markers.py::test_signup                                SKIPPED (unconditional skip)
# ## test_markers.py::test_reg                                   SKIPPED (reg completed)
# ## test_markers.py::test_logout        logout executing        PASSED


############################################################################################################

# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login         SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup        SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_reg           SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout        SKIPPED (unconditional skip)

############################################################################################################

# class TestSample:
#
#     @pytest.mark.skip
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.skip
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login                             SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup        signup executing    PASSED
# ## test_markers.py::TestSample::test_reg           reg executing       PASSED
# ## test_markers.py::TestSample::test_logout                            SKIPPED (unconditional skip)

############################################################################################################

'''
skipif  :   skipif is also used to skip the execution of the testcases, but the skip is based on a condition.
            It takes two parameters, condition and reason.
            condition is the first parameter, reason is the second parameter.
            Both are mandatory parameters
            
            SYNTAX  :   @pytest.mark.skipif(condition, reason)
                        def test_case():
                            pass
                        
                        If the condition is True, it will skip the execution of the testcase
                        If the condition is False, it will execute the testcase 
            
'''

# @pytest.mark.skipif(True, reason="login already done")
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login         SKIPPED (login already done)

##----------------------------------------------------------------------------
#
# @pytest.mark.skipif(False, reason="login already done")
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     login executing     PASSED

############################################################################################################

# @pytest.mark.skipif(False)
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login         ERROR

'''
reason is the mandatory parameter
'''

############################################################################################################

# @pytest.mark.skipif(reason="login already done")
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login         SKIPPED (login already done)

'''
If the condition is not given, by default the condition will be considered as True.
And it will skip the execution when the condition is not given
'''

############################################################################################################

# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))
#
# @pytest.mark.skipif(a<0 and b<0, reason="The values are not positive")
# def test_add():
#     print(a + b)
#
# ## collecting ...
# ## Enter the value of a : -10
# ## Enter the value of b : -20
# ## collected 1 item
# ## test_markers.py::test_add       SKIPPED (The values are not positive)

############################################################################################################

'''
xfail   :   This is an expected failure

            SYNTAX  :   @pytest.mark.xfail
                        def test_func():
                            pass  
                        
                        We are expecting the test_func to fail.
                        If the testcase is failed, then the output will be XFAIL
                        If the testcase is passed, then the output will be XPASS
'''

# def test_login():
#     print("login executing")
#
# def test_signup():              ## unexpected error
#     raise Exception
#
# @pytest.mark.xfail
# def test_reg():                 ## expected error
#     pt("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login         login executing         PASSED
# ## test_markers.py::test_signup                                FAILED
# ## test_markers.py::test_reg                                   XFAIL
# ## test_markers.py::test_logout        logout executing        PASSED

##--------------------------------------------------------------------------------
#
# def test_login():
#     print("login executing")
#
# def test_signup():              ## unexpected error
#     raise Exception
#
# @pytest.mark.xfail
# def test_reg():                 ## expected error
#     print("reg executing")
#
# ## collected 3 items
# ## test_markers.py::test_login         login executing     PASSED
# ## test_markers.py::test_signup                            FAILED
# ## test_markers.py::test_reg           reg executing       XPASS

##--------------------------------------------------------------------------------

# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# @pytest.mark.xfail
# def test_login():
#     driver.find_element('id', 'user-name').send_keys('standard_userrrrr')
#     time.sleep(1)
#     driver.find_element('id', 'password').send_keys('secret_sauceeee')
#     time.sleep(1)
#     driver.find_element('id', 'login-button').click()
#     time.sleep(2)
#     wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))

############################################################################################################

'''
parametrize :
'''

# @pytest.mark.parametrize("a, b", [(10, 20)])
# def test_add(a, b):
#     print(a + b)
#
# ## collected 1 item
# ## test_markers.py::test_add[10-20]        30     PASSED

##------------------------------------------------------------------------------------

# @pytest.mark.parametrize("a, b", [(10, 20), (10, -10), (1, 1), (100, 200), (3, 4)])
# def test_add(a, b):
#     print(a + b)
#
# ## collected 5 items
# ## test_markers.py::test_add[10-20]        30      PASSED
# ## test_markers.py::test_add[10--10]       0       PASSED
# ## test_markers.py::test_add[1-1]          2       PASSED
# ## test_markers.py::test_add[100-200]      300     PASSED
# ## test_markers.py::test_add[3-4]          7       PASSED

##------------------------------------------------------------------------------------

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 10)


@pytest.mark.parametrize("username, password", [('standard_user', 'secret_sauce'), ('standard', 'secret'), ('abcdefgh', '123456789')])
def test_login(username, password):
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.find_element('id', 'user-name').send_keys(username)
    time.sleep(1)
    driver.find_element('id', 'password').send_keys(password)
    time.sleep(1)
    driver.find_element('id', 'login-button').click()
    time.sleep(2)

    try:
        wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
        print(f"{username}-{password} --> successfull login")
    except:
        print(f"{username}-{password} --> unsuccessfull login")



































































