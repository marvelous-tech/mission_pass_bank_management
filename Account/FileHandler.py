import json
import config
def write_file(self,ob):
    with open(config.ACCOUNT_FILE_PATH, 'w') as f:
        temp = {'fullname': ob.user['fullname'], 'email': ob.user['email'], 'account_type': ob.type}
        print(temp)
        json.dumps(temp, f, indent=4)

def read_file(self):
    with open(config.ACCOUNT_FILE_PATH,'r') as f:
        data = json.loads(f)
        return data