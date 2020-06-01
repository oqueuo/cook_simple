from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import numpy as np
import time

br = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
br.get("https://www.allrecipes.com/recipe/278888/slow-cooker-creamy-chicken-taco-soup/")

title = br.find_element_by_tag_name('h1').text
print(title)

try:
    time_type   = br.find_elements(By.CLASS_NAME, "prepTime__item--type")
    time_number = br.find_elements(By.TAG_NAME, "time")

    time_dict = {}
    for tt, tn in zip(time_type, time_number):
        time_dict[tt.text] = tn.text

    # allrecipes.com uses two different recipe html layouts. Try second one if first doesn't work
    if not time_dict:
        time_type   = br.find_elements(By.CLASS_NAME, "recipe-meta-item-header")
        time_number = br.find_elements(By.CLASS_NAME, "recipe-meta-item-body")

        time_dict = {}
        for tt, tn in zip(time_type, time_number):
            time_dict[tt.text] = tn.text

except:
    time_dict = {}

print(time_dict)




# br.get("https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%207")

# title = br.find_element_by_tag_name('h1').text
# print(title)


# try:
#     time_type   = br.find_elements(By.CLASS_NAME, "prepTime__item--type")
#     time_number = br.find_elements(By.CLASS_NAME, "prepTime__item--time")

#     time_dict = {}
#     for tt, tn in zip(time_type, time_number):
#         time_dict[tt.text] = tn.text

#     # allrecipes.com uses two different recipe html layouts. Try second one if first doesn't work
#     if not time_dict:
#         time_type   = br.find_elements(By.CLASS_NAME, "recipe-meta-item-header")
#         time_number = br.find_elements(By.CLASS_NAME, "recipe-meta-item-body")

#         time_dict = {}
#         for tt, tn in zip(time_type, time_number):
#             time_dict[tt.text] = tn.text

# except:
#     time_dict = {}

# print(time_dict)