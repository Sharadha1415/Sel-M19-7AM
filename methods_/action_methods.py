'''
Action Methods  :   Action methods are used to perform the actions on web-elements like entering the data, clicking on web-elements
                    submitting the forms, clearing the existing data.

'''

import time

'''
click()     :   To click on a web-elemet, we use click() method.
                The web-element could be a link, button, checkbox, radio button etc,..
                SYNTAX  :   web_element.click()
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()      ## clicking on a link
# time.sleep(2)
# driver.find_element('id', 'gender-male').click()                    ## clicking on a radio button
# time.sleep(2)
# driver.find_element('id', 'register-button').click()                ## clicking on a button


#####################################################################################################

'''
send_keys   :   To enter the data to the web_element
                To send the Keyboard actions, we use send_keys
                SYNTAX  :   web_element.send_keys("data") 
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/register")
# time.sleep(2)
# driver.find_element('id', 'FirstName').send_keys("Shravya")             ## entering firstname
# time.sleep(2)
# driver.find_element('id', 'small-searchterms').send_keys("Books")       ## entering data in searchbox

#####################################################################################################

'''
clear() :   clears the existing text from textarea fields
            SYNTAX  :   web_element.clear()
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/register")
# time.sleep(2)
# driver.find_element('id', 'FirstName').send_keys("Shravya")
# time.sleep(2)
# driver.find_element('id', 'FirstName').clear()

#####################################################################################################

'''
submit  :   To submit a form, we use submit()
            This works only if the element is present inside a <form> tag 
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/register")
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@type="submit"])[1]').submit()
# ## driver.find_element('xpath', '(//input[@type="submit"])[1]/ancestor::form')

'''
The above element is present inside the form tag. <form> is the ancestor of the above element
'''
##-----------------------------------------------------------------------

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
driver.find_element('xpath', '//a[text()="Register"]').submit()

'''
WebDriverException: Message: To submit an element, it must be nested inside a form element
ERROR because the web-element is not present inside the form tag
'''

#####################################################################################################

'''
Difference between click() and submit()
    *   click()     :   It clicks on any webelement, not specific to any tagname
    *   submit()    :   It clicks on the elements which belong to form tag(form-related elements) 

'''












































