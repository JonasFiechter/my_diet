from .profile import Profile
from ..meals_generator.food_list import foods
from time import sleep

def profile_generator2():
    profile_instance = Profile(                        
                        name=input(f'Input your name: '), 
                        sex=input(f'Input your sex: '),
                        weight=input(f'Input your weight: '),
                        alergics=generate_alergics(),
                        calorie_consumption=input(f'Input your daily calorie comsumption: '),
                        diet=input(f'Input your diet type(low_carb, dash, paleolithic or ketogenic): '),
                        )
    return profile_instance

def profile_generator():
    profile_instance = Profile(                        
                        name='TEST', 
                        sex=1,
                        weight=1,
                        alergics=check_allergy(),
                        calorie_consumption=3500,
                        diet='low_carb',
                        )
    return profile_instance

def check_allergy():
    command = input(f'Do you have any alergic ingredient to avoid? (enter "yes" or press "Enter" to continue): ')
    if command.lower() == 'yes':
        return generate_alergics()
    elif command and command != 'yes':
        print(f'Invalid command! try again...')
        check_allergy()
    else:
        return []

def generate_alergics(alergic_list=[]):
    alergic = input('Input your alergic: ')

    #  Invalid commands check
    if alergic not in foods:
        alergic = input(f'Alergic not found, check the spelling and try again or press "ENTER" to contiue: ')
    elif alergic in alergic_list:
        sleep(0.5)
        print(f'Alergic already added!')
    if alergic and alergic not in alergic_list:
        alergic_list.append(alergic)
        sleep(0.5)
        print('Alergic added!')
    else:
        return alergic_list
    run = True
    while run:
        print(f'Your list => {alergic_list}')
        command = input(f'Input "add" to add more alergics or press "Enter" to exit: ').lower()
        if command == 'add':
            return generate_alergics(alergic_list)
        elif command and command != 'add':
            sleep(0.5)
            print(f'Command invalid! try again.')
        else:
            print(f'Closing function...')
            return alergic_list
    

