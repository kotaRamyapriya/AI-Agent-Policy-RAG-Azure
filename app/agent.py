import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI # Use Gemini instead
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool

# 1. Load Environment Variables
load_dotenv()

# 2. Setup Google Gemini (Free Tier)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", # If this fails, try "models/gemini-1.5-flash"
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)
