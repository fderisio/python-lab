def selection_sort(a_list):
    for fills_lot in range(len(a_list) - 1, 0, -1):
        position_max=0
        for location in range(1, fills_lot+1):
            if a_list[location] > a_list[position_max]:
                position_max = location

        temp = a_list[fills_lot]
        a_list[fills_lot] = a_list[position_max]
        a_list[position_max] = temp
    return a_list
