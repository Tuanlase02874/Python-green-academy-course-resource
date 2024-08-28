from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Define the instruction for translating text to Spanish
instruction = (
    "Translate the following text to Spanish. Provide only the translated text, "
    "without any additional comments or the original text.\n\n"
    "Text: \"Good morning!\"\n\n"
    "Output:"
)

# Create a completion request using ChatGPT
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": instruction}
    ]
)

# Extract and print the translated text from the response
print("completion:", completion)
translated_text = completion.choices[0].message.content
print("Translated Text to Spanish:", translated_text)
