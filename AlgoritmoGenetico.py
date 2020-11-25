import Populacao
import Individuo
import matplotlib.pyplot as mtp
import random as rnd
import math as mt


class AlgoritmoGenetico:

    def __init__(self):
        self.taxaCruzamento = 0
        self.taxaMutacao = 0
        self.geracoes = 0
        self.populacao = []

    def executaAG(self, tam_populacao, tam_cromossomo, geracoes, taxaCruzamento, taxaMutacao):
        self.populacao = self.criarPopulacao(tam_populacao, tam_cromossomo)
        self.calulos()
        self.geracoes = geracoes
        self.taxaCruzamento = taxaCruzamento
        self.taxaMutacao = taxaMutacao
        i = 0
        while i < self.geracoes:
            nova_geracao = []
            print("Geracao {}".format(i + 1))
            while len(nova_geracao) < tam_populacao:
                pai, mae = self.roleta()
                #print("roletou")
                #print(pai, mae)
                if pai is not None and mae is not None:
                    filho1, filho2 = self.cruzamento(pai, mae, taxaCruzamento, tam_cromossomo)
                    #print("cruzou", filho2, filho1)
                    if filho1 is not None and filho2 is not None:
                        f1, f2 = self.mutacao(filho1, filho2, taxaMutacao, tam_cromossomo)
                        #print("mutou")
                        nova_geracao.append(f1)
                        nova_geracao.append(f2)
            self.populacao.__setPopulacao__(nova_geracao)
            #print("adicionou nova geracao")
            self.calulos()
            i += 1

    def roleta(self):
        pai = rnd.random() * 100
        mae = rnd.random() * 100
        selecao1 = None
        selecao2 = None
        #print(pai)
        #print(mae)
        for individuo in self.populacao.__getPopulacao__():
            #print(individuo.__getFaixaRoleta__())
            if individuo.__getFaixaRoleta__()[1] >= pai > individuo.__getFaixaRoleta__()[0]:
                #print("entrou selecao 1")
                selecao1 = individuo
            elif individuo.__getFaixaRoleta__()[1] >= mae > individuo.__getFaixaRoleta__()[0]:
                #print("entrou selecao 2")
                selecao2 = individuo
        return selecao1, selecao2

    def cruzamento(self, pai, mae, taxaCruzamento, tam_cromossomo):
        if rnd.random() < taxaCruzamento:
            ponto_de_corte = rnd.randint(1, tam_cromossomo)
            filho1 = Individuo.Individuo()
            filho2 = Individuo.Individuo()
            filho1.__setCromossomo__(pai.__getCromossomo__()[:ponto_de_corte] + mae.__getCromossomo__()[ponto_de_corte:])
            filho1.__setFenotipo__()
            filho2.__setCromossomo__(mae.__getCromossomo__()[:ponto_de_corte] + pai.__getCromossomo__()[ponto_de_corte:])
            filho2.__setFenotipo__()
            return filho1, filho2
        return None, None

    def mutacao(self, filho1, filho2, taxaMutacao, tam_cromossomo):
        if rnd.random() < taxaMutacao:
            i = rnd.randint(0, tam_cromossomo - 1)
            filho1.mudarBit(i)
        if rnd.random() < taxaMutacao:
            i = rnd.randint(0, tam_cromossomo - 1)
            filho2.mudarBit(i)
        return filho1, filho2

    def criarPopulacao(self, tam_populacao, tam_cromossomo):
        popula = Populacao.Populacao()
        for i in range(tam_populacao):
            cromossomo = []
            for j in range(tam_cromossomo):
                gene = rnd.randint(0, 1)
                cromossomo.append(gene)
            popula.addIndividuo(cromossomo)
        return popula

    def plotFuncaoDeMaximizacao(self):
        x_original = []
        y_original = []

        # esse for virar função e vai pro AG
        for i in range(512):
            x_original.append(i)
            z = 100 + mt.fabs(i * mt.sin(mt.sqrt(mt.fabs(i))))
            y_original.append(z)

        mtp.plot(x_original, y_original)
        mtp.show()

    def calulos(self):
        self.populacao.calculaFitness()
        self.populacao.calculaFitnessPorcentagem()
        self.populacao.calculaAlcanceRoleta()

