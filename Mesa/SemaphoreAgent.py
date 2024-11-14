import mesa
import seaborn as sns
import numpy as np
import pandas as pd

class SemaphoreAgent(mesa.Agent):
    def __init__(self, model, controlled_cells):
        # A state equal to True means green
        self.state = model.random.choice([True, False])
        self.controlled_cells = controlled_cells
        for cell in self.controlled_cells:
            model.grid.properties["semaphore"].set_cell(cell, self.state)

    def toggle_state(self):
        if model.global_steps % 5 == 0:
            self.state = not self.state
            for cell in self.controlled_cells:
                model.grid.properties["semaphore"].set_cell(cell, self.state)