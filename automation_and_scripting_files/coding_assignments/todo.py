# Started as example of how to use open() and write(), modified to be a working To Do list text file generator.
"""
Simple to-do list creator, if file 'todo.txt' does not exist, will create it, if it does exist,
will append new tasks until the user enters the text "quit"
"""

# Use with open() in append mode and file.write() to append two additional items to the todo.txt file
"""continue_todo = True

with open('todo.txt', 'a') as file:    
    while continue_todo:
        new_task = input("Enter New task, 'print' or 'quit': ")
        if new_task == 'quit':
            continue_todo = False
            print("Exiting ToDo!")
            break        
        elif new_task == 'print':
            with open('todo.txt', 'r') as file:
                content = file.read()
                print(content)           
        else:
            with open('todo.txt', 'a') as file:
                to_do = file.write(new_task + '\n')
"""
# The following changes were recommended by Gemini AI to reduce the number of open/read/write operations
# and moving new task creation to happen in memory via todo_list, which is written to the txt file as part of the exiting process.
# When reopening the app, the exsiting todo.txt file content is read into the todo_list, with new tasks appended to the current list
# of previous tasks.

continue_todo = True
todo_list = []  # Store tasks in memory

try:
    with open('todo.txt', 'r') as file:
        todo_list = file.readlines()  # Read existing tasks into the list
except FileNotFoundError:
    pass  # Handle the case where the file doesn't exist yet

while continue_todo:
    new_task = input("Enter New task, 'print' or 'quit': ")
    if new_task == 'quit':
        continue_todo = False
        print("Exiting ToDo!") #removed 'break'
    elif new_task == 'print':
        for task in todo_list:
            print(task.strip())  # Print each task without extra newlines
    else:
        todo_list.append(new_task + '\n')  # Add the new task to the list

with open('todo.txt', 'w') as file:  # Open the file once for writing
    file.writelines(todo_list)  # Write all tasks to the file