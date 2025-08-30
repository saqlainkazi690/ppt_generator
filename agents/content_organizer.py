from crewai import Agent
from utils.llm_config import get_perplexity_llm

def create_content_organizer_agent():
    return Agent(
        role='Content Strategist and Organizer',
        goal='Structure research findings into a coherent presentation outline with clear sections',
        backstory="""You are a skilled content strategist who excels at organizing complex 
        information into clear, logical structures. You have a talent for identifying key 
        points and creating compelling narratives that engage audiences.""",
        verbose=True,
        allow_delegation=False,
        llm=get_perplexity_llm()
    )