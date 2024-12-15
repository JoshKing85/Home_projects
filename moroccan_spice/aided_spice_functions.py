from itertools import combinations
from my_spice_functions import *


def asort_boxes(spice_list):
    box_list =[[], [], []]
    
    for box_num in range(3):
        for spice_comb in combinations(spice_list, 3):
            if sum(spice_comb) == 250:
                box_list[box_num]= list(spice_comb)
                for spice in box_list[box_num]:
                    spice_list.remove(spice)
                break
    
    box_list[2] = spice_list
    return box_list


