class Graph:
    def __init__(self, edges):
        self.edges = edges    # from this ("Mumbai", "Paris"), ("Mumbai", "Dubai")
        self.graph_dict = {}  # converting to this, Mumbai(key) = [Paris, Dubai](value as a list)
        for start, end in edges:
            if start in self.graph_dict:  # if start already exists add the end
                self.graph_dict[start].append(end)
            else:  # if start doesn't exist add the start and end
                self.graph_dict[start] = [end]
        print('Graph Dictionary:', self.graph_dict)

    def get_paths(self, start, end, path=[]):  # starting value to ending value and path can be empty or contain keys
        path = path + [start]

        if start == end:   # if Mumbai==Mumbai
            return [path]  # return path[Mumbai]

        if start not in self.graph_dict:  # if the starting point(key) is not in dictionary
            return []

        paths = []                       # for finding all paths between two destinations
        for node in self.graph_dict[start]:  # this will give node(values) for key(start) from dictionary
            if node not in path:             # if already visited the value will be in path[key]
                new_paths = self.get_paths(node, end, path)  # passing the values as key and checking do these values
                # exists as a key in the dictionary i.e. Mumbai=[Paris, Dubai], so Paris=[Dubai, NewYork] & Dubai =[NYC]
                for p in new_paths:  # adding all the different paths
                    paths.append(p)
        return paths  # the 1st time parameters of path[Mumbai], 2nd time[Mumbai, Paris], 3rd[Mumbai, Dubai], and so on

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:  # if we don't have the shortest path yet then add it, if we have it, compare it with the new
                    if shortest_path is None or len(sp) < len(shortest_path):  # shortest path(sp), if the new path is
                        shortest_path = sp  # smaller than add it or else the if condition will fail cause of 0 OR 0
        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    route_graph = Graph(routes)
    start = 'Mumbai'
    end = 'New York'

    print(f"All paths between: {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))

    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))

