from src.features.main_menu.components.menu import menu

def main():
    if check():
        menu()
    else:
        print('See ya...')

def check():
    print('''
    Terms of use:
    ------------------------------
    This app creates an optimized sugestion of diet for you depending on your diet choice.
    This sugestion does not overrides an especiallist diet or Nutricionist or any other
    health professional order or sugestion.
    ------------------------------
    Diets with lower calories and carbohidrates than your daily needs can cause NAUSEA, WEAKNESS,
    HEADACHE and other sintoms, if you want to loose weight without experience, check again your
    daily calories needs and make sure the diference between 'total daily meals calories' and your
    'daily calories needs' is smaller than 200cal.
    ------------------------------
    ''')
    run = True
    while run:
        choice = input(f'If you agree with the terms enter "yes" or press "Enter" to exit: ')
        if choice.lower() == 'yes':
            run = False
            return True
        elif choice and choice != 'yes':
            print('Command invalid!')
        else:
            run = False
            return False

if __name__ == '__main__':
    main()