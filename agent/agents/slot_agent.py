from google.adk.agents.llm_agent import Agent
from agent.tools.calendar_tool import find_common_slots

slot_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="slot_agent",
    description="Proposes 2-3 meeting time options within the provided window and duration.",
    instruction=(
        "Use the calendar tool with the provided time window and duration to generate options. "
        "Return a short list of 2-3 ISO timestamps (start and end) and highlight the recommended option."
    ),
    tools=[find_common_slots],
)
