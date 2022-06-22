from numpy import percentile
from .meal import Meal
from .food_list import foods, food_filter, calculate_calories
from random import randint


def meal_distribution(profile):
    diet_dict = {
        'low_carb': (2, 0, 1, 1),
        'dash': (2, 2, 2, 2),
        'paleolithic': (4, 0, 1, 1),
        'ketogenic': (3, 0, 1, 2),
    }
    protein_variety, carbohidrate_variety, fat_variety, extra_meals = diet_dict[profile.diet]

    return protein_variety, carbohidrate_variety, fat_variety, extra_meals

#  The MealsGenerator class will be responsable for storage the types of meals, sort the 
class MealsGenerator():

    def __init__(self, profile):

        self.profile = profile
        self.protein_variety = meal_distribution(profile)[0]
        self.carbohidrate_variety = meal_distribution(profile)[0]
        self.fat_variety = meal_distribution(profile)[0]
        self.extra_meals = meal_distribution(profile)[0]
        #  Inside properties
        #  These will be the lists used to separate the ingredients accordly to the profile 
        # preference and the type of the ingredient
        self.protein_ing_list = food_filter(_type='protein', allergics = self.profile.allergics)
        self.carbo_ing_list = food_filter(_type='carbohidrate', allergics = self.profile.allergics)
        self.fat_ing_list = food_filter(_type='fat', allergics = self.profile.allergics)
        #  Diet List will provide the major filter to build up the meal
        self.meals = ['breakfast', 'lunch', 'dinner']
        self.meal_dict = {}
    
    def count_meals(self):
        print(f'Building instances...')
        count=1
        #  each meal will be a instance of Meal class inside meal_dict
        for meal_time in self.meals:
            self.meal_dict[meal_time] = Meal(ingredients=[], meal_time=meal_time)
            if self.extra_meals:
                self.meal_dict[f'snack_{count}'] = Meal(ingredients=[], meal_time='snack')
                self.extra_meals -= 1
                count += 1

    #  This function will generate a dict with each meal according to the extra meals from profile
    # each key of the dict will be the meal_time itself and its values will be an instance of the 
    # Meal class
    def generate_meals(self):
        print(f'Preparing your dishes...')
        #  First thing to do is populate the number of meals
        self.count_meals()

        for meal_key in self.meal_dict.keys():
            for ingredient_num in range(self.protein_variety):
                #  Adding protein to the the Meal object
                random_protein = self.protein_ing_list[randint(0, len(self.protein_ing_list) -1)]
                self.meal_dict[meal_key].ingredients.append(random_protein)
            
            for ingredient_num in range(self.carbohidrate_variety):
                #  Adding carbo to the Meal object
                random_carbo = self.carbo_ing_list[randint(0, len(self.carbo_ing_list) -1)]
                self.meal_dict[meal_key].ingredients.append(random_carbo)

            for ingredient_num in range(self.fat_variety):
                #  Adding fat to the Meal object
                random_fat = self.fat_ing_list[randint(0, len(self.fat_ing_list) -1)]
                self.meal_dict[meal_key].ingredients.append(random_fat)
        
        return self.meal_dict

    #  Calculate and returns in grams the ammount of each ingredient need to fill the meal
    def calculate_ing_cal_need(self, min_meal_cal, ingredients_num, ingredients_cal):
        return (min_meal_cal / ingredients_num) / ingredients_cal

    #  This function will take the simple dictionary from generate_meals and calculate extra
    # properties
    def generate_detailed_meals(self):
        self.profile.calculate_parameters()

        #  This var calc the ammount of calories according to the profile wish
        target_calories = self.profile.calorie_consumption + (((self.profile.target_weight - self.profile.weight) / 30) * 200)
        print(target_calories)
        min_meal_calories = round(target_calories / (3 + self.extra_meals))

        self.generate_meals()
        for key in self.meal_dict.keys():
            for n, ingredient in enumerate(self.meal_dict[key].ingredients):

                ingredient_quant = self.calculate_ing_cal_need(
                    min_meal_cal=min_meal_calories, 
                    ingredients_num=len(self.meal_dict[key].ingredients), 
                    ingredients_cal=calculate_calories(ingredient))

                self.meal_dict[key].ingredients[n] = [ingredient, round(ingredient_quant, 2)]

            self.meal_dict[key].calculate_totals()
        
        return self.meal_dict

    def show_information(self):
        for key, value in self.meal_dict.items():
            print(f'\n{key} =>')
            print(f'    Ingredients =>', end='')
            for ingredient in value.ingredients:
                print(f' *{ingredient[0].capitalize()} - {ingredient[1]}g', end=' ')
            print(f'\n    Total calories => {round(value.total_calories)}cal')
            print(f'    Total protein => {round(value.total_protein)}g')
            print(f'    Total carbohidrates => {round(value.total_carbohidrate)}g')
            print(f'    Total fat => {round(value.total_fat)}g')