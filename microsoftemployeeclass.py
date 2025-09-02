class programmer:
    # def _getinfo_(self,name,salary,language):
    def _getinfo_(self):
        print("Microsoft")
        self.name=input("Enter your name :")
        self.salary=int(input("Enter your Salary :"))


s1=programmer()
s1._getinfo_()
print(s1)