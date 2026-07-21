class Employee:
    def __init__(self):
        self.empid=int(input("enter employee id"))
        self.name=input("enter employee name")
        self.basic_pay=float(input("enter basicpay amount"))
        self.ta=float(input("enter ta"))
        self.da=float(input("enter da"))
    def calc(self):
        self.gross_pay=self.basic_pay +(0.10 * self.ta)+(0.40 * self.da)
    def disp(self):
        print("\nEmployee Details")
        print("Employee ID",self.empid)
        print("Basic_pay:",self.basic_pay)
        print("TA:",self.ta)
        print("DA:",self.da)
        print("Gross pay:",self.gross_pay)
e=Employee()
e.calc()
e.disp()


