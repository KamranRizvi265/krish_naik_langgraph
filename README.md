# Agentic LangGraph

A comprehensive collection of practical examples demonstrating the power of **LangGraph** for building intelligent, agentic applications using modern language models and tool integration.

## 📋 Overview

This repository contains educational projects and implementations showcasing:
- **LangGraph Framework**: State-of-the-art graph-based workflow orchestration for LLM applications
- **Agentic Systems**: Building autonomous agents with decision-making capabilities
- **Tool Integration**: Seamless integration with external APIs and services via MCP (Model Context Protocol)
- **Multi-Model Support**: Examples using OpenAI, Google Generative AI, and Groq

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- pip or UV package manager
- API keys for LLM providers (OpenAI, Google Generative AI, or Groq)

### Installation

Clone the repository:
```bash
git clone https://github.com/KamranRizvi265/krish_naik_langgraph.git
cd krish_naik_langgraph
```

Install dependencies using UV (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the project root with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## 📁 Project Structure

### 1. Basic Chatbot (`1-BasicChatbot/`)
Your first introduction to LangGraph and conversational AI.

**Contents:**
- `1-basicchatbot.ipynb` - Interactive Jupyter notebook demonstrating basic chatbot implementation

**Topics Covered:**
- Setting up LLM connections
- Creating simple conversation chains
- State management in LangGraph
- Basic message handling

### 2. Model Context Protocol (`2-mcp/`)
Advanced examples showcasing tool integration and agent capabilities using the Model Context Protocol.

**Contents:**
- `client.py` - MCP client implementation for connecting agents to tools
- `mathserver.py` - Mathematical tool server providing computation capabilities
- `weather.py` - Weather information tool server for real-world data integration

**Topics Covered:**
- MCP client-server architecture
- Tool definition and implementation
- Agent-tool interaction patterns
- Real-world data integration

## 📦 Dependencies

Core dependencies:
- **langgraph** (>=1.2.6) - Graph-based workflow orchestration
- **langchain** (>=1.3.10) - LLM framework and tools
- **langchain-openai** (>=1.3.3) - OpenAI integration
- **langchain-google-genai** (>=4.2.5) - Google Generative AI integration
- **langchain-groq** (>=1.1.3) - Groq API integration
- **langchain-mcp-adapters** (>=0.3.0) - MCP protocol support
- **langchain-tavily** (>=0.2.18) - Web search capabilities
- **mcp** (>=1.28.1) - Model Context Protocol
- **python-dotenv** (>=1.2.2) - Environment variable management
- **ipykernel** (>=7.3.0) - Jupyter notebook support

See `pyproject.toml` for complete dependency information.

## 🎯 Use Cases

- **Conversational Agents**: Build chatbots with stateful conversations
- **Tool-Augmented Systems**: Create agents that can use external tools and APIs
- **Autonomous Workflows**: Implement decision-making agents for complex tasks
- **Multi-Model Applications**: Leverage different LLM providers in a unified framework

## 🔧 Configuration

### Python Version
This project requires Python 3.13 or higher. The required version is specified in `.python-version`.

### Package Management
The project uses UV for fast, reliable dependency management. Dependencies are locked in `uv.lock` for reproducible builds.

## 📚 Getting Started Guide

1. **Start with the Basic Chatbot**: Open `1-BasicChatbot/1-basicchatbot.ipynb` in Jupyter to understand LangGraph fundamentals
2. **Explore MCP Integration**: Review the MCP examples to see how agents interact with tools
3. **Experiment**: Modify the examples to integrate your own LLM provider or custom tools
4. **Scale**: Use these patterns as a foundation for building production-ready applications

## 🛠️ Development

### Running Jupyter Notebooks
```bash
jupyter notebook
```

### Running Python Scripts
```bash
python 2-mcp/client.py
python 2-mcp/mathserver.py
python 2-mcp/weather.py
```

## 📖 Learning Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Tavily API Documentation](https://tavily.com/)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Submit issues for bugs or improvements
- Create pull requests with new examples or enhancements
- Share feedback and suggestions

## 📄 License

This project is open source and available for educational and personal use.

## 👤 Author

**Kamran Rizvi**  
Repository: [krish_naik_langgraph](https://github.com/KamranRizvi265/krish_naik_langgraph)

## 🙏 Acknowledgments

Built with inspiration from the works of Krish Naik and the broader LangChain community.

---

**Happy coding!** 🚀 Feel free to explore the examples and build amazing agentic applications with LangGraph.
