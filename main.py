from simulation import simulate, get_population_grid

from outbreak_statistics import (
    display_daily_statistics,
    compare_scenarios,
    plot_infection_comparison,
    display_population_grid
)


ROWS = 20
COLS = 20
DAYS = 30
INFECTION_PROBABILITY = 0.3
RECOVERY_DAYS = 5


def main():

    print("======================================")
    print("       OUTBREAKSIM SIMULATION")
    print("======================================")

    print("\nRunning Scenario A: 0% Vaccination")

    scenario_a = simulate(
        ROWS, COLS, 0, DAYS,
        INFECTION_PROBABILITY,
        RECOVERY_DAYS
    )

    display_daily_statistics(scenario_a)

    print("\nRunning Scenario B: 50% Vaccination")

    scenario_b = simulate(
        ROWS, COLS, 50, DAYS,
        INFECTION_PROBABILITY,
        RECOVERY_DAYS
    )

    display_daily_statistics(scenario_b)

    compare_scenarios(scenario_a, scenario_b)

    plot_infection_comparison(scenario_a, scenario_b)

    grid = get_population_grid(
        ROWS,
        COLS,
        50,
        INFECTION_PROBABILITY,
        RECOVERY_DAYS,
        target_day=10
    )

    display_population_grid(grid, 10)


if __name__ == "__main__":
    main()