from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import os
import asyncio

from dotenv import load_dotenv
load_dotenv()

async def main():
    try:
        client = MultiServerMCPClient(
            {
                "math": {
                    "command": "python",
                    "args": ["mathserver.py"],   # Ensure correct absolute path
                    "transport": "stdio"
                },
                "weather": {
                    "url": "http://localhost:8000/mcp",
                    "transport": "streamable-http"
                }
            }
        )
    except Exception as e:
        print(f"Failed to initialize MCP client: {e}")
        return

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY is not set. Add it to your .env file.")
        return
    os.environ["GROQ_API_KEY"] = api_key

    try:
        tools = await client.get_tools()
    except Exception as e:
        print(f"Failed to load MCP tools (check that mathserver.py and weather server are running): {e}")
        return

    try:
        llm = ChatGroq(model="qwen/qwen3-32b")
        agent = create_agent(llm, tools)

        math_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "What is 5*15?"}]}
        )
        print(math_response["messages"][-1].content)
    except Exception as e:
        print(f"Agent invocation failed: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user.")