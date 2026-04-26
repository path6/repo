# GitHub: ai_engine.py
from gradio_client import Client

class AI:
    def __init__(self, mode="reasoning"):
        # Hum public spaces use kar rahe hain jo hosted hain
        if mode == "reasoning":
            # DeepSeek-R1 hosted space
            self.client = Client("deepseek-ai/DeepSeek-R1")
        else:
            # Qwen-Coder hosted space
            self.client = Client("Qwen/Qwen2.5-Coder-32B-Instruct")

    def ask(self, prompt):
        # API key ki zaroorat nahi hai yahan
        result = self.client.predict(
            message=prompt,
            api_name="/chat"
        )
        return result
