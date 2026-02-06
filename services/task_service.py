from storage.file_manager import load_task, save_task
from util import generate_id
import auth.auth_decorator as auth
from util import print_table

def get_user_task():
    tasks = load_task()
    return tasks.get(auth.CURRENT_USER,[])

def save_user_task(user_task):
    tasks = load_task()

    tasks[auth.CURRENT_USER] = user_task
    save_task(tasks)
    
    
def add_task():
    tasks = get_user_task()

    id = generate_id(tasks)
    title = input("Enter title : ")
    description = input("Enter description : ")

    task = {
        "id": id,
        "title": title,
        "description": description,
        "status": "pending"
    }

    tasks.append(task)
    save_user_task(tasks)
    print("Task add successfully")


def view_task():
    print_table(get_user_task())

def view_task_status(status):
    tasks = get_user_task()
    task = [t for t in tasks if t["status"] == status]
    print_table(task)

def update_task():
    tasks = get_user_task()

    task_id = int(input("Enter task ID : "))
    for t in tasks:
        if t["id"] == task_id:
            print("updating task....")
            print("1. update title")
            print("2. update description")

            choice = int(input("Enter your choice : "))

            match choice:
                case 1:
                    title = input("Enter Title : ")
                    t["title"] = title
                case 2:
                    description = input("Enter description : ")
                    t["description"] = description
                case _:
                    print("invalid choice")
            save_user_task(tasks)
            print("task update successfully")
            return
        else:
            print("Task not found")
    

def mark_task_complete():
    tasks = get_user_task()

    task_id = int(input("Enter task ID : "))
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "complete"
            save_user_task(tasks)
            print("task marked successfully")
            return
        else:
            print("Task not found")

def delete_task():
    tasks = get_user_task()

    task_id = int(input("Enter task ID : "))

    task = [t for t in tasks if t["id"] != task_id]
    save_user_task(task)
    print("task deleted successfully")
