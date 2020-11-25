import AlgoritmoGenetico
import time
t0 = time.time()
ag = AlgoritmoGenetico.AlgoritmoGenetico()
ag.executaAG(50, 9, 100, 0.8, 0.05)
t1 = time.time()-t0
print("Tempo de execução = ", t1)
ag.populacao.printPopulacao()
ag.populacao.plotPopulacao()

'''
mtp.plot(x, y, 'r o')
mtp.show()
'''
