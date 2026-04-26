# GitHub: model.py
import requests
import json

def ask_gemini(prompt):
    # 2026 Updated Endpoint
    url = "https://www.blackbox.ai/api/chat"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Origin": "https://www.blackbox.ai",
        "Referer": "https://www.blackbox.ai/"
    }

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "deepseek-r1", # 2026 logic model
        "max_tokens": 1024,
        "codeModelMode": True,  # Coding ke liye isse output better aata hai
        "agentMode": {},
        "trendingAgentMode": {},
        "isFinalRefresh": True
    }

    try:
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        
        if r.status_code == 200:
            # 2026 mein Blackbox kabhi kabhi extra text bhejta hai, hum saaf karenge
            response_text = r.text
            # Agar output mein markdown blocks hain toh unhe clean karne ka logic yahan daal sakte ho
            return response_text.strip()
        else:
            return f"Error {r.status_code}: Bhai, API ne dhokha de diya. Naya rasta dhoondna padega."
            
    except Exception as e:
        return f"Bhai, connection error: {str(e)}"
