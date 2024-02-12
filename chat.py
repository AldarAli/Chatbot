
from langchain import Chain
import openai
import glob

# Provide your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Create a langchain object
lc = Chain()

# Train the model with your text files
for file in glob.glob("*.txt"):
    with open(file, 'r') as f:
        lc.train(f.read())


def chat_with_bot(prompt):
    # Generate a response using langchain
    response = lc.generate_string(prompt)

    # Now improve response by using openai's api
    improved_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=response,
        max_tokens=150
    )

    return improved_response.choices[0].text.strip()

