import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

## launch the application
driver.get("https://www.myntra.com/")
time.sleep(2)

## maximize the window
driver.maximize_window()
time.sleep(2)

## minimize the window
driver.minimize_window()
time.sleep(2)

## maximize the window
driver.maximize_window()
time.sleep(2)

## To go back
driver.back()
time.sleep(2)

## To go to next page
driver.forward()
time.sleep(2)

## To refresh
driver.refresh()
#
# ## current_url
# print(driver.current_url)
#
# ## title
# print(driver.title)
#
# ## name
# print(driver.name)

# ## page_source
# print(driver.page_source)

########################################################################
'''
Take screenshot

save_screenshot :   It will take the screenshot of the entire page
                    SYNTAX  :   driver.save_screenshot("name.png")
                    
                    By default, the screenshot will be saved in the same location as our python file 
                    
                    To save the screenshot in different location,
                    SYNTAX  :   driver.save_screenshot(r"absolute_pth_of_folder\screenshot_name.png")
'''

# driver.save_screenshot("myntra_")

# driver.save_screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\screenshots\myn_ss.png')

########################################################################

# ## To close the browser
# driver.close()







































