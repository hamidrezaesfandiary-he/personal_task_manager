def add_task(tasks, task):
    tasks.append(task)


def show_tasks(tasks):
    print("Your tasks:")

    for task in tasks:
        print(task)


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(" - " + task)