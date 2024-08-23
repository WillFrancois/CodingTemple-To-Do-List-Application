#Initial variables for storing and using the To-Do list
menu_text = "Welcome to the To-Do List App!\n\nMenu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete or incomplete\n4. Delete a task\n5. Quit\n\n"
todo_list = []
user_inp = input(menu_text)

#Functions for modifying the todo_list variable
def add_task(task):
    todo_list.append([task, False])
    print()

def view_tasks():
    if len(todo_list) == 0:
        print("\nNo tasks!\n")
    else:
        #Extra print statements are used for readability as newlines in the for loop can lead to messy output!
        #These are also used in in the mark_complete and delete_task function for readability and spacing.
        print()
        for i in range(len(todo_list)):
            print(i+1, ". ", todo_list[i][0], " - Complete" if todo_list[i][1] else " - Incomplete", sep="")
        print()

def mark_complete(task_number):
    todo_list[task_number-1][1] = not todo_list[task_number-1][1]
    print()

def delete_task(task_number):
    todo_list.pop(task_number-1)
    print()

#Validates user input for cases 3 and 4 in the main menu
def validate_task_number(function):
    try:
        task_number = int(input("Please provide the task number you would like to delete: "))
        function(task_number)
    except IndexError:
            print("\nTask value doesn't exist, please try again!\n")
    except ValueError:
            print("\nInvalid input, please try again!\n")
    except Exception:
        print("\nSorry, something went wrong. Please try again!\n")
    else:
        print("Operation successful!\n")
    #A finally block would go here if there was a case where code would run regardless of whether
    #was a raised exception or not, but is not necessary for full functionality

while user_inp != "5":
    match user_inp:
        case '1':
            new_task = input("\nPlease provide the name of the task you would like to add: ")
            add_task(new_task)

        case '2':
            view_tasks()

        #Case 3 and 4 both utilize functions as arguments to allow both cases to
        #use the same code without needing to have it repeated and improve readability

        case '3':
            view_tasks()
            validate_task_number(mark_complete)

        case '4':
            view_tasks()
            validate_task_number(delete_task)

        case _:
            print("\nSorry, I was unable to process your input! Please try again.\n")

    #The loop begins again here!
    user_inp = input(menu_text)
