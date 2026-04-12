import config

from typing import TYPE_CHECKING, Callable
from entities import Tree, Rock, Grass, Predator, Herbivore

if TYPE_CHECKING:
    from entities import Entity


EntityFactory = Callable[[], 'Entity']



def RockFactory() -> 'Entity': 
    return Rock()

def TreeFactory() -> 'Entity': 
    return Tree()

def GrassFactory() -> 'Entity': 
    return Grass()

def HerbivoreFactory() -> 'Entity': 
    return Herbivore(config.HERBIVORE.speed, config.HERBIVORE.health)

def PredatorFactory() -> 'Entity':
    return Predator(config.PREDATOR.health, config.PREDATOR.speed, config.PREDATOR.attack)
