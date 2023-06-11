from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from numpy import average, unique, meshgrid, arange
from notmine import bench_k_means


# Carrega os dígitos
# Data -> carrega o nosso conjunto de dados
# Inspecionando o shape do retorno, não é necessário o tratamento de dados
# Labels -> carrega as classificações corretas (não usadas para o treinamento)
(data, labels) = datasets.load_digits(return_X_y=True)

# Extrai a quantidade de números e a quantidade de informações de cada número
(quantidade, dimensao) = data.shape 
classificacoes = 10 


# trata os dados e reduz a dimensão do dado com PCA
standard_data = StandardScaler().fit_transform(X=data)
pca = PCA(); pca.fit(standard_data)


# Selecionamos a melhor quantidade de componentes (nova dimensão)
# Nós não sabemos ainda bem o melhor processo de decisão
media = average(pca.explained_variance_) #obsoleto
idx = 40
""" Isso não ajuda
idx = 0; current_dif = float('inf')
for i in range(0, len(pca.explained_variance_)):
    if (abs(pca.explained_variance_[i] - media) < current_dif):
        idx = i
"""

print("Quantidade de componentes selecionada = {}".format(idx));
pca = PCA(n_components=idx+1)
pca.fit(standard_data)
pca_transformed = pca.transform(standard_data)

# Inicializamos o kmeans com 10 clusters
kmeans_pca = KMeans(n_clusters=classificacoes, init='k-means++',n_init=4)
kmeans_pca.fit(pca_transformed)
print("Clusters definidos : {}".format(unique(kmeans_pca.labels_)))
print("Problemática: O cluster \"0\" pode ser reservado aos números 2!")
print(82 * "_")
print("init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI\tsilhouette")
bench_k_means(kmeans=kmeans_pca, name="Kmeans com PCA", data=data, labels=labels)
print(82 * "_")

# Seria necessário o tratamento de dados para importar imagens e realizar o predict
# mas nois tamo com preguiça demais pq a gnt ta mais preocupado em estudar esse pca ;9