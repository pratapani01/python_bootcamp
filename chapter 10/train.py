from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Your ticket has been booked in train No.:{self.trainNo}"
              f" from {fro} to {to}")
        

    def getStatus(self):
        print(f"Train No.: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"The fare for train No.:{self.trainNo} from {fro} to {to} is {randint(100, 1000)}")

t=Train(12345)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")