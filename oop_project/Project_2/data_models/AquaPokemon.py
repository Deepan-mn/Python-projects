from __future__ import annotations

from typing import List, Tuple

from oop_project.Project_2.data_models.PokeType import PokeType
from oop_project.Project_2.data_models.Pokemon import Pokemon


class AquaPokemon(Pokemon):
    def __init__(self, name: str, pokedexId: str, level: int, living_points: int, attacking_points: int,
                 defense_points: int, attack: List[Tuple[str, int]]):
        super().__init__(name, pokedexId, level, living_points, attacking_points, defense_points, attack)
        self.type : PokeType = PokeType(0)

    def levelup(self) -> Pokemon:
        pass