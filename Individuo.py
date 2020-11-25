class Individuo:

    def __init__(self):
        self.cromossomo = []
        self.fitness = 0
        self.fitnessPorcentagem = 0
        self.faixaRoleta = []
        self.fenotipo = 0

    def __getCromossomo__(self):
        if len(self.cromossomo) != 0:
            return self.cromossomo

    def __setCromossomo__(self, cromossomo):
        self.cromossomo = cromossomo.copy()

    def __getFitness__(self):
        return self.fitness

    def __setFitness__(self, fitness):
        self.fitness = fitness

    def __getFitnessPorcentagem__(self):
        return self.fitnessPorcentagem

    def __setFitnessPorcentagem__(self, fitnessPorcentagem):
        self.fitnessPorcentagem = fitnessPorcentagem

    def __getFaixaRoleta__(self):
        return self.faixaRoleta

    def __setFaixaRoleta__(self, faixaRoleta):
        self.faixaRoleta = faixaRoleta

    def __getFenotipo__(self):
        return self.fenotipo

    def __setFenotipo__(self):
        binar = self.__getCromossomo__()
        binary = ''.join(map(str, binar))
        decimal = int(binary, 2)
        self.fenotipo = decimal

    def mudarBit(self, i):
        if self.cromossomo[i] == 1:
            self.cromossomo[i] = 0
        self.cromossomo[i] = 1

    def printCromossomo(self):
        print(self.cromossomo)


