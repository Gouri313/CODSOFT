print("=" * 50)
print("      Welcome to CodSoft Chatbot")
print("=" * 50)

print("\nYou can ask me:")
print("- hello")
print("- how are you")
print("- your name")
print("- who created you")
print("- what is python")
print("- thank you")
print("- bye")

while True:

    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is CodSoft Chatbot.")

    elif user == "who created you":
        print("Bot: I was created by Gouri Parashar.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry! I don't understand that.")