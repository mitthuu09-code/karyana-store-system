class Bill:
    def __init__(self, shop_name, customer_name, stock):
        self.shop_name = shop_name
        self.customer_name = customer_name
        self.total = 0
        self.items = []
        self.discount = 0
        self.stock = stock

    def bill_save_kro(self):
        file_name = f"{self.customer_name}.txt"
        file = open(file_name, "a")
        file.write(f"---{self.shop_name}---\n")
        file.write(f"customer:{self.customer_name}---\n")
        for cheez, price in self.items:
            file.write(f"-{cheez}:{price}\n")
        file.write(f"Total:{self.total}\n")
        file.write(f"discount:{self.discount}\n")
        file.write(f"FINAL TOTAL:{self.total-self.discount}")
        file.close()
        print(f"file name is :{file_name}")

    def saman_add_kro(self, name, price, qty, stock):
        if name not in self.stock:
            print("ye saman nhi hai")
            return
        if self.stock[name] < qty:
            print(f"{name} ka stock kamm hai,sirf {self.stock[name]} hai")
            return
        # self.total = self.total + price
        # self.items.append((name, price))

        self.stock[name] = self.stock[name] - qty
        total_price = price * qty
        self.total = self.total + total_price
        self.items.append((name, total_price))
        print(f"{name}x{qty}={total_price}\t|bacha stock:{self.stock[name]}")

    def discount_add_kro(self):
        # self.discount = discount
        # print(f"{discount} ka dicount ho gia")
        if self.total >= 3500:
            self.discount = self.total * 0.10
            print(f"automatic 10% Discount lagg gia:{self.discount}")
        else:
            ("No discount")

    def khatam_bill(self):
        print(f"----{self.shop_name}---")
        print(f"customer:{self.customer_name}")
        for items, price in self.items:
            print(f"-{items} : {price}")
        print(f"TOTAL:{self.total}")
        print(f"Discount:{self.discount}")
        print(f"FINAL TOTAL:{self.total-self.discount}")

stock = {"football": 5, "bat": 3}

while True:
    name = input("Enter customer name:\t\n(bs krne keliye 'ok' likho):")
    if name == "ok":
        print("Shop Close")
        break

    bill1 = Bill("Talha karyana store", name, stock)

    while True:
        cheez = input("Customer ne kia cheez li hai:\t\n(bs krne keliye 'ok' likho):\n")
        if cheez == "ok":
            break
        qty = int(input("kitni qty chayie :"))
        price = int(input("Price kitni hai cheez ki:"))
        bill1.saman_add_kro(cheez, price, qty, stock)

    bill1.discount_add_kro()
    bill1.khatam_bill()
    bill1.bill_save_kro()
print(f"remain Stock:{stock}")
