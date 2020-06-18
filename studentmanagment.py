''' This program stores students names and classes.'''

class students:
    '''This class (student) has a name, class, age, phone number, gender.'''

    def __init__(self, name, age, phone_number, gender, classes):
        '''This funcation runs all at the start and sets up all atributes.'''
        self._name = name
        self._age = age
        self._phone_number = phone_number
        self._classes = classes
        self._enrolled = True
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
        return(self._phone_number)
    def get_class(self._classes):
        '''This funcation returns the classes of the student.'''
        return(self._class)
    def get_enrolled(self._enrolled):
        '''This funcation returns the status of enrollment.'''
        return(_enrolled)
def create_student():
    '''This funcation allows the user to input a new students name, age, gender, phone number.'''
    new_name = input("Enter the new Students name: ")
    new_age = int(input("Enter the new students age: "))
    new_gender = bool(input("Enter gender (M or F): "))
    new_phone_number = int(input("Enter phone number: "))
def show_all():
    '''This funation allows the user to see all students and all deails.'''
    
#the list of students enrolled
student_list=[]
