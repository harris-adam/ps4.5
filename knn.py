# knn.py
# Completed by:
import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Fish:
    species: str
    weight: float
    length1: float
    length2: float
    length3: float
    height: float
    width: float

# Read a CSV file
# The first column is the fish species
# The second column is the weight of the fish
# The rest of the columns are the length1, length2, length3, height, width
# Created with assistance from GitHub Copilot
def read_fish_CSV(file_path: Path, species: str = "") -> list[Fish]:
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        fishes = []
        for row in reader:
            fishes.append(Fish(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6])))
            
        return fishes

# Find the euclidean distance between two fish based on their length1, length2, length3, height, and width
def distance(fish1: Fish, fish2: Fish) -> float:
    # YOUR CODE HERE
    pass

# Find the k nearest neighbors of a given fish based on the distance function
def nearest(k: int, fish: Fish, all_fish: list[Fish]) -> list[Fish]:
    # YOUR CODE HERE
    pass

# Classify a fish based on the k nearest neighbors
# Choose the fish species with the most neighbors and return it
def classify(k: int, fish: Fish, all_fish: list[Fish]) -> str:
    # YOUR CODE HERE
    pass

# Predict the weight of a fish based on the k nearest neighbors
# Choose the average (mean) weight of the neighbors and return it
def predict(k: int, fish: Fish, all_fish: list[Fish]) -> float:
    # YOUR CODE HERE
    pass

# Plot the fish data with matplotlib by height and width, showing a different color
# for each species
# Created with assistance from GitHub Copilot
def plot_fish(all_fish: list[Fish]) -> None:
    import matplotlib.pyplot as plt
    species = {}
    for fish in all_fish:
        if fish.species in species:
            species[fish.species].append(fish)
        else:
            species[fish.species] = [fish]
    for key in species:
        plt.scatter([fish.height for fish in species[key]], [fish.width for fish in species[key]], label=key)
    # add height and width to the plot
    plt.xlabel("Height")
    plt.ylabel("Width")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    p = Path(__file__).with_name('Fish.csv')
    all_fish = read_fish_CSV(p.absolute())
    plot_fish(all_fish)
