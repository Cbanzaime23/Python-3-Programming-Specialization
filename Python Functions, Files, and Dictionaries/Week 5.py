
# nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
#
# nums_sorted_lambda = sorted(nums, key = lambda str : str[-1], reverse = True)
#
# print(nums)
# print(nums_sorted_lambda)

#
# weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
#            'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
#            'Cairo': {'temp': 96, 'condition': 'sunny'},
#            'Berlin': {'temp': 89, 'condition': 'sunny'},
#            'Caloocan': {'temp': 78, 'condition': 'sunny'}}
#
# sorted_weather = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse=True)
#
# print(sorted_weather)


# def s_cities_count(city_list):
#     """ This function return the number of instance of "S" in a city_list
#     """
#
#     ct = 0
#     for city in city_list:
#         if city[0] == "S":
#             ct += 1
#     return ct
#
# states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
#           "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
#           "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}
#
# print(sorted(states, key=lambda state: s_cities_count(states[state])))



ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key = lambda id: str(id)[-4:])
