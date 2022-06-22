from .profile import Profile

def profile_generator2():
    profile_instance = Profile(                        
                        name=input(f'Input your name: '), 
                        sex=input(f'Input your sex: '),
                        weight=input(f'Input your weight: '),
                        alergics=input(f'Input your alergics: '),
                        calorie_consumption=input(f'Input your daily calorie comsumption: '),
                        diet=input(f'Input your diet type(low_carb, dash, paleolithic or ketogenic): '),
                        )
    return profile_instance

def profile_generator():
    profile_instance = Profile(                        
                        name='TEST', 
                        sex=1,
                        weight=1,
                        alergics=1,
                        calorie_consumption=3500,
                        diet='low_carb',
                        )
    return profile_instance
