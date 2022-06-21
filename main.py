from src.features.profile_generator.components.profile_generator import profile_generator
from src.features.meals_generator.components.meals_generator import MealsGenerator


def main():
    while True:
        profile = profile_generator()
        print(f'Profile name: {profile.name}')
        meals_gen = MealsGenerator(diet=profile.diet, extra_meals=2)
        my_meals = meals_gen.generate_meals()
        for key, value in my_meals.items():
            print(f'{key} => {value.ingredients}')
        input('press any key')


if __name__ == '__main__':
    main()