from Classes import Individuo
from random import randint, shuffle, random
from Transicao import Transicao
import numpy as np
from copy import copy


class Cidade:
  """Estrutura da cidade"""
  nome: str
  peso: int
  tempo: int
  valor: int

  def __init__(self, Nome, Peso, Tempo, Valor):
    self.nome = Nome
    self.peso = Peso
    self.tempo = Tempo
    self.valor = Valor


class Rota(Individuo):
  """Indivíduo do problema"""

  def __init__(self, Cidades, Transicao: Transicao):
    """Construtor"""
    self.tamanho = len(Cidades) + 2
    self.valor_max = 0
    self.cidades = np.empty(self.tamanho, dtype=Cidade)
    self.transicoes = Transicao

    # inicializa cidades
    rindex = randint(2, self.tamanho - 1)
    self.cidades[0] = Cidade("E", 0, 0, 0)
    self.cidades[rindex] = self.cidades[0]

    tempCidades = Cidades.copy()
    shuffle(tempCidades)

    i1 = 0
    for i2 in range(0, self.tamanho):
      if self.cidades[i2] == None:
        self.cidades[i2] = tempCidades[i1]
        i1 += 1

    # inicializa o valor_max
    for cidade in Cidades:
      self.valor_max += cidade.valor

  def fitness(self):
    Tempo = 0
    Peso = 0
    Valor = 0

    for i1 in range(0, self.tamanho):
      cidade_atual = self.cidades[i1]
      cidade_prox = self.cidades[i1 + 1]

      Tempo += cidade_prox.tempo
      Peso += cidade_prox.peso
      Valor += cidade_prox.valor

      (tTempo, tValor) = self.transicoes.Custo(cidade_atual.nome,
                                               cidade_prox.nome)
      Tempo += tTempo
      Valor -= tValor

      if (cidade_prox.nome == "E"):
        break

    if Tempo > 72:
      auxTempo = Tempo - 72
      Valor -= self.valor_max * auxTempo

    if Peso > 20:
      auxPeso = Peso - 20
      Valor -= self.valor_max * auxPeso

    return Valor

  # Peso >
  def mutacao(self):
    """
    70% de chance de trocar uma cidade que está dentro da rota
    com uma que está fora da rota.
  
    30% de chance de trocar a posição de E
    """

    eIndex: int
    for i in range(1, self.tamanho):
      if self.cidades[i].nome == "E":
        eIndex = i

    ret = Rota(self.cidades, self.transicoes)
    ret.cidades = copy(self.cidades)
    ret.tamanho = self.tamanho
    
    def swap(i1, i2, struct):
      aux = struct[i1]
      struct[i1] = struct[i2]
      struct[i2] = aux

    if (random() > 0.3):
      rIndex1 = 1
      if (eIndex > 2):
        rIndex1 = randint(1, eIndex - 1)

      if ((ret.tamanho - 1) - eIndex == 1):  # SE eINDEX FOR PENULTIMO
        rIndex2 = ret.tamanho - 1  # CIDADE FINAL
        swap(rIndex1, rIndex2, ret.cidades)

      elif (ret.tamanho - 1) != eIndex:  # SE eINDEX NÃO FOR O ULTIMO
        rIndex2 = randint(eIndex + 1, ret.tamanho - 1)
        swap(rIndex1, rIndex2, ret.cidades)

    else:
      fitness = ret.fitness()
      if fitness > 0:  # se fitness maior que 0, tentar tornar a rota maior, movendo o esconderijo para direita.
        swap(eIndex, min(eIndex + 1, ret.tamanho - 2), ret.cidades)

      else:
        swap(eIndex, max(2, eIndex - 1), ret.cidades)

    return ret

  def crossover(self, alvo: Individuo):
    s = 1
    a = 1
    i = 1
    ret = Rota(self.cidades, self.transicoes)
    ret.cidades = np.empty(self.tamanho, dtype=Cidade)
    ret.tamanho = self.tamanho

    while i < ret.tamanho:
      while (True):
        inside = False
        for cidade in ret.cidades:
          if cidade != None and self.cidades[s].nome == cidade.nome:
            inside = True
            break

        if inside == True:
          s += 1
        else:
          break
      ret.cidades[i] = self.cidades[s]
      i += 1

      while (True):
        inside = False
        for cidade in ret.cidades:
          if cidade != None and alvo.cidades[a].nome == cidade.nome:
            inside = True
            break

        if inside == True:
          a += 1
        else:
          break
      ret.cidades[i] = alvo.cidades[a]
      i += 1

    ret.cidades[0] = Cidade("E", 0, 0, 0)
    return ret
