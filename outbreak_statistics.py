import matplotlib.pyplot as plt


def display_daily_statistics(history):

    print("\n========== DAILY OUTBREAK REPORT ==========")

    print(
        f"{'Day':<8}"
        f"{'Susceptible':<15}"
        f"{'Infected':<12}"
        f"{'Recovered':<12}"
        f"{'Vaccinated':<12}"
    )

    print("-" * 59)

    for record in history:
        print(
            f"{record['day']:<8}"
            f"{record['S']:<15}"
            f"{record['I']:<12}"
            f"{record['R']:<12}"
            f"{record['V']:<12}"
        )


def find_peak_infections(history):

    peak_record = max(history, key=lambda record: record["I"])

    return {
        "peak_day": peak_record["day"],
        "peak_infections": peak_record["I"]
    }


def compare_scenarios(scenario_a, scenario_b):

    peak_a = find_peak_infections(scenario_a)
    peak_b = find_peak_infections(scenario_b)

    print("\n========== SCENARIO COMPARISON ==========")

    print("\nScenario A: 0% Vaccination")
    print(f"Peak Day: {peak_a['peak_day']}")
    print(f"Peak Infections: {peak_a['peak_infections']}")

    print("\nScenario B: 50% Vaccination")
    print(f"Peak Day: {peak_b['peak_day']}")
    print(f"Peak Infections: {peak_b['peak_infections']}")

    reduction = peak_a["peak_infections"] - peak_b["peak_infections"]

    print("\nPeak Infection Reduction:", reduction)


def plot_infection_comparison(scenario_a, scenario_b):

    days_a = [x["day"] for x in scenario_a]
    infections_a = [x["I"] for x in scenario_a]

    days_b = [x["day"] for x in scenario_b]
    infections_b = [x["I"] for x in scenario_b]

    plt.figure(figsize=(10, 6))

    plt.plot(days_a, infections_a, marker="o", label="0% Vaccination")
    plt.plot(days_b, infections_b, marker="s", label="50% Vaccination")

    plt.title("OutbreakSim - Vaccination Impact")
    plt.xlabel("Simulation Days")
    plt.ylabel("Number of Infected People")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("infection_comparison.png")
    plt.show()


def display_population_grid(grid, day):

    state_values = {
        "S": 0,
        "I": 1,
        "R": 2,
        "V": 3
    }

    numeric_grid = [
        [state_values[cell] for cell in row]
        for row in grid
    ]

    plt.figure(figsize=(8, 8))

    plt.imshow(
        numeric_grid,
        cmap="RdYlGn",
        vmin=0,
        vmax=3
    )

    plt.title(f"OutbreakSim Population Grid - Day {day}")
    plt.xlabel("Columns")
    plt.ylabel("Rows")

    colorbar = plt.colorbar(ticks=[0, 1, 2, 3])
    colorbar.ax.set_yticklabels([
        "Susceptible",
        "Infected",
        "Recovered",
        "Vaccinated"
    ])

    plt.tight_layout()
    plt.savefig(f"population_day_{day}.png")
    plt.show()