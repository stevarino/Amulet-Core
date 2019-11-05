from __future__ import annotations

from amulet.world_interface.chunk.translators.bedrock import BaseBedrockTranslator


class BedrockNBTBlockstateTranslator(BaseBedrockTranslator):
    @staticmethod
    def is_valid(key):
        if key[0] != "leveldb":
            return False
        if not (1, 13, 0) <= key[1]:
            return False
        return True


TRANSLATOR_CLASS = BedrockNBTBlockstateTranslator
