

class Registro:
    def __init__(self, value: int, flag: int = None):
        self.value = value
        self.flag = 1 if flag is not None else 0
    
    def __lt__(self, other: 'Registro') -> bool:
        if (self.flag != other.flag):
            return self.flag < other.flag
        return self.value < other.value