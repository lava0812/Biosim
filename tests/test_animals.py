__author__ = "Sathuriyan Sivathas & Lavanyan Rathy"
__email__ = "sathuriyan.sivathas@nmbu.no & lavanyan.rathy@nmbu.no"

from src.biosim.animals import Herbivore
import pytest


def test_aging():
    herbivore = Herbivore()
    herbivore.aging()

    assert herbivore.age == 1


def test_weight_baby():
    pass


def test_weight_increase():
    pass


def test_weight_decrease():
    pass


def test_fitness_herbivores():
    pass


def test_death_herbivores():
    pass


def test_birth_herbivore():
    pass


def test_birth_herbivore_probability():
    pass


def test_birth_weight_loss():
    pass
