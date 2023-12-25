class Employee:
    empCount = 0

    def __init__(self, empid, name, salary):
        self.empid = empid
        self.empname = name
        self.empsalary = salary
        Employee.empCount += 1


    def dispEmployee(self):
        print("EMPID : ",self.empid,"\nNAME : ",self.empname,"\nSALARY: ",self.empsalary)

    def TotalCountOfEmployee(self):
        print("Total Employee : ",Employee.empCount)

emp1 = Employee(101,"Demo",40000)
emp1.dispEmployee()
emp2 = Employee(102,"Demo2",42000)
emp2.dispEmployee()
emp1.TotalCountOfEmployee()


#def __init__(self):
#    self.empid = 0
#   self.empname = "demo"
#    self.empsalary = 0
#    Employee.empCount += 1