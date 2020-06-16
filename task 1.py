'''This program does variations and inputs.'''

#variations can store one piece of infomation
#name them well, lower case, underscore between words

inputs = []
ask = True
while ask == True:
    mydick = input()
    if mydick=='#':
        ask = False
    else:
        inputs.append(mydick)

for i in range(len(penis)-1):
    if inputs[i+1]<inputs[i]:
        print('Down')
    elif inputs[i+1]>inputs[i]:
        print('Up')

    
    
          
