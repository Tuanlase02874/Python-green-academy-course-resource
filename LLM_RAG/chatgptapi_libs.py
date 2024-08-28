from openai import OpenAI
import os
from dotenv import load_dotenv

def getchatgpt_response(instruction):
    """
    
    
    Parameters:
    - text (str): The text to be translated.
    
    Returns:
    - str: The translated text in Spanish.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the OpenAI API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=api_key)

    try:
        # Create a completion request using ChatGPT
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Adjust model name if necessary
            messages=[
                {"role": "user", "content": instruction}
            ]
        )

        # Extract and return the translated text from the response
        translated_text = completion.choices[0].message.content.strip()
        return translated_text

    except Exception as e:
        print(f"Error during translation: {e}")
        return None

# Example usage
if __name__ == "__main__":
    instruction = "Good morning!"
    translated_text = getchatgpt_response(instruction)

