import streamlit as st
import os
import sys
from pathlib import Path

# Add the current directory to Python path to import our modules
sys.path.append(str(Path(__file__).parent))

from crewai import Crew, Process
from tasks.research_task import create_research_task
from tasks.organize_task import create_organization_task
from tasks.generation_task import create_generation_task
from utils.ppt_formatter import PowerPointFormatter
from utils.config_loader import Config
from utils.llm_config import get_perplexity_llm

# Page configuration
st.set_page_config(
    page_title="AI Presentation Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .status-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
</style>
""", unsafe_allow_html=True)

def validate_config():
    """Validate the configuration"""
    try:
        Config.validate()
        return True
    except ValueError as e:
        st.error(f"Configuration Error: {str(e)}")
        st.info("Please make sure you have set up your PERPLEXITY_API_KEY in the .env file")
        return False

def generate_presentation(topic, filename):
    """Generate the presentation using CrewAI"""
    try:
        # Create tasks
        with st.status("Creating research task...", expanded=True) as status:
            research_task = create_research_task(topic)
            status.update(label="Research task created successfully!", state="complete")
        
        with st.status("Creating organization task...", expanded=True) as status:
            organization_task = create_organization_task(topic, research_task)
            status.update(label="Organization task created successfully!", state="complete")
        
        with st.status("Creating generation task...", expanded=True) as status:
            generation_task = create_generation_task(topic, organization_task)
            status.update(label="Generation task created successfully!", state="complete")
        
        # Form the crew
        with st.status("Forming AI crew...", expanded=True) as status:
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
            status.update(label="AI crew formed successfully!", state="complete")
        
        # Execute the crew's work
        with st.status("Starting research and presentation generation...", expanded=True) as status:
            status.update(label="Researching topic...", state="running")
            result = crew.kickoff()
            status.update(label="Research completed! Generating PowerPoint...", state="running")
        
        # Generate PowerPoint
        with st.status("Creating PowerPoint presentation...", expanded=True) as status:
            formatter = PowerPointFormatter()
            formatter.format_content_from_outline(str(result))
            output_path = formatter.save_presentation(filename)
            status.update(label="PowerPoint created successfully!", state="complete")
        
        return output_path, str(result)
        
    except Exception as e:
        st.error(f"Error during presentation generation: {str(e)}")
        return None, None

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Presentation Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Generate professional PowerPoint presentations using AI agents</p>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Check configuration
        if not validate_config():
            st.stop()
        
        st.success("✅ Configuration validated!")
        
        st.header("📋 Instructions")
        st.markdown("""
        1. Enter your presentation topic
        2. Choose a filename for your presentation
        3. Click 'Generate Presentation'
        4. Wait for the AI agents to work their magic!
        """)
        
        st.header("🔧 Features")
        st.markdown("""
        - **Research Agent**: Gathers comprehensive information
        - **Organizer Agent**: Structures content logically
        - **Generator Agent**: Creates professional slides
        - **Small Font Sizes**: Optimized for readability
        """)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🎯 Presentation Details")
        
        # Topic input
        topic = st.text_input(
            "Enter your presentation topic:",
            placeholder="e.g., Artificial Intelligence in Healthcare, Climate Change Solutions, etc.",
            help="Be specific about what you want to present"
        )
        
        # Filename input
        filename = st.text_input(
            "Enter filename for your presentation (without extension):",
            placeholder="my_presentation",
            help="The presentation will be saved as [filename].pptx"
        )
        
        # Generate button
        if st.button("🚀 Generate Presentation", type="primary", use_container_width=True):
            if not topic.strip():
                st.error("Please enter a topic for your presentation!")
            elif not filename.strip():
                st.error("Please enter a filename for your presentation!")
            else:
                # Clear previous results
                if 'output_path' in st.session_state:
                    del st.session_state['output_path']
                if 'result_content' in st.session_state:
                    del st.session_state['result_content']
                
                # Generate presentation
                with st.spinner("AI agents are working on your presentation..."):
                    output_path, result_content = generate_presentation(topic.strip(), filename.strip())
                
                if output_path:
                    st.session_state['output_path'] = output_path
                    st.session_state['result_content'] = result_content
    
    with col2:
        st.header("📊 Status")
        
        if 'output_path' in st.session_state:
            st.success("✅ Presentation Generated!")
            
            # Download button
            with open(st.session_state['output_path'], 'rb') as file:
                st.download_button(
                    label="📥 Download PowerPoint",
                    data=file.read(),
                    file_name=f"{filename}.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    use_container_width=True
                )
            
            # Show file info
            st.info(f"📁 Saved as: {os.path.basename(st.session_state['output_path'])}")
            
            # Show raw content option
            if st.checkbox("Show generated content"):
                st.text_area("Generated Content:", st.session_state['result_content'], height=300)
        else:
            st.info("👆 Enter topic and filename, then click 'Generate Presentation' to get started!")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #666;'>Powered by CrewAI and Perplexity API</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
