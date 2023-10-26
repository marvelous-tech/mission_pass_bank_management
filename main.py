import json
import uuid
from accounts.accounts import Account
from User.user import User


def read_session():
    with open('session.json', 'r') as file:
        session_data = json.load(file)
    return session_data


def save_session(session_data):
    with open('session.json', 'w') as file:
        json.dump(session_data, file, indent=4)


def register():
    name = input("Enter Full Name: ")
    email = input("Enter your Email: ")
    password = input("Enter your Password: ")


def log_in():
    email = input("Enter your email: ")
    password = input("Enter your Password: ")
    user = User.login(email, password)
    if user:
        session_data = read_session()
        current_session = str(uuid.uuid4())
        session_data.append({
            "session_id": current_session,
            "user_id": email
        })
        save_session(session_data)


def create_account():
    type = input("Enter your choice:\n1. FDR Account \n2. Current Account\n3.Savings Account\n: ")
    account= Account.create_account(userid=user_id,account_type=type)


while True:
    choice = input("1. Register \n2. Log In \n:")
    if choice == '1':
        register()
    if choice == '2':
        log_in()
