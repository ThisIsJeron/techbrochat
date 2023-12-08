import openai
import os

# Set your API key here (preferably as an environment variable for security reasons)
API_KEY = os.getenv('API_KEY')

def get_response_from_gpt(prompt_text):
    openai.api_key = API_KEY
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": "You are a listener of a lifestyle podcast from two San Francisco bros"},
        {"role": "user", "content": prompt_text}
        ]
    )
    
    print(response)
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    boilerplate1 = "these are topics we have discussed in the past: "
    boilerplate2 = "not repeating any of the previous topics, what are 3 topics you want to hear from the podcast today?"
    
    #open usedTopics.txt, read the topics, and store them in a list
    usedTopics = []
    with open('usedTopics.txt', 'r') as f:
        usedTopics = f.read().splitlines()


    prompt = boilerplate1 + ', '.join(usedTopics) + "\n" + boilerplate2


    print(prompt)
    answer = get_response_from_gpt(prompt)
    print(answer)

