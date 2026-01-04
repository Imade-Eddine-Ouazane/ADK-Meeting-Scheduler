from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.tools.catering_tool import find_catering
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

catering_agent = LlmAgent(
    name="catering_agent",
model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    tools=[find_catering],
    instruction=(
        "Tu proposes des options traiteur. "
        "Demande/extrais la ville, préférences (diet: standard/vegetarian/vegan/gluten-free), et budget par personne. "
        "Appelle find_catering(city, diet, max_per_person_eur) et rends 2-3 options."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
