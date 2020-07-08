#atama islemleri
age = input("Are you a cigarette addict older than 75 years old? ")
chronic = input("Do you have a severe chronic disease? ")
immune = input("Is your immune system too weak? ")

# risk e boolen değer atanır
risk = age == "Yes" or chronic == "Yes" or immune == "Yes"

#risk dogruluğuna göre print yazdırılır
if(risk):
    print("You are in risky group")
else:
    print("You are not in risky group")
