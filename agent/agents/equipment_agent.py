from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.tools.equipment_tool import get_equipment_recommendations
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

equipment_agent = LlmAgent(
    name="equipment_agent",
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    tools=[get_equipment_recommendations],
    instruction=(
        "Tu recommandes l'équipement audio/vidéo. "
        "Demande/extrais le nombre de participants, si des personnes sont à distance, et si la salle a de la visio. "
        "Appelle get_equipment_recommendations(participants, remote_attendees, has_room_video) et résume la liste."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
