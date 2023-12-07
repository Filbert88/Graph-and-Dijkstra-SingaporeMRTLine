from datetime import datetime, time
from graph import *
from plot import *

PEAK_HOURS = [(time(7, 00), time(9, 30)), (time(17, 00), time(20, 00))]
OFF_PEAK_HOURS = [(time(9, 30), time(17, 00)), (time(20, 00), time(23, 59)), (time(0, 00), time(7, 00))]

def display_stations(station_codes):
    print("\nHere is a list of MRT stations sorted by line for your reference:")
    lines = {}
    for station, code in station_codes.items():
        line = ''.join(filter(str.isalpha, code))
        if line not in lines:
            lines[line] = []
        lines[line].append(station)

    for line, stations in sorted(lines.items()):
        print(f"Line {line}:")
        for station in sorted(stations):
            print(f"  - {station}")
        print()

def validate_input(msg, valid_stations, interchange_codes):
    while True:
        station_name = input(msg).strip()
        station_name_lower = station_name.lower()
        station_name = next((name for name in valid_stations if name.lower() == station_name_lower), None)

        if station_name in valid_stations or station_name in interchange_codes:
            return station_name
        else:
            print("Invalid station name. Please try again.")

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

def main(graph, station_codes, interchange_codes):
    print("Welcome to the Singapore MRT Route Finder!")
    print("Let's find the most optimized route for your journey.")
    print("Enjoy your trip planning with us! ^.^")

    inputs = input("\nDo you want to see the list of the MRT stations (YES/NO): ")
    if inputs.lower() == "yes":
        display_stations(station_codes)

    while inputs.lower() not in ["yes", "no"]:
        print("Invalid Input. Please Try again.")
        inputs = input("\nDo you want to see the list of the MRT stations (YES/NO): ")
        if inputs.lower() == "yes":
            display_stations(station_codes)

    valid_stations = set(station_codes.keys())
    source = validate_input("\nEnter the source MRT station: ", valid_stations, interchange_codes)
    destination = validate_input("Enter the destination MRT station: ", valid_stations, interchange_codes)

    start_codes = interchange_codes.get(source, [station_codes.get(source)])
    end_codes = interchange_codes.get(destination, [station_codes.get(destination)])

    current_time = datetime.now().time()
    is_weekend = datetime.now().weekday() >= 5
    adjusted_graph = adjust_graph_weights(graph, current_time, is_weekend)

    shortest_path = "Route Not Possible"
    shortest_path_length = float('inf')

    for start_code in start_codes:
        for end_code in end_codes:
            current_path = dijkstra(adjusted_graph, start_code, end_code)
            if current_path != "Route Not Possible" and len(current_path) < shortest_path_length:
                shortest_path = current_path
                shortest_path_length = len(current_path)

    if shortest_path == "Route Not Possible":
        return shortest_path
    
    shortest_path_stations = []
    path_with_names = []
    for i, code in enumerate(shortest_path):
        station_name = None
        for name, codes in interchange_codes.items():
            if code in codes:
                station_name = name
                break

        if not station_name:
            station_name = next((name for name, station_code in station_codes.items() if station_code == code), None)

        if station_name:
            path_with_names.append(f"{station_name} ({code})")
            shortest_path_stations.append(station_name)

        if i < len(shortest_path) - 1:
            next_code = shortest_path[i + 1]
            current_line = ''.join(filter(str.isalpha, code))
            next_line = ''.join(filter(str.isalpha, next_code))

            if station_name in interchange_codes  and current_line != next_line:
                change_message = f"Changing Stations at {station_name} from {current_line} line to {next_line} line"
                path_with_names.append(change_message)

    return  ' -> '.join(path_with_names), shortest_path_stations

shortest_path,shortest_path_stations = main(graph, station_codes, interchanges)
print("\nThe shortest path is:", shortest_path)
print("\nThank you for using the Singapore MRT Route Finder. Have a great trip!")

display = input("\nLast but not least, Do you want to view the visualization of the graph (YES/NO) ? ")

if display.lower() == "yes":
    plot_graph(shortest_path_stations)

while display.lower() not in ["yes", "no"]:
    print("Invalid Input. Please Try again.")
    display = input("\nDo you want to view the visualization of the graph (YES/NO) ? ")
    if display.lower() == "yes":
        plot_graph(shortest_path_stations)
    if display.lower() == "no":
        break

print("\nGoodbye!!!")