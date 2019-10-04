class employee:
    count=0
    def __init__(self,empid,empname,empsal):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
        employee.count=employee.count+1
    def display(self):
        print("the employee id is:",self.empid)
        print("the employee name is:",self.empname)
        print("the employee salary is:",self.empsal)
        print("the no. of objects in the class:",employee.count)
e1=employee(10,"ram",23400)
e1.display()
e2=employee(20,'aman',23500)
e2.display()
print(hasattr(e1,'empname'))
print(getattr(e1,'empsal'))
print(setattr(e1,'empname','shyam'))
print(delattr(e1,'empid'))
print("employee.__doc__",employee.__doc__)
print("employee.__name__",employee.__name__)
print("employee.__module__",employee.__module__)
print("employee.__bases__",employee.__bases__)
print("employee.__dict__",employee.__dict__)
    
        
    
    
