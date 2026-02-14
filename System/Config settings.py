import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY")
    MODEL_NAME = "gpt-4o"
    TEMPERATURE = 0

settings = Settings()

