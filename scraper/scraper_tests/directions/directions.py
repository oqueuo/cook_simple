from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import numpy as np
import time

br = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
br.get("https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%207")

title = br.find_element_by_tag_name('h1').text
print(title)

try:
    directions_elements = br.find_elements(By.CLASS_NAME, "recipe-directions__list--item")

    direction_list = []
    for i, direction in enumerate(directions_elements):
        direction_list.append(direction.text)

    # allrecipes.com uses two different recipe html layouts. Try second one if first doesn't work
    if not direction_list:
        directions_elements = br.find_elements(By.CLASS_NAME, "instructions-section-item")

        direction_list = []
        for i, direction in enumerate(directions_elements):
            direction_list.append(direction.text)
except TimeoutException:
    direction_list = []

print(direction_list)