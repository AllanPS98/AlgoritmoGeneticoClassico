import Individuo
import math as mt
import matplotlib.pyplot as mtp


class Populacao:

    def __init__(self):
        self.list_individuos = []

    def addIndividuo(self, cromossomo):
        ind = Individuo.Individuo()
        ind.__setCromossomo__(cromossomo)
        ind.__setFenotipo__()
        self.list_individuos.append(ind)

    def __getPopulacao__(self):
        if len(self.list_individuos) != 0:
            return self.list_individuos
        return []

    def __setPopulacao__(self, populacao):
        self.list_individuos = populacao.copy()

    def __getIndividuo__(self, i):
        return self.list_individuos[i]

    def calculaFitness(self):
        for individuo in self.list_individuos:
            decimal = individuo.__getFenotipo__()
            z = 100 + mt.fabs(decimal * mt.sin(mt.sqrt(mt.fabs(decimal))))
            individuo.__setFitness__(z)

    def printPopulacao(self):
        for individuo in self.list_individuos:
            print(individuo.__getCromossomo__(), " : ", individuo.__getFenotipo__(),
                  "[ Fitness : ", individuo.__getFitness__(),
                  ", Porcentagem fitness : ", individuo.__getFitnessPorcentagem__(),
                  ", Faixa da roleta : ", individuo.__getFaixaRoleta__(), "]")

    def calculaFitnessPorcentagem(self):
        self.list_individuos.sort(key=Individuo.Individuo.__getFitness__)
        somatorio = 0
        for individuo in self.list_individuos:
            somatorio = somatorio + individuo.__getFitness__()

        for individuo in self.list_individuos:
            individuo.__setFitnessPorcentagem__((individuo.__getFitness__() / somatorio) * 100)

    def calculaAlcanceRoleta(self):
        primeiraEntrada = True
        faixaRoletaIndividuoAnterior = 0
        for individuo in self.list_individuos:
            if primeiraEntrada:
                individuo.__setFaixaRoleta__([0, individuo.__getFitnessPorcentagem__()])
                primeiraEntrada = False
            else:
                individuo.__setFaixaRoleta__([faixaRoletaIndividuoAnterior,
                                              faixaRoletaIndividuoAnterior + individuo.__getFitnessPorcentagem__()])
            faixaRoletaIndividuoAnterior = individuo.__getFaixaRoleta__()[1]

    def __getMediaPopulacao__(self):
        soma = 0
        for individuo in self.list_individuos:
            soma = soma + individuo.__getFitness__()

        return soma / len(self.list_individuos)

    def plotPopulacao(self):
        x = []
        y = []
        for individuo in self.list_individuos:
            x.append(individuo.__getFenotipo__())
            y.append(individuo.__getFitness__())

        x_original = []
        y_original = []

        # esse for virar função e vai pro AG
        for i in range(512):
            x_original.append(i)
            z = 100 + mt.fabs(i * mt.sin(mt.sqrt(mt.fabs(i))))
            y_original.append(z)

        mtp.plot(x_original, y_original)
        mtp.plot(x, y, 'r o')
        mtp.show()


