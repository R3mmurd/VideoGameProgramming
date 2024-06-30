import pygame

import settings


class Scene:
    def __init__(self) -> None:
        self.level = 1
        self.tilemap = {}
        self.items = []
        self.creatures = []
        settings.SceneLoader().load(self, settings.build_scene_path(self.level))

    def render(self, surface: pygame.Surface) -> None:
        for layer in self.tilemap["layers"]:
            for i in range(self.tilemap["rows"]):
                for j in range(self.tilemap["cols"]):
                    surface.blit(
                        settings.TEXTURES["tiles"],
                        layer[i][j]["position"],
                        settings.FRAMES["tiles"][layer[i][j]["frame_index"]],
                    )

        for item in self.items:
            surface.blit(
                settings.TEXTURES["tiles"],
                item["position"],
                settings.FRAMES["tiles"][item["frame_index"]],
            )

        for creature in self.creatures:
            surface.blit(
                settings.TEXTURES["creatures"],
                creature["position"],
                settings.FRAMES["creatures"][creature["frame_index"]],
            )
