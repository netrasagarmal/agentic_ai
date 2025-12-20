import asyncio
from fastmcp import Client

######################################################################
# Method 1: Connect to each MCP server via its HTTP endpoint
######################################################################

print("\n\n--- Method 1: Connecting to Multiple MCP Servers via HTTP  ---")

async def sample_client1():
    # Connect via the full URL (FastMCP uses /mcp as the default path)
    airbnb_mcp_url = "http://localhost:8000/mcp"
    easemytrip_mcp_url = "http://localhost:8001/mcp"
    makemytrip_mcp_url = "http://localhost:8002/mcp"

    print("--- Connecting to HTTP MCP Servers ---")
    
    # Initialize clients with the URLs
    async with Client(airbnb_mcp_url) as airbnb_client, \
                Client(easemytrip_mcp_url) as easemytrip_client, \
                Client(makemytrip_mcp_url) as makemytrip_client:

        print("\n[Querying Airbnb Server via HTTP] to get hotel rates")
        response = await airbnb_client.call_tool(name="fetch_hotel_prices", arguments={"city": "Mumbai", "date": "2025-01-02"})
        print(f"Server Response:\n{response.data}")

        print("\n[Querying EaseMyTrip Server via HTTP] to get flight prices")
        response = await easemytrip_client.call_tool(name="fetch_flight_prices", arguments={"boarding":"Mumbai", "destination":"Delhi", "travel_date":"2025-01-01"})
        print(f"Server Response:\n{response.data}")

        print("\n[Querying MakeMyTrip Server via HTTP] to get flight prices")
        response = await makemytrip_client.call_tool(name="fetch_flight_prices", arguments={"boarding":"Mumbai", "destination":"Pune", "travel_date":"2025-01-01"})
        print(f"Server Response:\n{response.data}")

        print("\n[Querying MakeMyTrip Server via HTTP to get hotel rates]")
        response = await makemytrip_client.call_tool(name="fetch_hotel_prices", arguments={"city": "Mumbai", "date": "2025-01-02"})
        print(f"Server Response:\n{response.data}")

######################################################################
# Method 2: Connecting to Multiple MCP Servers via Config
######################################################################

print("\n\n--- Method 2: Connecting to Multiple MCP Servers via Config ---")

mcp_config = {
     "mcpServers": {
          "airbnb-mcp": {
               "url": "http://localhost:8000/mcp",
               "transport": "streamable-http"
          },
          "easemytrip-mcp": {
               "url": "http://localhost:8001/mcp",
               "transport": "streamable-http"
          },
          "makemytrip-mcp": {
               "url": "http://localhost:8002/mcp",
               "transport": "streamable-http"
          },
     }
}

# Create a client that connects to all servers
client = Client(mcp_config)

async def sample_client2():
    # Connect via stdio to a local script
    async with client:
        tools = await client.list_tools()
        print(f"\n Available tools: {tools}\n\n")

        # Example calls to airbnb-mcp (specify name as {server_name}_{tool_name}, eg: airbnb-mcp_get_hotel_rates)
        response = await client.call_tool(name="airbnb-mcp_get_hotel_rates", arguments={"city": "Mumbai", "date": "2025-01-02"})
        print("\n\n Get Airbnb hotel Rates: \n")
        print(response.data)

        # Example calls to easemytrip-mcp (specify name as {server_name}_{tool_name}, eg: easemytrip-mcp_fetch_flight_price)
        response = await client.call_tool(name="easemytrip-mcp_fetch_flight_price", arguments={"boarding":"Mumbai", "destination":"Delhi", "travel_date":"2025-01-01"})
        print("\n\n Get easemytrip flight Rates: \n")
        print(response.data)

        # Example calls to makemytrip-mcp (specify name as {server_name}_{tool_name}, eg: makemytrip-mcp_fetch_flight_price)
        response = await client.call_tool(name="makemytrip-mcp_fetch_flight_price", arguments={"boarding":"Mumbai", "destination":"Pune", "travel_date":"2025-01-01"})
        print("\n\n Get makemytrip flight Rates: \n")
        print(response.data)

        # Example calls to makemytrip-mcp (specify name as {server_name}_{tool_name}, eg: makemytrip-mcp_fetch_flight_price)
        response = await client.call_tool(name="makemytrip-mcp_get_hotel_rates", arguments={"city": "Mumbai", "date": "2025-01-02"})
        print("\n\n Get makemytrip hotel Rates: \n")
        print(response.data)

if __name__ == "__main__":
    # Run both sample clients
    asyncio.run(sample_client1())  # Run Method 1
    asyncio.run(sample_client2())  # Run Method 2