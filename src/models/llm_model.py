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
        prompt,          # Limit the total output length
        max_new_tokens=max_new_tokens,    # Limit the number of new tokens generated
        num_return_sequences=1,              # Ensure that the input is truncated if it exceeds the token limit
    )
    return result[0]['generated_text']