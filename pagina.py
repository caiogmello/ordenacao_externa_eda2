class pagina:
    def __init__(self):
        self.registros = []
        self.blocked = False

    def get(self, index:int) -> int:
        if (self.registros[index] is not None):
            return self.registros[index]
        return -1;

    def set(self, index:int, value:int):
        if(len(self.registros) > index):
            self.registros[index] = value

    def add(self, value:int):
        self.registros.append(value)
        
