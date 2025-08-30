from crewai import Task
from agents.content_organizer import create_content_organizer_agent

def create_organization_task(topic, research_data):
    organizer = create_content_organizer_agent()
    
    return Task(
        description=f"""Organize the research findings about {topic} into a structured presentation outline.
        
        The presentation should follow this structure:
        1. Title Slide: Engaging title and subtitle
        2. Overview/Introduction: Context and importance of the topic
        3. Key Points/Trends/Arguments: 3-4 slides with main content
        4. Conclusion/Takeaways: Summary and implications
        
        Ensure the content flows logically and highlights the most important information.""",
        agent=organizer,
        context=[research_data],
        expected_output="A structured outline for a PowerPoint presentation with clear sections and bullet points for each slide."
    )