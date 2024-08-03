

class value:
    def __init__(self, value, flag):
        self.value = value
        if (flag != 1):
            self.flag = 0;
        else: self.flag = 1
    
    def __lt__(self, other):
        if (self.flag != other.flag):
            return self.flag < other.flag
        return self.value < other.value