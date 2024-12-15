from my_spice_functions import *
from aided_spice_functions import *
from address_functions import *
import os

spice_list = create_spice_list()
ship_packets = asort_boxes(spice_list)

if weigh_boxes(ship_packets):
    print('Boxes ready to ship')
    ship_add = address_file()


ship_arr = create_ship_arr(ship_add, ship_packets)
ship_csv = shipping_list(ship_arr)
create_spread_sheet(ship_csv)

