from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


def generate_story_from_captions(captions, max_length=300, temperature=0.7, top_k=50, top_p=0.9, repetition_penalty=1.5, num_return_sequences=1):
    
    # Load the tokenizer and model
    model_path = 'B:/projec/model'
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    model = GPT2LMHeadModel.from_pretrained(model_path)


# Set the model to evaluation mode
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model.eval().to(device)
    
    # Concatenate captions with separators
    prompt = " ".join(captions)
    print(prompt)
    prompt = captions
    
    # Encode the prompt and create attention mask
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)  # Explicit attention mask

    # Generate story
    output_sequences = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        num_return_sequences=num_return_sequences
    )
    stories =[]
    # Decode and print the generated sequences
    for generated_sequence_idx, generated_sequence in enumerate(output_sequences):
        print(f"=== GENERATED SEQUENCE {generated_sequence_idx + 1} ===")
        generated_sequence = generated_sequence.tolist()
        text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)
        text = text[:text.find(tokenizer.eos_token)]  # Remove any EOS token from the output
        print(text)
        stories.append(text)
    return(stories)
# # Example usage
# captions = [
#     "A man driving a car.",
#     "A woman about to cross the road.",
#     "The car hit the woman.",
#     "The police reached the accident site.",
#     "The driver is dead."
# ]

# generate_story_from_captions(captions)
