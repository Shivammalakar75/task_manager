
import json
import os

USER_FILE = 'user.json'
TASK_FILE = 'task.json'

def load_data(file):
    if not os.path.exists(file):
        return {}

    with open(file, "r") as f:
        data = json.load(f)
    return data

def save_data(file,data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
    
def load_users():
    return load_data(USER_FILE)

def save_users(user):
    save_data(USER_FILE,user)

def load_task():
    return load_data(TASK_FILE)

def save_task(task):
    save_data(TASK_FILE,task)