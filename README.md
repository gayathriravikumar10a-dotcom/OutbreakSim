# OutbreakSim: Grid-Based Epidemic Spread Simulation Model

## 1. Project Overview

OutbreakSim is a Python-based epidemic simulation system that models how an infectious disease spreads through a population using a two-dimensional grid.

Each cell represents one individual. The simulation demonstrates infection transmission, recovery, and vaccination, helping users understand how vaccination can influence the spread of an epidemic.

## 2. Objectives

- Simulate epidemic spread using a grid-based population.
- Model infection transmission between neighbouring individuals.
- Simulate recovery after a fixed infection period.
- Study the impact of vaccination on infection spread.
- Generate statistical reports and graphical visualizations.

## 3. Technologies Used

- Python 3
- Matplotlib
- Random module
- Unittest framework

## 4. Population States

| Symbol | Meaning |
|---|---|
| S | Susceptible |
| I | Infected |
| R | Recovered |
| V | Vaccinated |

## 5. Key Features

1. Grid-based population modelling.
2. Probabilistic infection transmission.
3. Four-directional neighbour infection.
4. Recovery after a fixed number of days.
5. Vaccination-based scenario comparison.
6. Daily population statistics.
7. Peak infection analysis.
8. Infection comparison graph.
9. Population grid visualization.
10. Unit testing.

## 6. Project Structure

```text
OutbreakSim/
│
├── main.py
├── simulation.py
├── population.py
├── outbreak_statistics.py
├── README.md
│
└── tests/
    └── test_simulation.py
```

## 7. Installation

Install Python 3 and Matplotlib.

```bash
pip install matplotlib
```

## 8. How to Run

Open the terminal in the project directory.

Run:

```bash
python main.py
```

The program generates daily outbreak statistics, compares vaccination scenarios, and displays graphical visualizations.

## 9. Simulation Parameters

| Parameter | Value |
|---|---:|
| Grid size | 20 × 20 |
| Population | 400 |
| Simulation duration | 30 days |
| Infection probability | 0.3 |
| Recovery duration | 5 days |
| Scenario A vaccination | 0% |
| Scenario B vaccination | 50% |

## 10. Testing

Run the unit tests using:

```bash
python -m unittest discover -s tests -v
```

**Test result:** 8 tests passed successfully.

## 11. Expected Outputs

- Daily susceptible, infected, recovered, and vaccinated population counts.
- Peak infection statistics.
- Comparison of 0% and 50% vaccination scenarios.
- Infection comparison graph.
- Population grid visualization.

## 12. Conclusion

OutbreakSim demonstrates how infectious diseases can spread through a population and how vaccination can affect epidemic transmission.

The project combines Python programming, probability, simulation modelling, statistical analysis, visualization, and software testing.

## 13. Limitations

- The model uses a simplified grid-based population.
- Individuals move neither within nor outside the grid.
- Infection probability is assumed to be constant.
- Real-world epidemic factors such as age, travel, and social behaviour are not included.

**Note:** This project is an educational simulation and is not intended for real-world medical or epidemiological forecasting.