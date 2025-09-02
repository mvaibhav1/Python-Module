from random import randint

class train :
    def __init__(sel,trainNo):
        sel.trainNo=trainNo

    
    def book(sf,fro,to):
        print(f"ticket is booked in train no. {self.trainNo} from {fro} to {to}")

    def getstatus(self) :
        print(f"train no.  : {self.trainNo} is running on time .")

    def getfare(self,fro,to):
        print(f"Ticket fair in train no. {self.trainNo} from {fro} to {to} is {randint(222,6000)}")

t=train(555)
t.book("delhi","vrindavan")
t.getfare("Delhi","vrindavan")