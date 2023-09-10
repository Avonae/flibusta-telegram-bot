# import libraries
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint
from selenium import webdriver

###########################
# Loop of all the pages
###########################

# Loop to go over all pages
pages = np.arange(1, 60, 20)
data = []

for page in pages:
    page = "https://wiki.dxbx.ru/spaces/listattachmentsforspace.action?key=WIKI&startsWith=&sortBy=date&fileExtension=&labels=&\
	startIndex=" + str(page)
    driver = webdriver.Chrome()
    driver.get(page)
    sleep(randint(2, 10))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    my_table = soup.find_all(class_=['url fn'])

    for tag in my_table:
        data.append(tag.get_text())

print(my_table)
