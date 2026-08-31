from datetime import datetime
"""
# display current date in the format dd/mm/yy
current_date = datetime.now()
print(current_date.strftime('%d %B %Y'))

# display current time
current_time = datetime.now()
print(current_time.strftime('%X'))
"""

# allow user to create a task
task_name = input("What is the name of your task?: ")
print(f"I am now setting up {task_name}")

# get user to confirm a date for deadline of task
valid_date = True
while valid_date == True:
    task_due = input("When is your task due? Please enter the due date in the form of dd/mm/yyyy: ")
    try:
        task_due = datetime.strptime(task_due, '%d/%m/%Y')
        valid_date = False
    except:
        print("Wrong input, please try again.")

print(f"{task_name} is due on {task_due.strftime('%d/%m/%Y')}")

"""
# allow user to update the deadline date
valid_date = True
while valid_date == True:
    update_deadline = input(
        f"What is the new deadline for {task_name}? Please enter the date in the format of dd/mm/yyyy: ")
    try:
        update_deadline = datetime.strptime(update_deadline, '%d/%m/%Y')
        valid_date = False
    except:
        print("Wrong input, please try again.")

print(f"The deadline for {task_name} has been updated and is now due on {update_deadline.strftime('%d/%m/%Y')}")
"""

# order tasks by their deadline

# user should be able to add task name and deadline to a list
task_list = [
    {"task": "assignment 1", "deadline": "01/12/2026"}
]

task_list.append({"task": task_name, "deadline": task_due.strftime('%d/%m/%Y')})

print(task_list)

# order tasks by deadline

