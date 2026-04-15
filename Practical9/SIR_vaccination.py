import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

from SIR import Population, SIR_simulation

def plot_SIR_all(infected_counts_list, vaccination_rates, fig_path="SIR_vaccination_plot.png"):
    plt.figure(figsize=(10, 6))
    for i, infected_counts in enumerate(infected_counts_list):
        rate = vaccination_rates[i]
        plt.plot(infected_counts, label=f'Infected (vaccination rate: {rate * 100:.0f}%)', color=cm.viridis(rate))  # Use a colormap to differentiate lines by vaccination rate
    plt.xlabel('Time Steps')
    plt.ylabel('Number of Individuals')
    plt.title('SIR Model with Different Vaccination Rates')
    plt.legend()
    plt.grid()
    plt.savefig(fig_path)
    plt.close()

if __name__ == "__main__":
    # load config
    with open("Practical9/config.json", "r") as f:
        config = json.load(f)

    # get parameters from an external json file for easy modification
    N = config["SIR"]["population"]
    infected = config["SIR"]["infected_initial"]
    beta = config["SIR"]["beta"]
    gamma = config["SIR"]["gamma"]
    time_points = config["SIR"]["times"]
    vaccination_rate_list = config["SIR_vaccination"]["vaccination_rate"]
    
    infected_counts_list = []
    
    for vaccination_rate in vaccination_rate_list:
        # Create a new population for each vaccine rate
        population = Population(N, infected)
        
        # Vaccinate a portion of the population at the start (set to recovered state)
        # Vaccinate the last vaccinated_num individuals to avoid vaccinating the initial infected
        vaccinated_num = int(N * vaccination_rate)
        if vaccinated_num > 0:
            population.population[-vaccinated_num:] = 2  # Set vaccinated individuals to recovered state
        
        # Run the SIR simulation with the vaccinated population
        susceptible_counts, infected_counts, recovered_counts = SIR_simulation(population, N, infected, beta, gamma, time_points)
        
        infected_counts_list.append(infected_counts)
    
    # Plot all results in one figure
    figpath = "Practical9/SIR_vaccination_plot_all.png"
    plot_SIR_all(infected_counts_list, vaccination_rate_list, fig_path=figpath)
