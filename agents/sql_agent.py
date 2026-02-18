from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from dotenv import load_dotenv

load_dotenv()

def get_sql_agent():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    db = SQLDatabase.from_uri("sqlite:///support.db")

    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        verbose=True
    )

    return agent_executor
