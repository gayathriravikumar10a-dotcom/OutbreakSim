import random


def create_population(rows, cols, vaccination_rate):
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be positive.")

    if not 0 <= vaccination_rate <= 100:
        raise ValueError("Vaccination rate must be between 0 and 100.")

    total_population = rows * cols

    if total_population < 1:
        raise ValueError("Population cannot be empty.")

    population = [["S" for _ in range(cols)] for _ in range(rows)]

    vaccination_count = round(
        total_population * vaccination_rate / 100
    )

    positions = [
        (r, c)
        for r in range(rows)
        for c in range(cols)
    ]

    random.shuffle(positions)

    for r, c in positions[:vaccination_count]:
        population[r][c] = "V"

    susceptible_positions = [
        (r, c)
        for r in range(rows)
        for c in range(cols)
        if population[r][c] == "S"
    ]

    if susceptible_positions:
        r, c = random.choice(susceptible_positions)
        population[r][c] = "I"

    return population