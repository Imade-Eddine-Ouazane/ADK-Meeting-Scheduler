from google.adk.agents import SequentialAgent
from agent.agents.intake_agent import intake_agent
from agent.agents.slot_agent import slot_agent
from agent.agents.room_agent import room_agent
from agent.agents.agenda_agent import agenda_agent
from agent.agents.followups_agent import followups_agent
from agent.agents.meteo_agent import agent_meteo
from agent.agents.participants_agent import participants_agent
from agent.agents.equipment_agent import equipment_agent
from agent.agents.catering_agent import catering_agent
from agent.agents.invites_agent import invites_agent
from agent.agents.budget_agent import budget_agent
from agent.agents.minutes_agent import minutes_agent


def build_root_agent() -> SequentialAgent:
    intake = intake_agent.clone()
    participants = participants_agent.clone()
    slots = slot_agent.clone()
    meteo = agent_meteo.clone()
    rooms = room_agent.clone()
    equipment = equipment_agent.clone()
    catering = catering_agent.clone()
    agenda = agenda_agent.clone()
    invites = invites_agent.clone()
    budget = budget_agent.clone()
    followups = followups_agent.clone()
    minutes = minutes_agent.clone()
    return SequentialAgent(
        name="meeting_scheduler",
        description=(
            "Multi-agent assistant to schedule meetings: intake, participants, slots, weather, rooms, "
            "equipment, catering, agenda, invites, budget, follow-ups, minutes."
        ),
        sub_agents=[
            intake,
            participants,
            slots,
            meteo,
            rooms,
            equipment,
            catering,
            agenda,
            invites,
            budget,
            followups,
            minutes,
        ],
    )


root_agent = build_root_agent()
