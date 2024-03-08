class Pot:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    
    def cook(self):
        return f"{self.name} Used for cooking"
    
    
# sunking = Pot("Deep pot", "Iron")
# print(sunking.cook())