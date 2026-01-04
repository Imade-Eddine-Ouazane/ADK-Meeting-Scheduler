from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

minutes_agent = LlmAgent(
    name="minutes_agent",
model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    instruction=(
        "Tu rédiges le compte-rendu (minutes) de la réunion. "
        "Si un transcript est fourni (texte brut), synthétise en sections: Participants, Décisions, Actions, Prochains jalons. "
        "Sinon, génère un modèle de compte-rendu clair et concis à remplir."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
