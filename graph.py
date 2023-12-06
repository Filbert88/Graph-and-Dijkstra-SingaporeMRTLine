blue_stations = ["Cashew", "Hillview", "Beauty World", "King Albert Park", "Sixth Avenue", 
 "Tan Kah Kee", "Botenic Gardens", "Stevens", "Newton", "Little India", "Rochor", "Bugis", 
 "Promenade", "Bayfront", "Downtown", "Telok Ayer", "Chinatown", "Fort Canning", "Bencoolen", 
 "Jalan Besar", "Bendemeer", "Geylang Bahru", "Mattar", "MacPherson", "Ubi", "Kaki Bukit",
 "Bedok North", "Bedok Reservoir", "Tampines West", "Tampines", "Tampines East", "Upper Changi", "Expo"]

blue_times= [2,3,2,2,2,2,2,2,3,1,2,2,2,2,1,2,2,2,1,2,2,2,2,2,2,2,2,3,2,2,3,2]

purple_stations =["Sengkang", "Bunagkok", "Hougang", "Kovan", "Serangoon", "Woodleigh", "Potong Pasir", "Boon Keng", "Farrer Park", 
"Little India", "Dhoby Ghout", "Clark Quay", "Chinatown", "Outrum Park", "Harbour Front"]

purple_times= [2,2,2,3,2,1,3,2,1,1,3,2,1,4]

green_stations = ["Tuas Link","Tuas West Road", "Tuas Crescent", "Gul Circle", "Joo Koon", 
"Pioneer", "Boon Lay", "Lakeside", "Chinese Garden", "Jurong East", "Clementi", "Dover", "Bouna Vista", 
"Commonwealth", "Queenstown", "Redhill", "Tiong Bahru", "Outram Park", "Tanjong Pagar", "Raffles Place", 
"City Hall", "Bugis", "Lavender", "Kallang", "Aljunied", "Paya Lebar", "Eunos", "Kembangan", 
"Bedok", "Tanah Merah", "Simei", "Tampines", "Pasir Ris"]

green_times= [3,4, 3, 3, 3, 3, 2, 3, 2, 5, 2, 3, 2, 3, 2, 3, 3, 2, 2, 2, 3, 2, 2, 3, 2, 3, 
2, 2, 3, 3, 3, 3]

red_stations= ["Bukit Batok", "Bukit Gombak", "Chua Chu Kang", "Yew Tee", "Kranji", 
"Marsiling", "Woodlands", "Admiralty", "Sembawang", "Canberra" ,"Yishun", "Khatib", "Yio Chu Kang", "Ang Mo Kio", 
"Bishan", "Braddell", "Toa Payoh", "Novena", "Newton", "Orchard", "Somerset", "Dhoby Ghout", 
"City Hall", "Raffles Place", "Marina Bay", "Marina South Pier"]

red_times= [2, 3, 3, 4, 3, 2, 3, 3, 2, 2, 3, 5, 2, 3, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2]

circle_stations= ["Bras Basah", "Esplanade", "Promenade", "Nicoll Highway", "Stadium", 
"Mountbatten", "Dakota", "Paya Lebar", "MacPherson", "Tai Seng", "Bartley", "Serangoon", 
"Lorong Chuan", "Bishan", "Marymount", "Caldecott", "Botanic Gardens", "Farrer Road", "Holland Village", 
"Bouna Vista", "One-north", "Kent Ridge", "Haw Par Villa", "Pasir Pajang", "Labrador Park", 
"Telok Blangah", "Harbour Front"]

circle_times= [1,3,2,2,2,1,3,2,2,2,3,2,3,2,2,5,2,3,2,2,1,3,2,2,1,2]

interchanges= ["Chinatown", "Little India", "Bugis", "Outram Park", "Tampines", "Jurong East", "Newton", "Dhoby Ghout", 
"City Hall", "Raffles Place", "Tanah Merah", "Expo", "Promenade", "Bayfront", "Marina Bay", 
"Paya Lebar", "MacPherson", "Serangoon", "Bishan", "Caldecott", "Botanic Gardens", "Bouna Vista",
"Harbour Front"]

def build_graph(stations, times, graph):
    for i in range(len(stations) - 1):
        station1 = stations[i]
        station2 = stations[i + 1]
        time = times[i]

        if station1 not in graph:
            graph[station1] = {}
        if station2 not in graph:
            graph[station2] = {}

        graph[station1][station2] = time
        graph[station2][station1] = time

graph = {}

build_graph(blue_stations, blue_times, graph)
build_graph(purple_stations, purple_times, graph)
build_graph(green_stations, green_times, graph)
build_graph(red_stations, red_times, graph)
build_graph(circle_stations, circle_times, graph)

# print("Graph structure:")
# for station, connections in graph.items():
#     print(f"{station}: {connections}")