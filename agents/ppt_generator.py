from crewai import Agent
from utils.llm_config import get_perplexity_llm

def create_pptx_generator_agent():
    return Agent(
        role='PowerPoint Presentation Specialist',
        goal='Transform structured content into a well-formatted PowerPoint presentation',
        backstory="""You are an expert in creating professional PowerPoint presentations. 
        You have a keen eye for design and know how to present information in a visually 
        appealing and effective manner. You understand how to balance text and visuals 
        to create engaging slides.""",
        verbose=True,
        allow_delegation=False,
        llm=get_perplexity_llm()
    )