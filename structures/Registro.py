class Registro:
    def __init__(self, value: int):
        self.value = value
        self.flag = 0
        self.index = None

    def setFlag(self):
        self.flag = 1

    def delFlag(self):
        self.flag = 0

    def setIndex(self, index:int):
        self.index=index
    
    def __lt__(self, other: 'Registro') -> bool:
        if (self.flag != other.flag):
            return self.flag < other.flag
        return self.value < other.value
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)