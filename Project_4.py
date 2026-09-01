score = 0
capital = input("What is the capital of France? ")
if  "paris" == capital.lower().strip():
    print ("CORRECT!!!")
    score += 1
else :
    print("Wrong answer, Try Again! ")
    
water = input("What is the chemical symbol of Water? ")
if "H2O" == water.upper().strip():
    print ("CORRECT!!!")
    score += 1
else :
    print("Wrong answer, Try Again! ")
    
planet = input(" Which Planet is the largest planet among the Solar System? ")
if "jupiter" == planet.lower().strip():
    print ("CORRECT!!!")
    score += 1
else :
    print("Wrong answer, Try Again! ")
    
print(f"Your total score is: {score}")
    
    