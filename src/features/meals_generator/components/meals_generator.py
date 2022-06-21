from meal import Meal
from food_list import foods


class MealsGenerator():
    def __init__(self):
        self.foods_list = foods
        self.max_protein = 0
        self.max_carbohidrates = 0
        self.max_fat = 0
        self.meal_list = []

    #  The idea with this testing function is to calc the minimum of each nutrient needed for meal
    # and return 4 Meals instances each one with the right ammount of mass for person's profile.
    # after its working it will be intersting to add a functionality that creates a category for the
    # meal, like: "low-carb", "extra-protein" etc...
    def calc_meal_test(self):

        meal_1, meal_2, meal_3, meal_4 = Meal()
        self.meal_list.append(meal_1)
        
        for key, value in self.foods_list.items():

            self.meal_list.append({key: foods[key]})
        
            if  >= self.max_protein:
                break
        
        return f'Meal = {self.meal}'

