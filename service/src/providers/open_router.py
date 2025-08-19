from ..somad import Somad
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY",  # Replace with your actual API key
)

def respond(somad: Somad) -> str:
    response = client.chat.completions.create(
        # Example model, choose from OpenRouter's available models
        model="google/gemini-2.5-pro",
        messages=[
            {"role": "user", "content": "Explain the concept of quantum entanglement."},
        ],
    )
    print(response.choices[0].message.content)
