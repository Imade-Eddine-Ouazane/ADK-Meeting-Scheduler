from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agent.tools.meteo_tool import get_weather_tool
from agent.callbacks.log_callbacks import (
    before_agent, after_agent,
    before_model, after_model,
    before_tool, after_tool,
)

agent_meteo = LlmAgent(
    name="agent_meteo",
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    tools=[get_weather_tool],
    instruction=(
        "Tu es l'agent météo. "
        "Demande/extrais la ville et la date (YYYY-MM-DD), puis appelle get_weather_tool(city, date). "
        "Après le tool, résume la météo en 1 phrase."
    ),
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
