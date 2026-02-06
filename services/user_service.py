
from storage.file_manager import load_users,save_users
from user import User
import auth.auth_decorator as auth


def register():
    users = load_users()

    username: str = input("Enter your name : ").strip()
    password: str = input("Enter your password : ").strip()
    if username.lower() in str(users[username]).lower() and users[username]["password"] == password:
        print("user already exists")
        return
    
    user = User(username, password)
    users[username] = user.to_dict()
    save_users(users)
    print(f"{user.username} have registered successfully")

def login():
    users = load_users()

    username: str = input("Enter your name : ").strip().lower()
    password: str = input("Enter your password : ").strip().lower()

    if username.lower() in str(users[username]).lower() and users[username]["password"] == password:
        auth.CURRENT_USER = username
        print("login successfully")
    else:
        print("User not found")

def logout():
    auth.CURRENT_USER = None
    print("user logout successfully")
