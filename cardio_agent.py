# multi_agent_diagnosis/app/agents/cardio_agent.py

from app.agents.base_agent import BaseAgent
from app.services.gemini_service import GeminiService

class CardioAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="CardioAgent", specialty="Cardiology")
        self.llm = GeminiService()

    def process(self, user_message: str) -> str:
        msg = user_message.lower()
        
        keywords = [
            "chest pain",
            "chest tightness",
            "palpitations",
            "shortness of breath",
            "heart racing",
            "pressure in chest",
            "left arm pain",
            "sweating with chest pain"
        ]

        # Check if any keyword exists
        if any(k in msg for k in keywords):
            # Create a specialized prompt for cardiology
            prompt = f"""
            A patient reports the following symptoms: "{user_message}"

            You are a cardiologist. Please:
            - Explain possible cardiac causes in clear language
            - Highlight warning signs that require emergency care
            - Advise on next steps for the patient
            """
            llm_reply = self.llm.chat(prompt)
            
            return f"[{self.name}] {llm_reply}"
        
        else:
            return f"[{self.name}] I specialize in {self.specialty}. You said: {user_message}"
