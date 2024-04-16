import cohere
co = cohere.Client('<apiKey>')
marking_signature = "&& glossy-forma &&"

chat_log = [{
    "role": "SYSTEM", 
    "message": f"You are an AI trained to help create OSL shaders for Blender. Whenever providing shader code, start and end it with '{marking_signature}'"
}]
while True:
    user_message = input()
    chat_response = ''

    for event in co.chat_stream(
        chat_history=chat_log,
        message=user_message
    ):
        if event.event_type == "text-generation":
            chat_response += event.text
            print(event.text, end='')
        # elif event.event_type == "stream-end":
            # print(f"\nevent.finish_reason\n")

    chat_log.append({"role": "USER", "message": user_message})
    chat_log.append({"role": "CHATBOT", "message": chat_response})
    
    segmented_answer = chat_response.split(marking_signature)
    if len(segmented_answer) > 1:
        code = segmented_answer[1]
        filename = "shader.osl"
        
        # Writing to file
        with open(filename, 'w') as file:
            file.write(code)