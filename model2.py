# ai.py

import json
import urllib.request

POLLINATIONS_URL = "https://pollinations.ai/openai/v1/chat/completions"


def _call_model(prompt, model):
    data = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are an expert programmer. Think step by step and give correct, optimized code."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    req = urllib.request.Request(
        POLLINATIONS_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=20) as res:
            response_data = json.loads(res.read().decode("utf-8"))
            return response_data["choices"][0]["message"]["content"]
    except:
        return None


def ask(prompt, model="llama"):
    """
    prompt: your question
    model: 'llama', 'mistral', 'openai', 'mixtral'
    """

    # models priority list (user choice first)
    models_to_try = [model]

    # add smart fallbacks
    fallback_models = ["llama", "mixtral", "mistral", "openai"]

    for m in fallback_models:
        if m not in models_to_try:
            models_to_try.append(m)

    # try all models
    for m in models_to_try:
        result = _call_model(prompt, m)
        if result:
            return f"[model: {m}]\n{result}"

    return "Error: All models failed."


# quick shortcuts
def ask_llama(prompt):
    return ask(prompt, "llama")

def ask_fast(prompt):
    return ask(prompt, "mistral")
