# Genetic Algorithms

<a name="start"></a> 
[English](#lang_en) $\cdot$ [Português](#lang_pt)

<br>
<hr>

<a name="lang_pt"></a>
### Seção Português $\cdot$ [Início](#start)

### Conceito de um algoritmo genético
Um algoritmo genético é um algoritmo baseado na evolução sob um ponto de vista biológico, ele se baseia em indivíduos que sofrem alterações aleatórias em sua estrutura, estes que então são sujeitos à "seleção natural". Ou seja, um algoritmo genético é em sua essência um algoritmo que tenta resolver um problema adotando alterações aleatórias ou parcialmente aleatórias (condicionadas através de heurísticas) em sua solução, aonde as piores soluções são descartadas à cada iteração.  

De acordo com a introdução é possível deduzir as componentes de um algoritmo genético, é necessário:

### Indivíduo 

Seja $I$ um indivíduo, cujo deve ter uma estrutura de dados correspondente ao problema. A estrutura é um gene ou é composta de vários genes, que são os componentes sujeitos à mudança.

$f(I) = \sigma\quad$ é uma função que quantifica a qualidade da solução, pode ser crescente ou não. Definimos o seu nome em quase todas as aplicações como função de fitness.

$m(I_x) = I_y\quad$ é uma função que realiza uma mutação no gene (ou genes) de um indivíduo $I_x$. Definimos o seu nome em quase todas as aplicações como função de mutação.

$c(I_x, I_y) = I_z\quad$ é uma função que mistura os genes de dois indivíduos, a maneira que se misturam-se os genes é flexível e depende do problema. Definimos o seu nome como função de crossover.

> Para aplicar estas três coisas é necessário uma base sobre software, com isso já é possível montar um conjunto de indivíduos e iterar sob o conjunto realizando mutações e mantendo as óptimas (que retornam um fitness melhor), eu não vou entrar em detalhes sobre como isso é realizado já que foge do assunto.

<br>


### População
Para facilitar a modelagem, e também descrever o processo biológico com maior fidelidade, também definimos $P$ como uma população de indivíduos, ou seja, um conjunto de indivíduos $P = \{I_0, I_1, ..., I_n\}$. E definindo suas funções temos: 

Seja $f_P$ uma função de fitness que recebe uma população e $f_I$ uma função que recebe um indivíduo:

$f_P(P) = \{ f_I(I_0), ..., f_I(I_n)\}\quad$, **pode** retornar um conjunto de fitness individuais.


Seja $m_p$ uma função de mutação que recebe uma população:

$m_P(P) = P_x\quad$ Retorna uma população com indivíduos mutados a partir da primeira.

Seja $c_P$ uma função de crossover que recebe duas populações:

$c_P(P_1,P_2) = P_3\quad$ Retorna uma população cujo indivíduos sejam crossovers dos indíviduos da população $P_1$ com os da $P_2$. O método que deve-se utilizar varia, por exemplo, poderíamos cruzar indivíduos com base em seu fitness (ordenando as populações e então fazer $c(I_x^n, I_y^n)$) ou realizar todas as combinações possíveis retornando $n \cdot m$ indivíduos, seja $n = |P_1|$ e $m =|P_2|$.

<br>

<br>
<hr>

<a name="lang_en"></a>

### English Section $\cdot$ [Start](#start)
