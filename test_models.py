import urllib.request
import json
import os

env_path = os.path.join(os.path.dirname(__file__), ".env")
api_key = None
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("GOOGLE_API_KEY="):
                api_key = line.split("=", 1)[1].strip()

if not api_key:
    print("No api key found")
    exit(1)

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        for m in data.get("models", []):
            print(m.get("name"), m.get("supportedGenerationMethods", []))
except Exception as e:
    print("Error:", e)
