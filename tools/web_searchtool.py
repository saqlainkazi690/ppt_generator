import requests
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from utils.config_loader import Config

class WebSearchToolInput(BaseModel):
    query: str = Field(..., description="The search query to look up")

class WebSearchTool(BaseTool):
    name: str = "web_search_tool"
    description: str = "Search the web for up-to-date information on a given topic"
    args_schema: Type[BaseModel] = WebSearchToolInput

    def _run(self, query: str) -> str:
        Config.validate()
        
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {Config.PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar",
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert researcher. Provide comprehensive, accurate information with sources."
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            "temperature": 0.2,
            "max_tokens": 2000
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except Exception as e:
            return f"Error performing web search: {str(e)}"