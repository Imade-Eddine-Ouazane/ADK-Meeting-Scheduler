from google.adk.agents.llm_agent import Agent

followups_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="followups_agent",
    description="Generates follow-up tasks and a short email draft to participants.",
    instruction=(
        "List action items with owners and due dates. Provide a brief follow-up email summarizing decisions and next steps."
    ),
)
