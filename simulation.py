import random
from population import create_population


def get_neighbors(row, col, rows, cols):
    neighbors = []

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col))

    return neighbors


def count_states(grid):
    counts = {
        "S": 0,
        "I": 0,
        "R": 0,
        "V": 0
    }

    for row in grid:
        for cell in row:
            counts[cell] += 1

    return counts


def simulate(
    rows,
    cols,
    vaccination_rate,
    days,
    infection_probability=0.3,
    recovery_days=5
):
    if days < 0:
        raise ValueError("Days cannot be negative.")

    if not 0 <= infection_probability <= 1:
        raise ValueError("Infection probability must be between 0 and 1.")

    if recovery_days <= 0:
        raise ValueError("Recovery days must be positive.")

    grid = create_population(rows, cols, vaccination_rate)

    infection_timers = {}

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "I":
                infection_timers[(r, c)] = 0

    history = []

    history.append({
        "day": 0,
        **count_states(grid)
    })

    for day in range(1, days + 1):

        new_infections = []
        new_recoveries = []

        for (r, c), infected_days in list(infection_timers.items()):

            for nr, nc in get_neighbors(r, c, rows, cols):

                if grid[nr][nc] == "S":
                    if random.random() < infection_probability:
                        new_infections.append((nr, nc))

            if infected_days + 1 >= recovery_days:
                new_recoveries.append((r, c))

        for r, c in new_infections:
            if grid[r][c] == "S":
                grid[r][c] = "I"
                infection_timers[(r, c)] = 0

        for r, c in new_recoveries:
            grid[r][c] = "R"
            infection_timers.pop((r, c), None)

        for position in list(infection_timers):
            infection_timers[position] += 1

        history.append({
            "day": day,
            **count_states(grid)
        })

    return history
def get_population_grid(
    rows,
    cols,
    vaccination_rate,
    infection_probability=0.3,
    recovery_days=5,
    target_day=0
):
    grid = create_population(rows, cols, vaccination_rate)

    infection_timers = {}

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "I":
                infection_timers[(r, c)] = 0

    for day in range(1, target_day + 1):

        new_infections = []
        new_recoveries = []

        for (r, c), infected_days in list(infection_timers.items()):

            for nr, nc in get_neighbors(r, c, rows, cols):
                if grid[nr][nc] == "S":
                    if random.random() < infection_probability:
                        new_infections.append((nr, nc))

            if infected_days + 1 >= recovery_days:
                new_recoveries.append((r, c))

        for r, c in new_infections:
            if grid[r][c] == "S":
                grid[r][c] = "I"
                infection_timers[(r, c)] = 0

        for r, c in new_recoveries:
            grid[r][c] = "R"
            infection_timers.pop((r, c), None)

        for position in list(infection_timers):
            infection_timers[position] += 1

    return grid