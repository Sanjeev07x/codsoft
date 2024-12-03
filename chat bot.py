def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for uniformity
    
    # Greetings
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I assist you today?"
    
    # Farewell
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    
    # Ask about the chatbot
    elif 'who are you' in user_input or 'what is your name' in user_input:
        return "I am a simple chatbot, created to assist you with basic queries."
    
    # Ask about the weather
    elif 'weather' in user_input:
        return "I can't check real-time weather, but you can check a weather website for updates!"
    
    # Thank you response
    elif 'thank you' in user_input or 'thanks' in user_input:
        return "You're welcome! Let me know if you need anything else."
    
    # Default response for unknown input
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main function to run the chatbot
def chat():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if 'bye' in user_input or 'goodbye' in user_input:
            print(f"Chatbot: {chatbot_response(user_input)}")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
chat()
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for uniformity
    
    # Greetings
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I assist you today?"
    
    # Farewell
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    
    # Ask about the chatbot
    elif 'who are you' in user_input or 'what is your name' in user_input:
        return "I am a simple chatbot, created to assist you with basic queries."
    
    # Ask about the weather
    elif 'weather' in user_input:
        return "I can't check real-time weather, but you can check a weather website for updates!"
    
    # Thank you response
    elif 'thank you' in user_input or 'thanks' in user_input:
        return "You're welcome! Let me know if you need anything else."
    
    # Default response for unknown input
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main function to run the chatbot
def chat():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if 'bye' in user_input or 'goodbye' in user_input:
            print(f"Chatbot: {chatbot_response(user_input)}")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
chat()
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for uniformity
    
    # Greetings
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I assist you today?"
    
    # Farewell
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    
    # Ask about the chatbot
    elif 'who are you' in user_input or 'what is your name' in user_input:
        return "I am a simple chatbot, created to assist you with basic queries."
    
    # Ask about the weather
    elif 'weather' in user_input:
        return "I can't check real-time weather, but you can check a weather website for updates!"
    
    # Thank you response
    elif 'thank you' in user_input or 'thanks' in user_input:
        return "You're welcome! Let me know if you need anything else."
    
    # Default response for unknown input
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main function to run the chatbot
def chat():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if 'bye' in user_input or 'goodbye' in user_input:
            print(f"Chatbot: {chatbot_response(user_input)}")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
chat()