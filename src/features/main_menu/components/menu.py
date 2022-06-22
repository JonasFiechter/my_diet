from src.features.profile_generator.profile_generator import profile_generator, generate_alergics
from src.features.meals_generator.meals_generator import MealsGenerator

def menu():
    #  Generate profile
    print(f'Welcome to MyDiet app!')

    profile = profile_generator()
    print(f'Hello: {profile.name}!')
    meals = MealsGenerator(profile=profile, extra_meals=0)
    meals.generate_detailed_meals()
    meals.show_information()
    while True:
        if input(f'\npress: ') == 'e':
            return False