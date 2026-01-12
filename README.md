**Live Demo:** http://ramya-final-app-99.azurewebsites.net/docs


#  AI Agent for Corporate Policy RAG 

This is a production-ready AI Agent built with **FastAPI**, **LangChain**, and **FAISS**, fully deployed on **Azure App Service**. It uses Retrieval-Augmented Generation (RAG) to answer questions about company policy documents.

##  Architecture Overview
The system follows a standard RAG pipeline:
1. **Ingestion**: Documents are chunked and stored as vectors.
2. **Retrieval**: The agent uses a FAISS vector store to find relevant chunks.
3. **Generation**: A **Gemini 1.5 Flash** model provides grounded answers based on the retrieved context.

##  Tech Stack
- **Framework:** FastAPI
- **LLM:** Google Gemini 1.5 Flash (Free Tier)
- **Vector Store:** FAISS (Local storage)
- **Deployment:** Azure App Service (Linux)
- **Containerization:** Docker (as seen in `Dockerfile`)

##  Setup & Deployment
### Local Setup
1. `pip install -r requirements.txt`
2. Configure `.env` with `GOOGLE_API_KEY`
3. `uvicorn app.main:app --reload`

### Azure Deployment
Deployed via Azure CLI:
`az webapp up --sku F1 --name ramya-final-app-99`

##  Design Decisions
- **LLM Choice:** Switched from Azure OpenAI to **Google Gemini** to utilize the free-tier for the assignment while maintaining identical logic.
- **Docker:** Included a `Dockerfile` to ensure the app runs consistently in the cloud.

##  Limitations & Future Improvements
- **Security:** In production, I would move local FAISS storage to **Azure AI Search**.
- **Monitoring:** Integration with **Azure Monitor** for better logging.
