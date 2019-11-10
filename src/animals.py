class Animal:

    def __init__(self, behaviour, attributes):
        self.x = 0
        self.y = 0
        self.lifes = 0
        self.behaviour = behaviour
        self.initiative = attributes.get('initiative', 0)

    def act(self, input):
        return self.behaviour.decide(input)

class Hunter(Animal):
    pass

class Prey(Animal):
    pass

class Horse(Prey):
    pass

class Wolf(Hunter):
    pass
