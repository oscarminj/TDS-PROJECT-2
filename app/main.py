from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import Optional
from app.utils.openai_client import get_openai_response
from app.utils.file_handler import save_upload_file_temporarily

# Initialize FastAPI app
app = FastAPI(title="IITM Assignment API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "HEAD", "POST"],  # Explicitly allow HEAD
    allow_headers=["*"],
)
@app.head("/")
async def head_check():
    return {"status": "ok"}

@app.get("/")  # No need to specify methods
def home():
    return {"message": "FastAPI is running!"}

@app.get("/health")  # No need to specify methods
def health_check():
    return {"status": "ok"}


@app.post("/api/")
async def process_question(
    question: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    try:
        # Save file temporarily if provided
        temp_file_path = None
        if file:
            temp_file_path = await save_upload_file_temporarily(file)
        
        # Get answer from OpenAI
        answer = await get_openai_response(question, temp_file_path)
        
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import uvicorn
import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Render provides PORT dynamically
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
