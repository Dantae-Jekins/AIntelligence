from Classes import Populacao
from Individuo import Rota
import numpy as np


class Populacao_Rotas(Populacao):

  def __init__(self, Tamanho, Cidades, Transicoes):
    self.individuos = np.empty(Tamanho, dtype=Rota)
    self.tamanho = Tamanho
    self.cidades = Cidades
    self.transicoes = Transicoes

  def fitness(self):
    ## deve chamar o fitness do indivíduo
    # média de fitnessa da pop
    fitness = 0
    for individuo in self.individuos:
      fitness += individuo.fitness()
    return fitness / self.tamanho

  def mutacao(self):
    ret = Populacao_Rotas(self.tamanho, self.cidades, self.transicoes)
    for i in range(0, self.tamanho):
      ret.individuos[i] = self.individuos[i].mutacao()
    return ret

  def crossover(self, alvo: Populacao):
    tamanho = self.tamanho * alvo.tamanho
    ret = Populacao_Rotas(tamanho, self.cidades, self.transicoes)
    for i in range(0, self.tamanho):
      for j in range(0, alvo.tamanho):
        ret.individuos[i * alvo.tamanho + j] = self.individuos[i].crossover(
          alvo.individuos[j])

    return ret

  def selecionar(self, tamanho):
    # Ordena classe com
    # Usar numpy.sort
    lista = sorted(self.individuos, key=lambda indv: indv.fitness(), reverse=True)
    self.individuos = np.array(lista[0:tamanho], dtype=Rota)
    self.tamanho = tamanho

  def merge(self, alvo: Populacao):
    tamanho = self.tamanho + alvo.tamanho
    ret = Populacao_Rotas(tamanho, self.cidades, self.transicoes)
    ret.individuos = np.concatenate(self.individuos, alvo.individuos)
    return ret

  def gerar_populacao(self):
    for i in range(self.tamanho):
      self.individuos[i] = Rota(self.cidades, self.transicoes)

