import openai
import requests  
openai.api_key = "Empty if you don't use embeddings, otherwise your hugginface token"
openai.api_base = "https://supreme-space-waffle-r9w6x7j7pxhxwqr-1337.app.github.dev/v1"
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
        print()
        print("".join(content_list))
        
    num_cvs = 10  # Change this to the desired number of CVs

    # Create a loop to generate and save the CVs
    for i in range(1, num_cvs + 1):
        # Construct the filename using string formatting
        filename = f'cv{i}.json'

        # Replace this with the content you want to save in each CV
        content_list = ["This is CV number", str(i)]

        # Save the text to the JSON file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("".join(content_list))
        
    # Load data from the JSON file
    with open(f'cv{i}.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        

    # Open a CSV file for writing
    with open('cv1.csv', 'w', newline='', encoding='utf-8') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write the header row if needed (replace fieldnames with your own)
        fieldnames = ['name', 'adresse', 'age']  # Replace with your actual field names
        csv_writer.writerow(fieldnames)

        # Write the data to the CSV file
        for item in data:
            # Replace fieldnames with the corresponding keys from your JSON data
            row = [item['field1'], item['field2'], item['field3']]  # Replace with your actual keys
            csv_writer.writerow(row)
    
if __name__ == "__main__":
    main()
