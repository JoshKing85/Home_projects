import csv
import pandas as pd
import os
def address_file():

    with open('Address list.txt', 'w') as file:
        file.write('Josh King, 15 South Road, Weymouth, DT4 9NR,')
        file.write('\nKaren Tarrier, 15 South Road, Weymouth, DT4 9NR,')
        file.write('\nDeborah Darvell, 34 Saint Leonards Road, Weymouth, DT4 8LE')

    with open('Address list.txt', 'r') as file:
        address_list = []
        for line in file:
            
            arr = line.split(',')
            arr = [elem for elem in arr if elem != '\n']
            address_list.append(arr)

        return address_list

def create_ship_arr(add_list, add_ship_pack):
    
    ship_order_arr = [['Customer', 'Street Address', 'Town', 'Postcode', 'spice 1', 'spice 2', 'spice 3', 'spice 4']]
    
    for i in range(len(add_list)):

        temp = add_list[i] + add_ship_pack[i]
        if len(temp) ==7:
            temp.append('none')
        ship_order_arr.append(temp)
    return ship_order_arr


def shipping_list(ship_order_arr):
    with open('ship_list.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(ship_order_arr)

        return file



def create_spread_sheet(csv_file_path):
    file_path = os.path.abspath('ship_list.csv')
    try:
        data = pd.read_csv(file_path)
        excel_file = 'shipping order.xlsx'  
        data.to_excel(excel_file, index=True)
        os.startfile(excel_file)
        print(f'Excel file {excel_file} created.')

    except FileNotFoundError:
        print(f'csv file {file_path} not found.')
    
    except Exception as e:
        print(f'An error {e} occured creating spreasheet.')






 



