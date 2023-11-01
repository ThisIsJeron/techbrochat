import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Set your API key here (preferably as an environment variable for security reasons)
API_KEY = os.getenv('API_KEY')

def get_response_from_gpt(prompt_text):
    openai.api_key = API_KEY
    
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a listener of a lifestyle podcast from two San Francisco bros that are software engineers"},
        {"role": "user", "content": prompt_text}
    ]
    )
    print(response)
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    question = "What are 5 topics you want to hear from the podcast today?"
    answer = get_response_from_gpt(question)
    print(answer)

