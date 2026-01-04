from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.tools.budget_tool import estimate_budget
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

budget_scenarios_agent = LlmAgent(
    name="budget_scenarios_agent",
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    tools=[estimate_budget],
    instruction=(
        "Tu proposes 3 scénarios de budget (léger, standard, premium). "
        "Si l'utilisateur fournit des coûts (catering_pp_eur, room_cost_eur, equipment_cost_eur, other_costs_eur), utilise-les. "
        "Sinon, suggère des hypothèses raisonnables: léger (10€/pp catering), standard (15€/pp), premium (25€/pp) et ajuste room/equipment/other selon le contexte. "
        "Appelle estimate_budget(...) séparément pour chaque scénario et rends un tableau comparatif avec total_eur et un bref commentaire."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
