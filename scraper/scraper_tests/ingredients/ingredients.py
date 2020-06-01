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
    ingredient_elements = br.find_elements(By.CLASS_NAME, "recipe-ingred_txt")

    ingredient_list = []
    for i, ingredient in enumerate(ingredient_elements):
        ingredient_list.append(ingredient.text)

    # allrecipes.com uses two different recipe html layouts. Try second one if first doesn't work
    if not ingredient_list:
        ingredient_elements = br.find_elements(By.CLASS_NAME, "ingredients-item-name")

        ingredient_list = []
        for i, ingredient in enumerate(ingredient_elements):
            ingredient_list.append(ingredient.text)
except TimeoutException:
    ingredient_list = []

print(ingredient_list)


