# GitHub: model.py
import requests
import uuid
import json

def ask_gemini(prompt):
    # 2026-Verified Public Space for DeepSeek-R1 (Distilled 32B)
    # Ye Space Reasoning aur Coding dono ke liye best hai
    url = "https://m-a-p-deepseek-r1-distill-qwen-32b.hf.space/gradio_api/call/predict"
    
    # Gradio requires a unique session hash
    session_hash = str(uuid.uuid4())[:11]
    
    # Payload as per 2026 Gradio API standards
    payload = {
        "data": [prompt, [], ""], # [message, history, system_prompt]
        "event_data": None,
        "fn_index": 0,
        "session_hash": session_hash
    }

    try:
        # Step 1: Request the prediction
        r = requests.post(url, json=payload, timeout=30)
        if r.status_code != 200:
            return f"Error {r.status_code}: Bhai, server busy hai."
            
        event_id = r.json().get("event_id")
        
        # Step 2: Get the result (polling the event)
        # 2026 Update: Public spaces now use 'eventdata' stream
        result_url = f"https://m-a-p-deepseek-r1-distill-qwen-32b.hf.space/gradio_api/call/predict/{event_id}"
        
        while True:
            res = requests.get(result_url, stream=True, timeout=30)
            for line in res.iter_lines():
                if line:
                    line_text = line.decode('utf-8')
                    if "data:" in line_text:
                        data = json.loads(line_text.replace("data: ", ""))
                        # Returns the actual model response
                        if isinstance(data, list) and len(data) > 0:
                            return data[0]
            break

    except Exception as e:
        return f"Bhai, connection error: {str(e)}"

# Alias to match your prompt
def ask_ai(prompt):
    return ask_gemini(prompt)
