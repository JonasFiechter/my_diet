from .food_list import foods

class Meal:
    def __init__(self, 
                    ingredients=[],
                    total_protein=0, 
                    total_fat=0, 
                    total_carbohidrate=0,
                    total_calories=0,
                    meal_time=''):

        self.ingredients = ingredients
        self.total_protein = total_protein
        self.total_fat = total_fat
        self.total_carbohidrate = total_carbohidrate
        self.total_calories = total_calories
        self.meal_time = meal_time
    
    def calculate_totals(self):
        for i in self.ingredients:
            self.total_protein += foods[i[0]]['protein'] * i[1]
            self.total_fat += foods[i[0]]['fat'] * i[1]
            self.total_carbohidrate += foods[i[0]]['carbohidrate'] * i[1]
            self.total_calories = (self.total_fat * 9) + \
                                  (self.total_carbohidrate * 4) + \
                                  (self.total_protein * 4)

    