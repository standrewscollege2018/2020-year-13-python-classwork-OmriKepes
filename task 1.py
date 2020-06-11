'''This program does variations and inputs.'''

#variations can store one piece of infomation
#name them well, lower case, underscore between words

ask= True
num1 = int(input("Enter first number: "))
counter = 0
total_add = 0
while ask==True:
    num=int(input("Number: "))
    counter = counter+1
    if counter<num1:
        total_add = total_add+num
    else:
        total_add = total_add+num
        ask= False
print (total_add)
    
