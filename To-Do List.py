#Initial variables for storing the To-Do list
todo_list = []
user_inp = input("Welcome to the To-Do List App!\n\nMenu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete or incomplete\n4. Delete a task\n5. Quit\n\n")

#Functions for modifying the todo_list variable
def add_task(task):
    todo_list.append([task, False])
    print()

def view_tasks():
    if len(todo_list) == 0:
        print("\nNo tasks!\n")
    else:
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

def validate_task_number(number, function):
    try:
        function(number)
    except IndexError:
            print("\nTask value doesn't exist, please try again!\n")
    except ValueError:
            print("\nInvalid input, please try again!\n")
    except Exception:
        print("\nSorry, something went wrong. Please try again!\n")
    else:
        print("Operation successful!\n")

while user_inp != "5":
    match user_inp:
        case '1':
            new_task = input("\nPlease provide the name of the task you would like to add: ")
            add_task(new_task)

        case '2':
            view_tasks()

        case '3':
            view_tasks()
            try:
                task_number = int(input("Please provide the task number you would like to mark as complete or incomplete: "))
                mark_complete(task_number)
            except IndexError:
                print("\nTask value doesn't exist, please try again!\n")
            except ValueError:
                print("\nInvalid input, please try again!\n")
            except Exception:
                print("\nSorry, something went wrong. Please try again!\n")
            else:
                print("Operation successful!\n")

        case '4':
            view_tasks()
            try:
                task_number = int(input("Please provide the task number you would like to delete: "))
                delete_task(task_number)
            except IndexError:
                print("\nTask value doesn't exist, please try again!\n")
            except ValueError:
                print("\nInvalid input, please try again!\n")
            except Exception:
                print("\nSorry, something went wrong. Please try again!\n")
            else:
                print("Operation successful!\n")

        case _:
            print("Sorry, I was unable to process your input! Please try again.")

    user_inp = input("Welcome to the To-Do List App!\n\nMenu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete or incomplete\n4. Delete a task\n5. Quit\n\n")
