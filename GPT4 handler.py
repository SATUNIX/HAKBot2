import json
import openai
import os

#Write a funciton where if there is no content in the json file, use a default. 

# Function to return content from JSON file
def getContent():
    try:
        with open("content.json", "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        content = {"This is a default message."}
    return content

# Get content from JSON file
contentCache = getContent()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat(content):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )
   
    return chat_completion.choices[0].message.content

def main ():
    getContent()
    chat()
if __name__ == "__main__":
    main()
