'''This program does variations and inputs.'''

#variations can store one piece of infomation
#name them well, lower case, underscore between words

ask= True
counter=0
old_num=0
while ask== True:
    num = int(input("Enter number: "))
    if num == 0:
        ask = False
    else:
        counter+=1
        old_num+=num
avg=old_num/counter
avgr=round(avg,1)
print (avgr)
        


