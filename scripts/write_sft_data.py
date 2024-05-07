import json
import os

def convert_to_jsonl(text_file, jsonl_file):
    entries = []
    current_dialogue = {"messages": []}
    current_role = None
    content_text = ''

    def add_message(role, msg):
        current_dialogue["messages"].append(
            {
                "role": role,
                "content": msg.rstrip()
            }
        )

    with open(text_file, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line in ['SYSTEM:', 'USER:', 'CHATBOT:']:
                if current_role is not None:
                    add_message(current_role, content_text)
                    content_text = ''
                if stripped_line == 'SYSTEM:':
                    current_role = 'System'
                elif stripped_line == 'USER:':
                    current_role = 'User'
                elif stripped_line == 'CHATBOT:':
                    current_role = 'Chatbot'
            else:
                content_text += line
    if current_role is not None:
        add_message(current_role, content_text)
        content_text = ''

    entries.append(current_dialogue)
    with open(jsonl_file, 'a') as jfile:
        for entry in entries:
            jfile.write(json.dumps(entry) + "\n")

# Usage
convert_to_jsonl("conversation.txt", "data.jsonl")

def process_txt_files(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a .txt file
        if filename.endswith(".txt"):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            # Call the convert_to_jsonl function on the file
            convert_to_jsonl(file_path, "data.jsonl")

# Replace 'directory_path' with the path to your directory containing the .txt files
directory_path = "."
process_txt_files(directory_path)