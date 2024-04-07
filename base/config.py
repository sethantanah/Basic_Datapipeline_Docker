import os
from dotenv import load_dotenv, find_dotenv

# Load env file
load_dotenv(find_dotenv())


DB_HOST=os.environ.get('DB_HOST')
DB_USER=os.environ.get('DB_USER')
DB_PASSWORD=os.environ.get('DB_PASSWORD')
