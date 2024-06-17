class employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = fname + lname + "@gmail.com"

    def fullname(self):
        return self.fname + " " + self.lname

emp1 = employee("sachindu", "kavishka")

print(emp1.fullname())
print(emp1.fname)
print(employee.fullname(emp1))