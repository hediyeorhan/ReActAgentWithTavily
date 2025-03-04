from dotenv import load_dotenv

import os

import sqlite3

from langchain import hub
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain.agents import AgentExecutor, create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key = os.getenv("GEMINI_API_KEY"))

db_path = "checkpoints.db"

# Bir db dosyasi yoksa olusturuluyor
if not os.path.exists(db_path):
    open(db_path, 'w').close()  


conn = sqlite3.connect(db_path, check_same_thread=False)
memory = SqliteSaver(conn)


search = TavilySearchResults(max_results=2)
tools = [search]


prompt = hub.pull("hwchase17/react-chat")

agent = create_react_agent(model, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, checkpoint=memory)
config = {"configurable": {"thread_id": "12345"}}

# Program sonlandiginda dosya tamamen siliniyor
def cleanup():
    conn.close()
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Veritabani dosyasi silindi.")


if __name__ == '__main__':
    chat_history = []

    while True:
        user_input = input("> ")
        if user_input == 'q':
            cleanup()
            break
        
        chat_history.append(f"Human: {user_input}")

        response = []
        for chunk in agent_executor.stream(
                {
                    "input": user_input,
                    "chat_history": "\n".join(chat_history),
                },
                config
        ):
            if 'text' in chunk:
                print(chunk['text'], end='')
                response.append(chunk['text'])

        chat_history.append(f"AI: {''.join(response)}")
        print("\n----")