from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ACCOUNT_FILE_PATH = BASE_DIR / "Account/AccountDetails.json"
USER_FILE_PATH = BASE_DIR / "user/user_data.json"
print(ACCOUNT_FILE_PATH)
print(USER_FILE_PATH)