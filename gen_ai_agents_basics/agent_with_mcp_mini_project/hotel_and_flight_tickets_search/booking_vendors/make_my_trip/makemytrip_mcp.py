from fastmcp import FastMCP
from makemytrip import MakeMyTripSystem

# Initialize the MCP Server
mcp = FastMCP("MakeMyTrip-Booking-System", host="127.0.0.1", port=8002)

@mcp.tool()
def fetch_flight_prices(boarding: str, destination: str, travel_date: str) -> str:
    """
    Description:
        Get the ticket fare between two cities from MakeMyTrip.
    
    Args:
        boarding (str): The departure city (e.g., 'Delhi', 'Mumbai').
        destination (str): The arrival city (e.g., 'Pune', 'Delhi').
        travel_date (str): The date of travel in 'YYYY-MM-DD' format.
        
    Returns:
        str: The fare information or an error message if route not found.
    """
    # Calling the internal class method
    mmt_object = MakeMyTripSystem()
    response = mmt_object.get_flight_prices(boarding=boarding, destination=destination, travel_date=travel_date)
    return response

@mcp.tool()
def fetch_hotel_prices(city: str, date: str) -> str:
    """
    Description:
        Search for available hotels and their prices in a specific city and date on MakeMyTrip.
    
    Args:
        city (str): The name of the city (e.g., 'Mumbai', 'Goa').
        date (str): The check-in date in YYYY-MM-DD format (e.g., '2025-01-01').
        
    Returns:
        str: A list of hotels and their rates, or an error message.
    """
    mmt_object = MakeMyTripSystem()
    response = mmt_object.get_hotel_prices(city=city, date=date)
    return response

if __name__ == "__main__":
    mcp.run(transport="streamable-http")