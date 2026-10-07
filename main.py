from tasks import add_task, show_tasks, save_tasks

name = input("What is your name: ")

print(f"Welcome, {name}")

tasks = []

while True:
    task = input("Enter a task (or type done to finish): ")

    if task == "done":
        break

    add_task(tasks, task)

save_tasks(tasks)
show_tasks(tasks)