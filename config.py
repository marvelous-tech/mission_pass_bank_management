from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ACCOUNT_FILE_PATH = BASE_DIR / "Account/AccountDetails.json"
print(ACCOUNT_FILE_PATH)