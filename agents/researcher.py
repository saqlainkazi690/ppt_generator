from crewai import Agent
from tools.web_searchtool import WebSearchTool
from utils.llm_config import get_perplexity_llm

def create_researcher_agent():
    return Agent(
        role='Senior Research Analyst',
        goal='Gather comprehensive, accurate, and up-to-date information on the given topic',
        backstory="""You are an expert research analyst with years of experience in gathering 
        and synthesizing information from various sources. You have a keen eye for detail 
        and always ensure the information you provide is accurate, relevant, and current.""",
        tools=[WebSearchTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_perplexity_llm()
    )