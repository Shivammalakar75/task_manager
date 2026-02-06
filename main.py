

from services.user_service import register, login, logout
from services.task_service import add_task, view_task, view_task_status, update_task, mark_task_complete,delete_task
import auth.auth_decorator as auth

def task_menu():
    
    while auth.CURRENT_USER:
        print("=" * 75)
        print(f"{f'Welcome {auth.CURRENT_USER}':^75}")
        print("=" * 75)

        print("1. ADD NEW TASK")
        print("2. VIEW ALL TASK")
        print("3. VIEW PENDING TASK")
        print("4. VIEW COMPLETED TASK")
        print("5. UPDATE TASK")
        print("6. TASK MARK AS COMPLETE")
        print("7. DELETE TASK")
        print("8. LOGOUT")

        choice: int = int(input("Enter your choice : "))

        match choice:
            case 1:
                add_task()
            case 2:
                view_task()
            case 3:
                view_task_status("pending")
            case 4:
                view_task_status("complete")
            case 5:
                update_task()
            case 6:
                mark_task_complete()
            case 7:
                delete_task()
            case 8:
                logout()
            case _:
                print("invalid choice : please enter correct choice!")


def menu():
    while True:
        print("=" * 50)
        print("TASK MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice: int = int(input("Enter your choice : "))

        match choice:
            case 1:
                register()
            case 2:
                login()
                task_menu()
            case 3:
                print("Exit...")
                break
            case _:
                print("invalid choice : please enter correct choice!")
    


if __name__ == "__main__":
    menu()