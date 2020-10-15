from __future__ import annotations

from .chunk_world import ChunkWorld
from amulet.api.wrapper import WorldFormatWrapper


class World(ChunkWorld):
    """
    Class that handles world editing of any world format via an separate and flexible data format
    """

    def __init__(
        self, directory: str, world_wrapper: WorldFormatWrapper, temp_dir: str = None
    ):
        assert isinstance(world_wrapper, WorldFormatWrapper)
        super().__init__(directory, world_wrapper, temp_dir)

    @property
    def world_wrapper(self) -> WorldFormatWrapper:
        return self._format_wrapper
