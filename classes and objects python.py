''' This program demonstrates how to use classes and objects.'''

class Enemy:
    ''' The enemy class has life, name, and funcations that do something.'''
    def __init__(self, name, life):
        '''This funcation runs on instantiation and sets up all attributes.'''
        self._life = life
        self._name = name
        #add the new enemy object to the enemy_list list
        enemy_list.append(self)
    def get_name(self):
        '''This funcation returns the name of the enemy.'''
        return(self._name)
    def get_life(self):
        '''This funcation returns the amount of life remaining.'''
        return self._life
    def attack(self):
        '''This funcation substracts 1 from the object's health.'''
        print("Ouch!")
        self._life -= 1
    def add(self):
        print("Increased health!")
        self._life+=1
def show_all():
    '''This funcation displays details of all enemies in enemy_list.'''
    for enemy in enemy_list:
        print(enemy.get_name())
        
def life_check():
    '''This funcation asks the user for an integar, and then returns the names of all enemies who have at least that much life left.'''
    check =  int(input("Enter a number: "))
    for enemy in enemy_list:
        if enemy.get_life()>= check:
            print(enemy.get_name())
def create_enemy():
    '''This funcation creates a new enemy with a name and life.'''
    new_name = input("Enter new name: ")
    new_life = int(input("Enter new life: "))
    Enemy(new_name, new_life)
    enemy_list.append(new_name, new_life)
# The enemy_list stores all the enemy objects
enemy_list = []
create_enemy()
life_check()



