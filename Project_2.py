running_total = 0
while  True:
   expense =  input("Type in an expense: ")
   if expense == "done":
       break
   try:
        expense = int(expense)
        running_total += expense
   except ValueError:
        print("That is not a valid response, \n Please input an expense")
   
print(f"Total expense is:  {running_total}")