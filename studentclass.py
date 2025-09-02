class student():
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def display_info(self):
        print(f"Name : {self.name}, Age : {self.age}, Grade : {self.grade}")

s1=student("Alice",20,"A")
s2=student("Sam", 25,"B")
s1.display_info()
s2.display_info()