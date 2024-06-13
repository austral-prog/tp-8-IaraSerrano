from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    unique_ingredients= set(dish_ingredients)
    result= (dish_name, unique_ingredients)
    return result



def check_drinks(drink_name, drink_ingredients):
   for ingredient in ingredients:
        if ingredient in ALCOHOLS:
            return f"{drink_name} cocktail"
    return f'{drink_name} mocktail'
