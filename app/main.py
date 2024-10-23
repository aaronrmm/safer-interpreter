import requests

ollama_url = 'http://host.docker.internal:11434/api/chat'

payload = {
    "model": "nemotron-mini",
    "messages": [
        {"role": "user", "content": "Say hi!"}
    ],
    "stream": False,
}

try:
    response = requests.post(ollama_url, json=payload)
    response.raise_for_status()
    result = response.json()
    print(f"Ollama response: {result['message']['content']}")
except requests.exceptions.RequestException as e:
    print(f"Failed to make request: {e}")
