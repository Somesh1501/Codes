#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# creating new firefox session
driver = webdriver.Firefox()
driver.maximize_window()

# accessing web page
driver.get('http://www.twitter.com')

#log in button
# finding email box
username = driver.find_element_by_name('session[username_or_email]')
username.clear()

#finding pass box
password = driver.find_element_by_name('session[password]')
password.clear()

#sending email
username.send_keys("9766831938")
password.send_keys('somesh@1501')

submit =driver.find_element_by_class_name('submit EdgeButton')
submit.click()