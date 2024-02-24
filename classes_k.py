import psycopg2
from base_k import Database
import os
from dotenv import load_dotenv

load_dotenv()

class Base:
    @staticmethod
    def select(table: str):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column: str, data: str, table: str):
        if isinstance(data, str):
            query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""

        else:
            query = f"""DELETE FROM {table} WHERE {column} = {data};"""

        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Region(Base):
    def __init__(self, name: str):
        self.name = name

    def insert(self):
        query = f"""INSERT INTO region(name) VALUES('{self.name}');"""
        return Database.connect(query, "insert")


class District(Region):
    def __init__(self, name: str, region_id: int):
        super().__init__(name)
        self.region_id = region_id

    def insert(self):
        query = f"""INSERT INTO district(name, region_id) VALUES('{self.name}', '{self.region_id}');"""
        return Database.connect(query, "insert")


class Address(Region):
    def __init__(self, name: str, district_id: int):
        super().__init__(name)
        self.district_id = district_id

    def insert(self):
        query = f"""INSERT INTO address(name, district_id) VALUES('{self.name}', '{self.district_id}');"""
        return Database.connect(query, "insert")


class Category(Region):
    def __init__(self, name: str, description: str):
        super().__init__(name)
        self.description = description

    def insert(self):
        query = f"""INSERT INTO category(name, description) VALUES('{self.name}', '{self.description}');"""
        return Database.connect(query, "insert")


class PriceType(Region):
    def __init__(self, name: str):
        super().__init__(name)

    def insert(self):
        query = f"""INSERT INTO price_type(name) VALUES('{self.name}');"""
        return Database.connect(query, "insert")


class Product(Base):
    def __init__(self, name: str, price: float, made: str, term: int, price_type_id: int):
        self.name = name
        self.made = made
        self.term = term
        self.price = price
        self.price_type_id = price_type_id

    def insert(self):
        query = f"""INSERT INTO product(name, price, made, term, price_type_id) VALUES('{self.name}', '{self.price}', '{self.made}', '{self.term}', '{self.price_type_id}');"""
        return Database.connect(query, "insert")


class ProductCategory(Base):
    def __init__(self, product_id: int, category_id: int):
        self.product_id = product_id
        self.category_id = category_id

    def insert(self):
        query = f"""INSERT INTO product_category(product_id, category_id) VALUES('{self.product_id}', '{self.category_id}');"""
        return Database.connect(query, "insert")


class Staff(Base):
    def __init__(self, first_name: str, last_name: str, birt_date: str, level: int):
        self.first_name = first_name
        self.last_name = last_name
        self.birt_date = birt_date
        self.level = level

    def insert(self):
        query = f"""INSERT INTO staff(first_name, last_name, birt_date, level) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.birt_date}', '{self.level}');"""
        return Database.connect(query, "insert")


class Smena(Base):
    def __init__(self, title: str, start_time: str, end_time: str):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

    def insert(self):
        query = f"""INSERT INTO smena(title, start_time, end_time) VALUES('{self.title}', '{self.start_time}', '{self.end_time}');"""
        return Database.connect(query, "insert")


class StaffSmena(Base):
    def __init__(self, staff_id: int, smena_id: int):
        self.staff_id = staff_id
        self.smena_id = smena_id

    def insert(self):
        query = f"""INSERT INTO staff_smena(staff_id, smena_id) VALUES('{self.staff_id}', '{self.smena_id}');"""
        return Database.connect(query, "insert")


class Check(Base):
    def __init__(self, staff_id: int, address_id: int):
        self.staff_id = staff_id
        self.address_id = address_id

    def insert(self):
        query = f"""INSERT INTO checks(staff_id, address_id) VALUES('{self.staff_id}', '{self.address_id}');"""
        return Database.connect(query, "insert")


class ProductCheck(Base):
    def __init__(self, product_id: int, check_id: int, count: float):
        self.product_id = product_id
        self.check_id = check_id
        self.count = count

        product_price = Database.connect(f"SELECT price FROM product WHERE product_id = {self.product_id};", "select")
        self.product_price = count * product_price[0][0]

    def insert(self):
        query = f"""INSERT INTO product_check(product_id, check_id, count, product_price) 
        VALUES('{self.product_id}', '{self.check_id}', '{self.count}', '{self.product_price}');"""

        return Database.connect(query, "insert")


class PaymentType(Base):
    def __init__(self, name: str):
        self.name = name

    def insert(self):
        query = f""" INSERT INTO payment_type(name) VALUES('{self.name}');"""
        return Database.connect(query, "insert")


class CheckPayment(Base):
    def __init__(self, check_id: int, payment_type_id: int):
        self.check_id = check_id
        self.payment_type_id = payment_type_id

    def insert(self):
        query = f"""INSERT INTO check_payment(check_id, payment_type_id) VALUES('{self.check_id}', '{self.payment_type_id}');"""
        return Database.connect(query, "insert")
