import os
import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# --- GEMINI SETUP ---
# 1. Configure the library with your key
# It looks for "GEMINI_API_KEY" in your environment variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Select the Model
# "gemini-1.5-flash" is free, fast, and smart
model = genai.GenerativeModel('gemini-1.5-flash')

# Define the input format
class QueryRequest(BaseModel):
    query: str
    session_id: str = "default"

@app.post("/ask")
async def ask_agent(request: QueryRequest):
    try:
        # --- THE AI LOGIC ---
        
        # 3. Create the Prompt
        # We tell Gemini who it is and pass the user's question
        prompt = f"""
        You are an expert HR Policy Assistant for a company.
        Answer the following question clearly and professionally based on standard corporate policies.
        
        User Question: {request.query}
        """

        # 4. Ask Gemini
        response = model.generate_content(prompt)
        
        # 5. Get the Answer Text
        # .text extracts the string from the AI response
        answer_text = response.text

        # 6. Return the JSON format required by your Assignment
        return {
            "answer": answer_text,
            "source": ["AI_Generated_Response (Gemini 1.5)"]
        }

    except Exception as e:
        # If something breaks, show the error
        return {
            "answer": f"Error connecting to AI: {str(e)}", 
            "source": []
        }