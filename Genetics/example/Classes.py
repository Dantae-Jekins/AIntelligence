import numpy as np;

class Populacao:
  def __init__(self, length):
    self.individuos = np.array(dtype = Individuo);
    raise NotImplementedError("Implementar")

  def fitness(self, individuo):
    raise NotImplementedError("Implementar")

  def mutacao(self):
    raise NotImplementedError("Implementar")

  def crossover(self):
    raise NotImplementedError("Implementar")

  def selecionar(self, length):
    # Ordena classe com
    # Usar numpy.sort
    nova_lista = sorted(self.individuos, key=self.fitness, reverse=True)
    self.populacao = nova_lista[0:length];

  def gerar_populacao(self):
    self.populacao = []
    for i in range(self.tamanho):
      self.populacao.append(Individuo())



class Individuo:

  def __init__(self):
    raise NotImplementedError("Implementar")
    
  def fitness(self, alvo, gravidade):
    raise NotImplementedError("Implementar")

  def mutacao(self, var_theta, var_veloc):
    raise NotImplementedError("Implementar")