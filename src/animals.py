class Animal:

    def __init__(self, behaviour, attributes):
        self.x = 0
        self.y = 0
        self.lifes = 0
        self.behaviour = behaviour
        self.initiative = attributes.get('initiative', 0)
        self.visualRange = attributes.get('visualRange', 0)

    def act(self, input):
        return self.behaviour.decide(input)

class Horse(Animal):
    pass

class Wolf(Animal):
    pass
