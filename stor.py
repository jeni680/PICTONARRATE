
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the tokenizer and model
#tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
#model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neox-20b")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")

# Prepare input text
input_text = "A boy is playing in a park. The sun is setting. A dog is running towards him."
inputs = tokenizer(input_text, return_tensors="pt")

# Generate text
outputs = model.generate(**inputs, max_length=100, num_return_sequences=1)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)