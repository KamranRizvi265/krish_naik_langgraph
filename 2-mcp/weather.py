from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get the weather for a given city
    """
    return f"The weather in {city} is sunny"

# The transport="streamable-http" argument means that the MCP will use the Streamable HTTP transport to communicate with the client.
# This is a good transport for web applications, as it allows the MCP to be used in a web browser.

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    print(mcp.get_tool("get_weather")(city="New York"))