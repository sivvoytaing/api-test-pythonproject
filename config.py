# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    BASE_URL = 'https://api.thedogapi.com/v1'
    API_KEY = os.getenv('DOG_API_KEY')
    
    @staticmethod
    def get_headers():
        return {
            'Content-Type': 'application/json',
            'x-api-key': Config.API_KEY
        }
