from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "mistralai/Mistral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16).to("cuda")

# Prepare input text
input_text = "two kids reading under the tree.a boy and a girl reading a book.a family at the park."
inputs = tokenizer(input_text, return_tensors="pt")

# Generate text
outputs = model.generate(**inputs, max_length=100, num_return_sequences=1)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)