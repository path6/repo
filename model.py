import urllib.request
import json

def ask_gemini(prompt):
    # 2026 Latest Free API: Pollinations.ai
    # (No API Key Required, Unlimited, Officially Free)
    url = "https://text.pollinations.ai/"
    
    # 500 लाइन्स के प्रॉम्प्ट के लिए POST Payload
    payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "model": "openai" # यह बाय डिफॉल्ट सबसे समझदार मॉडल चुनेगा
    }
    
    data = json.dumps(payload).encode('utf-8')
    
    # Headers ताकि API को लगे कि यह एक सही रिक्वेस्ट है
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Jupyter-AI-Client/1.0"
    }
    
    req = urllib.request.Request(url, data=data, headers=headers)
    
    try:
        # सीधा कॉल - नो वेटिंग, नो हैंडशेक!
        with urllib.request.urlopen(req) as response:
            # Pollinations सीधा टेक्स्ट रिस्पॉन्स देता है, कोई JSON डिकोडिंग का झंझट नहीं
            result = response.read().decode('utf-8')
            return result
    except Exception as e:
        # अगर Pollinations डाउन हो, तो एक और Free Backup (MLVoca - DeepSeek R1)
        print("Pollinations API slow, switching to Backup (DeepSeek)...")
        backup_url = "https://mlvoca.com/api/generate"
        backup_payload = {"model": "deepseek-r1:1.5b", "prompt": prompt, "stream": False}
        backup_req = urllib.request.Request(backup_url, data=json.dumps(backup_payload).encode('utf-8'), headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(backup_req) as b_res:
                return json.loads(b_res.read().decode('utf-8'))['response']
        except Exception as backup_e:
            return f"❌ All Free APIs are currently busy: {str(backup_e)}"

print("✅ NEW 2026 AI Loaded! (Powered by Pollinations - No API Key Needed)")
