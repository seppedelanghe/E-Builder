import random

def randomFloat(min: float, max: float):
    return min + random.random() * (max - min)

def randomInt(min: int, max: int):
    return round(min + random.random() * (max - min))