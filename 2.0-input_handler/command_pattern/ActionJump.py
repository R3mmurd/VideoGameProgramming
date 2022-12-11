
from Action import Action
from Actor import Actor

class ActionJump(Action):
    def execute(self, target: Actor) -> None:
        print(f"{target} jumps")
