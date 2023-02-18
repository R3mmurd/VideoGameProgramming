from pathlib import Path
import json


class JsonSceneLoader:
    FILE_EXT = "json"

    def __init__(self) -> None:
        self.height = None
        self.width = None
        self.tilewidth = None
        self.tileheight = None
        self.first_ids = {}

    def load(self, scene: any, scene_path: Path) -> None:
        with open(f"{scene_path}.{self.FILE_EXT}", "r") as f:
            obj = json.load(f)

        self.width = int(obj["map"]["width"])
        self.height = int(obj["map"]["height"])
        self.tilewidth = int(obj["map"]["tilewidth"])
        self.tileheight = int(obj["map"]["tileheight"])

        for tileset in obj["map"]["tileset"]:
            name = Path(tileset["source"]).stem
            self.first_ids[name] = int(tileset["firstgid"])

        for group in obj["map"]["group"]:
            group_name = group["name"]
            getattr(self, f"load_{group_name}")(scene, group)

    def load_tilemap(self, scene: any, group: dict[str, any]) -> None:
        scene.tilemap.update({"rows": self.height, "cols": self.width, "layers": []})

        for layer in group["layer"]:
            l = [[None for _ in range(self.width)] for _ in range(self.height)]
            data = [
                line for line in layer["data"]["text"].splitlines() if len(line) > 0
            ]
            for i in range(self.height):
                line = [s for s in data[i].split(",") if len(s) > 0]
                for j in range(self.width):
                    frame_index = int(line[j]) - self.first_ids["tiles"]
                    l[i][j] = {
                        "position": (j * self.tilewidth, i * self.tileheight),
                        "frame_index": frame_index,
                    }

            scene.tilemap["layers"].append(l)

    def load_items(self, scene: any, group: dict[str, any]) -> None:
        layer = group["layer"]
        data = [line for line in layer["data"]["text"].splitlines() if len(line) > 0]
        for i in range(self.height):
            line = [s for s in data[i].split(",") if len(s) > 0]
            for j in range(self.width):
                value = int(line[j])

                if value == 0:
                    continue

                scene.items.append(
                    {
                        "position": (j * self.tilewidth, i * self.tileheight),
                        "frame_index": value - self.first_ids["tiles"],
                    }
                )

    def load_creatures(self, scene: any, group: dict[str, any]) -> None:
        layer = group["layer"]
        data = [line for line in layer["data"]["text"].splitlines() if len(line) > 0]
        for i in range(self.height):
            line = [s for s in data[i].split(",") if len(s) > 0]
            for j in range(self.width):
                value = int(line[j])

                if value == 0:
                    continue

                scene.creatures.append(
                    {
                        "position": (j * self.tilewidth, i * self.tileheight),
                        "frame_index": value - self.first_ids["creatures"],
                    }
                )
