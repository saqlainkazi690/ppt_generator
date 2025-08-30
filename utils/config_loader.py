import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
    
    @classmethod
    def validate(cls):
        if not cls.PERPLEXITY_API_KEY:
            raise ValueError("PERPLEXITY_API_KEY not found in environment variables")