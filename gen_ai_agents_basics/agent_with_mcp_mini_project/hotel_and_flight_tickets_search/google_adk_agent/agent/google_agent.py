# from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams
# from langchain_openai import ChatOpenAI
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import os
import asyncio
import litellm # Import to handle the cleanup
from dotenv import load_dotenv
# Load .env values
load_dotenv()


# 2. Define your MCP Server inputs
# Assuming your servers are running at these addresses
mcp_servers = [
    {"name": "Airbnb-MCP", "url": "http://localhost:8003/mcp"},
    {"name": "EaseMyTrip-MCP", "url": "http://localhost:8001/mcp"},
    {"name": "MakeMyTrip-MCP", "url": "http://localhost:8002/mcp"}
]

model_name = f"openai/{os.getenv('LLM_MODEL_NAME')}"

llm_object = LiteLlm(
        model = model_name,
        api_key = os.getenv("LLM_API_KEY"),
        # base_url = os.getenv("LLM_URL") # Uncomment and set if using a custom base URL
    )

# Initialize toolsets for each MCP server
# The ADK automatically fetches tool definitions from these URLs
toolsets = []
for config in mcp_servers:
     toolset = McpToolset(
          connection_params=StreamableHTTPConnectionParams(url=config["url"])
     )
     toolsets.append(toolset)

travel_agent = LlmAgent(
     name="travel_agent",
     model = llm_object,
     description=(
        "Agent to assist users with travel-related queries such as flight bookings, hotel reservations."
     ),
     instruction="""
        You are a comprehensive travel assistant. 
        You have access to different booking vendors like Airbnb, EaseMyTrip, and MakeMyTrip.
        When a user asks for travel options, use these tools to find the best 
        accommodations and flights. Compare results and give a concise summary.
        """,
     tools=toolsets

)
APP_NAME="google_search_agent"
USER_ID="user1234"
SESSION_ID="1234"

# Session and Runner
async def setup_session_and_runner():
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    runner = Runner(agent=travel_agent, app_name=APP_NAME, session_service=session_service)
    return session, runner

# Agent Interaction
async def call_agent_async(query):
    content = types.Content(role='user', parts=[types.Part(text=query)])
    session, runner = await setup_session_and_runner()
    events = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)

# Note: In Colab, you can directly use 'await' at the top level.
# If running this code as a standalone Python script, you'll need to use asyncio.run() or manage the event loop.
asyncio.run(call_agent_async("I need a flight from Delhi to Mumbai on 2025-01-01 and a hotel in Mumbai for 2025-01-02."))

# async def main():
#     try:
#         query = "Find me a flight from Delhi to Mumbai on 2025-01-01 and a hotel in Mumbai."
#         await call_agent_async(query)
#     finally:
#         # This resolves the 'close_litellm_async_clients' warning
#         print("\nCleaning up connections...")
#         await litellm.aclosing_httpx_client()

# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         pass