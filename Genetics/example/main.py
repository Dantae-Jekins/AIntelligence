from Individuo import Cidade
from Populacao import Populacao_Rotas
from Transicao import Transicao
from random import randint
import sys
import numpy as np

Cidades = np.array([
  Cidade("Santa Paula", 5, 10, 10000),
  Cidade("Campos", 6, 5, 6500),
  Cidade("Riacho de Fevereiro", 2, 6, 7000),
  Cidade("Algas", 1, 7, 2500),
  Cidade("Além-do-Mar", 2, 10, 5400),
  Cidade("Guardião", 1, 2, 3000),
  Cidade("Foz da Água Quente", 4, 4, 2000),
  Cidade("Leão", 2, 5, 4000),
  Cidade("Granada", 2, 1, 2500),
  Cidade("Lagos", 1, 7, 3000),
  Cidade("Ponte-do-Sol", 6, 5, 1500),
  Cidade("Porto", 1, 2, 2300),
  Cidade("Limões", 2, 4, 4000),
])

link = None # Hidden
Transicoes = Transicao(
  link
)

pop_size = 10
max_iters = 1000
max_bad = 5
max_stale = 5

max_fitness = float('-inf')
max_individuo = None
mutation_factor = 10

pop1 = Populacao_Rotas(pop_size, Cidades, Transicoes)
pop1.gerar_populacao()

counter = 0
bad_counter = 0
stalemate = 0
while counter < max_iters and stalemate < (max_stale*4):
  pop1fit = pop1.fitness()

  #POP MUTADA
  pop2 = pop1.mutacao()
  for i in range(0, randint(1, mutation_factor)):
    pop2 = pop2.mutacao()

  
  # BAD VALUES
  if (pop1fit < 0):
    bad_counter += 1
  if (bad_counter > max_bad):
    bad_counter = 0
    pop1.gerar_populacao()
    pop1fit = pop1.fitness()


  # STALEMATE 
  if (stalemate > max_stale-1):
    i = 0
    popaux = pop1.mutacao()
    while(pop1fit > popaux.fitness()):
      popaux.mutacao()
      i += 1
      if i > 10:
        break;

    popauxfit = popaux.fitness()
    if popauxfit > pop1fit:
      pop1 = popaux
      pop1fit = popauxfit

  
  #POP CROSSOVER
  pop3 = pop1.crossover(pop2)
  pop3.selecionar(pop_size)
  pop3fit = pop3.fitness()
  if pop3fit > pop1fit:
    pop1fit = pop3fit
    pop1 = pop3

  if (pop1fit == max_fitness):
    stalemate += 1
  
  elif (pop1fit > max_fitness):
    stale_mate = 0
    max_fitness = pop1fit
    pop1.selecionar(pop_size)
    max_individuo = pop1.individuos[0]

  else:
    print(pop1fit)

  if (counter % 10 == 0):
    print(f"\n MELHOR FITNESS I={counter} : {max_fitness}")
    sys.stdout.flush()

  counter += 1

print("")
print("MELHOR FITNESS = ", max_fitness)

print("Rota: ", end="")
aux=0
for city in max_individuo.cidades:
  print(city.nome, " ")
  if city.nome == "E" and aux > 0:
    break
  aux+=1