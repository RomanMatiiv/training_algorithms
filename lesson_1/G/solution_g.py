"""
https://contest.yandex.ru/contest/27393/problems/G/
"""
from dataclasses import dataclass


class WeightException(Exception):
    pass


@dataclass
class Unit:
    count: int
    unnecessary_kg: int


class MetalPipeline:
    def __init__(self, kg_metal: int, weight_work_piece: int, weight_piece: int):
        self._kg_metal = kg_metal
        self._weight_work_piece = weight_work_piece
        self._weight_piece = weight_piece

        if self._weight_work_piece < self._weight_piece:
            raise WeightException

    def _make_work_piece(self, kg_metal: int) -> Unit:
        count_work_piece = kg_metal // self._weight_work_piece
        unnecessary_metal = kg_metal % self._weight_work_piece

        unit = Unit(count=count_work_piece, unnecessary_kg=unnecessary_metal)

        return unit

    def _make_piece(self, count_work_piece: int) -> Unit:
        count_piece = self._weight_work_piece // self._weight_piece
        unnecessary_metal = self._weight_work_piece % self._weight_piece

        count_piece *= count_work_piece
        unnecessary_metal *= count_work_piece

        unit = Unit(count=count_piece, unnecessary_kg=unnecessary_metal)

        return unit

    def enough_metal(self) -> bool:
        if self._kg_metal >= self._weight_work_piece:
            return True
        else:
            return False

    def start_iteration(self) -> int:
        extracted_all_metal = self._kg_metal
        self._kg_metal = 0

        unit_stage_1 = self._make_work_piece(kg_metal=extracted_all_metal)
        self._kg_metal += unit_stage_1.unnecessary_kg

        unit_stage_2 = self._make_piece(count_work_piece=unit_stage_1.count)
        self._kg_metal += unit_stage_2.unnecessary_kg

        return unit_stage_2.count


if __name__ == "__main__":
    kg_metal, weight_work_piece, weight_piece = [int(i) for i in input().split()]

    count_item = 0
    try:
        pipe = MetalPipeline(kg_metal, weight_work_piece, weight_piece)
        while pipe.enough_metal():
            count_item += pipe.start_iteration()

    except WeightException:
        pass

    print(count_item)