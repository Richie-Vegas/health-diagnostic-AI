from app.agents.base_agent import BaseAgent
from app.services.gemini_service import GeminiService

class NeuroAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="NeuroAgent", specialty="Neurology")
        self.llm = GeminiService()

    def process(self, user_message: str) -> str:
        msg = user_message.lower()
        keywords = ["headache", "dizziness", "seizure", "numbness"]

        if any(k in msg for k in keywords):
            prompt = f"""
            A patient reports the following symptoms: "{user_message}"
            As a neurologist, explain possible causes in simple terms, and advise whether they should see a doctor.
            """
            llm_reply = self.llm.chat(prompt)
            return f"[{self.name}] {llm_reply}"

        else:
            return f"[{self.name}] I specialize in {self.specialty}. You said: {user_message}"
