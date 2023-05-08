# Constraint Satisfaction

<a name="start"></a> 
[English](#lang_en) $\cdot$ [Português](#lang_pt)

Enquanto não há implementação, interprete $\sub$ como subconjunto.

While there is no implementation, interpret $\sub$ as subset.

<br>
<hr>

<a name="lang_pt"></a>
### Seção Português $\cdot$ [Início](#start)

Uma modelagem sob satisfação de restrições define que um estado ou contexto só é aceito como solução ao problema se ele atende à todas as restrições impostas.

De um ponto de vista matemático, definimos um conjunto para as nossas variáveis, um conjunto para os nossos domínios e um conjunto para as nossas restrições:

$X = \set{X_1, ..., X_n}$, variáveis,

$D = \set{D_1, ..., D_n}$, domínios,

$R = \set{R_1, ..., R_n}$, restrições,

Cada variável $x \in X$ deve ser atribuída a algum domínio de D, podemos dizer que cada variável pode receber algum (único) valor dos domínios, então um domínio pode estabelecer uma relação de um para muitas variáveis mas não vice-versa.

Uma restrição $R_j$ por outro lado, é um par $\set{X_j, r_j}$, seja $X_j \sub X$ e $r_j$ seja um conjunto de relações que estabelecem regras entre $X_j$ e os domínios atribuidos, $D_j$.

### Algoritmos usados

Uma solução à um problema é quando todas as satisfações $R_j$ são atendidas e todas as variáveis atribuídas, para alcançar um estado de atribuições aceitas, normalmente são usadas as técnicas como **Depth First Search (DFS)** e backtracking, que compõem um algoritmo de força bruta, mas sob necessidade de performance heurísticas seriam necessárias.

<br>
<hr>

<a name="lang_en"></a>

### English Section $\cdot$ [Start](#start)

A problem modeled over the constraint satisfaction idea defines a state in which is only accepted as a a solution when all "constaints" are satisfied.


From a mathematical viewpoint, we define a set to our variables, a set to our domains and a set to our constraints:

$X = \set{X_1, ..., X_n}$, variables,

$D = \set{D_1, ..., D_n}$, domains,

$C = \set{C_1, ..., C_n}$, constraints,

Each variable $x \in X$ should be assigned to any domain from D, we could say that each variable can recieve a single value from the domains, so a domain could establish a relationship to one or many variables but not the other way around.

A constraint $C_j$ on the other hand, is a pair $\set{X_j, r_j}$, let $X_j \sub X$ and $r_j$ be a set of rules between the subset of variables and a subset of domains $D_j$.

### Appliable Algorithms

A solution to a problem using constaint satisfaction is given when all constraints $C_j$ are satisfied and all variables are assigned to a domain, to achieve a state where this is true, we could use techniques such as **Depth First Search (DFS)** and backtracking, which are brute forcing techniques, but under necessity heuristics are also appliable to the problem.