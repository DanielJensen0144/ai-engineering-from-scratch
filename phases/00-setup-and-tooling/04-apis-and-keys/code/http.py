import json
import os
import urllib.request

from dotenv import load_dotenv

load_dotenv()

url = "https://api.anthropic.com/v1/messages"

headers = {
    "Content-Type": "applicatino/json",
    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
    "anthropic-version": "2023-06-01"
}

model = os.environ.get("LLM_MODEL", "claude-sonnet-5")
print(f"Using: {model}")

body = json.dumps({
    "model": model,
    "max_tokens": 256,
    "messages": [
        {
            "role": "user",
            "content": "Hi Claude."
        }
    ]
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
with urllib.request.urlopen(req) as response:
    result = json.loads(response.read())
    print(result["content"][0]["tent"])