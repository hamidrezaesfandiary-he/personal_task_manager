from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv
import os


load_dotenv()
name = input("enter your name:")

admin_mode = input("do you want to open admin mode? (yes/no): ")
if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("ADMIN_PASSWORD"):
        print("admin mode activated")
    else:
        print("wrong password")

print("WElcome back " , name)
tasks = load_tasks()
count = int(input("how many tasks do you want to add? :"))
for i in range(count):
    task_name = input("enter a task :")
    priority = input("enter priority(low, medium, high): ").lower()
    task = {
        "name": task_name, 
        "priority": priority
    }
    tasks.append(task)


show_tasks(tasks)
save_tasks(tasks)