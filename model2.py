# ai.py (FIXED)

import json
import urllib.request

POLLINATIONS_URL = "https://pollinations.ai/openai/v1/chat/completions"


def _call_model(prompt, model):
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    req = urllib.request.Request(
        POLLINATIONS_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as res:
            raw = res.read().decode("utf-8")
            
            # DEBUG print (optional)
            # print(raw)

            response_data = json.loads(raw)

            # safer parsing
            if "choices" in response_data:
                return response_data["choices"][0]["message"]["content"]

            return str(response_data)

    except Exception as e:
        return f"ERROR: {str(e)}"


def ask(prompt, model="llama"):
    models = [model, "llama", "mistral", "openai"]

    for m in models:
        result = _call_model(prompt, m)

        if result and not result.startswith("ERROR"):
            return f"[model: {m}]\n{result}"

    return "Error: All models failed."
