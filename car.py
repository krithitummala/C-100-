class Car(object):
    def __init__(self,modal,color,company,speed_limit):
        self.modal = modal
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
    
    def start(self):
        print("started")
    
    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating")

    def speed_limit(self,speed_limit):
        print(int(speed_limit))

BMV = Car("A5","black","BMV",60)
BMV.start()
BMV.speed_limit(60)