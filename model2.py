# ai.py (GitHub par host karne ke liye - KEYLESS VERSION)
import json
import urllib.request
import urllib.error

# Free, no-key endpoint for Pollinations
POLLINATIONS_URL = "https://text.pollinations.ai/openai/v1/chat/completions"

def ask(prompt, model="openai"):
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2, # Low temp rakha hai taaki code accurate aaye
        "stream": False
    }

    req = urllib.request.Request(
        POLLINATIONS_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "JupyterNotebook-FreeClient"
        }
    )

    try:
        # Free models ke liye 60 seconds ka timeout kaafi hai
        with urllib.request.urlopen(req, timeout=60) as res:
            raw = res.read().decode("utf-8")
            response_data = json.loads(raw)
            
            if "choices" in response_data and len(response_data["choices"]) > 0:
                return f"\n=== [Model: {model}] ===\n" + response_data["choices"][0]["message"]["content"]
            return "Error: Unexpected response format."

    except urllib.error.HTTPError as e:
        return f"HTTP Error {e.code}: {e.reason} - Sayad model ka naam galat hai ya limit cross ho gayi."
    except Exception as e:
        return f"Connection Error: {str(e)}"
