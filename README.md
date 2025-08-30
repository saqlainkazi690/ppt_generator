# AI Presentation Generator

An intelligent presentation generator powered by CrewAI that creates professional PowerPoint presentations using multiple AI agents.

## Features

- 🤖 **Multi-Agent System**: Uses specialized AI agents for research, organization, and presentation generation
- 📊 **Professional PowerPoint Output**: Creates well-formatted presentations with smaller, readable fonts
- 🔍 **Web Research**: Gathers up-to-date information from the internet
- 🎨 **Beautiful UI**: Streamlit web interface for easy interaction
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**:
   Create a `.env` file in the project root and add your Perplexity API key:
   ```
   PERPLEXITY_API_KEY=your_api_key_here
   ```

## Usage

### Option 1: Streamlit Web Interface (Recommended)

Run the web interface:
```bash
streamlit run app.py
```

This will open a beautiful web interface where you can:
- Enter your presentation topic
- Choose a filename
- Generate presentations with a single click
- Download the PowerPoint file directly
- View the generated content

### Option 2: Terminal Interface

Run the traditional terminal interface:
```bash
python main.py
```

Follow the prompts to enter your topic and filename.

## How It Works

The system uses three specialized AI agents:

1. **Research Agent**: Gathers comprehensive information about your topic
2. **Organizer Agent**: Structures the content into a logical presentation outline
3. **Generator Agent**: Creates the final PowerPoint presentation

## Output

- Presentations are saved in the `output/` directory
- Font sizes are optimized for readability (smaller than default)
- Professional formatting with proper slide structure

## Requirements

- Python 3.8+
- Perplexity API key
- Internet connection for web research

## File Structure

```
crew_ai_wave/
├── agents/           # AI agent definitions
├── tasks/           # Task definitions
├── tools/           # Custom tools (web search)
├── utils/           # Utilities (config, formatter)
├── output/          # Generated presentations
├── app.py           # Streamlit web interface
├── main.py          # Terminal interface
└── requirements.txt # Dependencies
```

## Troubleshooting

- **API Key Error**: Make sure your `.env` file contains the correct Perplexity API key
- **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **Permission Errors**: Make sure the `output/` directory is writable

## License

This project is open source and available under the MIT License.
