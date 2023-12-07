blue_stations = ["Bukit Panjang","Cashew", "Hillview", "Beauty World", "King Albert Park", "Sixth Avenue", 
 "Tan Kah Kee", "Botanic Gardens", "Stevens", "Newton", "Little India", "Rochor", "Bugis", 
 "Promenade", "Bayfront", "Downtown", "Telok Ayer", "Chinatown", "Fort Canning", "Bencoolen", 
 "Jalan Besar", "Bendemeer", "Geylang Bahru", "Mattar", "MacPherson", "Ubi", "Kaki Bukit",
 "Bedok North", "Bedok Reservoir", "Tampines West", "Tampines", "Tampines East", "Upper Changi", "Expo"]

blue_times= [2,2,3,2,2,2,2,2,2,3,1,2,2,2,2,1,2,2,2,1,2,2,2,2,2,2,2,2,3,2,2,3,2]

purple_stations = ["Punggol","Sengkang", "Buangkok", "Hougang", "Kovan", "Serangoon", "Woodleigh", "Potong Pasir", "Boon Keng", "Farrer Park", 
"Little India", "Dhoby Ghout", "Clark Quay", "Chinatown", "Outram Park", "Harbour Front"]

purple_times= [4,2,2,2,3,2,1,3,2,1,1,3,2,1,4]

green_stations = ["Tuas Link","Tuas West Road", "Tuas Crescent", "Gul Circle", "Joo Koon", 
"Pioneer", "Boon Lay", "Lakeside", "Chinese Garden", "Jurong East", "Clementi", "Dover", "Buona Vista", 
"Commonwealth", "Queenstown", "Redhill", "Tiong Bahru", "Outram Park", "Tanjong Pagar", "Raffles Place", 
"City Hall", "Bugis", "Lavender", "Kallang", "Aljunied", "Paya Lebar", "Eunos", "Kembangan", 
"Bedok", "Tanah Merah", "Simei", "Tampines", "Pasir Ris"]

green_times= [3,4, 3, 3, 3, 3, 2, 3, 2, 5, 2, 3, 2, 3, 2, 3, 3, 2, 2, 2, 3, 2, 2, 3, 2, 3, 
2, 2, 3, 3, 3, 3]

red_stations= ["Jurong East","Bukit Batok", "Bukit Gombak", "Choa Chu Kang", "Yew Tee", "Kranji", 
"Marsiling", "Woodlands", "Admiralty", "Sembawang", "Canberra" ,"Yishun", "Khatib", "Yio Chu Kang", "Ang Mo Kio", 
"Bishan", "Braddell", "Toa Payoh", "Novena", "Newton", "Orchard", "Somerset", "Dhoby Ghaut", 
"City Hall", "Raffles Place", "Marina Bay", "Marina South Pier"]

red_times = [3,2, 3, 3, 4, 3, 2, 3, 3, 2, 2, 3, 5, 2, 3, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2]

circle_stations = ["Dhoby Ghaut","Bras Basah", "Esplanade", "Promenade", "Nicoll Highway", "Stadium", 
"Mountbatten", "Dakota", "Paya Lebar", "MacPherson", "Tai Seng", "Bartley", "Serangoon", 
"Lorong Chuan", "Bishan", "Marymount", "Caldecott", "Botanic Gardens", "Farrer Road", "Holland Village", 
"Buona Vista", "One-north", "Kent Ridge", "Haw Par Villa", "Pasir Pajang", "Labrador Park", 
"Telok Blangah", "Harbour Front"]

circle_times= [2,2,3,2,2,2,1,3,2,2,2,3,2,3,2,2,5,2,3,2,2,1,3,2,2,1,2]

thomson_stations = ["Woodlands North","Woodlands","Woodlands South","Springleaf","Lentor","Mayflower","Bright Hill","Upper Thomson","Caldecott","Stevens","Napier","Orchard Boulevard","Orchard","Great World","Havelock","Outram Park","Maxwell","Shenton Way","Marina Bay","Gardens by the Bay"]

thomson_times = [3,2,2,2,2,2,2,2,3,2,2,2,2,2,4,2,3,2,4]

interchanges = {
    "Chinatown":["NE3", "DT19"], "Little India": ["NE6", "DT11"], "Bugis" : ["DT13", "EW12"], "Outram Park" : ["NE2", "EW16", "TE16"], "Tampines": ["DT32", "EW2"], "Jurong East": ["NS1", "EW24"], "Newton": ["NS21", "DT10"], "Dhoby Ghaut": ["NS23", "NE5", "CC1"], "City Hall": ["NS25", "EW13"], "Raffles Place": ["NS26", "EW14"], "Tanah Merah": ["EW4"], "Expo": ["DT35"], "Promenade": ["CC4", "DT14"], "Bayfront":["CE1", "DT15"], "Marina Bay": ["NS26","TE19"], "Paya Lebar": ["CC9", "EW8"], "MacPherson": ["CC10", "DT25"], "Serangoon":["NE11", "CC13"], "Bishan":["NS17", "CC15"], "Caldecott":["CC17","TE9"], "Botanic Gardens":["CC19", "DT8"], "Buona Vista":["CC22", "EW21"],"Harbour Front":["CC29", "NE1"],"Woodlands":["NS8","TE2"],"Stevens":["TE10","DT9"],"Orchard":["TE13","NS21"]
}

def generate_station_codes(stations, line_prefix):
    station_codes = {}
    for i, station in enumerate(stations):
        code = f"{line_prefix}{len(stations) - i}"
        station_codes[station] = code
    return station_codes

def generate_station_codes_from_start(stations, line_prefix):
    station_codes = {}
    for i, station in enumerate(stations):
        code = f"{line_prefix}{i + 1}"
        station_codes[station] = code
    return station_codes

green_station_codes = generate_station_codes(green_stations, "EW")
blue_station_codes =  generate_station_codes_from_start(blue_stations, "DT")
purple_station_codes =  generate_station_codes(purple_stations, "NE")
red_station_codes =  generate_station_codes_from_start(red_stations, "NS")
circle_station_codes = generate_station_codes_from_start(circle_stations, "CC")
thomson_station_codes = generate_station_codes_from_start(thomson_stations, "TE")

station_codes = {**green_station_codes, **blue_station_codes, **purple_station_codes, **red_station_codes, **circle_station_codes,**thomson_station_codes}

def build_graph(stations, times, graph, station_codes, interchange_codes):
    for i in range(len(stations) - 1):
        station1 = stations[i]
        station2 = stations[i + 1]
        time = times[i]

        station1_code = station_codes[station1]
        station2_code = station_codes[station2]

        if station1_code not in graph:
            graph[station1_code] = {}
        if station2_code not in graph:
            graph[station2_code] = {}

        graph[station1_code][station2_code] = time
        graph[station2_code][station1_code] = time

    # Handle interchange stations
    for station in interchange_codes:
        codes = interchange_codes[station]
        for i in range(len(codes)):
            for j in range(i + 1, len(codes)):
                if codes[i] not in graph:
                    graph[codes[i]] = {}
                if codes[j] not in graph:
                    graph[codes[j]] = {}
                graph[codes[i]][codes[j]] = 0.1  
                graph[codes[j]][codes[i]] = 0.1

graph = {}

build_graph(blue_stations, blue_times, graph,blue_station_codes,interchanges)
build_graph(purple_stations, purple_times, graph,purple_station_codes,interchanges)
build_graph(green_stations, green_times, graph, green_station_codes,interchanges)
build_graph(red_stations, red_times, graph,red_station_codes,interchanges)
build_graph(circle_stations, circle_times, graph,circle_station_codes,interchanges)
build_graph(thomson_stations, thomson_times, graph,thomson_station_codes,interchanges)

# for line_codes in [green_station_codes, blue_station_codes, purple_station_codes, red_station_codes, circle_station_codes]:
#     for station, code in line_codes.items():
#         print(f"{station}: {code}")