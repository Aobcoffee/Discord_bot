import requests
import json
import os

def handle_response(message) -> str:
    p_message = message.lower() 
	
    api_key = os.getenv("OPENAI_TOKEN")

    headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}

    data = {"model": "YOUR_MODEL","messages": [{"role": "system", "content": "YOUR_DESIRED_SYSTEM_ROLE"}],"max_tokens": 150,}
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
    return response.json()["choices"][0]["message"]["content"]