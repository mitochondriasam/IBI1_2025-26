import numpy as np
import matplotlib.pyplot as plt
import json
from tqdm import tqdm
import cv2
import os

class Population:
    def __init__(self, size):
        self.population = np.zeros((size, size), dtype=int)  # 0=healthy, 1=infected, 2=recovered
        # set initial infected individuals
        outbreak = np.random.choice(range(size), 2)
        self.population[outbreak[0], outbreak[1]] = 1

    def update(self, beta, gamma):
        # infectedIndex = np.where(self.population == 1)
        # for i in range(len(infectedIndex[0])):
        #     x = infectedIndex[0][i]
        #     y = infectedIndex[1][i]
        #     for xNeighbour in range(x-1, x+2):
        #         for yNeighbour in range(y-1, y+2):
        #             if (xNeighbour, yNeighbour) != (x, y):
        #                 if 0 <= xNeighbour < self.population.shape[0] and 0 <= yNeighbour < self.population.shape[1]:
        #                     if self.population[xNeighbour, yNeighbour] == 0:
        #                         self.population[xNeighbour, yNeighbour] = np.random.choice(range(2), 1, p=[1-beta, beta])[0]
        # # Update recovered individuals
        # for i in range(self.population.shape[0]):
        
        infected = self.population == 1
        
        # Count infected neighbors without wrapping (no periodic boundaries)
        # neighbors = (np.roll(infected, 1, 0) + np.roll(infected, -1, 0) +
        #              np.roll(infected, 1, 1) + np.roll(infected, -1, 1) +
        #              np.roll(infected, (1, 1), (0, 1)) + np.roll(infected, (-1, 1), (0, 1)) +
        #              np.roll(infected, (1, -1), (0, 1)) + np.roll(infected, (-1, -1), (0, 1)))

        
        neighbors = np.zeros_like(infected, dtype=int)
        # Horizontal and vertical
        neighbors[:, :-1] += infected[:, 1:]  # right
        neighbors[:, 1:] += infected[:, :-1]  # left
        neighbors[:-1, :] += infected[1:, :]  # down
        neighbors[1:, :] += infected[:-1, :]  # up
        # Diagonals
        neighbors[:-1, :-1] += infected[1:, 1:]  # down-right
        neighbors[:-1, 1:] += infected[1:, :-1]  # down-left
        neighbors[1:, :-1] += infected[:-1, 1:]  # up-right
        neighbors[1:, 1:] += infected[:-1, :-1]  # up-left
        
        # Calculate infection probability
        infection_prob = 1 - (1 - beta) ** neighbors
        
        # Generate random values and infect
        random_vals = np.random.rand(*self.population.shape)
        infect_mask = (self.population == 0) & (random_vals < infection_prob)
        self.population[infect_mask] = 1
        
        # Vectorized recovery
        recover_random = np.random.rand(*self.population.shape)
        recover_mask = (self.population == 1) & (recover_random < gamma)
        self.population[recover_mask] = 2


    def get_counts(self, state):
        return np.sum(self.population == state)
    
    def draw(self, figpath):
        plt.imshow(self.population, cmap='viridis', vmin=0, vmax=2)
        plt.colorbar(ticks=[0, 1, 2], label='State (0=healthy, 1=infected, 2=recovered)')
        plt.title('SIR Model Simulation')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.savefig(figpath)
        plt.close()

def SIR_simulation(population, time_points, beta, gamma, plot_interval):
    os.makedirs("Practical9/temp", exist_ok=True)    # Remove existing files in temp
    
    susceptible_counts = []
    infected_counts = []
    recovered_counts = []
    population.draw("Practical9/temp/state_0.png")  # Draw initial state
    for _ in tqdm(range(time_points)):
        susceptible_counts.append(population.get_counts(0))
        infected_counts.append(population.get_counts(1))
        recovered_counts.append(population.get_counts(2))
        population.update(beta, gamma)
        if (_ + 1) % plot_interval == 0:  # Draw every plot_interval time steps
            population.draw(f"Practical9/temp/state_{_ + 1}.png")
    return susceptible_counts, infected_counts, recovered_counts

def video(path="Practical9/spatial_SIR_simulation.mp4"):

    img_array = []
    for filename in sorted(os.listdir("Practical9/temp/"), key=lambda x: int(x.split('_')[1].split('.')[0])):
        if filename.startswith("state_"):
            img = cv2.imread(os.path.join("Practical9/temp/", filename))
            img_array.append(img)

    height, width, layers = img_array[0].shape
    video = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    for img in img_array:
        video.write(img)

    video.release()
    
    for filename in os.listdir("Practical9/temp/"):
        os.remove(os.path.join("Practical9/temp/", filename))    
        
    print(f"Video saved to {path}")

if __name__ == "__main__":
    # load config
    with open("Practical9/config.json", "r") as f:
        config = json.load(f)
    
    # get parameters from an external json file for easy modification
    size = config["spatial_SIR"]["square_size"]
    beta = config["spatial_SIR"]["beta"]
    gamma = config["spatial_SIR"]["gamma"]
    time_points = config["spatial_SIR"]["steps"]
    plot_interval = config["spatial_SIR"]["plot_interval"]
    
    population = Population(size)
    susceptible_counts, infected_counts, recovered_counts = SIR_simulation(population, time_points, beta, gamma, plot_interval)
    
    video("Practical9/spatial_SIR_simulation.mp4")
