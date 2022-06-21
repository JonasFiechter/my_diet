from food_list import foods

class Meal:
    def __init__(self, 
                    ingredients=[], 
                    total_protein=0, 
                    total_fat=0, 
                    total_carbohidrates=0, 
                    meal_time='',
                    category=''):

        self.ingredients = ingredients
        self.total_protein = total_protein
        self.total_fat = total_fat
        self.total_carbohidrates = total_carbohidrates
        self.meal_time = meal_time
        self.category = category

