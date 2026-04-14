import numpy as np
import matplotlib.pyplot as plt
import json
from tqdm import tqdm

class Population:
    def __init__(self, N, infected):
        self.population = np.array([0]*N, dtype=int)  # 0=healthy, 1=infected, 2=recovered
        # set initial infected individuals
        for i in range(infected):
            self.population[i] = 1

    def __repr__(self):
        return f"Population(N={len(self.population)}, infected={np.sum(self.population == 1)}, recovered={np.sum(self.population == 2)})"
    
    def update(self, beta, gamma):
        total = len(self.population)
        
        # Create boolean masks for current states
        infected_mask = (self.population == 1)  # a boolean array of the same length as self.population, where True indicates infected individuals
        susceptible_mask = (self.population == 0)   # a boolean array where True indicates susceptible individuals
        
        infected_num = np.sum(infected_mask)
        
        if infected_num == 0:
            return  # Simulation over
        
        # Standard SIR probability of a susceptible person getting infected
        prob_infection = beta * infected_num / total
        
        # Generate random numbers for all susceptible individuals at once
        S_count = np.sum(susceptible_mask)
        new_infections = np.random.rand(S_count) < prob_infection
        
        # Map the new infections back to the main array (1 if infected, 0 if still susceptible)
        self.population[susceptible_mask] = np.where(new_infections, 1, 0)
        
        # Generate random numbers for all currently infected individuals
        # (We use the original infected_mask, so newly infected people don't recover on day 0)
        new_recoveries = np.random.rand(infected_num) < gamma
        
        # Map the recoveries back to the main array (2 if recovered, 1 if still infected)
        self.population[infected_mask] = np.where(new_recoveries, 2, 1)
        
    def get_counts(self, state):
        return np.sum(self.population == state)
    
def SIR_simulation(N, infected, beta, gamma, time_points):
    # create population
    # a one-dimensional array of 10000 points, where 0=healthy, 1=infected, 2=recovered
    population = Population(N, infected)

    susceptible_counts = []
    infected_counts = []
    recovered_counts = []
    # run simulation
    for i in tqdm(range(time_points)):
        susceptible_counts.append(population.get_counts(0))
        infected_counts.append(population.get_counts(1))
        recovered_counts.append(population.get_counts(2))
        population.update(beta, gamma)
    
    return susceptible_counts, infected_counts, recovered_counts

def plot_SIR(susceptible_counts, infected_counts, recovered_counts, figpath):
    plt.figure(figsize=(10, 6))
    plt.plot(susceptible_counts, label='Susceptible', color='blue')
    plt.plot(infected_counts, label='Infected', color='red')
    plt.plot(recovered_counts, label='Recovered', color='green')
    plt.xlabel('Time Steps')
    plt.ylabel('Number of Individuals')
    plt.title('SIR Model Simulation')
    plt.legend()
    plt.grid()
    plt.savefig(figpath)
    plt.close()
    
if __name__ == "__main__":
    # load config
    with open("Practical9/config.json", "r") as f:
        config = json.load(f)
    
    # set random seed to ensure reproducibility
    if config["seed"] is not None:
        np.random.seed(config["seed"])

    # set parameters
    N = config["population"]
    infected = config["infected_initial"]
    beta = config["beta"]
    gamma = config["gamma"]
    time_points = config["times"]
    figpath = "Practical9/SIR_plot.png"

    susceptible_counts, infected_counts, recovered_counts = SIR_simulation(N, infected, beta, gamma, time_points)
    plot_SIR(susceptible_counts, infected_counts, recovered_counts, figpath)

