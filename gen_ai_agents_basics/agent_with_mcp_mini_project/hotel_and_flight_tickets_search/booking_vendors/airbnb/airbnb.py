class Airbnb:
    def __init__(self):
        # Data Structure: { City: { Date: [ {Hotel Info}, ... ] } }
        self._inventory = {
            "Mumbai": {
                "2025-01-01": [
                    {"hotel": "Taj Mahal Palace", "rate": 25000, "currency": "INR"},
                    {"hotel": "Ibis Airport", "rate": 5000, "currency": "INR"}
                ],
                "2025-01-02": [
                    {"hotel": "Taj Mahal Palace", "rate": 22000, "currency": "INR"},
                    {"hotel": "Ibis Airport", "rate": 4500, "currency": "INR"}
                ],
                "2025-01-03": [
                    {"hotel": "Taj Mahal Palace", "rate": 20000, "currency": "INR"},
                    {"hotel": "Ibis Airport", "rate": 4000, "currency": "INR"}
                ]
            },
            "Delhi": {
                "2025-01-01": [
                    {"hotel": "The Oberoi", "rate": 18000, "currency": "INR"},
                    {"hotel": "Red Fox Hotel", "rate": 3500, "currency": "INR"}
                ],
                "2025-01-02": [
                    {"hotel": "The Oberoi", "rate": 17000, "currency": "INR"},
                    {"hotel": "Red Fox Hotel", "rate": 3200, "currency": "INR"}
                ],
                "2025-01-03": [
                    {"hotel": "The Oberoi", "rate": 16000, "currency": "INR"},
                    {"hotel": "Red Fox Hotel", "rate": 3000, "currency": "INR"}
                ]
            },
            "Pune": {
                "2025-01-01": [
                    {"hotel": "W Goa", "rate": 35000, "currency": "INR"},
                    {"hotel": "Lemon Tree", "rate": 6000, "currency": "INR"},
                    {"hotel": "Zostel", "rate": 1200, "currency": "INR"}
                ],
                "2025-01-02": [
                    {"hotel": "W Goa", "rate": 30000, "currency": "INR"},
                    {"hotel": "Lemon Tree", "rate": 5500, "currency": "INR"},
                    {"hotel": "Zostel", "rate": 1000, "currency": "INR"}
                ],
                "2025-01-03": [
                    {"hotel": "W Goa", "rate": 28000, "currency": "INR"},
                    {"hotel": "Lemon Tree", "rate": 5000, "currency": "INR"}
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

if __name__ == "__main__":
    
     # Instantiate the system
     hotel_system = Airbnb()
     # Example query
     print(hotel_system.get_hotel_prices("Mumbai", "2025-01-01"))