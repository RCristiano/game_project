from typing import  Protocol


class Entity(Protocol):
    def update(self):
        """Update the entity"""