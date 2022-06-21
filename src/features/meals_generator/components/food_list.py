'''
This list of dicts returns each food nutritional values based into a portion of 100g
and each item of food returns the percentage of its total mass
'''

# Groups = ['Pasta','Cereal','Vegetable','Fruit','Milk','animal_protein', 'vegetable_protein', ]

def food_filter(_type):
    return [key for key in foods.keys() if foods[key]['type'] == str(_type)]

foods = {
    'rice': {
        'group': 'vegetable',
        'type': 'carbohidrate',
        'protein': 0.8,
        'fat': 0.4,
        'carbohidrate': 15,
        'calories': 74,
    },
    'apple': {
        'group': 'fruit',
        'type': 'fat',
        'protein': 0.1,
        'fat': 0.1,
        'carbohidrate': 11,
        'calories': 74,
    },
    'bean': {
        'group': 'vegetable',
        'type': 'carbohidrate',
        'protein': 11,
        'fat': 0.4,
        'carbohidrate': 15,
        'calories': 74,
    },
    'meat': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 24,
        'fat': 21,
        'carbohidrate': 0.5,
        'calories': 74,
    },
    'egg': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 28,
        'fat': 14,
        'carbohidrate': 0.5,
        'calories': 74,
    },
    'chicken': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 26,
        'fat': 14,
        'carbohidrate': 0.5,
        'calories': 74,
    },
    'fish': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 26,
        'fat': 14,
        'carbohidrate': 0.5,
        'calories': 74,
    },
    'sheep': {
        'group': 'animal_protein',
        'type': 'protein',
        'protein': 26,
        'fat': 14,
        'carbohidrate': 0.5,
        'calories': 74,
    },
    'lasagna': {
        'group': 'pasta',
        'type': 'carbohidrate',
        'protein': 10,
        'fat': 20,
        'carbohidrate': 27,
        'calories': 261,
    },
    
}

if __name__ == '__main__':
    print(foods.items())