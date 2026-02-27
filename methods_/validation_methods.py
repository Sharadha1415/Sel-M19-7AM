'''
validation methods  :   They are used to validate the data from the web-application
'''

'''
is_displayed()  :   This method will check whether the element is displayed on the page or not.
                    SYNTAX  :   web_element.is_displayed()
                    
                    Return True if the web_element is displayed
                    Return False if the web_element is not displayed
          
'''

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

ele1 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[1]')
print(ele1.is_displayed())          ## True

ele2 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[2]')
print(ele2.is_displayed())          ## False

'''
NOTE    :   To check whether the element is displayed or not, first the web-element should be there on the application.
            If the web-element is not available, then is_displayed() will give Error
'''


#################################################################################################

'''
is_selected     :       Will check if the element(checkbox, radio_btn, option) is selected or not
                        SYNTAX  :   web_element.is_selected()
                        
                        Returns True if the web_element is selected
                        Returns False if the web_element is not selected
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
# male_gender_btn = driver.find_element('id', 'gender-male')
# female_radio_btn = driver.find_element('id', 'gender-female')
#
# male_gender_btn.click()
# time.sleep(1)
#
# print(male_gender_btn.is_selected())            ## True
# print(female_radio_btn.is_selected())           ## False


#################################################################################################

'''
is_enabled  :   This method checks whether the element is enabled to perform the operations or not
                SYNTAX  :   web_element.is_enabled()
                
                Returns True if the element is enabled
                Returns False if the element is disabled

'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(2)

facebook = driver.find_element('xpath', '//button[text()="Log in with Facebook"]')
signup = driver.find_element('xpath', '//button[text()="Sign up"]')

print(facebook.is_enabled())        ## True
print(signup.is_enabled())


































