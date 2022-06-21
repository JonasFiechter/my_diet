from .meal import Meal
from .food_list import foods


class MealsGenerator():
    def __init__(self):
        self.foods_list = foods
        self.max_protein = 10
        self.max_carbohidrates = 10
        self.max_fat = 10
        self.meal_dict = {}

    #  The idea with this testing function is to calc the minimum of each nutrient needed for meal
    # and return 4 Meals instances each one with the right ammount of mass for person's profile.
    # after its working it will be intersting to add a functionality that creates a category for the
    # meal, like: "low-carb", "extra-protein" etc...
    def calc_meal_test(self):

        #  each meal will be a instance of Meal class inside meal_dict
        self.meal_dict['breakfast'] = Meal(ingredients=[], meal_time='breakfast')
        self.meal_dict['lunch'] = Meal(ingredients=[], meal_time='lunch')
        self.meal_dict['snack'] = Meal(ingredients=[], meal_time='snack')
        self.meal_dict['dinner'] = Meal(ingredients=[], meal_time='dinner')

        for meal_key in self.meal_dict.keys():
            for food_key, food_value in foods.items():

                #  Adding ingredients to the the Meal object
                self.meal_dict[meal_key].ingredients.append(food_key)

                #  Adding each property to each Meal instance
                self.meal_dict[meal_key].total_protein += food_value['protein']
                self.meal_dict[meal_key].total_fat += food_value['fat']
                self.meal_dict[meal_key].total_carbohidrate += food_value['carbohidrate']
            
        print(f'Meals => {self.meal_dict.items()}')
        return f'Meals = {self.meal_dict}'

