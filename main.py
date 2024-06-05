from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a history buff that can take any American state, any year after 1776, and talk out what was going on in that state at that time"),
        ("user", "State: {state}\n Year: {year}")
    ]
)
model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

chain = prompt_template | model | parser

response = chain.invoke({
    "state": "Montana",
    "year": "2006"
})

print(response)