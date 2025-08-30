from crewai import Task
from agents.ppt_generator import create_pptx_generator_agent

def create_generation_task(topic, structured_content):
    generator = create_pptx_generator_agent()
    
    return Task(
        description=f"""Create a PowerPoint presentation on {topic} based on the provided structured content.
        
        Create a professional presentation with:
        - A title slide with an engaging title and subtitle
        - An overview slide introducing the topic
        - 3-4 content slides with key points, trends, or arguments
        - A conclusion slide with takeaways
        
        Format each slide with appropriate titles and bullet points.
        Ensure the presentation is visually appealing and well-organized.""",
        agent=generator,
        context=[structured_content],
        expected_output="A complete PowerPoint presentation saved as a .pptx file with all content properly formatted."
    )