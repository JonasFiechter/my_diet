from .profile import Profile

def profile_generator2():
    profile_instance = Profile(                        
                        name=input(f'Input your name: '), 
                        age=input(f'Input your age: '), 
                        sex=input(f'Input your sex: '),
                        height=input(f'Input your height: '), 
                        weight=input(f'Input your weight: '),
                        alergics=input(f'Input your alergics: '),
                        daily_calorie_consumption=input(f'Input your daily calorie comsumption: '),
                        diet=input(f'Input your diet type(low_carb, dash, paleolithic or ketogenic): '),
                        )
    return profile_instance

def profile_generator():
    profile_instance = Profile(                        
                        name='TEST', 
                        age=1, 
                        sex=1,
                        height=1, 
                        weight=1,
                        alergics=1,
                        daily_calorie_consumption=1,
                        diet='low_carb',
                        )
    return profile_instance
