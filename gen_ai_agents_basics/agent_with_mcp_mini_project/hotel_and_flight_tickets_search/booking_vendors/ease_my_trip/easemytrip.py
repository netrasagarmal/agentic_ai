class EaseMyTripSystem:
    def __init__(self):
        # Structure: { (Boarding, Destination): { "YYYY-MM-DD": Price } }
        self._fares = {
            ("Delhi", "Mumbai"): {
                "2025-01-01": 5500,
                "2025-01-02": 5000,
                "2025-01-03": 4800
            },
            ("Mumbai", "Delhi"): {
                "2025-01-01": 5200,
                "2025-01-02": 5100,
                "2025-01-03": 4900
            },
            ("Mumbai", "Pune"): {
                "2025-01-01": 1200,
                "2025-01-02": 1100,
                "2025-01-03": 1000
            },
            ("Pune", "Delhi"): {
                "2025-01-01": 6000,
                "2025-01-02": 5800,
                "2025-01-03": 5500
            }
        }

    def get_flight_prices(self, boarding: str, destination: str, travel_date: str) -> str:
        """
        Retrieves the fare for a specific route and date.
        """
        route = (boarding.strip().title(), destination.strip().title())
        
        # Check if the route exists
        route_data = self._fares.get(route)
        if not route_data:
            return f"Sorry, no flights found from {boarding} to {destination}."
        
        # Check if the date exists for that route
        fare = route_data.get(travel_date)
        if fare:
            return f"EaseMyTrip: The fare from {route[0]} to {route[1]} on {travel_date} is ₹{fare}."
        else:
            return f"No flights available on {travel_date}. Available dates: {', '.join(route_data.keys())}."


if __name__ == "__main__":
    
    # Instantiate for use in the MCP
    emt_instance = EaseMyTripSystem()
    print(emt_instance.get_flight_prices("Delhi", "Mumbai", "2025-01-02"))