# GitHub: model.py
import requests

def ask_gemini(prompt):
    url = "https://api.blackbox.ai/api/chat"
    
    # 2026 April Update: Mandatory Headers to bypass bot-check
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Origin": "https://www.blackbox.ai",
        "Referer": "https://www.blackbox.ai/"
    }

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "deepseek-r1", # 2026's Best Reasoning Model
        "max_tokens": 1024
    }

    try:
        # Stream=False is better for simple scripts
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        if r.status_code == 200:
            return r.text.strip()
        else:
            return f"Error {r.status_code}: Bhai, endpoint change ho gaya shayad."
    except Exception as e:
        return f"Bhai, network issue hai: {str(e)}"
