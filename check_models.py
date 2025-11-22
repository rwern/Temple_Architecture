
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure API key (try to get from env or use a placeholder if running in a context where it's already set in the app but not env)
# In this environment, I might need to rely on the user having set it in the app, but for a script I need it in env.
# I'll check if I can see it in the previous file view... 
# The previous file view showed: os.environ["GOOGLE_API_KEY"] = api_key inside the app.
# I don't have the API key directly. 
# However, the user has been running the app.
# I'll try to list models. If it fails due to no API key, I'll ask the user or just assume standard models.
# Actually, I can't easily get the key if it's not in .env. 
# Let's try to see if there is a .env file.
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error listing models: {e}")
