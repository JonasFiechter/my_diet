from src.features.profile_generator.components.profile_generator import profile_generator
from src.features.meals_generator.components.meals_generator import MealsGenerator


def main():
    while True:
        profile = profile_generator()
        print(f'Hello: {profile.name}!')

        meals_gen = MealsGenerator(profile=profile, extra_meals=2)
        meals_gen.generate_detailed_meals()
        meals_gen.show_information()

        if input(f'\npress: ') == 'e':
            return False


if __name__ == '__main__':
    main()