# Traveling Salesman Problem
import math, sys


# Common functions
########################################################

def read_input(filename):
    cities = []
    with open(filename) as f:
        for data in f.read().splitlines():
            x = float(data.split(',')[0])
            y = float(data.split(',')[1])
            coord = (x,y)
            cities.append(coord)
    return cities

def format_tour(tour):
    return 'index\n' + '\n'.join(map(str, tour))

def print_tour(tour):
    print(format_tour(tour))

def totalDist(tour, cities):
    result = 0
    for i in range(len(tour) - 1):
        result += distance(cities[tour[i]], cities[tour[i + 1]])
    result += distance(cities[tour[0]], cities[tour[-1]])
    return result

#########################################################

# Calculates distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def greedy(cities):
    # Creates distance matrix
    distList = [[0]*len(cities) for i in range(len(cities))]
    for i in range(len(cities)):
        for j in range(i, len(cities)):
            distList[i][j] = distList[j][i] = distance(cities[i], cities[j])

    # Starts at node 0
    current = 0
    unvisited = set(range(1, len(cities)))
    tour = [current]

    # Unvisited > 0 -> adds nearest neighbor to tour
    while unvisited:
        nextcity = min(unvisited, key=lambda city: distList[current][city])
        unvisited.remove(nextcity)
        tour.append(nextcity)
        current = nextcity

    return tour

if __name__ == '__main__':
    cities = read_input('input0.txt')
    tour = greedy(cities)
    print_tour(tour)
    print(totalDist(tour, cities))
