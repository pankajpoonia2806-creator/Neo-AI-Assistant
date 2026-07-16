from memory import Memory
from memory_manager import MemoryManager

class MemoryHandler:
    def __init__(self):
        self.memory = Memory()
        self.memory_manager = MemoryManager(self.memory)

    def handle(self, user_input):
        return None