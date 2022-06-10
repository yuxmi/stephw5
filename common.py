def read_input(filename):
    cities = []
    with open(filename) as f:
        for data in f.readlines()[1:]:
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
