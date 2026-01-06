def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what's your name":
            print("Chatbot: I'm Chatbot.") 

        elif user_input == "age":
            print("Chatbot: I don't have an age.")   
        
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        
        else:
            print("Chatbot: Sorry, I don't understand.")

# Run the chatbot
chatbot()
