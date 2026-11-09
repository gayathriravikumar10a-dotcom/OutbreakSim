import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from population import create_population
from simulation import simulate, count_states, get_neighbors
from outbreak_statistics import find_peak_infections

class TestOutbreakSim(unittest.TestCase):

    def test_population_grid_size(self):
        grid = create_population(5, 5, 20)
        self.assertEqual(len(grid), 5)
        self.assertTrue(all(len(row) == 5 for row in grid))

    def test_initial_infected_person(self):
        grid = create_population(5, 5, 0)
        counts = count_states(grid)
        self.assertEqual(counts["I"], 1)

    def test_vaccination_count(self):
        grid = create_population(10, 10, 50)
        counts = count_states(grid)
        self.assertEqual(counts["V"], 50)

    def test_population_total(self):
        grid = create_population(10, 10, 20)
        counts = count_states(grid)
        self.assertEqual(sum(counts.values()), 100)

    def test_neighbor_detection(self):
        neighbors = get_neighbors(0, 0, 3, 3)
        self.assertEqual(len(neighbors), 2)

    def test_simulation_days(self):
        history = simulate(10, 10, 20, 15)
        self.assertEqual(len(history), 16)

    def test_daily_population_total(self):
        history = simulate(10, 10, 20, 15)

        for record in history:
            total = record["S"] + record["I"] + record["R"] + record["V"]
            self.assertEqual(total, 100)

    def test_peak_infections(self):
        history = [
            {"day": 0, "S": 9, "I": 1, "R": 0, "V": 0},
            {"day": 1, "S": 7, "I": 3, "R": 0, "V": 0},
            {"day": 2, "S": 4, "I": 6, "R": 0, "V": 0}
        ]

        peak = find_peak_infections(history)

        self.assertEqual(peak["peak_day"], 2)
        self.assertEqual(peak["peak_infections"], 6)


if __name__ == "__main__":
    unittest.main()