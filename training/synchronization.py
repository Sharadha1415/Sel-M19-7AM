'''
SYNCHRONIZATION :   Matching the speed of the webdriver to the speed of the web-application.

There are 2 types of synchronization
    *   unconditional synchronization   :   No conditions are passed
            We achieve synchronization by passing time.sleep().
            Whenever there is time.sleep(n), the executes pauses for whole n seconds and only after n seconds are completed, the execution will resume.
            So, irrespective of the application's status, we have to wait for the complete n seconds.
            So, unnecessary wait is too much here.
            This is a static wait.
            Not very reliable.

    *   conditional synchronization     :   Conditions are passed
            There are 2 types of conditional synchronization
            *   implicit_wait   :   Conditions are internally passed
                        SYNTAX  :   driver.implicitly_wait(n)
                        Whenever there is a delay in the loading of the web-element, automatically implicit_wait will make the driver wait for maximum of n seconds.
                        As soon as the element is available, it will start performing the operations right away.
                        So no unnecessary wait
                        One implicit_wait is sufficient for the whole program.
                        It will be applied globally.

            *   explicit_wait   :   Conditions are externally given
                                    Here the wait is based on a condition.

                                    First we have to import WebDriverWait and expected_conditions

                                    from selenium.webdriver.support.ui import WebDriverWait
                                    from selenium.webdriver.support import expected_conditions

                                    wait_obj = WebDriverWait(driver, timeouttime)

                                    wait_obj.until(expected_conditions.condition)

            WebDriverWait   :   It allows the driver to wait for a certain condition to check before we continue the operation.
                            Instead of waiting for a fixed amount of time, it waits until a condition is True or maximum time is reached.

            expected_conditions :   The conditions to be applied on the web-elements are already pre-defined and they are defined in expected_conditions.py
                                To make use of the pre-defined conditions we import expected_conditions

            until()         :   It is a method of WebDriverWait
                                It checks whether the given condition is satisfied or not
                                If the condition is True, it will continue the operations.
                                If the condition is False, it will always gives TimeOutException




'''


import time


# ## time.sleep()
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\loading.html')
# time.sleep(20)
#
# driver.find_element('name', 'fname').send_keys('Lolla')
# time.sleep(1)
# driver.find_element('name', 'lname').send_keys('Venkat')


##############################################################################

# ## implicit_wait
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\loading.html')
#
# driver.find_element('name', 'fname').send_keys('Lolla')
# time.sleep(1)
# driver.find_element('name', 'lname').send_keys('Venkat')

##############################################################################

# ## explicit_wait
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\loading.html')
#
# wait_obj.until(EC.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))
#
# driver.find_element('name', 'fname').send_keys('Lolla')
# time.sleep(1)
# driver.find_element('name', 'lname').send_keys('Venkat')

##############################################################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 10)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('id', 'user-name').send_keys('standard_user')
time.sleep(1)
driver.find_element('id', 'password').send_keys('secret_sauceeee')
time.sleep(1)
driver.find_element('id', 'login-button').click()
time.sleep(2)

try:
    wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
    print("successfull login")
except:
    print("unsuccessfull login")


##############################################################################

'''     using time.sleep()      '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# time.sleep(50)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

##############################################################################

'''     using implicit_wait      '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(50)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# driver.find_element('xpath', '//div[text()="100%"]')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()


##############################################################################

'''     using explicit_wait      '''

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 50)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
#
# wait_obj.until(EC.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
# time.sleep(1)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

##############################################################################

'''
fluent_wait :   A wait that waits for a maximum time
                Checks condition at regular intervals
                ignored_exceptions  :   Ignores specific exceptions
                Poll frequency  :   Check every few seconds until element appears or timeout happens
                Key Features:
                    Polling frequency
                    Timeout
                    Exception handling
                By default polling frequency is 5seconds
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 50, poll_frequency=8, ignored_exceptions=[TimeoutError])

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\progressbar.html')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click Me"]').click()

wait_obj.until(EC.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
time.sleep(1)

driver.find_element('xpath', '//button[text()="Click Me"]').click()















































