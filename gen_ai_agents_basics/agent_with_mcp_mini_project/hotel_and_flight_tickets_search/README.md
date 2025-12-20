# 🌍 AI Travel Assistant: Multi-Vendor Agent (MCP & Google ADK)

A comprehensive travel booking assistant built using the **Google Agent Development Kit (ADK)** and the **Model Context Protocol (MCP)**. This agent aggregates flight and hotel data from three different simulated vendors (Airbnb, EaseMyTrip, and MakeMyTrip) to provide a unified travel planning experience.

## 📂 Project Structure

| File | Description |
| --- | --- |
| [`airbnb.py`](./booking_vendors/airbnb/airbnb.py) | The backend logic class (`Airbnb`) for providing hotels prices. |
| [`easemytrip.py`](./booking_vendors/ease_my_trip/easemytrip.py) | The backend logic class (`EaseMyTripSystem`) for providing flights prices. |
| [`makemytrip.py`](./booking_vendors/make_my_trip/makemytrip.py) | The backend logic class (`MakeMyTripSystem`) for providing flights and hotels prices. |
| [`airbnb_mcp_server.py`](./booking_vendors/airbnb/airbnb_mcp_server.py) | MCP Server providing **Hotel** prices for specific cities and dates. |
| [`easemytrip_mcp_server.py`](./booking_vendors/ease_my_trip/easemytrip_mcp.py) | MCP Server providing **Flight** fares between cities. |
| [`makemytrip_mcp_server.py`](./booking_vendors/make_my_trip/makemytrip_mcp.py) | MCP Server providing both **Flight and Hotel** price information. |
| [`mcp_client_test.py`](./mcp_client/mcp_client.py) | A standalone testing utility to verify MCP server connectivity without the LLM/Agent. |
| [`agent.py`](./google_adk_agent/agent/agent.py) | The primary Google ADK script that runs the `LlmAgent` to run using `adk web` command. |
| [`google_agent.py`](./google_adk_agent/agent/google_agent.py) | The primary Google ADK script that runs the `LlmAgent` using a `Runner` class. |
| `.env` | Stores sensitive environment variables like `LLM_API_KEY`. |

---

## 🚀 Setup & Execution

### 1. Prerequisites

* Python 3.10+
* An OpenAI API Key (used via `LiteLlm`)
* Install dependencies:

```bash
pip install google-adk litellm fastmcp python-dotenv

```

### 2. Launch the MCP Servers

The agent requires all three vendor servers to be active. Open three separate terminals and run:

* **Airbnb (Port 8003):** `python3 airbnb_mcp_server.py`
* **EaseMyTrip (Port 8001):** `python3 easemytrip_mcp_server.py`
* **MakeMyTrip (Port 8002):** `python3 makemytrip_mcp_server.py`

### 3. (Optional) Test the Servers

Before running the AI, verify the tools are reachable using the test client:

```bash
python3 mcp_client_test.py

```

### 4. Run the AI Travel Agent

Ensure your `.env` file is configured, then start the main agent:

```bash
python3 main_agent.py

```

---

## 🤖 System Capabilities

The agent is instructed to use the following toolsets to answer user queries:

1. **Airbnb-MCP:** Used exclusively for hotel comparisons.
2. **EaseMyTrip-MCP:** Used exclusively for checking flight fares.
3. **MakeMyTrip-MCP:** A versatile tool used for both flight and hotel queries.

The **LlmAgent** implements a reasoning loop. When you ask: *"Find a flight from Delhi to Mumbai and a hotel in Mumbai,"* the agent will:

1. Call `fetch_flight_prices` on EaseMyTrip or MakeMyTrip.
2. Call `fetch_hotel_prices` on Airbnb or MakeMyTrip.
3. Summarize and compare the best rates for the user.

## ⚠️ Important Implementation Notes

* **Transport:** Servers use `streamable-http` transport, making them accessible via standard HTTP requests.
* **Memory:** The project uses `InMemorySessionService`, allowing the agent to remember your travel dates across a single conversation session.

