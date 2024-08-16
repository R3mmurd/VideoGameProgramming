"""
ISPPV1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class TmxLevelLoader.
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from src.Tilemap import Tilemap


class TmxLevelLoader:
    FILE_EXT = "tmx"

    def __init__(self) -> None:
        self.height = None
        self.width = None
        self.tilewidth = None
        self.tileheight = None
        self.first_ids = {}

    def load(self, level: Any, level_path: Path) -> None:
        tree = ET.parse(f"{level_path}.{self.FILE_EXT}")
        root = tree.getroot()

        self.width = int(root.attrib["width"])
        self.height = int(root.attrib["height"])
        self.tilewidth = int(root.attrib["tilewidth"])
        self.tileheight = int(root.attrib["tileheight"])

        for tileset in root.findall("tileset"):
            name = Path(tileset.attrib["source"]).stem
            self.first_ids[name] = int(tileset.attrib["firstgid"])

        for group in root.findall("group"):
            group_name = group.attrib["name"]
            getattr(self, f"load_{group_name}")(level, group)

    def load_tilemap(self, level: Any, group: ET.Element) -> None:
        tilemap = Tilemap(self.height, self.width, self.tilewidth, self.tileheight)

        for layer in group.findall("layer"):
            tilemap.create_layer()
            data = [
                line for line in layer.find("data").text.splitlines() if len(line) > 0
            ]
            for i in range(self.height):
                line = [s for s in data[i].split(",") if len(s) > 0]
                for j in range(self.width):
                    frame_index = int(line[j]) - self.first_ids["tiles"]
                    tilemap.set_new_tile(i, j, frame_index)

        level.tilemap = tilemap

    def load_items(self, level: Any, group: ET.Element) -> None:
        layer = group.find("layer")
        item_name = layer.attrib["name"]
        data = [line for line in layer.find("data").text.splitlines() if len(line) > 0]
        for i in range(self.height):
            line = [s for s in data[i].split(",") if len(s) > 0]
            for j in range(self.width):
                value = int(line[j])

                if value == 0:
                    continue

                frame_index = value - self.first_ids["tiles"]

                level.add_item(
                    {
                        "item_name": item_name,
                        "frame_index": frame_index,
                        "x": j * self.tilewidth,
                        "y": i * self.tileheight,
                        "width": self.tilewidth,
                        "height": self.tileheight,
                    }
                )

    def load_creatures(self, level: Any, group: ET.Element) -> None:
        layer = group.find("layer")
        data = [line for line in layer.find("data").text.splitlines() if len(line) > 0]
        for i in range(self.height):
            line = [s for s in data[i].split(",") if len(s) > 0]
            for j in range(self.width):
                value = int(line[j])

                if value == 0:
                    continue

                frame_index = value - self.first_ids["creatures"]

                level.add_creature(
                    {
                        "tile_index": frame_index,
                        "x": j * self.tilewidth,
                        "y": i * self.tileheight,
                        "width": self.tilewidth,
                        "height": self.tileheight,
                    }
                )
