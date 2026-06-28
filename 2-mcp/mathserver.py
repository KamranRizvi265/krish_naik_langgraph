from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers together
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract two numbers together
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers together
    """
    return a * b

# The transport="stdio" argument means that the MCP will use the standard input and output streams to communicate with the client.
# It is not recommended to use this transport for web applications, as it is not secure.

if __name__ == "__main__":
    mcp.run(transport="stdio")