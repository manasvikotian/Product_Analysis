from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Template for the chatbot to follow the conversation
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Loading llama3.2 model from Ollama
model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


# Function with an infinite loop to keep the chat going on
def handle_conversation():
    context = ""
    print("Start chatting. Type quit, exit or bye to quit")
    while True:
        user_input = input("You: ")
        
        # Breaks, to stop the chat
        if user_input.lower() in ['quit', "exit", "bye"]:
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)

        # Storing chat history for the Bot to continue the conversation
        context += f"\nUser: {user_input}\nAI: {result}"
    


if __name__ == "__main__":
    handle_conversation()