class Profile:
    def __init__(self, name, sex, weight, target_weight, allergics, calorie_consumption, diet):
        self.name = name
        self.sex = sex
        self.weight = weight
        self.target_weight = target_weight
        self.allergics = allergics
        self.calorie_consumption = calorie_consumption
        self.diet = diet

    def calculate_parameters(self):
        pass
        # return min_protein, min_carbohidrate, min_fat