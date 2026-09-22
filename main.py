import numpy as np
import matplotlib.pyplot as plt

class Cell:
    def __init__(self, position:tuple, state: str, timer: int = 0):
        self.position = position
        self.state = state
        self.timer = timer