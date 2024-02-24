
from base_k import Database


def insert():
    region = f"""CREATE TABLE region(
        region_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        last_update TIMESTAMP DEFAULT now());"""

    district = f"""CREATE TABLE district(
        district_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        region_id INT   REFERENCES region(region_id),
        last_update TIMESTAMP DEFAULT now());"""

    address = f"""CREATE TABLE address(
        address_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        district_id INT   REFERENCES district(district_id),
        last_update TIMESTAMP DEFAULT now());"""

    category = f"""CREATE TABLE category(
        category_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        description TEXT,
        last_update TIMESTAMP DEFAULT now());"""

    price_type = f"""CREATE TABLE price_type(
        price_type_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        last_update TIMESTAMP DEFAULT now());"""

    product = f"""CREATE TABLE product(
        product_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        price NUMERIC,
        made DATE,
        term SMALLINT,
        price_type_id INT REFERENCES price_type(price_type_id),
        last_update TIMESTAMP DEFAULT now());"""

    product_category = f"""CREATE TABLE product_category(
        product_category_id SERIAL PRIMARY KEY,
        product_id INT REFERENCES product(product_id),
        category_id INT REFERENCES category(category_id),
        last_update TIMESTAMP DEFAULT now());"""

    staff = f"""CREATE TABLE staff(
        staff_id SERIAL PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(25),
        birt_date DATE,
        level SMALLINT,
        last_update TIMESTAMP DEFAULT now());"""

    smena = f"""CREATE TABLE smena(
        smena_id SERIAL PRIMARY KEY,
        title VARCHAR(20),
        start_time TIME,
        end_time TIME,
        last_update TIMESTAMP DEFAULT now());"""

    staff_smena = f"""CREATE TABLE staff_smena(
        staff_smena_id SERIAL PRIMARY KEY,
        staff_id INT REFERENCES staff(staff_id),
        smena_id INT REFERENCES smena(smena_id),
        last_update TIMESTAMP DEFAULT now());"""      #level -- ishchining tajribasi

    check = f"""CREATE TABLE checks(
        check_id SERIAL PRIMARY KEY,
        staff_id INT REFERENCES staff(staff_id),
        address_id INT REFERENCES address(address_id));"""

    products_check = f"""CREATE TABLE products_check(
        products_check_id SERIAL PRIMARY KEY,
        product_id INT REFERENCES product(product_id),
        check_id INT REFERENCES checks(check_id),
        count NUMERIC,
        product_price NUMERIC,
        last_update TIMESTAMP DEFAULT now());"""

    payment_type = f"""CREATE TABLE payment_type(
        payment_type_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        last_update TIMESTAMP DEFAULT now());"""

    check_payment = f"""CREATE TABLE check_payment(
        check_payment_id SERIAL PRIMARY KEY,
        check_id INT REFERENCES checks(check_id),
        payment_type_id INT REFERENCES payment_type(payment_type_id));"""

    data = {
        "region": region,
        "district": district,
        "address": address,
        "category": category,
        "price_type": price_type,
        "product": product,
        "product_category": product_category,
        "staff": staff,
        "smena": smena,
        "staff_smena": staff_smena,
        "check": check,
        "products_check": products_check,
        "payment_type": payment_type,
        "check_payment": check_payment
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


# if __name__ == "__main__":
#     insert()
