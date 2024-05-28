from pathlib import Path
import xml.etree.ElementTree as ET


class TmxSceneLoader:
    FILE_EXT = "tmx"

    def __init__(self) -> None:
        self.height = None
        self.width = None
        self.tilewidth = None
        self.tileheight = None
        self.first_ids = {}

    def load(self, scene: any, scene_path: Path) -> None:
        tree = ET.parse(f"{scene_path}.{self.FILE_EXT}")
        root = tree.getroot()

        self.width = int(root.attrib["width"])
        self.height = int(root.attrib["height"])
        self.tilewidth = int(root.attrib["tilewidth"])
        self.tileheight = int(root.attrib["tileheight"])

        for child in root.findall("tileset"):
            name = Path(child.attrib["source"]).stem
            self.first_ids[name] = int(child.attrib["firstgid"])

        for child in root.findall("group"):
            group_name = child.attrib["name"]
            getattr(self, f"load_{group_name}")(scene, child)

    def load_tilemap(self, scene: any, group: ET.Element) -> None:
        scene.tilemap.update({"rows": self.height, "cols": self.width, "layers": []})

        for layer in group.findall("layer"):
            l = [[None for _ in range(self.width)] for _ in range(self.height)]
            data = [
                line for line in layer.find("data").text.splitlines() if len(line) > 0
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

    def load_items(self, scene: any, group: ET.Element) -> None:
        layer = group.find("layer")
        data = [line for line in layer.find("data").text.splitlines() if len(line) > 0]
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

    def load_creatures(self, scene: any, group: ET.Element) -> None:
        layer = group.find("layer")
        data = [line for line in layer.find("data").text.splitlines() if len(line) > 0]
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
