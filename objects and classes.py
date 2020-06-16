''' This program demonstrates how to use classes and objects.'''

class Enemy:
    ''' The enemy class has life, name, and funcations that do something.'''

    def __init__(self, name, life):
        '''This funcation runs on instantiation and sets up all attributes.'''
        self._life = life
        self._name = name
    def get_life(self):
        '''This funcation returns the amount of life remaining.'''
        return self._life
    def attack(self):
        '''This funcation substracts 1 from the object's health.'''
        print("Ouch!")
        return self._name
        self._life -= 1
    def add(self):
        print("Increased health!")
        self._life+=1
#create an enemy object and store in variable called enemy1
enemy1 = Enemy("Jordan",5)
enemy2 = Enemy("Alan",10)
#call the get_life funcation and print out the life
print(enemy1.get_life())
print(enemy1.attack())
print(enemy1.get_life())

