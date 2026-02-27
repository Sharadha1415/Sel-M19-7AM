'''
GETTER METHODS
'''
import time

'''
tag_name :   
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
# ele1 = driver.find_element('id', 'FirstName')
# print(ele1.tag_name)        ## input
#
# ele2 = driver.find_element('class name', 'ico-register')
# print(ele2.tag_name)        ## a

####################################################################################

'''
text    :   It is a inbuilt property.
            It will give the text of the web-element  
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# men = driver.find_element('xpath', '//a[@data-group="men"]')
# print(men.text)             ## MEN
#
# women = driver.find_element('xpath', '//a[@data-group="women"]')
# print(women.text)           ## WOMEN

####################################################################################

'''
get_attribute()     :   This method will give the attribute value
                        SYNTAX  :   web_element.get_attribute("attr_name") 
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# print(women.get_attribute("href"))          ## https://www.myntra.com/shop/women
# print(women.get_attribute("class"))         ## desktop-main

####################################################################################

'''
get_dom_attribute()     :   This method will give the attribute value as it is written in the html
                            SYNTAX  :   web_element.get_dom_attribute("attr_name")
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# print(women.get_attribute("href"))              ## https://www.myntra.com/shop/women
# print(women.get_dom_attribute("href"))          ## /shop/women


####################################################################################

'''
accessible_name :   It is a property.
                    It returns the accessible name used by the readers
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# # driver.get("https://www.myntra.com/")
# # time.sleep(2)
# # search = driver.find_element('xpath', '//input[@placeholder="Search for products, brands and more"]')
# # print(search.accessible_name)       ## Search for products, brands and more
#
#
# ##----------------------
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# ele1 = driver.find_element('id', 'newsletter-subscribe-button')
# print(ele1.accessible_name)         ## Subscribe
#
# ele2 = driver.find_element('css selector', 'input[value="Search"]')
# print(ele2.accessible_name)         ## Search

################################################################################################

'''
aria_role   :   Returns the role of a web-element
                SYNTAX  :   web_element.aria_role
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/register')
# time.sleep(2)
# ele1 = driver.find_element('link text', 'Register')
# print(ele1.aria_role)           ## link
#
# ele2 = driver.find_element('css selector', 'input[value="Search"]')
# print(ele2.aria_role)           ## button
#
# ele3 = driver.find_element('id', 'gender-male')
# print(ele3.aria_role)           ## radio
#
# ele4 = driver.find_element('xpath', '//img[@alt="Tricentis Demo Web Shop"]')
# print(ele4.aria_role)           ## image
#

################################################################################################

'''
value_of_css_property   :   Fetches the css value of the web-element
                            Used to verify styles like font-size, color etc,..
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/register')
# time.sleep(2)
# ele1 = driver.find_element('link text', 'Register')
# print(ele1.value_of_css_property("color"))          ## rgba(175, 3, 4, 1)
# print(ele1.value_of_css_property("font-style"))     ## normal
# print(ele1.value_of_css_property("font-size"))      ## 12px

################################################################################################

'''
screenshot  :   To take the screenshot of a webelement, we use screenshot()     
'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

# ## If the location is not give, by default the screenshot will be saved in the same package as our python file.
# ele1 = driver.find_element('link text', 'Register')
# ele1.screenshot("reg.png")
#
# ## To store the screenshots in different location
# ## web_element.screenshot(r"path_of_location\screenshot_name.png)
ele1 = driver.find_element('link text', 'Register')
ele1.screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\screenshots\register.png')
































