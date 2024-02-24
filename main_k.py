
import classes_k as cl


def insertion_check_payment():
    check_id = int(input("\t\tCheck id: "))
    payment_type_id = int(input("\t\tPayment type id: "))
    chp = cl.CheckPayment(check_id, payment_type_id)
    return chp.insert()


def insertion_payment_type():
    name = input("\t\tTolov turi nomi: ")
    pt = cl.PaymentType(name)
    return pt.insert()


def insertion_products_check():
    product_id = int(input("\t\tProduct id: "))
    check_id = int(input("\t\tCheck id: "))
    count = float(input("\t\tMiqdori (Necha kg, litr, dona): "))
    product_check = cl.ProductCheck(product_id, check_id, count)
    return product_check.insert()


def insertion_check():
    staff_id = int(input("\t\tStaff id: "))
    address_id = int(input("\t\tAddress id: "))
    check = cl.Check(staff_id, address_id)
    return check.insert()


def insertion_staff_smena():
    staff_id = int(input("\t\tStaff id: "))
    smena_id = int(input("\t\tSmena id: "))
    ss = cl.StaffSmena(staff_id, smena_id)
    return ss.insert()


def insertion_smena():
    title = input("\t\tsmena nomi (tongi, tushgi, kechki): ")
    start_time = input("\t\tBoshlanish vaqti: ")
    end_time = input("\t\tTugash vaqti: ")
    smena = cl.Smena(title, start_time, end_time)
    return smena.insert()


def insertion_staff():
    first_name = input("\t\tFirst name: ")
    last_name = input("\t\tLast name: ")
    birt_date = input("\t\tTug'ilgan yil-oy-kun: ")
    level = int(input("\t\tTajribasi: "))
    staff = cl.Staff(first_name, last_name, birt_date, level)
    return staff.insert()


def insertion_product_category():
    product_id = int(input("\t\tProduct id: "))
    category_id = int(input("\t\tCategory id: "))
    pc = cl.ProductCategory(product_id, category_id)
    return pc.insert()


def insertion_product():
    name = input("\t\tProduct name: ")
    price = float(input("\t\tProduct price 1 birlik uchun: "))
    made = input("\t\tIshlab chiqarilgan masalan(2020-12-11): ")
    term = int(input("\t\tYaroqligi (oy): "))
    price_type_id = int(input("\t\tPrice type id:"))
    product = cl.Product(name, price, made, term, price_type_id)
    return product.insert()


def insertion_price_type():
    name = input("\t\tBirlikda o'lchanishi(kilogramm, litr, dona): ")
    price_type = cl.PriceType(name)
    return price_type.insert()


def insertion_category():
    name = input("\t\tCategory name: ")
    description = input("\t\tDescription: ")
    category = cl.Category(name, description)
    return category.insert()


def insertion_address():
    name = input("\t\tAdress name: ")
    district_id = int(input("\t\tDistrict id: "))
    address = cl.Address(name, district_id)
    return address.insert()


def insertion_district():
    name = input("\t\t District name: ")
    region_id = int(input("\t\t Region id: "))
    district = cl.District(name, region_id)
    return district.insert()


def insertion_region():
    name = input("\t\tRegion name: ")
    region = cl.Region(name)
    return region.insert()


def insertion(table):
    if table == "region":
        return insertion_region()

    elif table == "district":
        return insertion_district()

    elif table == "address":
        return insertion_address()

    elif table == "category":
        return insertion_category()

    elif table == "price_type":
        return insertion_price_type()

    elif table == "product":
        return insertion_product()

    elif table == "product_category":
        return insertion_product_category()

    elif table == "staff":
        return insertion_staff()

    elif table == "smena":
        return insertion_smena()

    elif table == "staff_smena":
        return insertion_staff_smena()

    elif table == "check":
        return insertion_check()

    elif table == "products_check":
        return insertion_products_check()

    elif table == "payment_type":
        return insertion_payment_type()

    elif table == "check_payment":
        return insertion_check_payment()

    else:
        print("<--- Aniqlanmagan buyruq --->")
        return insertion(table)


def task(table):
    choose = input("""
        <--- Tanalng --->
        1. SELECT
        2. INSERT
        3. DELETE
        4. UPDATE
        
        0.back
          =>> """)
    if choose == "1":
        for i in  cl.Base.select(table):
            print("=> ", i)
        return task(table)

    elif choose == "2":
        print(insertion(table))
        return task(table)

    elif choose == "3":
        column = input("\t\tColumn name: ")
        data = input("\t\tCondition: ")

        try:
            data = int(data)

        except ValueError or TypeError:
            data = str(data)
        print("Status: ", cl.Base.delete(column, data, table))
        return task(table)

    elif choose == "4":
        print("\t\t<--- Turli hil yo'llar orqali update qilish mumkin --->")
        query = input("\t\tQuery: ")
        print(cl.Base.update(query))

    elif choose == "0":
        return main()

    else:
        print("\t\t<--- Bunday buyruq mavjud emas --->")
        return task(table)


def main():
    choose = input("""
        1. region
        2. district
        3. address
        4. category
        5. price_type
        6. product
        7. product_category
        8. staff
        9. smena
        10. staff_smena
        11. checks
        12. product_check
        13. payment_type
        14 check_payment
            =>> """)

    data = {
        "1": "region",
        "2": "district",
        "3": "address",
        "4": "category",
        "5": "price_type",
        "6": "product",
        "7": "product_category",
        "8": "staff",
        "9": "smena",
        "10": "staff_smena",
        "11": "checks",
        "12": "products_check",
        "13": "payment_type",
        "14": "check_payment"
    }

    if choose in data.keys():
        task(data[choose])


if __name__ == "__main__":
    main()