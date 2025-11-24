import os
import time
import requests
from temple_data import temples
import random

# Create images directory if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

print("Downloading temple images...")

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
]

for name, data in temples.items():
    url = data["image_url"]
    filename = name.lower().replace(" ", "_") + ".jpg"
    filepath = os.path.join("images", filename)
    
    # Skip if already exists
    if os.path.exists(filepath):
        print(f"[SKIP] {name} already exists")
        continue

    try:
        headers = {
            'User-Agent': random.choice(user_agents)
        }
        
        print(f"Downloading {name}...")
        response = requests.get(url, headers=headers, stream=True, timeout=10)
        
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"[OK] Downloaded: {name}")
        else:
            print(f"[FAIL] Failed to download {name}: Status {response.status_code}")
            
        # Wait to avoid rate limiting
        time.sleep(3)
            
    except Exception as e:
        print(f"[ERROR] Error downloading {name}: {str(e)}")

print("\nDownload process completed!")
