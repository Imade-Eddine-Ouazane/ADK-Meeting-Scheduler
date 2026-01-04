from google.adk.agents.llm_agent import Agent

agenda_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="agenda_agent",
    description="Drafts a concise agenda and roles based on meeting purpose.",
    instruction=(
        "Produce a timeboxed agenda with objectives, owners and expected outcomes. Keep it brief and actionable."
    ),
)
