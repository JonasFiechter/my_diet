from .profile import Profile

def profile_generator():
    profile_instance = Profile(                        
                        name=input(f'Input your name: '), 
                        age=input(f'Input your age: '), 
                        sex=input(f'Input your sex: '),
                        height=input(f'Input your height: '), 
                        weight=input(f'Input your weight: ')
                        )
    return profile_instance

