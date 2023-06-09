import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def read_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        return file.read()
    
def summary(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()

file = 'article.txt'
text = read_file(file)
print(summary(text))


