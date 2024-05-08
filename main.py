import cohere
co = cohere.Client('<apiKey>')
marking_signature = "&& glossy-forma &&"

SYSTEM_SETUP = f"""You are an AI trained to help create OSL shaders.
PLATFORM: Blender
FORMATTING: Whenever providing shader code, you MUST start and end it with '{marking_signature}'.
"""

chat_log = [{
    "role": "SYSTEM", 
    "message": SYSTEM_SETUP
}]
while True:
    # Take in multiple lines of user input, end with Ctrl+D on Unix on an EMPTY LINE.
    user_message = ""
    print("USER: ", end='')
    while True:
        try:
            line = input()
        except EOFError:
            break
        user_message += line + "\n"
    
    chat_response = ''
    print("GLOSSY AI: ", end='')

    for event in co.chat_stream(
        model="command-r",
        chat_history=chat_log,
        message=user_message
    ):
        if event.event_type == "text-generation":
            chat_response += event.text
            print(event.text, end='')
    print("")
    chat_log.append({"role": "USER", "message": user_message})
    chat_log.append({"role": "CHATBOT", "message": chat_response})
    
    segmented_answer = chat_response.split(marking_signature)
    if len(segmented_answer) > 1:
        code = segmented_answer[1]
        filename = "shader.osl"
        
        # Writing to file
        with open(filename, 'w') as file:
            file.write(code)