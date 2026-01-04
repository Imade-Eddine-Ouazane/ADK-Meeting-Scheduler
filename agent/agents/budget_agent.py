from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.tools.budget_tool import estimate_budget
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

budget_agent = LlmAgent(
    name="budget_agent",
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    tools=[estimate_budget],
    instruction=(
        "Tu estimes le budget de la réunion. "
        "Demande/extrais: participants, catering_pp_eur, room_cost_eur, equipment_cost_eur, other_costs_eur. "
        "Appelle estimate_budget(participants, catering_pp_eur, room_cost_eur, equipment_cost_eur, other_costs_eur) et résume le total et le détail."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
