import os           
from dotenv import load_dotenv
from tasks import add_task, show_tasks, save_tasks

name = input("What is your name: ")

print(f"Welcome, {name}")

tasks = []
load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? yes/no: ")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin! hi")
    else:
        print("wrong password")
while True:
    task = input("Enter a task (or type done to finish): ")

    if task == "done":
        break

    add_task(tasks, task)

save_tasks(tasks)
show_tasks(tasks)