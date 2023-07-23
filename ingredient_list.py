'''
@Author = Jabeena Lalsab Moolimani
@Modified Date = 19-July-2023
@Last Mobified by = Jabeena L M
@Title : Inventry Management(creating ingredients list, displaying, writing into json and calculating the item price based on quantity)

'''

import pandas as pd
import json

#class for creating ingredients list, displaying, writing into json and calculating the item price based on quantity

ingrediants_list = {}

class Inventry:

#creating dictionary for ingredients    
    def create_ingrediants_list(self):

        
        count = int(input("Enter the number of ingrediants:"))

        while count > 0:

            ingrediant_name = input("Enter the ingrediant name: ")

            if ingrediant_name not in ingrediants_list.keys():

                ingrediants_list[ingrediant_name] = {}

                name = input("Enter the type of ingrediant name: ")
                ingrediants_list[ingrediant_name]['Ingrediant Type'] = name

                price = float(input("Enter the price per kg: "))
                ingrediants_list[ingrediant_name]['Price/kg'] = price

                count -= 1

            else:
                count = count

        return ingrediants_list
    

#Display of ingredients list
    def display_ingrediant_list(self):
        print(ingrediants_list)
        df = pd.DataFrame(ingrediants_list)
        print(df)


#writing data to json file
    def write_to_json(self):
        json_obj = json.dumps(ingrediants_list, indent=4)
        with open("Inventory.json", 'w') as output:
            output.write(json_obj)


#writing data to json file (data from calculate_item_price function)
    def write_to_json_Total_price(self):
        json_obj = json.dumps(ingrediants_list, indent=4)
        with open("management.json", 'w') as output:
            output.write(json_obj)


#calculate the total price of items based on quantity(kg)
    def calculate_item_price(self):
        count = int(input("Enter the number of ingrediants:"))

        while count > 0:
            ingrediant_name = input("Enter the ingrediant name which you want to calculate the price: ")
            
            if ingrediant_name in ingrediants_list.keys():
                quantity = int(input("How much KG you want : "))
                total_price = ingrediants_list[ingrediant_name]['Price/kg'] * quantity
                ingrediants_list[ingrediant_name]['Total Price'] = total_price

                count -= 1

            else:
                print("item is not there in the list")
                continue

        return ingrediants_list

            











        

