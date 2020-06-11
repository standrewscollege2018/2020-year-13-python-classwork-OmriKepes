'''This program does variations and inputs.'''

#variations can store one piece of infomation
#name them well, lower case, underscore between words

penis = []
ask = True
while ask == True:
    mydick = input()
    if mydick=='#':
        ask = False
    else:
        penis.append(mydick)

for i in range(len(penis)-1):
    if penis[i+1]<penis[i]:
        print('Down')
    elif penis[i+1]>penis[i]:
        print('Up')

    
    
          
