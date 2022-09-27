income = float(input("Enter the annual income: "))\
if (10000<= income <= 85528):\
    Tax = ((income*18)/100)-556.2\
elif income >= 85528: \
    Tax =((income- 85528)*32)/100+14839.2\
elif (-100 <= income<=1000): \
    Tax = 0.0\
Tax = round(Tax, 0)\
print("The tax is:", Tax, "thalers")}
