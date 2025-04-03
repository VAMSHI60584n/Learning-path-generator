from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# Allow frontend requests from any origin (change in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

available_languages = ["Python", "JavaScript", "C++", "Java", "Go", "Rust"]

class LanguageRequest(BaseModel):
    language: str

@app.get("/languages")
def get_languages():
    return {"languages": available_languages}

@app.post("/generate-path")
def generate_learning_path(request: LanguageRequest):
    if request.language not in available_languages:
        return {"error": "Language not supported."}

    learning_path = [
        f"Introduction to {request.language}",
        f"Basic Syntax of {request.language}",
        f"Data Structures in {request.language}",
        f"Advanced Concepts in {request.language}",
        f"Projects and Real-World Applications in {request.language}"
    ]
    return {"language": request.language, "learning_path": learning_path}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
