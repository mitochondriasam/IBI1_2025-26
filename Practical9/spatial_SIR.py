import numpy as np
import matplotlib.pyplot as plt
import json
from tqdm import tqdm

class Population:
    def __init__(self, size):
        self.population = np.zeros((size, size), dtype=int)  # 0=healthy, 1=infected, 2=recovered
        # set initial infected individuals
        outbreak = np.random.choice(range(size), 2)
        self.population[outbreak[0], outbreak[1]] = 1

    def update(self, beta, gamma):
        infectedIndex = np.where(self.population == 1)
        for i in range(len(infectedIndex[0])):
            x = infectedIndex[0][i]
            y = infectedIndex[1][i]
            for xNeighbour in range(x-1, x+2):
                for yNeighbour in range(y-1, y+2):
                    if (xNeighbour, yNeighbour) != (x, y):
                        if 0 <= xNeighbour < self.population.shape[0] and 0 <= yNeighbour < self.population.shape[1]:
                            if self.population[xNeighbour, yNeighbour] == 0:
                                self.population[xNeighbour, yNeighbour] = np.random.choice(range(2), 1, p=[1-beta, beta])[0]
        # Update recovered individuals
        for i in range(self.population.shape[0]):
            for j in range(self.population.shape[1]):
                if self.population[i, j] == 1 and np.random.rand() < gamma:
                    self.population[i, j] = 2


    def get_counts(self, state):
        return np.sum(self.population == state)
    
    def draw(self):
        plt.imshow(self.population, cmap='viridis', vmin=0, vmax=2)
        plt.colorbar(ticks=[0, 1, 2], label='State (0=healthy, 1=infected, 2=recovered)')
        plt.title('SIR Model Simulation')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.show()
        
def SIR_simulation(population, time_points, beta, gamma):
    susceptible_counts = []
    infected_counts = []
    recovered_counts = []
    population.draw()  # Draw initial state
    for _ in tqdm(range(time_points)):
        susceptible_counts.append(population.get_counts(0))
        infected_counts.append(population.get_counts(1))
        recovered_counts.append(population.get_counts(2))
        population.update(beta, gamma)
        if (_ + 1) % 10 == 0:  # Draw every 10 time steps
            population.draw()
    return susceptible_counts, infected_counts, recovered_counts

if __name__ == "__main__":
    # load config
    with open("Practical9/config.json", "r") as f:
        config = json.load(f)
    
    # get parameters from an external json file for easy modification
    size = config["SIR"]["population"]
    beta = config["SIR"]["beta"]
    gamma = config["SIR"]["gamma"]
    time_points = config["SIR"]["times"]
    
    population = Population(size)
    susceptible_counts, infected_counts, recovered_counts = SIR_simulation(population, time_points, beta, gamma)
    
    
    # figpath = "Practical9/spatial_SIR_plot.png"
    # plt.figure(figsize=(10, 6))
    # plt.plot(susceptible_counts, label='Susceptible', color='blue')
    # plt.plot(infected_counts, label='Infected', color='red')
    # plt.plot(recovered_counts, label='Recovered', color='green')
    # plt.xlabel('Time Steps')
    # plt.ylabel('Number of Individuals')
    # plt.title('Spatial SIR Model Simulation')
    # plt.legend()
    # plt.grid()
    # plt.savefig(figpath)
    # plt.show()