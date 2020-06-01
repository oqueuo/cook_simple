from my_imports import *
"""
Function to scrape allrecipes.com/recipe/id for the following information:
Title, Time Taken, Ingredients, Directions
"""
class Recipe:

    def scrape_recipe(self, br):
        # Try/Except each info section we want
        # This website uses two different HTML layouts for recipes. Checks both for info.

        ### Title
        try:
            title = br.find_element_by_tag_name('h1').text
        except:
            title = 'N/A'

        ### Time taken
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

        ### Ingredients
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

        ### Instructions
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

        # Create the datatable to return
        database = [title, time_dict, ingredient_list, direction_list]
        return database