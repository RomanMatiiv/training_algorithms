import pytest

from solution_g import MetalPipeline
from solution_g import WeightException


def test_pipeline_case_1():
    wanted_item = 4

    pipe = MetalPipeline(kg_metal=10, weight_work_piece=5, weight_piece=2)

    real_item = 0
    while pipe.enough_metal():
        real_item += pipe.start_iteration()

    assert real_item == wanted_item


def test_pipeline_case_2():
    wanted_item = 3

    pipe = MetalPipeline(kg_metal=13, weight_work_piece=5, weight_piece=3)

    real_item = 0
    while pipe.enough_metal():
        real_item += pipe.start_iteration()

    assert real_item == wanted_item


def test_pipeline_case_3():
    with pytest.raises(WeightException):
        MetalPipeline(kg_metal=13, weight_work_piece=5, weight_piece=7)


def test_enough_metal_true():
    pipe = MetalPipeline(kg_metal=6, weight_work_piece=4, weight_piece=3)

    assert pipe.enough_metal()


def test_enough_metal_fasle():
    pipe = MetalPipeline(kg_metal=2, weight_work_piece=4, weight_piece=3)

    assert not pipe.enough_metal()