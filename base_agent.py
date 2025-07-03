# multi_agent_diagnosis/app/agents/base_agent.py

from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Abstract base class for all medical diagnostic agents.
    """

    def __init__(self, name: str, specialty: str):
        self.name = name
        self.specialty = specialty

    @abstractmethod
    def process(self, user_message: str) -> str:
        """
        Process the user's message and return a response.
        Must be implemented by subclasses.
        """
        pass
