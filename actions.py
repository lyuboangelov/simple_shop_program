import yaml


def new_product(name, quantity, price, barcode, code):
    product_dict = {name:
                        {'quantity': int(quantity),
                         'price': int(price),
                         'barcode': int(barcode),
                         'code': int(code)
                         }
                    }
    f = open("products.yml", "a+")
    yaml.dump(product_dict, f)
    f.close()


def add_product(name, quantity):
    f = open("products.yml", "r")
    all_products = yaml.full_load(f)
    f.close()

    if name in all_products:
        old_quantity = int(all_products[name]['quantity'])
        new_quantity = int(quantity) + old_quantity
        all_products[name]['quantity'] = new_quantity
        f = open("products.yml", "w+")
        yaml.dump(all_products, f)
        f.close()
        return True
    else:
        return False


def remove_product():
    f = open("products.yml", "r")
    all_products = yaml.full_load(f)
    work_products = dict(all_products)
    f.close()
    value = input("Which value would you input name/barcode/code: ")

    if value == "name":
        name = input("Product name: ")
        if name in all_products:
            qunatity = int(input("How much quantity you want to remove?: "))
        else:
            print("Product is not available!")

    elif value == "barcode":
        barcode = int(input("Input barcode: "))
        qunatity = int(input("How much quantity you want to remove?: "))
        for key, item in all_products.items():
            check = chek_for_product(key, all_products)
            if check[0]:
                pass
            else:
                print(check[1])
                break
            for key_item, item_value in item.items():
                if item_value == barcode and key_item == "barcode":
                    work_products.pop(key)
                    break

    elif value == "code":
        code = int(input("Input code: "))
        qunatity = int(input("How much quantity you want to remove?: "))
        for key, item in all_products.items():
            check = chek_for_product(key, all_products)
            if check[0]:
                pass
            else:
                print(check[1])
                break
            for key_item, item_value in item.items():
                if item_value == code and key_item == "code":
                    work_products.pop(key)
                    break

    else:
        print("Invalid input!")

    f = open("products.yml", "w")
    yaml.dump(work_products, f)
    f.close()


def sell_product():
    total_price = 0
    sold_items = []
    f = open("products.yml", "r")
    all_products = yaml.full_load(f)
    work_products = dict(all_products)
    f.close()
    print("Type 'end' to stop selling")
    value = input("Which value would you input name/barcode/code: ")
    while not value == "end":

        if value == "name":
            name = input("Product name: ")
            if name in all_products:
                quantity = int(input("Quantity: "))
                price = all_products[name]['price']
                quantity_of_product = take_quantity(name, all_products)
            else:
                print("Product is not available!")

        elif value == "barcode":
            barcode = int(input("Input barcode: "))
            for key, item in all_products.items():
                check = chek_for_product(key, all_products)
                if check[0]:
                    pass
                else:
                    print(check[1])
                    break
                for key_item, item_value in item.items():
                    if item_value == barcode and key_item == "barcode":
                        quantity = int(input("Quantity: "))
                        price = all_products[key]['price']
                        quantity_of_product = take_quantity(key, all_products)


        elif value == "code":
            code = int(input("Input code: "))
            for key, item in all_products.items():
                check = chek_for_product(key, all_products)
                if check[0]:
                    pass
                else:
                    print(check[1])
                    break
                for key_item, item_value in item.items():
                    if item_value == code and key_item == "code":
                        quantity = int(input("Quantity: "))
                        price = all_products[key]['price']
                        quantity = take_quantity(key, all_products)

        else:
            print("Invalid input!")

        # total_price += int(price) * quantity
        print("Item sold!")
        value = input("Which value would you input name/barcode/code: ")
    return print(f"Price without VAT: {total_price}"), print(f"Price with VAT: {(total_price * 1.2):.2f}")


def inventory():
    f = open("products.yml", "r")
    all_products = yaml.full_load(f)
    for product, value in all_products.items():
        print(product)
        print(value)


def take_quantity(value, products):
    quantity = products[value]['quantity']
    return int(quantity)


def chek_for_product(key, products):
    is_valid = False
    if key in products:
        is_valid = True
        return is_valid
    else:
        return is_valid, "Product is not available!"
