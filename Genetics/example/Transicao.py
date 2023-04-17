import pandas as pd


class Transicao(object):
  """
  Mensura custo de transição entre duas cidades.
  Custo() -> Usa a função custo para mensurar o tempo e custo entre
    duas cidades.
  """
  DataFrame: pd.DataFrame

  def __init__(self, dataset):
    self.DataFrame = pd.read_csv(dataset, names= ["A", "B", "C", "D"], header=None)
    #self.DataFrame.columns = ["A", "B", "C", "D"]
    self.DataFrame.loc[self.DataFrame['A'] == "Escondidos", 'A'] = "E"

  def Custo(self, Origem, Destino):
    """
    Retorna (Tempo de Transorte, Custo)
    """
    if Origem == Destino:
      return (0, 0)
      
    try:
      a = self.DataFrame.loc[(self.DataFrame['A'] == Origem) & (self.DataFrame['B'] == Destino)]
      return (int(a.iloc[0]['C']), int(a.iloc[0]['D']))
    except IndexError:
      a = self.DataFrame.loc[(self.DataFrame['B'] == Origem) & (self.DataFrame['A'] == Destino)]
      return (int(a.iloc[0]['C']), int(a.iloc[0]['D']))


# dataframe
# se coluna/nome == "Escodindo",  coluna/nome = "E"
# Transicao(nome1, nome2) -> return ( custo,  tempo);
# se dataframe[nome1][nome2] não existe, tentar dataframe[nome2][nome1]
