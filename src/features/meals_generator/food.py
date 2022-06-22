#  This class will instanciate an object for food with more parameters than original dicts list.
# Like quantity and others


class Food:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight