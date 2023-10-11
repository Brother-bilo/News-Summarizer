from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")

print('Hey')

# Prepare the prompt
prompt = "What is the meaning of life?"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate response
outputs = model.generate(**inputs)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print response
print(response)
