from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.tools.validator_tool import validate_contact
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

participants_agent = LlmAgent(
    name="participants_agent",
model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    tools=[validate_contact],
    instruction=(
        "Tu gères la liste des participants. Demande/extrais les noms, emails et rôles. "
        "Valide les emails via validate_contact(email). "
        "Produit une liste structurée (nom, email, rôle) et un résumé en bullet points."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
