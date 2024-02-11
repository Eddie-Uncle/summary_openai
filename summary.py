import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file} not found.")
        return None

def summary(text):
    if text is None:
        return "No text provided for summarization."

    response = client.completions.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None
    )

    return response['choices'][0]['text'].strip()

def main():
    file = 'article.txt'
    text = read_file(file)
    print(summary(text))
    

if __name__ == "__main__":
    main()