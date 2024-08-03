

class Registro:
    def __init__(self, value: int, flag: int):
        self.value = value
        if (flag != 1):
            self.flag = 0
        else: self.flag = 1
    
    def __lt__(self, other: 'Registro') -> bool:
        if (self.flag != other.flag):
            return self.flag < other.flag
        return self.value < other.value