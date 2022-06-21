from src.features.profile_generator.components.profile_generator import profile_generator
from src.features.meals_generator.components.meals_generator import MealsGenerator


def main():
    while True:
        profile = profile_generator()
        meals_gen = MealsGenerator()
        meals_gen.calc_meal_test()
        input('press any key')


if __name__ == '__main__':
    main()