# def spam():         ## function
#     print("spam executing")
#
#
# class Sample:
#
#     def greet(self):
#         print("Good morning")
#
#     @property
#     def display(self):          ## method/attribute
#         return "display executing"
#
# s = Sample()
# s.greet()
# print(s.display)


##############################################################################

# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(1)
# driver.find_element('id', 'gender-male').click()
# driver.find_element('id', 'FirstName').send_keys('Lolla')
# driver.find_element('id', 'LastName').send_keys('Venkat')
# driver.find_element('id', 'Email').send_keys('venkat@gmail.com')
# driver.find_element('id', 'Password').send_keys('venkat@12345')
# driver.find_element('id', 'ConfirmPassword').send_keys('venkat@12345')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Log in"]').click()
# time.sleep(1)
# driver.find_element('id', 'Email').send_keys('venkat@gmail.com')
# driver.find_element('id', 'Password').send_keys('venkat@12345')

################################################################################


# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#         print("Good evening")
#     return wrapper
#
#
# @outer              ## addition = outer(addition)
# def addition(a, b):
#     print(a + b)
#
# addition(1, 2)

from selenium import webdriver

driver = webdriver.Chrome()



































































