import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)


'''         Mouse Hovering operations       '''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# men = driver.find_element('xpath', '(//a[text()="Men"])[1]')
# ac_obj.move_to_element(men).perform()
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# ac_obj.move_to_element(women).perform()
# time.sleep(2)
#
# kids = driver.find_element('xpath', '(//a[text()="Kids"])[1]')
# ac_obj.move_to_element(kids).perform()
# time.sleep(2)
#
# home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# ac_obj.move_to_element(home).perform()
#
# ## ac_obj.move_to_element(men).move_to_element(women).move_to_element(kids).move_to_element(home).perform()

####################################################################################################

'''         DOUBLE CLICK        '''

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//button[text()="Copy Text"]')
# ac_obj.double_click(ele).perform()
# time.sleep(2)
#
# ele2 = driver.find_element('xpath', '//label[text()="Name:"]')
# ac_obj.double_click(ele2).perform()


####################################################################################################

'''         RIGHT CLICK        '''

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ## ac_obj.context_click().perform()        ## It will right click at the start of the application
#
# ## to right click on any web-element
# ele = driver.find_element('xpath', '//h2[text()="Dynamic Button"]')
# ac_obj.context_click(ele).perform()

####################################################################################################

'''     SCROLLING OPERATIONS        '''

# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//div[text()=" POPULAR SEARCHES "]')
# ac_obj.scroll_to_element(ele).perform()
#
# #--------------------------------------------------------------------------------
#
# ## scroll_by_amount
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# ac_obj.scroll_by_amount(0, 500).perform()
# time.sleep(2)
# ac_obj.scroll_by_amount(0, -200).perform()
#
# #--------------------------------------------------------------------------------
#
# ## execute_script
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//div[text()=" POPULAR SEARCHES "]')
# driver.execute_script("arguments[0].scrollIntoView();", ele)
#
# ##--------------------------------------------------------------------------------
#
# ## scroll down till the end of the application
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## To go back to the start of the application
# ac_obj.send_keys(Keys.HOME).perform()
#
# ##--------------------------------------------------------------------------------
#
# ## using execute_script
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# ## To go back to the start of the application
# driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
#
# ##--------------------------------------------------------------------------------
#
# ## pagewise scrolling
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
#
#
# ##--------------------------------------------------------------------------------
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 600);")       ## will scroll down by 600 pixels
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, -600);")       ## will scroll up by 600 pixels

##--------------------------------------------------------------------------------

# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# ac_obj.scroll_by_amount(0, 1000).perform()

####################################################################################################

'''         DRAG AND DROP       '''

## drag_and_drop
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ref_ele).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
#
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()

##-------------------------------------------------------------------------

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ref_ele).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
#
# ac_obj.drag_and_drop_by_offset(draggable_ele, 70, 100).perform()

##-------------------------------------------------------------------------

# ## scroll_from_origin
#
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h4[text()="RISING STARS"]')
#
# origin = ScrollOrigin.from_element(ele)
#
# ac_obj.scroll_from_origin(origin, 0, 1500).perform()

##-----------------------------------------------------------

# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '(//div[@class="form-group"])[6]')
#
# origin = ScrollOrigin.from_viewport(0, 0)
#
# ac_obj.scroll_from_origin(origin, 0, 100).perform()


####################################################################################################

'''     SLIDER      '''

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//h2[text()="Scrolling DropDown"]')
# ac_obj.scroll_to_element(ref_ele).perform()
# time.sleep(2)
#
# left_slider = driver.find_element('xpath', '(//div[@id="slider-range"]/span)[1]')
#
# ## Move the slider Right by 100 pixels
# ac_obj.click_and_hold(left_slider).move_by_offset(100, 0).release().perform()
# time.sleep(2)
#
# ## Move the slider Left by 100 pixels
# ac_obj.click_and_hold(left_slider).move_by_offset(-100, 0).release().perform()
# time.sleep(2)
#
# right_slider = driver.find_element('xpath', '(//div[@id="slider-range"]/span)[2]')
#
# ## Move the slider Right by 100 pixels
# ac_obj.click_and_hold(right_slider).move_by_offset(100, 0).release().perform()
# time.sleep(2)
#
# ## Move the slider Left by 100 pixels
# ac_obj.click_and_hold(right_slider).move_by_offset(-100, 0).release().perform()

####################################################################################################


'''
ANALYZE THE BELOW CODE
'''

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Harry')
# time.sleep(1)
#
# ac_obj.send_keys(Keys.TAB).perform()        ## The control will shift to the lastname
# time.sleep(1)
# ac_obj.send_keys('Potter').perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.BACKSPACE).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.BACKSPACE).perform()

# ##-------------------------------------------------------------------

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# fname = driver.find_element('xpath', '//input[@name="firstname"]')
# lname = driver.find_element('xpath', '//input[@name="lastname"]')
#
# fname.send_keys('Harry')
# time.sleep(2)
#
# fname.send_keys(Keys.CONTROL + 'a')         ## select the data
# fname.send_keys(Keys.CONTROL + 'c')         ## copy the data
#
# ac_obj.send_keys(Keys.TAB).perform()        ## switching the control to last name
# lname.send_keys(Keys.CONTROL + 'v')         ## paste the data

# # ##-------------------------------------------------------------------
#
# ## ctrl + a
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# ac_obj.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
#
# # ############################################################################################################
#
# ## ctrl + backspace
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
# time.sleep(2)
# ac_obj.key_down(Keys.CONTROL).send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()
#
# # ##-------------------------------------------------------------------
#
# ## shift
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="name"]').send_keys('harry')
# time.sleep(2)
# ac_obj.key_down(Keys.SHIFT).send_keys('a').perform()

# # ##-------------------------------------------------------------------
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
# time.sleep(2)
# ac_obj.send_keys(Keys.TAB).perform()
# time.sleep(2)
# ac_obj.send_keys('harry@gmail.com').perform()


'''
Go to https://crossbrowsertesting.github.io/drag-and-drop.html, perform drag and drop
'''



































































