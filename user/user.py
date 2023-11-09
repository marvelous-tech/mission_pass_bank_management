import util
import hashlib
import json
import config
import uuid
util.check_file()


class User:
    def _hash_password(self, password):
        return hashlib.sha3_256(password.encode()).hexdigest()

    def signup(self, name, email, phone, password):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self.password = self._hash_password(password)

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
        return self


    def login(self, email, password):
        hashed_password = self._hash_password(password)

        with open(config.USER_FILE_PATH, 'r') as file:
            users = json.load(file)
            for user in users:
                if user['Email'] == email and user['Password'] == hashed_password:
                    print("Login successful")
                    return user
            print("Invalid email or password")


# if __name__ == '__main__':
#     print('Please Provide: ')
#     name = str(input('Name: '))
#     email = str(input('Email: '))
#     phone = str(input('Phone: '))
#     password = str(input('Password: '))
#
#     user = User()
#     # user.login(email, password)
#     user.signup(name, email, phone, password)