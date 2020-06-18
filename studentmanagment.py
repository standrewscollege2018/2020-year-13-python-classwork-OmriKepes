''' This program stores students names and classes.'''

class stduent:
    '''This class (student) has a name, class, age, phone number, gender.'''
    def __init__(self, name, age, phoneNumber, gender):
        '''This funcation runs all at the start and sets up all atributes.'''
        self._name = name
        self._age = age
        self._phone_number = phone_number
        # this funcation adds these adtributes to the student list
        student_list.append(self)
    def get_name(self):
        '''This funcation returns the name of the student.'''
        return(self._name)
    def get_age(self):
        '''This funcation returns the age of the student.'''
        return(self._age)
    def get_gender(self):
        '''This funcation returns the gender of the student.'''
        return(self._gender)
    def get_phoneNumber(self):
        '''This funcation returns the phoneNumber of the student.'''
        return(self._phoneNumber)
def create_student():
    '''This funcation allows the user to input a new students name, age, gender, phone number.'''
    new_name = input("Enter the new Students name: ")
    new_age = int(input("Enter the new students age: "))
    new_gender = input("Enter gender (F or F): ")
    new_phoneNumber = int(input("Enter phone number: "))
