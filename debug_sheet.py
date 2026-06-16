from dotenv import load_dotenv
import os

load_dotenv()

print("Spreadsheet ID:", os.getenv("SPREADSHEET_ID"))