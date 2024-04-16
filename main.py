import cohere
co = cohere.Client('<apiKey>')

chat_log = [{
    "role": "SYSTEM", 
    "message": "You are an AI trained to help create OSL shaders for Blender. Whenever providing shader code, start and end it with '==='"
}]
while True:
    user_message = input()
    chat_response = ''

    for event in co.chat_stream(
        chat_history=chat_log,
        message=user_message
        
        # perform web search before answering the question. You can also use your own custom connector.
        # connectors=[{"id": "web-search"}],
    ):
        if event.event_type == "text-generation":
            chat_response += event.text
            print(event.text, end='')
        elif event.event_type == "stream-end":
            print(f"\nevent.finish_reason")

    chat_log.append({"role": "USER", "message": user_message})
    chat_log.append({"role": "CHATBOT", "message": chat_response})