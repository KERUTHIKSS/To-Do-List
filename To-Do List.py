filename = "tasks.txt"

tasks = []

open(filename, 'a').close()

file = open(filename, 'r')
for line in file:
    tasks.append(line.strip())
file.close()


while True:
    print("\n----- To-Do List -----")
    print("1. See all tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")
    print("----------------------")

    choice = input("Enter your choice (1-4): ")


    if choice == '1':
        print("\n=== Your Tasks ===")

        if len(tasks) == 0:
            print("You have no tasks.")
        else:

            task_number = 1
            for task in tasks:
                print(f"{task_number}. {task}")
                task_number = task_number + 1

    elif choice == '2':

        new_task = input("What task do you want to add? ")

        tasks.append(new_task)
        print(f"'{new_task}' was added to your list!")

        file = open(filename, 'w') 
        
        for task in tasks:
            file.write(task + '\n') 
            
        file.close()

    elif choice == '3':
        print("\n=== Remove a Task ===")

        task_number = 1
        for task in tasks:
            print(f"{task_number}. {task}")
            task_number += 1 
            
        num_to_remove = int(input("Enter the number of the task to remove: "))

        index_to_remove = num_to_remove - 1

        if 0 <= index_to_remove < len(tasks):

            tasks.pop(index_to_remove)
            print("Task removed!")

            file = open(filename, 'w')
            for task in tasks:
                file.write(task + '\n')
            file.close()
        else:
            print("That's not a valid task number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")