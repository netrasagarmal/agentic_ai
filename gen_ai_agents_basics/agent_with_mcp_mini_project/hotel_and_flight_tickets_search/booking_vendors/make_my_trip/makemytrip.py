class MakeMyTripSystem:
    def __init__(self):
        # Structure: { (Boarding, Destination): { "YYYY-MM-DD": Price } }
        self._fares = {
            ("Delhi", "Mumbai"): {
                "2025-01-01": 2500,
                "2025-01-02": 3000,
                "2025-01-03": 3800
            },
            ("Mumbai", "Delhi"): {
                "2025-01-01": 1200,
                "2025-01-02": 2100,
                "2025-01-03": 2900
            },
            ("Mumbai", "Pune"): {
                "2025-01-01": 1100,
                "2025-01-02": 1000,
                "2025-01-03": 900
            },
            ("Pune", "Delhi"): {
                "2025-01-01": 5000,
                "2025-01-02": 4800,
                "2025-01-03": 4500
            }
        }
        self._inventory = {
                "Mumbai": {
                    "2025-01-01": [
                        {"hotel": "Taj Mahal Palace", "rate": 21000, "currency": "INR"},
                        {"hotel": "Ibis Airport", "rate": 4000, "currency": "INR"}
                    ],
                    "2025-01-02": [
                        {"hotel": "Taj Mahal Palace", "rate": 20000, "currency": "INR"},
                        {"hotel": "Ibis Airport", "rate": 4200, "currency": "INR"}
                    ],
                    "2025-01-03": [
                        {"hotel": "Taj Mahal Palace", "rate": 19000, "currency": "INR"},
                        {"hotel": "Ibis Airport", "rate": 3000, "currency": "INR"}
                    ]
                },
                "Delhi": {
                    "2025-01-01": [
                        {"hotel": "The Oberoi", "rate": 19000, "currency": "INR"},
                        {"hotel": "Red Fox Hotel", "rate": 3500, "currency": "INR"}
                    ],
                    "2025-01-02": [
                        {"hotel": "The Oberoi", "rate": 18000, "currency": "INR"},
                        {"hotel": "Red Fox Hotel", "rate": 3700, "currency": "INR"}
                    ],
                    "2025-01-03": [
                        {"hotel": "The Oberoi", "rate": 16500, "currency": "INR"},
                        {"hotel": "Red Fox Hotel", "rate": 3500, "currency": "INR"}
                    ]
                },
                "Pune": {
                    "2025-01-01": [
                        {"hotel": "W Goa", "rate": 32000, "currency": "INR"},
                        {"hotel": "Lemon Tree", "rate": 6200, "currency": "INR"},
                        {"hotel": "Zostel", "rate": 1400, "currency": "INR"}
                    ],
                    "2025-01-02": [
                        {"hotel": "W Goa", "rate": 31000, "currency": "INR"},
                        {"hotel": "Lemon Tree", "rate": 4500, "currency": "INR"},
                        {"hotel": "Zostel", "rate": 1100, "currency": "INR"}
                    ],
                    "2025-01-03": [
                        {"hotel": "W Goa", "rate": 28500, "currency": "INR"},
                        {"hotel": "Lemon Tree", "rate": 5200, "currency": "INR"}
                    ]
                }
            }

    def get_hotel_prices(self, city: str, date: str) -> str:
        """
        Queries the inventory for hotels in a city on a specific date.
        """
        city_data = self._inventory.get(city.strip().title())
        if not city_data:
            return f"Error: We currently only serve Mumbai, Delhi, and Goa."
        
        hotels = city_data.get(date)
        if not hotels:
            return f"Error: No data found for {date}. Try 2025-01-01 to 2025-01-03."
        
        # Format the response for the Agent
        response = f"Found {len(hotels)} hotels in {city} for {date}:\n"
        for h in hotels:
            response += f"- {h['hotel']}: {h['currency']} {h['rate']}\n"
        return response

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
            return f"MakeMyTrip: The fare from {route[0]} to {route[1]} on {travel_date} is ₹{fare}."
        else:
            return f"No flights available on {travel_date}. Available dates: {', '.join(route_data.keys())}."


if __name__ == "__main__":
    
    # Instantiate for use in the MCP
    mmt_instance = MakeMyTripSystem()
    print(mmt_instance.get_flight_prices("Delhi", "Mumbai", "2025-01-02"))