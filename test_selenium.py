# Python program to demonstrate 
# selenium 

# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.by import By

# create webdriver object 
driver = webdriver.Firefox() 

# enter keyword to search 
keyword = "geeksforgeeks"

# get geeksforgeeks.org 
driver.get("https://www.geeksforgeeks.org/") 

# get elements 
elements = driver.find_elements(By.XPATH,"//script") 

# print complete elements list 
print(elements) 
