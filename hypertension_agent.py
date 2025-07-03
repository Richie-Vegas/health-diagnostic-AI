# multi_agent_diagnosis/app/agents/hypertension_agent.py

from app.agents.base_agent import BaseAgent
from app.services.gemini_service import GeminiService

class HypertensionAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="HypertensionAgent",
            specialty="Hypertension and blood pressure disorders"
        )
        self.llm = GeminiService()

    def process(self, user_message: str) -> str:
        msg = user_message.lower()
        keywords = [
            "high blood pressure",
            "hypertension",
            "bp",
            "pressure headache",
            "elevated blood pressure",
            "hypertensive crisis",
            "hypertensive emergency"
        ]

        if any(k in msg for k in keywords):
            # Create a specialized medical prompt
            prompt = f"""
            A patient describes the following symptoms: "{user_message}"
            
            You are a hypertension specialist. Please:
            - Explain possible causes in simple language
            - Describe any warning signs requiring urgent care
            - Provide general lifestyle recommendations for hypertension management
            """
            llm_reply = self.llm.chat(prompt)

            return f"[{self.name}] {llm_reply}"

        else:
            return f"[{self.name}] I specialize in {self.specialty}. You said: {user_message}"
