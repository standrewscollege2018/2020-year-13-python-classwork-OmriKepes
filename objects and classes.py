''' This program demonstrates how to use classes and objects.'''

class Enemy:
    ''' The enemy class has life, name, and funcations that do something.'''
    ''' To support encapsulation, we put underscores in front of variable names.'''
    _life = 3

    def get_life(self):
        '''This funcation returns the amount of life remaining.'''
        return self._life
    def attack(self):
        '''This funcation substracts 1 from the object's health.'''
        print("Ouch!")
        self._life-=1
#create an enemy object and store in variable called enemy1
enemy1 = Enemy()
enemy1.attack()
#call the get_life funcation and print out the life
print(enemy1.get_life())


