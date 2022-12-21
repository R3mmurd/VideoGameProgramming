# The class Action is the interface for the commnand

from Actor import Actor

class Action:
    def execute(self, target: Actor) -> None:
        raise NotImplementedError()
