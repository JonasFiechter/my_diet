'''
This list of dicts returns each food nutritional values based into a portion of 100g
and each item of food returns the percentage of its total mass
'''

# Groups = ['Pasta','Cereal','Vegetable','Fruit','Milk','animal_protein', 'vegetable_protein', ]

def food_filter(_type, alergics):
    if not alergics:
        return [key for key in foods.keys() if foods[key]['type'] == str(_type)]
    else:
        return [key for key in foods.keys() if foods[key]['type'] == str(_type) and key not in alergics]

def calculate_calories(ingredient):
    return  (foods[ingredient]['protein'] * 4) + \
            (foods[ingredient]['carbohidrate'] * 4) + \
            (foods[ingredient]['fat'] * 9)

foods = {
    'rice': {
        'group': 'vegetable',
        'type': 'carbohidrate',
        'protein': 0.08,
        'fat': 0.04,
        'carbohidrate': 0.15,
    },
    'apple': {
        'group': 'fruit',
        'type': 'fat',
        'protein': 0.01,
        'fat': 0.01,
        'carbohidrate': 0.11,
    },
    'bean': {
        'group': 'vegetable',
        'type': 'carbohidrate',
        'protein': 0.11,
        'fat': 0.04,
        'carbohidrate': 0.15,
    },
    'meat': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 0.24,
        'fat': 0.21,
        'carbohidrate': 0.05,
    },
    'egg': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 0.28,
        'fat': 0.14,
        'carbohidrate': 0.05,
    },
    'chicken': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 0.26,
        'fat': 0.14,
        'carbohidrate': 0.05,
    },
    'fish': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 0.26,
        'fat': 0.14,
        'carbohidrate': 0.05,
    },
    'sheep': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 0.26,
        'fat': 0.14,
        'carbohidrate': 0.05,
    },
    'lasagna': {
        'group': 'pasta',
        'type': 'carbohidrate',
        'protein': 0.1,
        'fat': 0.20,
        'carbohidrate': 0.27,
    },
    'peanut': {
        'group': 'vegetable',
        'type': 'fat',
        'protein': 0.01,
        'fat': 0.30,
        'carbohidrate': 0.09,
    },
    'lettuce': {
        'group': 'vegetable',
        'type': 'carbohidrate',
        'protein': 0.04,
        'fat': 0.02,
        'carbohidrate': 0.14,
    },
    'cabbage': {
        'group': 'vegetable',
        'type': 'carbohidrate',
        'protein': 0.07,
        'fat': 0.03,
        'carbohidrate': 0.12,
    },
}

if __name__ == '__main__':
    pass