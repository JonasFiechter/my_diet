from meal import Meal
from food_list import foods


class MealsGenerator():
    def __init__(self):
        self.foods_list = foods
        self.meal = []
        self.max_protein = 0
        self.max_carbohidrates = ''
        self.max_fat = ''

    def calc_meal_low_carb(self):
        pass

    def calc_meal_test(self):
        protein_limit = 25
        temp_protein = 0
        for key, value in self.foods_list.items():

            self.meal.append({key: foods[key]})
            temp_protein += value['protein']

            if temp_protein >= protein_limit:
                break
        
        print(f'Meal = {self.meal}')


m1 = MealsGenerator()
m1.calc_meal_test()