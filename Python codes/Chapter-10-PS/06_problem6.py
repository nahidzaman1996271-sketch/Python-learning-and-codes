'''
Can you change the self-parameter inside a class to something else (say "harry").
Try changing self to "slf" or "harry" and see the effects.
'''

from random import randint

class Train:
    def __init__(slf, trainNo):         #  accept trainNo as parameter
        slf.trainNo = trainNo           #  assign it properly

    def book(self, fro, to):            
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")  # ✅ randint not random.randint


t = Train(12300)           
t.book("Dhaka", "Kuakata") 
t.getstatus()
t.getFare("Dhaka", "Kuakata")

# There is no changes...