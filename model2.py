# GitHub: ai_engine.py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

class LLMEngine:
    def __init__(self, model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"):
        self.model_id = model_id
        # 4-bit quantization for free usage on limited hardware
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4"
        )
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id, 
            quantization_config=bnb_config,
            device_map="auto"
        )

    def ask(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**inputs, max_new_tokens=1024, temperature=0.6)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
