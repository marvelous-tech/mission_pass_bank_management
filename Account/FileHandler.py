import json
import config
def write_file(user):
    with open(config.ACCOUNT_FILE_PATH, 'w') as f:
        json.dump(user, f, indent=4)

def read_file():
    with open(config.ACCOUNT_FILE_PATH,'r') as f:
        data = json.load(f)
    return data