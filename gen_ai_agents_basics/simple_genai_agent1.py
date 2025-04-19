import os
import sys
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="o4-mini")



@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b."""
    return a * b

llm_with_tools = llm.bind_tools([multiply])

response = llm_with_tools.invoke("What is 2 multiplied by 3?")
print(response)
