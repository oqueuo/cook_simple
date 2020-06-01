from my_imports import *
from recipe import Recipe
import pandas as pd
import random as rand

# Add incognito argument to webdriver
option = webdriver.ChromeOptions()
option.add_argument("- incognito")

# Make a Chrome instance
br = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/chromedriver.exe')

"""
Make the Request
"""
# 1. Pass in the desired website url
br.get("https://www.allrecipes.com/")
# 2. Implement a Try/Except to handle if website times out
timeout = 20
try:
    WebDriverWait(br, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "fixed-recipe-card__img")))
except TimeoutException:
    print("Timed out waiting for AllRecipes to load")
    br.quit

"""
Get the Response. We will be getting recipes on the front page of allrecipes.com
"""
# 1. URLS of the year in which we want the Hall of Fame recipes
recipe_grid = br.find_element_by_id("fixedGridSection")
recipe_box = recipe_grid.find_elements(By.CLASS_NAME, "favorite")

recipe_id = []
urls = []
for i, recipe in enumerate(recipe_box):
    recipe_id.append(recipe.get_attribute('data-id'))
    urls.append('https://allrecipes.com/recipe/' + str(recipe_id[i]))
    if i == 3:
        break

# 2. Scrape each url
rec = Recipe()
recipe_book = {}
for i, url in enumerate(urls):
    br.get(url)
    time.sleep(rand.randint(9,15))
    recipe_book[str(i + 1)] = rec.scrape_recipe(br)

# Create new DataFrame
df = pd.DataFrame(recipe_book, index=['Title', 'Time', 'Ingredients', 'Directions']).swapaxes("index", "columns")
# Try to open the existing DataFrame and append the new info 
try:
    df_existing = pd.read_csv('C:/Users/Cookie/Desktop/cook_simple/scraper/recipe_book.csv')
    df.append(df_existing)
except:
    print("No file")

# Remove duplicate recipes
df.drop_duplicates(subset='Title', keep=False)
# Write new csv file
df.to_csv(r'C:/Users/Cookie/Desktop/cook_simple/scraper/recipe_book.csv', mode='w')