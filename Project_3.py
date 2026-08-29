import string
import random

characters= (string.ascii_letters + string.digits + string.punctuation)  #combination of alphanumeric alphabet and special characters
password = []  #creates an empty list for the variable password as a base step
length = int(input("How long do you want your password to be? "))  #convert inputed stringed numbers to integers and save it to length


for i in range(length-2):  #the number of times the loop runs is acertained a for loop works well, and the length is reduced by 2 so that at least one number and special character are added
    password.append(random.choice(characters)) #the module random is called with choice to select characters and put it in tge empty list
    
password.append(random.choice(string.digits ))  # this ensures at least one digit is chosen
password.append(random.choice(string.punctuation)) #this ensures at least one special character is chosen
random.shuffle(password) #shuffles the appended password
final_password = ("".join(password)) #joins the shuffled password as a word with no quotes since its in a list and saves it to the variable
print(final_password) # prints the final results


