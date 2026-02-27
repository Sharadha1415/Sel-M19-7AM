'''
css selector   :    To locate the web-elements using any attribute, we go for css selector
                    SYNTAX  :   tagname[attr_name="attr_value"]

                    DRAWBACKS
                    *   Indexing is not possible
                        Whenever there are multiple occurances, css selector will always consider the first occurance
                    *   Cannot locate text using css selector

'''

import time

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('css selector', 'input[placeholder="Username"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('css selector', 'input[placeholder="Password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('css selector', 'input[id="login-button"]').click()
# time.sleep(3)
# driver.find_element('css selector', 'button[id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'a[id="logout_sidebar_link"]').click()

#######################################################################################################

## EG2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)
driver.find_element('css selector', 'a[data-group="men"]').click()
time.sleep(2)
driver.find_element('css selector', 'a[data-group="women"]').click()
time.sleep(2)
# driver.find_element('css selector', 'a[data-group="kids"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'a[data-group="home"]').click()

#######################################################################################################

# ## EG3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\css_selector.html')
# time.sleep(2)
# driver.find_element('css selector', 'input[name="fname"]').send_keys('Yamini')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="fname"]').send_keys('Pavithra')

#######################################################################################################
'''
1.  Go to https://www.facebook.com/r.php?entry_point=login, fill the signup form using css selector
2.  Go to https://www.instagram.com/accounts/emailsignup/, fill the details using css selector
'''


#######################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="firstname"]').send_keys('Surya')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="lastname"]').send_keys('Narayan')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="reg_email__"]').send_keys('surya@gmail.com')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="reg_passwd__"]').send_keys('surya@12345')

#######################################################################################################


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
# driver.find_element('css selector', 'a[class="ico-register"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'input[id="gender-male"]').click()
# driver.find_element('css selector', 'input[id="FirstName"]').send_keys('Surya')
# driver.find_element('css selector', 'input[id="LastName"]').send_keys('Narayan')
# driver.find_element('css selector', 'input[id="Email"]').send_keys('surya@gmail.com')
# driver.find_element('css selector', 'input[id="Password"]').send_keys('surya@12345')
# driver.find_element('css selector', 'input[id="ConfirmPassword"]').send_keys('surya@12345')
#




















