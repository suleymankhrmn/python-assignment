userInfo = {
    "Suleyman" : "123",
    "Joseph" : "ujk"
    }
checkValue = False
entryUsername = input("Please enter your username: ")

for value in userInfo:
    if(value == entryUsername):
        checkValue = True
    
        


if(checkValue):
    print("Hello " + entryUsername + " your password " + userInfo[entryUsername])
else:
    print("Hello " + entryUsername + ", See you later.")
