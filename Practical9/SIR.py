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
        infected_num = np.sum(self.population == 1)
        total = len(self.population)
        for i in range(total):  
            if self.population[i] == 1:  # If the individual is infected
                # Attempt to infect others
                for j in range(total):
                    if self.population[j] == 0 and np.random.rand() < beta * infected_num / total:  # If the individual is susceptible and gets infected
                        self.population[j] = 1
                # Attempt to recover
                if np.random.rand() < gamma:  # If the infected individual recovers
                    self.population[i] = 2

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

def plot_SIR(susceptible_counts, infected_counts, recovered_counts):
    plt.figure(figsize=(10, 6))
    plt.plot(susceptible_counts, label='Susceptible', color='blue')
    plt.plot(infected_counts, label='Infected', color='red')
    plt.plot(recovered_counts, label='Recovered', color='green')
    plt.xlabel('Time Steps')
    plt.ylabel('Number of Individuals')
    plt.title('SIR Model Simulation')
    plt.legend()
    plt.grid()
    plt.show()
    
    
if __name__ == "__main__":
    # load config
    with open("Practical9/config.json", "r") as f:
        config = json.load(f)
    
    # set random seed
    if config["seed"] is not None:
        np.random.seed(config["seed"])

    # set parameters
    N = config["population"]
    infected = config["infected_initial"]
    beta = config["beta"]
    gamma = config["gamma"]
    time_points = config["times"]

    susceptible_counts, infected_counts, recovered_counts = SIR_simulation(N, infected, beta, gamma, time_points)
    plot_SIR(susceptible_counts, infected_counts, recovered_counts)

