about: str = ''' 
    Hello everyone this is my first python project based on a simple 
    calculator.If you need do support DM me on the address below 
    
    With Regards,
    HARISH.B
    Team Capricorn
'''
name = str(input("Your name : "))
b_year = int(input("Enter the birth year : "))
cy_year = int(input("Enter the year from which to be calculated : "))
age = cy_year - b_year
age = str(age)
weight_kgs = int(input("Enter your weight(kgs) : "))
weight_lbs = str(round(weight_kgs * 2.205))
print("Hi " + name + " Your age is :" + age + "\n" + "weight (lbs) : " + weight_lbs + " lb ")
cname = name[:]
print(cname)