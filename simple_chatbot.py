import time

def welcome():
    print("=" * 50)
    print("         SIMPLE RULE-BASED CHATBOT")
    print("=" * 50)
    print("This chatbot responds to predefined commands.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit the chatbot.")
    print()

def show_help():
    print("\nAvailable Commands:")
    print("- hello")
    print("- how are you")
    print("- your name")
    print("- my name")
    print("- time")
    print("- tell me a joke")
    print("- thank you")
    print("- help")
    print("- bye")
    print()

def chatbot():
    user_name = input("Enter your name: ")

    print(f"\nBot: Hello {user_name}! Welcome to the chatbot.")
    print("Bot: How can I help you today?\n")

    conversation_count = 0

    while True:
        user_input = input("You: ").strip().lower()
        conversation_count += 1

        if user_input == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks for asking!")

        elif user_input == "your name":
            print("Bot: My name is SimpleBot.")

        elif user_input == "my name":
            print(f"Bot: Your name is {user_name}.")

        elif user_input == "time":
            current_time = time.strftime("%H:%M:%S")
            print(f"Bot: The current time is {current_time}")

        elif user_input == "tell me a joke":
            print("Bot: Why do programmers prefer dark mode?")
            print("Bot: Because light attracts bugs!")

        elif user_input == "thank you":
            print("Bot: You're welcome! Happy to help.")

        elif user_input == "help":
            show_help()

        elif user_input == "bye":
            print(f"\nBot: Goodbye, {user_name}!")
            print(f"Bot: Total messages exchanged: {conversation_count}")
            print("Bot: Thank you for using this chatbot.")
            break

        else:
            print("Bot: Sorry, I don't understand that command.")
            print("Bot: Type 'help' to see available commands.")

        print()

welcome()
chatbot()