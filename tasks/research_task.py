from crewai import Task
from agents.researcher import create_researcher_agent

def create_research_task(topic):
    researcher = create_researcher_agent()
    
    return Task(
        description=f"""Conduct comprehensive research on the topic: {topic}
        
        Gather information from reliable sources including:
        - Latest trends and developments
        - Key facts and statistics
        - Important stakeholders or influencers
        - Current challenges and opportunities
        - Future projections or forecasts
        
        Ensure the information is up-to-date, accurate, and comprehensive.""",
        agent=researcher,
        expected_output="A detailed research report with all relevant information about the topic, including sources where appropriate."
    )