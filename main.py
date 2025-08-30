from crewai import Crew, Process
from tasks.research_task import create_research_task
from tasks.organize_task import create_organization_task
from tasks.generation_task import create_generation_task
from utils.ppt_formatter import PowerPointFormatter
from utils.config_loader import Config
from utils.llm_config import get_perplexity_llm
import os

def main():
    # Validate configuration
    Config.validate()
    
    # Get user input
    topic = input("Enter the topic for your presentation: ").strip()
    if not topic:
        print("Topic cannot be empty!")
        return
    
    filename = input("Enter a filename for your presentation (without extension): ").strip()
    if not filename:
        filename = "presentation"
    
    print(f"\nStarting research on: {topic}")
    
    # Create tasks
    research_task = create_research_task(topic)
    organization_task = create_organization_task(topic, research_task)
    generation_task = create_generation_task(topic, organization_task)
    
    # Form the crew
    crew = Crew(
        agents=[
            research_task.agent,
            organization_task.agent,
            generation_task.agent
        ],
        tasks=[research_task, organization_task, generation_task],
        process=Process.sequential,
        verbose=True,
        llm=get_perplexity_llm() 
    )
    
    # Execute the crew's work
    print("Starting the research and presentation generation process...")
    result = crew.kickoff()
    
    print("\nResearch and organization completed. Generating PowerPoint...")
    
    # Parse the result and generate the PowerPoint
    try:
        formatter = PowerPointFormatter()
        formatter.format_content_from_outline(str(result))
        output_path = formatter.save_presentation(filename)
        
        print(f"\n✅ Presentation successfully created!")
        print(f"📁 Location: {os.path.abspath(output_path)}")
    except Exception as e:
        print(f"❌ Error creating PowerPoint: {str(e)}")
        # Fallback: save the raw content
        with open(f"output/{filename}_content.txt", "w") as f:
            f.write(str(result))
        print(f"Raw content saved to output/{filename}_content.txt")

if __name__ == "__main__":
    main()