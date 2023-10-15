from __future__ import annotations
from Pokemon import Pokemon
from typing import List, Tuple


class GrassPokemon(Pokemon):
    def __init__(self, name: str, pokedexId: str, level: int, living_points: int, attacking_points: int,
                 defense_points: int, attack: List[Tuple[str, int]]):
        super().__init__(name, pokedexId, level, living_points, attacking_points, defense_points, attack)
        self.type: PokeType = PokeType(2)
    def levelup(self) -> Pokemon:
        pass