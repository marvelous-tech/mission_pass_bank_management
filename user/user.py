import util
import hashlib
import json
import config
import uuid
util.check_file()


class User:
    def __init__(self, name, email, phone, password):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha3_256(password.encode()).hexdigest()

    def signup(self):
        with open(config.USER_FILE_PATH, 'r') as file:
            users = json.load(file)
            for user in users:
                if user['Email'] == self.email:
                    return 'User exists'
            users.append({
                'User_ID': self.user_id,
                'Name': self.name,
                'Email': self.email,
                'Phone': self.phone,
                'Password': self.password
            })

            with open(config.USER_FILE_PATH, 'w') as file:
                json.dump(users, file, indent=4)

        print("User registration successful")

    def login(self, email, password):
        with open(config.USER_FILE_PATH, 'r') as file:
            data = json.load(file)
            if email in data:
                user_data = data[email]
                if user_data['Password'] == self._hash_password(password):
                    print("Login successful")
                    return
        print("Login failed")


if __name__ == '__main__':
    print('Please Provide: ')
    name = str(input('Name: '))
    email = str(input('Email: '))
    phone = str(input('Phone: '))
    password = str(input('Password: '))

    user = User(name, email, phone, password)
    user.signup()
