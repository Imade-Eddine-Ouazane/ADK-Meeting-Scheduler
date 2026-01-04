from google.adk.agents.llm_agent import Agent
from agent.tools.room_tool import find_rooms

room_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="room_agent",
    description="Suggests rooms matching city, capacity and equipment needs.",
    instruction=(
        "Filter rooms by city and participant count. Prefer rooms with video if remote attendees. "
        "Present 2-3 options with name, capacity, video and notes."
    ),
    tools=[find_rooms],
)
