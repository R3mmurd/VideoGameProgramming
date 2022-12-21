from Action import Action
from Actor import Actor

class ActionShoot(Action):
    def execute(self, target: Actor) -> None:
        print(f"{target} shoots")
