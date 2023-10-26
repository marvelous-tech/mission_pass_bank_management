import os
import config


def check_file():
    file_path = config.USER_FILE_PATH

    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                file.write('')
            print('File Created Successfully')
        except OSError as e:
            print(f'File creation failed')
    else:
        print('File already exits!')


check_file()
file_name = config.USER_FILE_PATH
print(os.path.abspath(file_name))
