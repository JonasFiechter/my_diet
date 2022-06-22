from .profile import Profile
from ..meals_generator.food_list import foods
from time import sleep

def profile_generator():
    profile_instance = Profile(                        
                        name=input(f'Input your name: '), 
                        sex=input(f'Input your sex: '),
                        weight=input(f'Input your weight: '),
                        target_weight=input(f'Input your target weight: '),
                        allergics=check_allergy(),
                        calorie_consumption=input(f'Input your daily calorie comsumption: '),
                        diet=check_diet(),
                        )
    sleep(0.7)
    print(f'Profile created!')
    return profile_instance

def profile_generator2():
    profile_instance = Profile(                        
                        name='Peter Belly', 
                        sex='male',
                        weight=70,
                        target_weight=80,
                        allergics=check_allergy(),
                        calorie_consumption=2500,
                        diet='low_carb',
                        )
    return profile_instance

def check_diet():
    diet_list = ('low_carb', 'dash', 'paleolithic', 'ketogenic')
    diet = input(f'Input your diet type(LOW CARB, DASH, PALEOLITHIC or KETOGENIC): ').lower().replace(' ', '-')
    if diet not in diet_list:
        print(f'Invalid command! try again...')
        check_diet()
    else:
        return diet

def check_allergy():
    command = input(f'Do you have any allergic ingredient to avoid? (enter "yes" or press "Enter" to continue): ')
    if command.lower() == 'yes':
        return generate_allergics()
    elif command and command != 'yes':
        print(f'Invalid command! try again...')
        check_allergy()
    else:
        return []

def generate_allergics(allergic_list=[]):
    allergic = input('Input your allergic: ')

    #  Invalid commands check
    if allergic not in foods:
        allergic = input(f'Allergic not found, check the spelling and try again or press "ENTER" to contiue: ')
    elif allergic in allergic_list:
        sleep(0.5)
        print(f'Allergic already added!')
    if allergic and allergic not in allergic_list:
        allergic_list.append(allergic)
        sleep(0.5)
        print('Allergic added!')
    else:
        return allergic_list
    run = True
    while run:
        print(f'Your list => {allergic_list}')
        command = input(f'Input "add" to add more allergics or press "Enter" to exit: ').lower()
        if command == 'add':
            return generate_allergics(allergic_list)
        elif command and command != 'add':
            sleep(0.5)
            print(f'Command invalid! try again.')
        else:
            print(f'Closing function...')
            return allergic_list
    

