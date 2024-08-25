class fileManager:

    @staticmethod
    def read(filePath:str) -> tuple:

        f = open(filePath, 'r')

        mode = f.readline()[0]
        specs = [int(x) for x in f.readline().split()]
        numbers = [int(x) for x in f.readline().split()]  
        f.close()

        return mode, specs, numbers
        

