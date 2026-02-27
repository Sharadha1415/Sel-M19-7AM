import time


# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
#
# driver.find_element('name', 'username').send_keys('Manoj_kumar')
# time.sleep(1)
# driver.find_element('name', 'password').send_keys('manoj@12345')


##################################################################################

# ## EG2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
# driver.find_element('name', 'firstname').send_keys('Lolla')
# time.sleep(1)
# driver.find_element('name', 'lastname').send_keys('Venkat')
# time.sleep(1)
# driver.find_element('name', 'reg_email__').send_keys('venakt@gmail.com')
# time.sleep(1)
# driver.find_element('name', 'reg_passwd__').send_keys('venkat@12345')

##################################################################################

# ## EG3
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('name', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('name', 'password').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('name', 'login-button').click()

##################################################################################

## EG4
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\css_selector.html')
time.sleep(2)

driver.find_element('name', 'fname').send_keys('Shravya')
time.sleep(1)
driver.find_element('name', 'fname').send_keys('Yamini')















