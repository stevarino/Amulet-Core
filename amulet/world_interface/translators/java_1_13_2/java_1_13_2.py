from __future__ import annotations

from typing import Tuple, Union

from amulet.world_interface.translators import Translator


class Java_1_13_2_Translator(Translator):
    def _translator_key(self, version_number: int) -> Tuple[str, Union[int, Tuple[int, int, int]]]:
        return "java", version_number

    @staticmethod
    def is_valid(key):
        if key[0] != "anvil":
            return False
        if key[1] < 1444:
            return False
        return True


TRANSLATOR_CLASS = Java_1_13_2_Translator
