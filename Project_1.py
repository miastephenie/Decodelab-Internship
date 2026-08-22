import json


def add_tasks():  # defining a function (add_task)
    task = ""         # loops base step , starting point 
    while task != "done":
          task = input("Enter a task (or 'done' to finish): ")
          if task != "done":
                my_tasks.append(task) # stores the value placed in task in my_tasks
    with open("tasks.json", "w") as file:
           json.dump(my_tasks, file)


def view_tasks():  #defining a function (view_tasks)
    for index, task in enumerate(my_tasks): 
     #index align the number position enumerate gives with the task indently
         print(index +1 , task) #ensuring the alignment start with 1 not 0
         
         
if __name__ == "__main__":
  try:
    with open("tasks.json", "r") as file:
        my_tasks =json.load(file)
  except:
    my_tasks = [] 
  choice = ""
  while choice != 3:  #base step for the loop to keep running
    print("1.Add tasks")
    print("2.View tasks")
    print("3.Exit")
    
    try:
        choice= int(input("Pick a choice from 1 to 3:  "))
    except:
        print ("Please enter a number!")
        choice = 0
        
        
    
    if choice == 1:
        add_tasks()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        print("Goodbye!!!")
    else:
        print("Please pick a number between 1 and 3")
        
  
    
  
    
   


    
