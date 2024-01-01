import openai
import sttandtts as st

openai.api_key = "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"
conversation_memory = []

def chat_with_memory(input_message):
    conversation_memory.append({"role": "system", "content": "You are a helpful teaching assistant, answer any question within maximim 2 lines."})
    conversation_memory.append({"role": "user", "content": input_message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_memory,
        max_tokens=100
    )
    assistant_message = response['choices'][0]['message']['content']
    conversation_memory.append({"role": "assistant", "content": assistant_message})
    return assistant_message

if __name__ == "__main__":
    print("ChatGPT Assistant with Memory")
    print("You can exit by saying 'exit'.")
    while True:
        user_input = st.recognize_speech()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        assistant_response = chat_with_memory(user_input)
        print("Assistant:", assistant_response)
        st.convert_speech(assistant_response)
        #st.play_speech()

