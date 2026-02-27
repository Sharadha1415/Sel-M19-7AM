import time

# ## EG1
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
# driver.find_element('tag name', 'input').send_keys('Nagesh')
# time.sleep(1)
# driver.find_element('tag name', 'input').send_keys('Manoj')


###################################################################################

## EG2
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element('tag name', 'input').send_keys('standard_user')
time.sleep(1)
driver.find_element('tag name', 'input').send_keys('secret_sauce')




























