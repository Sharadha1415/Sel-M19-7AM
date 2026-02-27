## EG1
import time

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.find_element('class name', 'ico-register').click()
# time.sleep(2)
# driver.find_element('class name', 'ico-login').click()
# time.sleep(2)
# driver.find_element('class name', 'ico-cart').click()

###############################################################################

# ## EG2
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
#
# driver.find_element('class name', 'first_row').send_keys('Manjunath')
# time.sleep(1)
# driver.find_element('class name', 'second_row').send_keys('Venkat')
# time.sleep(1)
# driver.find_element('class name', 'third_row').send_keys('Mainak')

###############################################################################

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
#
# driver.find_element('class name', 'third_row').send_keys('Manjunath')
# time.sleep(1)
# driver.find_element('class name', 'third_row').send_keys('Venkat')

###############################################################################

# ## EG4
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('class name', 'inputtext _58mg _5dba _2ph-').send_keys('Mainak')
#
# ## NoSuchElementException
# ## Because, we are having space in the value of the class attribute.
# ## class name locator cannot recognize the spaces which are present in the value of the class attribute

##-------------------------------------------------------------------

## To overcome the above drawbacks, we will replace the space with dot(.)

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('class name', 'inputtext._58mg._5dba._2ph-').send_keys('Mainak')



























