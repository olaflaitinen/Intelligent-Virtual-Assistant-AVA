from transformers import pipeline

def generate_response(input_text):
    generator = pipeline('text-generation', model='distilgpt2')
    response = generator(input_text, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

if __name__ == "__main__":
    input_text = "Hello, how are you?"
    response = generate_response(input_text)
    print(response)
