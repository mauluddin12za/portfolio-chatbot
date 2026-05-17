import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from dotenv import load_dotenv

load_dotenv()



app = FastAPI(title="Portfolio Chatbot API")

allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(chat_router, prefix="/api")

APP_LANG = os.getenv("APP_LANG", "en")

# build path dynamically
knowledge_path = os.path.join(
    os.path.dirname(__file__),
    f"./data/{APP_LANG}/faq.json"
)


@app.get("/")
def root():
    return {"message": "Portfolio Chatbot API is running"}


@app.get("/api/faq")
def get_data():
    try:
        with open(knowledge_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "JSON file not found"}
