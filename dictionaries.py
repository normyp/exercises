def number(bus_stops):
    # Good Luck!
    bus = 0
    count = 0
    passengers_get_on = []
    passengers_get_off = []
    for stop in bus_stops:
        passengers_get_on.append(stop[0])
        bus += passengers_get_on[count]
        passengers_get_off.append(stop[1])
        bus -= passengers_get_off[count]
        count += 1

number([[10,0],[3,5],[5,8]])
