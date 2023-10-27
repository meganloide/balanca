def read_filizola_smart_file(pycharm):
    products = []
    with open(pycharm, 'r') as file:
        for line in file:
            code = line[:6]
            product_type = line[6]
            description = line[7:29].strip()
            price = line[29:36]
            validity = line[36:39]
            products.append((code, product_type, description, price, validity))
    return products

def read_toledo_mgv6_file(pycharm):
    products = []
    with open(pycharm, 'r') as file:
        for line in file:
            department_code = line[:2]
            product_type = line[2]
            code = line[3:9]
            price = line[9:15]
            validity = line[15:18]
            description = line[18:68].strip()
            extra_info_code = line[68:74]
            image_code = line[74:78]
            nutritional_info_code = line[78:84]
            products.append((department_code, product_type, code, price, validity, description, extra_info_code, image_code, nutritional_info_code))
    return products

def read_urano_integra_file(pycharm):
    products = []
    with open(pycharm, 'r') as file:
        for line in file:
            code = line[:6]
            flag = line[6]
            product_type = line[7]
            description = line[8:28].strip()
            price = line[28:37].replace(",", ".")
            validity1 = line[37:42]
            validity2 = line[42]
            products.append((code, flag, product_type, description, price, validity1, validity2))
    return products

def write_filizola_smart_file(products, pycharm):
    with open(pycharm, 'w') as file:
        for product in products:
            code, product_type, description, price, validity = product
            price = f"{float(price):07.2f}".replace(".", "")
            file.write(f"{code}{product_type}{description}{price}{validity}\n")

def write_toledo_mgv6_file(products, pycharm):
    with open(pycharm, 'w') as file:
        for product in products:
            department_code, product_type, code, price, validity, description = product
            price = f"{float(price):06.2f}".replace(".", "")
            file.write(f"{department_code}{product_type}{code}{price}{validity}{description}\n")

def write_urano_integra_file(products, pycharm):
    with open(pycharm, 'w') as file:
        for product in products:
            code, flag, product_type, description, price, validity1, validity2 = product
            price = f"{float(price):09.2f}".replace(".", ",")
            file.write(f"{code}{flag}{product_type}{description}{price}{validity1}{validity2}\n")

def main():

    products_filizola = read_filizola_smart_file("CADTXT.TXT")
    products_toledo = read_toledo_mgv6_file("ITENSMGV.TXT")
    products_urano = read_urano_integra_file("PRODUTOS.TXT")
    write_filizola_smart_file(products_filizola, "CADTXT_OUTPUT.TXT")
    write_toledo_mgv6_file(products_toledo, "ITENSMGV_OUTPUT.TXT")
    write_urano_integra_file(products_urano, "PRODUTOS_OUTPUT.TXT")

if __name__ == "__main__":
    main()
