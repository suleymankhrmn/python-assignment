number = input("Please entry value : ")


numberLenght = len(number)
createdNumber = 0
isString = False
for value in number:
    if(not(value.isdigit())):
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        isString = True
        break
    createdNumber = createdNumber + int(value) ** numberLenght
if(not isString):
    if( createdNumber == int(number)):
        print(number + " is an Armstrong number")
    else:
        print(number + " is not an Armstrong number")
        
