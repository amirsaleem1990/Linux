#!/home/amir/.venv_gemini/bin/python3

api_key = "AIzaSyChaep6ttjm0US-gSBokwtn-OPbl0cvb_0"


import google.generativeai as genai

# Configure the API key
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Start a chat session
chat = model.start_chat()

print("Gemini Chat Session Started. Type 'exit' to terminate the session.\n")

while True:
    # Take user input
    user_input = input("You: ")

    # Check if the user wants to exit the session
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the session. Goodbye!")
        break

    try:
        # Send the user's message to the chat session
        response = chat.send_message(user_input)
        gemini_reply = response.text

        # Print Gemini's reply
        print(f"Gemini: {gemini_reply}\n")
    except Exception as e:
        print(f"An error occurred: {e}")
