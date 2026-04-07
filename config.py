import os 
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL","https://opensource-demo.orangehrmlive.com/")
username = os.getenv("Username")
password = os.getenv("Password")