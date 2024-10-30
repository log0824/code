def start(gas, distance):
    t_gas = 0
    t_distance = 0
    cur_gas = 0
    index = 0
    for i in range(len(gas)):
        t_gas += gas[i]
        t_distance += distance[i]
        cur_gas += gas[i] - distance[i]

        if cur_gas < 0:
            cur_gas = 0
            index += 1

    if t_gas < t_distance: 
        return -1
    return index

gas = [4, 6, 7, 4]
distance = [6, 5, 3, 5]
print("start = " + str(start(gas, distance)))