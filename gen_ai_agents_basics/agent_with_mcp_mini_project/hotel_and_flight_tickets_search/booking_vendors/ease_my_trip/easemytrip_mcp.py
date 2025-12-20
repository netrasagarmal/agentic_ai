from fastmcp import FastMCP
from easemytrip import EaseMyTripSystem

# Initialize the MCP Server
mcp = FastMCP("EaseMyTrip-Booking-System", host="127.0.0.1", port=8001)

@mcp.tool()
def fetch_flight_prices(boarding: str, destination: str, travel_date: str) -> str:
    """
    Description:
          Get the ticket fare between two cities from EaseMyTrip.
    
    Args:
        boarding (str): The departure city (e.g., 'Delhi', 'Mumbai').
        destination (str): The arrival city (e.g., 'Pune', 'Delhi').
        travel_date (str): The date of travel in 'YYYY-MM-DD' format.
        
    Returns:
        str: The fare information or an error message if route not found.
    """
    # Calling the internal class method
    emt_object = EaseMyTripSystem()
    response = emt_object.get_fare(boarding=boarding, destination=destination, travel_date=travel_date)
    return response

if __name__ == "__main__":
    mcp.run(transport="streamable-http")