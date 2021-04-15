class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self,speed_limit):
        self.speed_limit=self.speed_limit+'50'
        print(self.speed_limit)

    def change_gear(self):
        print("Gear changed")

lamborghini=Car("XYZ","black","Lamborghini","100")
print(lamborghini.color)
lamborghini.start()
lamborghini.accelerate("100")

    