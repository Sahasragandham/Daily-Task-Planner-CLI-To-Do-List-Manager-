# Function to display welcome banner
def welcome():
  print("="*36)
  print(" "*6 +"📜 DAILY TASK PLANNER")
  print(" "*6 +"Organize • Plan • Achieve")
  print("="*36) 

# Function to display menu options
def display_menu():
    print("\nMY TASK MANAGER")
    print("\n1️⃣ Add Task")
    print("2️⃣ Remove Task")
    print("3️⃣ View Tasks")
    print("4️⃣ Exit")  

# Main function where the program runs
def main():
  welcome()   # Calling welcome function

  task_list=[]            # Stores current active tasks
  removed_task_list=[]    # Stores removed (completed) tasks
  total_tasks=[]          # Stores all tasks ever added

  # Infinite loop until user chooses Exit
  while True:
    display_menu()    # Show menu every time

    # Taking user choice
    choice = int(input("\nEnter your choice: ")) 

    # Option 1: Add Task
    if choice == 1:
      adding_task = input("\n➕ Enter Task to Add: ")
      task_list.append(adding_task)     # Add to active list
      total_tasks.append(adding_task)   # Add to total list
      print("Task added successfully!")
      continue

    # Option 2: Remove Task  
    elif choice == 2:
      length_of_task_list = len(task_list)
      print("These Are The Tasks Present In Your Task List")

      # Display tasks with numbering
      for i in range(length_of_task_list):
        print(f"{i+1}. {task_list[i]}")
      remove_task = input("\n❌ Enter the task to ramove: ")  
      task_list.remove(remove_task)         # Remove from active list
      removed_task_list.append(remove_task) # Add to removed list
      print("Task Removed successfully!")
      continue

    # Option 3: View Tasks  
    elif choice == 3:
      print("="*4 + "YOUR TASKS" + "="*4)
      length_of_total_tasks=len(total_tasks)

      # If tasks exist
      if length_of_total_tasks > 0: 
        for each_task in total_tasks:

          # If task is still active
          if each_task in task_list:
            print(f"[ ] {each_task}")

          # If task is completed/removed  
          elif each_task in removed_task_list:
            print(f"[✓] {each_task}")
      else:
        print("No tasks available.")
      continue  

    # Option 4: Exit program  
    elif choice == 4:   
      print("Thank you for using TO-DO List Manager💝")
      break

    # If user enters invalid choice  
    else:
      print("Invalid Choice")
      continue 

# Calling main function to start program             
main()  