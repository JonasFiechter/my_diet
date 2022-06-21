from .profile import Profile

class ProfileGenerator(Profile):
    def __init__(self):
        self.name = input(f'\nInput your name: ')
        self.age = input(f'\nInput your age: ')
        self.sex = input(f'\nInput your sex: ')
        self.height = input(f'\nInput your height: ')
        self.weight = input(f'\nInput your weight: ')

    def generator(self):
        profile_instance = Profile(
                                    name=self.name, 
                                    age=self.age, 
                                    sex=self.sex,
                                    height=self.height, 
                                    weight=self.weight
                                    )
        return profile_instance