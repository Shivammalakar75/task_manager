
from storage.file_manager import load_users,save_users
from user import User
import auth.auth_decorator as auth


def register():
    users = load_users()

    username: str = input("Enter your name : ")
    if username in users:
        print("user already exists")
        return
    
    password: str = input("Enter your password : ")
    user = User(username, password)
    users[username] = user.to_dict()
    save_users(users)
    print(f"{user.username} have registered successfully")

def login():
    users = load_users()

    username: str = input("Enter your name : ")
    password: str = input("Enter your password : ")

    if username in users and users[username]["password"] == password:
        auth.CURRENT_USER = username
        print("login successfully")
    else:
        print("User not found")

def logout():
    auth.CURRENT_USER = None
    print("user logout successfully")
