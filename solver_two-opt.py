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

# Nearest neighbor method
def greedy(cities, current):
    distList = [[0]*len(cities) for i in range(len(cities))]
    for i in range(len(cities)):
        for j in range(i, len(cities)):
            distList[i][j] = distList[j][i] = distance(cities[i], cities[j])

    unvisited = set(range(0, len(cities)))
    unvisited.remove(current)
    tour = [current]

    while unvisited:
        nextcity = min(unvisited, key=lambda city: distList[current][city])
        unvisited.remove(nextcity)
        tour.append(nextcity)
        current = nextcity

    return tour

# Determines if there is an intersection between two lines
def compare(i, j, tour, cities):
    len1 = distance(cities[tour[i]], cities[tour[i+1]])
    len2 = distance(cities[tour[j]], cities[tour[j+1]])
    len3 = distance(cities[tour[i]], cities[tour[j]])
    len4 = distance(cities[tour[i+1]], cities[tour[j+1]])
    return len1 + len2, len3 + len4

def two_opt(tour, cities):
    improved = True

    while improved:
        improved = False
        # Loops through every single combination of lines
        for i in range(len(tour)-3):
            for j in range(i+2, len(tour)-1):
                original, new = compare(i, j, tour, cities)
                # If there is an intersection, uncrosses them
                if new < original:
                    new_tour = tour[i+1:j+1]
                    tour[i+1:j+1] = new_tour[::-1]
                    improved = True
        # If there are no more intersections
        if improved == False:
            break

    return tour
                

if __name__ == '__main__':
    cities = read_input('input5.txt')
    inf = float('inf')
    minDist = inf
    finaltour = []
    for current in range(len(cities)):
        tour = greedy(cities, current)
        newtour = two_opt(tour, cities)
        dist = totalDist(newtour, cities)
        # Checks for the best starting point
        if dist < minDist:
            minDist = dist
            finaltour = newtour
    print_tour(finaltour)
    print(minDist)
