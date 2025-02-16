import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I assist you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?", "I'm great! How can I help?"]
    ],
    [
        r"(.*) your name ?",
        ["I am a chatbot created to assist you. You can call me ChatBot!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer basic questions, and assist with simple tasks. Try asking me something!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day ahead.", "It was nice talking to you. Bye!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase that?", "Interesting... Tell me more!"]
    ]
]


chatbot = Chat(pairs, reflections)

def chatbot_conversation():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chatbot_conversation()
