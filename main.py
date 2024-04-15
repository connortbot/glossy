import cohere
co = cohere.Client('<apiKey>')

for event in co.chat_stream(
    chat_history=[
    {"role": "USER", "message": "Who discovered gravity?"},
    {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
    ],
    message="Can you write a short biography about him?",
    # perform web search before answering the question. You can also use your own custom connector.
    connectors=[{"id": "web-search"}],
):
    if event.event_type == "text-generation":
        print(event.text, end='')
    elif event.event_type == "stream-end":
        print(f"\nevent.finish_reason")