from src.features.profile_generator.profile_generator import profile_generator
from src.features.meals_generator.meals_generator import MealsGenerator
from time import sleep

def menu():
    sleep(0.7)
    print(f'Welcome to MyDiet app!')
    #  Generate profile
    profile = profile_generator()
    meals = MealsGenerator(profile=profile)
    print(f'Hello: {profile.name}!')
    
    while True:
        sleep(0.7)
        print(f'\nTo generate your meals input "generate"')
        sleep(0.7)
        print(f'To print your meals input "print"')
        sleep(0.7)
        print(f'Input "exit" or "quit" to leave')
        command = input(f'\n=>').lower()
        if command == 'exit' or command == 'quit':
            return False
        else:
            options(command, meals)

def options(command, meals):
    if command == 'generate':
        meals.generate_detailed_meals()
    elif command == 'print':
        meals.show_information()