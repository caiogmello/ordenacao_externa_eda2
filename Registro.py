

class Registro:
    def __init__(self, value: int):
        self.value = value
        self.flag = 0

    def setFlag(self):
        self.flag = 1

    def delFlag(self):
        self.flag = 0
    
    def __lt__(self, other: 'Registro') -> bool:
        if (self.flag != other.flag):
            return self.flag < other.flag
        return self.value < other.value