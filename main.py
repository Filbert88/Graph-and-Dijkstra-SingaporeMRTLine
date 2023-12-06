from datetime import datetime, time
from graph import graph

PEAK_HOURS = [(time(7, 00), time(9, 30)), (time(17, 00), time(20, 00))]
OFF_PEAK_HOURS = [(time(9, 30), time(17, 00)), (time(20, 00), time(23, 59)), (time(0, 00), time(7, 00))]

def get_weight_factor(current_time, is_weekend):
    if is_weekend:
        return 1
    for start, end in PEAK_HOURS:
        if start <= current_time <= end:
            return 1.5
    return 1

def adjust_graph_weights(graph, current_time, is_weekend):
    weight_factor = get_weight_factor(current_time, is_weekend)
    adjusted_graph = {
        station: {neighbor: weight * weight_factor for neighbor, weight in neighbors.items()}
        for station, neighbors in graph.items()
    }
    return adjusted_graph

def dijkstra(graph, start, end):
    shortest_paths = {start: (None, 0)}
    visited = set()
    current_node = start

    while current_node != end:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current = shortest_paths[current_node][1]

        for next_node, weight in destinations.items():
            new_weight = weight + weight_to_current
            if new_weight < shortest_paths.get(next_node, (None, float('inf')))[1]:
                shortest_paths[next_node] = (current_node, new_weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    path = []
    while current_node:
        path.append(current_node)
        current_node = shortest_paths[current_node][0]
        
    return path[::-1]

def main(graph, start, end):
    current_time = datetime.now().time()
    is_weekend = datetime.now().weekday() >= 5
    adjusted_graph = adjust_graph_weights(graph, current_time, is_weekend)
    return dijkstra(adjusted_graph, start, end)

source = input("Enter the source MRT station: ")
destination = input("Enter the destination MRT station: ")
shortest_path = main(graph, source, destination)
print("The shortest path is:", shortest_path)
