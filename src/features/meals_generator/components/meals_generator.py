from .meal import Meal
from .food_list import foods, food_filter


#  The MealsGenerator class will be responsable for storage the types of meals, sort the 
class MealsGenerator():

    def __init__(self, diet, protein_variety=1, carbohidrate_variety=1, fat_variety=1, extra_meals=0):

        self.protein_variety = protein_variety
        self.carbohidrate_variety = carbohidrate_variety
        self.fat_variety = fat_variety
        self.extra_meals = extra_meals
        #  Inside properties
        self.foods_list = foods
        self.min_protein = 10
        self.min_carbohidrate = 10
        self.min_fat = 10
        #  This will be the list used to sort the ingredients accordly to the profile preference
        self.protein_ingredients_list = food_filter(_type='protein')
        self.carbohidrate_ingredients_list = food_filter(_type='carbohidrate')
        self.fat_ingredients_list = food_filter(_type='fat')
        #  Diet List will provide the major filter to build up the meal
        self.meals = ['breakfast', 'lunch', 'dinner']
        self.meal_dict = {}
    
    def count_meals(self):
        count=1
        #  each meal will be a instance of Meal class inside meal_dict
        for meal_hour in self.meals:
            self.meal_dict[meal_hour] = Meal(ingredients=[], meal_time=meal_hour)
            if self.extra_meals:
                self.meal_dict[f'snack_{count}'] = Meal(ingredients=[], meal_time='snack')
                self.extra_meals -= 1
                count += 1


    def generate_meals(self):
        #  First thing to do is populate the number of meals
        self.count_meals()

        for meal_key in self.meal_dict.keys():
            for food_key, food_value in foods.items():

                #  Adding ingredients to the the Meal object
                self.meal_dict[meal_key].ingredients.append(food_key)

                #  Adding each property to each Meal instance
                self.meal_dict[meal_key].total_protein += food_value['protein']
                self.meal_dict[meal_key].total_fat += food_value['fat']
                self.meal_dict[meal_key].total_carbohidrate += food_value['carbohidrate']
        
        return self.meal_dict

