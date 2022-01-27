"ร้านขายไก่เกาหลีเเห่งหนึ่ง มีสินค้าประกอบด้วย *ไก่ทอด*, *นักเก็ต* ถ้า*ลูกค้า*ซื้อครบ 7 อย่าง จะมีราคาทั้งหมด 100 บาท ร้านนี้มี*พนักงาน* 2 คน "

class chicken:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price

class nugget:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price

class customer:
    def __init__(self, age, favorite):
        self.age = age
        self.favorite = favorite

class employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

chicken1 = chicken("bonchon", 15)
chicken1.flavor = "mala"

nugget1 = nugget("mala", 15)
nugget1.price = 20

customer1 = customer(20, "bonchon")
customer1.favorite = "mala"

employee1 = employee("pisitpong", "rayong")
employee1.address = "muang"


    