from crewai import LLM
from utils.config_loader import Config

def get_perplexity_llm():
    """Configure CrewAI to use Perplexity API"""
    return LLM(
        model="perplexity/sonar",
        api_key=Config.PERPLEXITY_API_KEY,
        base_url="https://api.perplexity.ai",
        temperature=0.1
    )