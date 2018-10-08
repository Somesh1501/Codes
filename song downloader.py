from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
for i in range(15):
    driver.get("https://bestwap.co/category/25917/0/90s-romantic-love-songs/"+str(i)+".html")
    for a in driver.find_elements_by_xpath('.//a'):
        '''for j in range(195,400):
            l = "444"+str(j)
            if l in a:
               print(a.get_attribute('href'))
        '''
    for j in range(16):
        j = j + 1
        song = driver.find_element_by_class_name("item")
        song.click()
        driver.find_element_by_link_text("Download File").click()
        driver.back()
        song.send_keys(Keys.TAB)
        continue
