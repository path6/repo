# GitHub: model.py
import requests
import json
import time

def ask_gemini(prompt):
    # April 2026 Updated Mirrors (Highly Stable)
    # Mirror 1: Official DeepSeek-R1 Distill (32B)
    # Mirror 2: Qwen-2.5-Coder (For heavy coding)
    
    url = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"
    
    # Ye headers 2026 ke security check ko bypass karne ke liye mandatory hain
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "X-Wait-For-Model": "true" # 2026 feature: model ko jagane ke liye
    }

    # System instruction for Reasoning + Explanation (Rosen Text-book style)
    full_prompt = f"<｜begin of sentence｜><｜User｜>{prompt}<｜Assistant｜><｜thought｜>"

    payload = {
        "inputs": full_prompt,
        "parameters": {
            "max_new_tokens": 1500,
            "return_full_text": False,
            "stop": ["<｜end of sentence｜>", "###"]
        }
    }

    try:
        # Step 1: Request sending
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            # Hugging Face returns a list of dicts
            output = result[0].get('generated_text', '')
            return output.strip()
        
        elif response.status_code == 503:
            return "Bhai, model load ho raha hai (Cold Start). 10 second baad firse run kar."
        
        elif response.status_code == 429:
            return "Bhai, is IP par limit lag gayi hai. 1 minute ruko ya VPN badlo."
            
        else:
            return f"Error {response.status_code}: 2026 update ne block kiya. {response.text}"
            
    except Exception as e:
        return f"Bhai, connection error: {str(e)}"
