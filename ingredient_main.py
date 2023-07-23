from ingredient_list import Inventry

if __name__ == '__main__':
    print("Welcome to Inventory Management")

    inventry_obj = Inventry()

    while True:
        option = int(input("1:Create Ingrediant list\n2:Display List\n3:Write to JSON file\n4:Calculate price of the item\n5:JSON Total Price\n6:Exit the code\n"))

        if option == 1:
            inventry_obj.create_ingrediants_list()

        elif option == 2:
            inventry_obj.display_ingrediant_list()

        elif option == 3:
            inventry_obj.write_to_json()

        elif option == 4:
            inventry_obj.calculate_item_price()

        elif option == 5:
            inventry_obj.write_to_json_Total_price()

        elif option == 6:
            break