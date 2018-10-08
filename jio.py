#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
jio = driver.get("http://www.jio.com")

signIn = driver.find_element_by_link_text("Sign In")
signIn.click()

sgin = driver.find_element_by_tag_name("<a></a>")
sgin.click()