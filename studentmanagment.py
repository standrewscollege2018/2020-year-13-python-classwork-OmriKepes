from guizero import App

''' This program is a student management system, allowing users to add student records and run reports. '''
class Student:
    ''' The student class has a name, age, phone number, gender and a list of classes they are enrolled in. 
    All students are automatically set as enrolled when instantiated.
    Each student belongs to student_list. '''
    
    def __init__(self, name, age, phone, gender, classes):
        ''' This function sets the attributes of the new student.
        It sets every student to being enrolled by default. 
        It also adds the new student to student_list. '''
        
        self._name = name
        self._age = age
        self._phone = phone
        self._gender = gender
        self._classes = classes
        self._enrolled = True
        
        student_list.append(self)
        
    def get_name(self):
        ''' Return the name of the student. '''
        
        return self._name

    def get_age(self):
        ''' Return the age of the student. '''
        
        return self._age
    
    def get_phone(self):
        ''' Return the phone number of the student. '''
        
        return self._phone
    
    def get_gender(self):
        ''' Return the gender of the student. '''
        
        return self._gender
    
    def get_classes(self):
        ''' Return the list of classes the student is signed up for. '''
        
        return self._classes
    
    def get_enrolled(self):
        ''' Return whether or not a student is currently enrolled. '''
        
        return self._enrolled

def generateStudents():
    ''' Import students from the myRandomStudents csv file. '''
    
    import csv
    with open('names.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            classes=[]
            i=4
            while i in range(4, 9):
                classes.append(line[i])
                i+=1
            Student(line[0], int(line[1]), line[2],line[3], classes)


def show_all():
    ''' This function shows the names of all students. '''
    
    for student in student_list:
        print(student.get_name(),student.get_age(),student.get_classes())

def create_student():
    '''This funcation allows the user to create a new student entry.'''
    name = input("Enter name: ")
    age = int_check("Enter age:")
    phone = int(input("Phone: "))
    gender = input("Gender: ")
    enrolled =True

def count_class():
    classID=input("Enter class code")
    total = 0
    for student in student_list:
        if classID.upper() in student.get_classes():
            total = total + 1
        else:
            pass
    print (total)

def search():
    '''This funcation allows the user to search for a student.'''
    name = input("Enter name: ")
    for student in student_list:
        if name.lower() in student.get_name().lower():
            show_details(student)
            students_age(student)

def int_check(msg):
    '''This funcation checks if an input is an int.'''
    run = True
    while run == True:
        try:
            num = int(input(msg))
            return num
        except:
            print("Please enter an integer!")

def show_details(searched_student):
    '''This funcation displays the details of the student.'''
    print("#################")
    print(searched_student.get_name())
    print("#################")
    print(searched_student.get_age())
    print(searched_student.get_phone())
    print(searched_student.get_classes())
def students_age(searched_student):
    '''This function allows the user to search a student and get their age.'''
    print(" {} is {} years old".format(searched_student.get_name(), searched_student.get_age()))


student_list = []

# generateStudents()
search()

