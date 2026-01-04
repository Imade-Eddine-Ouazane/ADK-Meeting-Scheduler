from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.tools.validator_tool import validate_contact
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

intake_validator_agent = LlmAgent(
    name="intake_validator_agent",
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    tools=[validate_contact],
    instruction=(
        "Tu vérifies la complétude de l'intake de réunion. "
        "Assure-toi d'avoir: objectif, participants (noms/emails), ville, fenêtre temporelle ISO (start/end), durée (minutes), contraintes. "
        "Utilise validate_contact(email) pour vérifier les emails. "
        "Pose uniquement les questions manquantes et fournis un récapitulatif concis (bullet points) et un JSON minimal."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
