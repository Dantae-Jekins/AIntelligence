# Genetic Algorithms

<a name="start"></a> 
[English](#lang_en) $\cdot$ [Português](#lang_pt)

Explicação parcial do código

Partial explanation of the code

<br>
<hr>

<a name="lang_pt"></a>
### Seção Português $\cdot$ [Início](#start)

### Problema da ladra viajante

### Indivíduo
O problema da ladra viajante é um problema combinatório sem solução polinomial (NP). O problema é composto por uma entidade que deve passar por diversas cidades, roubar seus respectivos itens e retornar ao esconderijo, porém existe um peso, um tempo de roubo e um valor associado à cada item, ou seja: O problema resume-se em achar a combinatória ideal, que maximize o valor sob limitação do peso e do tempo.

Considerando que tenha lido sobre o algoritmo, modelamos então este da seguinte forma: Um indivíduo é um conjunto de cidades, um "caminho" que armazena TODA a sequência de cidades, porém que delimita um final, ou seja, o nosso indivíduo possui um formato:

Seja $C$ o nosso conjunto de cidades e $E$ o nosso esconderíjo:

$I = \{E, C_i, C_j, ..., E, C_k, ..., C_l\}$

Sendo que cada cidade é unica, ou seja, $i \neq j \neq k \neq l$

E definimos o caminho REAL como o subconjunto entre os esconderijos, e a contabilização de valores, tempo e peso incide sobre apenas esta seção.

### Mutação

A partir daqui é fácil concluir que o gene é uma cidade, mas existe um fato importante, o gene é **único**, ou seja, precisamos pensar que nossa mutação deve ser uma troca, e não uma simples alteração aleatória, definimos que a nossa mutação pode seguir dois caminhos:

- Sejam $C_i, C_j$ duas cidades adjacentes no caminho real, trocamos suas posições em $I$.
- Seja $C_i$ uma cidade no caminho real e $C_j$ uma cidade fora, trocamos suas posições em $I$.

E para isolar mutações que não são aplicáveis, precisamos do Fitness.

### Fitness

Simples, corresponde à somatória dos valores dos itens das cidades dentro do caminho real, porém sob duas condições

- Se a soma de pesos é maior que peso_máximo, para cada unidade excedente subtraimos o "valor máximo", tornando o fitness negativo.

- Se a soma dos tempos é maior que tempo_máximo, para cada unidade excedente subtraimos o "valor máximo", tornando o fitness negativo. 

Ou seja, se o indivíduo infrigir uma das regras que definimos, temos certeza de que seu fitness é negativo, PORÉM, até indivíduos inválidos são valorizados, uma infração menor de peso com um valor somado maior continua sendo melhor que uma infração maior de peso com um valor somado menor, evitando de que o algoritmo trate erros diferentes na genética como de mesma importância.


### Outros

É possível deduzir coisas como o crossover e o algoritmo genético no main, eu sei que é confuso, mas o intúito é apresentar o algoritmo genético, e não o "meu código".

<br>

<br>
<hr>

<a name="lang_en"></a>

### English Section $\cdot$ [Start](#start)

### Travelling thief problem


### Individual 
The travelling thief problem is a combinatory problem with no polynomial solution (NP). The problem is composed of an entity that must travel between cities, steal their items and return to their hideout, but there's a weight, a consumed time and a value associated with each item, so: The problem is about maximizing the value, considering the time and weight limitations.

Considering that you have read about the algorithm, we modeled the problem in the following way: We define an individual as a set of cities,a "path" that stores the WHOLE sequence of cities, but that also delimitates a final:

Let $C$ be our set of cities and $E$ our hideout:

$I = \{E, C_i, C_j, ..., E, C_k, ..., C_l\}$

Such that each item is unique, so $i \neq j \neq k \neq l$.

And we define our true path as the subset between the hideouts, and the summation of values, consumed time and weight will only include them.

### Mutation

Now it's easy to conclude that the gene is a city, but there's an important factor, the gene is unique, that is, we need to assume that our mutation will be an exchange, and not simply a random change, we define that our mutation can take on the two following paths:

- Let $C_i, C_j$ be two adjacent cities on our real path, we swap their positions in $I$.

- Let $C_i$ be a city on the real path and $C_j$ a city outside of it, we swap their positions in $I$.

And to define mutations that are not appliable, we need the fitness.

### Fitness

Simple, it corresponds to the summation of values of each item of the cities inside the real path, but under two conditions:

- If the sum of weights is bigger than max_weight, for each surplus unity we subtract the "max value", turning the fitness negative.

- If the sum of time is bigger than max_time, for each surplus unity we subtract the "max value", turning the fitness negative. 

That is, if the individual breaks a rule we defined, we make sure it's fitness is negative, BUT, even invalid individuals are valued, a lesser infraction with a bigger value is still better than a bigger infraction with a lesser value, treating different genetic failures as... different.

### Other

It's possible to figure out things such as the crossover and the genetic algorithm itself, i know that it's confusing, but the objective is to introduce the problem and not "my code".