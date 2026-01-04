from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.tools.budget_policy_tool import check_budget_policy
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

budget_policy_agent = LlmAgent(
    name="budget_policy_agent",
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    tools=[check_budget_policy],
    instruction=(
        "Tu contrôles la conformité budgétaire. "
        "Extrais participants, total_eur et, si disponibles, max_pp_eur et max_total_eur. "
        "Appelle check_budget_policy(participants, total_eur, max_pp_eur, max_total_eur). "
        "Si le statut est 'fail', explique brièvement les écarts et propose 2-3 pistes d'optimisation (réduire traiteur, équipement, salle). "
        "Retourne un court résumé + le JSON du tool."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
