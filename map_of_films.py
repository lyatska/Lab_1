import folium

def map_list():
    coordinates = []
    coordinates2 = []
    coordinates3 = []
    new_lst = []
    also_map = []
    new = []
    all = []
    next_map = []
    all_locations = open("locations.list",encoding = 'utf-8', errors ='ignore').readlines()
    all_locations = [ x.replace('\n', '').replace('(#', '') for x in all_locations ]

    locations = {}
    for i in range(len(all_locations)):
        lines = all_locations[i].strip()
        lines = all_locations[i].split()
        new_lst.append(lines)
    for j in range(len(new_lst)):
        for k in new_lst[j]:

            if k.startswith('"#'):
                new_lst[j].remove(k)
            if k.startswith('{'):
                el1 = new_lst[j].index(k)
            if k.endswith('}'):
                el2 = new_lst[j].index(k)
                del new_lst[j][el1:el2+1]

            if new_lst[j][-1].endswith(')') and new_lst[j][-2].startswith('('):
                new_lst[j] = new_lst[j][:-2]
            if new_lst[j][-1].endswith(')') and new_lst[j][-1].startswith('('):
                new_lst[j] = new_lst[j][:-1]

            for k in new_lst[j]:
                if k.startswith('(') and len(k) == 6 and k[-3].startswith('('):
                    if k in locations:
                        locations[k].append(' '.join(new_lst[j][-2:]))
                    else:
                        locations[k] = [' '.join(new_lst[j][-2:])]

                if k.startswith('(') and len(k) == 6:
                        if k in locations:
                            locations[k].append(' '.join(new_lst[j][-3:]))
                        else:
                            locations[k] = [' '.join(new_lst[j][-3:])]

    locations1 = locations.get('(1895)')

    for i in range(len(locations1)):
        if locations1[i] not in all:
            all.append(locations1[i])

    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout = None,scheme = 'http')
    for location in range(len(all)):
        try:

            location3 = geolocator.geocode(all[location])
            location3 =   [location3.latitude, location3.longitude]
            coordinates.append(location3)
        except AttributeError:
            continue


    locations2 = locations.get('(1905)')
    for i in range(len(locations2)):
        if locations2[i] not in next_map:
            next_map.append(locations2[i])

    geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout = None,scheme = 'http')
    for loc in range(len(next_map)):
        try:

            location4 = geolocator.geocode(next_map[loc])
            location4 =   [location4.latitude, location4.longitude]
            coordinates2.append(location4)
        except AttributeError:
            continue


    locations5 = locations.get('(1920)')
    for i in range(len(locations5)):
        if locations5[i] not in also_map:
            also_map.append(locations5[i])

    geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout = None,scheme = 'http')
    for locat in range(len(also_map)):
        try:

            location6 = geolocator.geocode(also_map[locat])
            location6 =   [location6.latitude, location6.longitude]
            coordinates3.append(location6)
        except AttributeError:
            continue


    map = folium.Map()
    fg_hc = folium.FeatureGroup(name="Films of 1895")
    for coord in range(len(coordinates)):

        fg_hc.add_child(folium.CircleMarker(location= coordinates[coord],
                            radius=10,
                            popup="1895 рік"+"\n",
                            fill_color = 'red',
                            color='red',
                            fill_opacity=0.5))

    fg = folium.FeatureGroup(name="Films of 1905")
    for coords in range(len(coordinates2)):

        fg.add_child(folium.CircleMarker(location= coordinates2[coords],
                            radius=10,
                            popup="1905 рік"+"\n",
                            fill_color = 'blue',
                            color='blue',
                            fill_opacity=0.5))

    fg3 = folium.FeatureGroup(name="Films of 1920")
    for coordi in range(len(coordinates3)):

        fg3.add_child(folium.CircleMarker(location= coordinates3[coordi],
                            radius=10,
                            popup="1920 рік"+"\n",
                            fill_color = 'green',
                            color='green',
                            fill_opacity=0.5))

    map.add_child(fg_hc)
    map.add_child(fg3)
    map.add_child(fg)
    map.add_child(folium.LayerControl())
    map.save('Films_map.html')

print(map_list())
