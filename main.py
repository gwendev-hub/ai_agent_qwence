from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import httpx
import wincertstore

load_dotenv()

client = httpx.Client(timeout=30)

llm = ChatOpenAI(model="gpt-5-nano",
                 api_key=os.getenv("OPENAI_API_KEY"),
                  http_client=client, )


response = llm.invoke("What is the capital of France?")
print(response.content)

#Fails because of proxy certificate issue, firewall from cap


# Test
# resp = httpx.get("https://www.google.com", timeout=15)
# print(resp.status_code, resp.headers.get("server"))
