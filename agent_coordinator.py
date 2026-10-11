# multi_agent_diagnosis/app/agents/agent_coordinator.py

from app.agents.cardio_agent import CardioAgent
from app.agents.neuro_agent import NeuroAgent
from app.agents.hypertension_agent import HypertensionAgent

class AgentCoordinator:
    def __init__(self):
        self.agents = [
            CardioAgent(),
            NeuroAgent(),
            HypertensionAgent(),
        ]

    def run_all(self, user_message: str) -> str:
        """
        Run all agents on the same user message and combine meaningful responses.
        """

        responses = []

        for agent in self.agents:
            result = agent.process(user_message)

            # Only include meaningful replies, skip generic fallback responses
            if not result.lower().startswith(f"[{agent.name.lower()}] i specialize"):
                responses.append(result.strip())

        if responses:
            combined = "\n\n---\n\n".join(responses)
            return f" AI Diagnostic Summary:\n\n{combined}"
        else:
            return (
                "🩺 Sorry, no specific diagnostic matches were found.\n"
                "Please describe your symptoms in more detail so we can better assist you."
            )
