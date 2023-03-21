# Gradient Descent
[English](#lang_en)

[Português](#lang_pt)

<br>
<hr>

<a name="lang_pt"></a>

## Gradiente

Antes de explicarmos o que é a técnica de descida gradiente, é melhor explicar (de forma rudimentar e curta) o que é o gradiente primeiro: Um gradiente de uma função $f(x_1, x_2, ... , x_n)$ é o vetor formado pelas derivadas parciais da função em relação a cada uma de suas variáveis, ou seja:

$$\Delta f(x_1, x_2, ... , x_n) = (\frac{\partial f}{\partial x_1}, \frac{\partial f}{ \partial x_2}, ..., \frac{\partial f}{\partial x_n})$$

Se reduzirmos à nossa função de tamanho indefinido ($n$) para uma função com três variáveis (Um tamanho finito, para usarmos as letras), podemos representar o gradiente com a soma das derivadas parciais aplicadas aos versores da base ortonormal, que é na essência a mesma coisa que acima:

$$\Delta f(x, y, z) = \frac{\partial f}{\partial x}i + \frac{\partial f}{ \partial y}j + \frac{\partial f}{\partial z} k$$




Então ter em sua mente a definição de derivada (Cálculo diferencial) é crucial para o desenvolvimento deste projeto.

Sabendo como se dá o gradiente, é importante também saber que ele representa uma direção (é um vetor) e sentido; Se imaginarmos uma situação tridimensional $f(x,y) = z$, o gradiente $\Delta f$ será um vetor bidimensional em um gráfico $(x, y, z)$ (vai fazer sentido na afirmação seguinte) e **este vetor será indicativo da direção $(x,y)$ em que $z$ mais varia, informando também a intensidade de variação pela sua norma**, e este conceito é provavelmente o mais importante de se saber para o entendimento do gradient descent.

<br>

## A Descida Gradiente

A descida gradiente é uma aplicação do que apresentamos acima, muito usado na computação no aprendizado de máquina.

> Primeiramente, seja $f(x,y) = z$, destacamos que o gradiente $(\frac{\partial f}{ \partial x}, \frac{\partial f}{\partial y})$ em um ponto $(x,y)$ representa a direção em que $z$ mais varia, ou seja, se seguirmos a direção em sentido positivo, a tendência é que $z$ aumente, e se seguirmos a direção em sentido negativo, a tendência é que $z$ diminue. Provavelmente para muitos que não sabem do tema, a ideia de "seguir" ficou ambígua, o que é de se esperar já que não foi definida, então definimos "seguir uma direção e sentido" como aplicar este vetor (gradiente) ao ponto $(x,y)$ para que $z$ aumente ou diminua na operação no próximo cálculo.

Então, como que o gradiente consegue ser de utilidade ao treinamento de um classificador? Bem, precisamos escolher uma "função de estimativa" e uma "função de erro", a estimativa é uma função que recebe todos os dados como variáveis e retorna dados que possam ser classificados o mais corretamente possível, enquanto a função de erro é uma função que quantia a diferença do reais e dos estimados. A descida gradiente se insere nesse contexto como técnica utilizada no treinamento dos coeficientes desta função de estimativa, e se não ficou claro, coeficientes são os termos que multiplicam as variáveis que são os nossos dados, como $a$ e $b$ na função $f(x,y) = ax + by$. E como que os coeficientes são treinados? Precisamos retomar a nossa função de erro anterior.

Seja $(x, y, R)_i$ (Vale a pena mencionar que quase todo problema possui muitas mais variáveis que apenas $x$ e $y$) o nosso conjunto de dados e $f(x,y)$ a nossa função de estimativa com coeficientes $a$ e $b$, vamos chamar a função de erro de ERR:

$$ERR(f(x_i, y_i), R_i)$$

Então para $i$ dados que temos, calculamos a diferença entre o estimado e o real com alguma função de erro. E o **objetivo é reduzir este erro**, ou seja, 'tratamos' o erro como uma função no seguinte formato (Forçando muito): $ERR(a, b)$ já que são os coeficientes de $f(x, y)$ que precisamos alterar para aproximar a função dos valores reais, e chegamos à um algoritmo iterativo:

Assumimos coeficientes $A = \{a_0, a_1, ..., a_n\}$ iniciais, e para cada iteração, aplicamos o sentido negativo do gradiente de $ERR$ aos coeficientes:

$$ A \leftarrow A - \Delta ERR$$

<br>
<hr> 

<a name="lang_en"></a>

## Gradient 

Before explaining what the gradient descent really means, it's better to fist explain (shortly and simple) what the gradient is: A gradient from a function
$f(x_1, x_2, ... , x_n)$ is given by the vector made up by the function's partial derivativatives with respect to each variable, that being:

$$\Delta f(x_1, x_2, ... , x_n) = (\frac{\partial f}{\partial x_1}, \frac{\partial f}{ \partial x_2}, ..., \frac{\partial f}{\partial x_n})$$

If we shorten this definition with size n to a three variable function (or any finite numbers, to avoid using $i_n$), we can represent the gradient as the sum of the partial derivatives applied to the versors of the orthonormal base, which is the same thing as the above described in a different way:

$$\Delta f(x, y, z) = \frac{\partial f}{\partial x}i + \frac{\partial f}{ \partial y}j + \frac{\partial f}{\partial z} k$$

So knowing about derivatives (Differential calculus) is crucial to understand this project.

Seeing how we can extract the gradient of a function, it's important to know that it's also a direction (after all, it's a vector); If we imagine a tridimensional situation $f(x,y) = z$, the gradient $\Delta f$ is going to be a bidimensional vector on the graph $(x,y,z)$ (it's going to make sense on the following declaration) and **this vector is going to be an indicator of the direction $(x,y)$ that $z$ varies the most, while also representing the intensity of variation with it's norm**, this concept is probably the most important to know about the understanding of the gradient descent.

## Gradient Descent
