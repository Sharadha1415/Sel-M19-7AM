'''
In web automation, sometimes actions open a new browser window or tab (e.g., clicking a link, pop-up, advertisement, or login window).
Selenium initially controls only the main window where the driver started.
To interact with other windows/tabs, we need to switch between them.

Window Handles
    Every window or tab opened by the browser has a unique ID, called a window handle.
    Selenium provides methods to get and switch between these handles.
    handles = driver.window_handles     ## Returns a list of handles for all open windows/tabs.

    To switch the driver to the window
    driver.switch_to.window(handle)

'''

import time

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
# ac = ActionChains(driver)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# parent_window = driver.current_window_handle
#
# ac.send_keys(Keys.END).perform()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Google+"]').click()
# time.sleep(2)
#
# handles2 = driver.window_handles
# print(handles2)         ## [parent_handle, child_handle]
#
# for handle in handles2:
#     driver.switch_to.window(handle)
#     if 'googleblog' in driver.current_url:
#         driver.find_element('xpath', '//input[@class="header__search"]').send_keys("Google pixel")
#         time.sleep(2)
#
# driver.switch_to.window(parent_window)
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Twitter"]').click()
# time.sleep(2)
#
# handles3 = driver.window_handles
# print(handles3)
#
# for handle in handles3:
#     driver.switch_to.window(handle)
#     if 'nopCommerce' in driver.current_url:
#         driver.find_element('xpath', '//span[text()="Follow"]').click()
#

###############################################################################################

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
# ac = ActionChains(driver)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# parent_window = driver.current_window_handle
#
# ac.send_keys(Keys.END).perform()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Google+"]').click()
# time.sleep(2)
#
# def handling_windows():
#     return driver.window_handles
#
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'googleblog' in driver.current_url:
#         driver.find_element('xpath', '//input[@class="header__search"]').send_keys("Google pixel")
#         time.sleep(2)
#
# driver.switch_to.window(parent_window)
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Twitter"]').click()
# time.sleep(2)
#
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'nopCommerce' in driver.current_url:
#         driver.find_element('xpath', '//span[text()="Follow"]').click()


###############################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@title="Search for Products, Brands and More"]').send_keys('phones under 30000')
# time.sleep(2)
# driver.find_element('xpath', '//button[@type="submit"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//div[@class="KzDlHZ"]').click()
# time.sleep(2)
#
# def handle_windows():
#     return driver.window_handles
#
# ## handle_windows() --> [parent, child,,..]
#
# for handle in handle_windows():
#     driver.switch_to.window(handle)
#     if 'samsung-galaxy-f36-5g-red-128-gb' in driver.current_url:
#         driver.find_element('xpath', '//button[text()="Add to cart"]').click()
#         time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Help Center"]').click()
# time.sleep(2)
#
# for handle in handle_windows():
#     driver.switch_to.window(handle)
#     if 'helpcentre' in driver.current_url:
#         driver.find_element('xpath', '//a[text()="Know more"]').click()


###############################################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

driver.get('https://www.flipkart.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@title="Search for Products, Brands and More"]').send_keys('phones under 30000')
time.sleep(2)
driver.find_element('xpath', '//button[@type="submit"]').click()
time.sleep(2)

driver.find_element('xpath', '//div[text()="realme P4 Power 5G (TransSilver, 256 GB)"]').click()
time.sleep(2)

def handle_windows():
    return driver.window_handles

## handle_windows() --> [parent, child,,..]

for handle in handle_windows():
    driver.switch_to.window(handle)
    if 'realme-p4' in driver.current_url:
        driver.find_element('xpath', '//button[text()="Add to cart"]').click()
        time.sleep(2)






