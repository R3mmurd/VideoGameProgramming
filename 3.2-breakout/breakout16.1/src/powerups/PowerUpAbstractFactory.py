from gale.factory import Factory

import sys


class PowerUpAbstractFactory:
    @staticmethod
    def get_factory(powerup_class_name: str) -> Factory:
        module_name = ".".join(__name__.split(".")[:-1])
        powerup_class = getattr(
            sys.modules[f"{module_name}.{powerup_class_name}"], powerup_class_name
        )

        if powerup_class is None:
            raise ValueError(f"Class {powerup_class_name} does not exist")

        return Factory(powerup_class)
