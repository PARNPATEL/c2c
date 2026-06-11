print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("ChatBot: Hi! Nice to meet you.")
        
    elif user == "how are you":
        print("ChatBot: I am fine. How about you?")
        
    elif user == "your name":
        print("ChatBot: My name is Python Bot.")
        
    elif user == "who made you":
        print("ChatBot: A Python programmer made me.")
        
    elif user == "what is python":
        print("ChatBot: Python is a popular programming language.")
        
    elif user == "what can you do":
        print("ChatBot: I can answer simple questions and chat with you.")
        
    elif user == "good morning":
        print("ChatBot: Good morning! Have a great day.")
        
    elif user == "good night":
        print("ChatBot: Good night! Sweet dreams.")
        
    elif user == "thank you":
        print("ChatBot: You're welcome!")
        
    elif user == "bye":
        print("ChatBot: Goodbye! Have a nice day.")
        break
        
    else:
        print("ChatBot: Sorry, I don't understand that.")
