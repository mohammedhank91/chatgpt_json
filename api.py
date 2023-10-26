import openai
import requests  
openai.api_key = "Empty if you don't use embeddings, otherwise your hugginface token"
openai.api_base = "https://animated-pancake-gwjg5p5rq9r29g56-1337.app.github.dev/v1"
import json , csv , pandas as pd

def main():
    text = "text.json"
    # read the text from the file
    with open(text, 'r',encoding='utf-8') as f:
        text = f.read()

    # Include the text in the ChatGPT API request
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"I want you to act as a proofreader. I will provide you a CV format text, and I would like you to review it. Once you have finished reviewing the text, provide me a JSON file. Now, begin with the first text:'{text}'",
            },
           ],
        stream=True,
    )



    if isinstance(chat_completion, dict):
        # not stream
        print(chat_completion.choices[0].message.content)
    else:
        # stream
        content_list = []
        for token in chat_completion:
            content = token["choices"][0]["delta"].get("content")
            if content != None:
                content_list.append(content)
                print(content, end="", flush=True)
        
    
if __name__ == "__main__":
    main()



# extractedText = "Your extracted text goes here" # Replace with the actual extracted text
# document.getElementById("message-input").value = extractedText
# $("#message-input").val(extractedText);