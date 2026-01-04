from google.adk.agents.llm_agent import Agent
from agent.tools.validator_tool import validate_contact

intake_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="intake_agent",
    description="Collects meeting goal, participants, time window, duration, city and constraints.",
    instruction=(
        "Ask concise questions to gather meeting purpose, list of participants and their emails, "
        "preferred city, time window (start/end), and desired duration in minutes. "
        "Validate contact details if provided. Summarize the collected info in bullet points and confirm readiness."
    ),
    tools=[validate_contact],
)
