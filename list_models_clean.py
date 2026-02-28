import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

try:
    response = requests.get(url)
    data = response.json()
    for m in data.get('models', []):
        print(m['name'])
except Exception as e:
    print(f"Error: {e}")
