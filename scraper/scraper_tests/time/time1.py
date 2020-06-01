from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import numpy as np
import time


br = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
br.get("https://www.allrecipes.com/recipe/244447/two-ingredient-pizza-dough/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%202")

title = br.find_element_by_tag_name('h1').text
print(title)

time_type   = br.find_elements(By.CLASS_NAME, "prepTime__item--type")
time_number = br.find_elements(By.CLASS_NAME, "prepTime__item--time")

try:
    time_type   = br.find_elements(By.CLASS_NAME, "prepTime__item--type")
    time_number = br.find_elements(By.CLASS_NAME, "prepTime__item--time")

    time_dict = {}
    for tt, tn in zip(time_type, time_number):
        time_dict[tt.text] = tn.text
        
except:
    time_dict = {}

print(time_dict)

# try:
    



# for i, t in enumerate(time_type):
#     print(time_type[i].text)

# def scrape_recipe(br, year, idnumber):
#     # Try/Except each info section we want
    
#     ### Title
#     try:
#         title = br.find_element_by_tag_name('h1').text
#     except:
#         title = 'N/A'
    
#     ### Time taken
#     # Prep
#     time_all = br.find_elements(By.CLASS_NAME, "recipe-meta-container")
#     for i, 

#     ### Ingredients

#     ### Instructions