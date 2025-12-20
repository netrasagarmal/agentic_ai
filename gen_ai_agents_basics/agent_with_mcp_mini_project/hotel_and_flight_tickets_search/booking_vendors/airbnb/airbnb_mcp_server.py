from fastmcp import FastMCP
from airbnb import Airbnb

# Create the MCP Server
mcp = FastMCP("Airbnb-Booking-MCP", host="127.0.0.1", port=8003)

@mcp.tool()
def fetch_hotel_prices(city: str, date: str) -> str:
    """
    Description:
        Search for available hotels and their prices in a specific city and date on Airbnb.
    
    Args:
        city (str): The name of the city (e.g., 'Mumbai', 'Goa').
        date (str): The check-in date in YYYY-MM-DD format (e.g., '2025-01-01').
        
    Returns:
        str: A list of hotels and their rates, or an error message.
    """
    airbnb_object = Airbnb()
    response = airbnb_object.get_hotel_prices(city=city, date=date)
    return response

if __name__ == "__main__":
    mcp.run(transport="streamable-http")