from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.tools.invite_tool import create_ics_event
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

invites_agent = LlmAgent(
    name="invites_agent",
model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    tools=[create_ics_event],
    instruction=(
        "Tu génères l'invitation calendrier. "
        "Demande/extrais le titre (summary), start_iso, end_iso, location, description, organizer et une liste d'emails. "
        "Appelle create_ics_event(summary, start_iso, end_iso, location, description, organizer, attendees). "
        "Retourne l'ICS (bloc texte) et rappelle brièvement les infos principales."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
