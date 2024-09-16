from dotenv import load_dotenv
import os 
from huggingface_hub import login
from transformers import pipeline

load_dotenv()

hf_key = os.getenv("HF_KEY")

login(hf_key)

generator = pipeline("text-generation", model="google/gemma-2-2b-it")

def generate_response(prompt,  max_new_tokens=4096):
    result = generator(
        prompt,
        max_new_tokens=max_new_tokens,
        num_return_sequences=1, 
    )
    return result[0]['generated_text']
