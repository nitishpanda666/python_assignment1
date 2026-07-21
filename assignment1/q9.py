class product:
    def input(self):
        self.product_no=int(input("enter product number"))
        self.product_name=input("enter product number")
        self.cost=float(input("enter product cost"))
        self.quantity=int(input("enter Quantity"))
    def calculate(self):
        self.total_amount=self.cost*self.quantity
    def display(self):
        print("product No",self.product_no)
        print("product Name",self.product_name)
        print("product cost",self.cost)
        print("Quantity",self.quantity)
        print("Total Amount",self.total_amount)
products=[]
for i in range(5):
    print("/nEnter Product",i+1)
    p=product()
    p.input()
    p.calculate()
    products.append(p)
highest=products[0]
pno=products[0]
for p in products:
    if p.total_amount>highest.total_amount:
         highest=p
         pno=p
print("/nproduct with highest total Amount")
highest.display()
pno.display()


