class Math:

    def self.__init__(x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        print("You are subtracting")
        return self.x - self.y

    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        return self.x/self.y