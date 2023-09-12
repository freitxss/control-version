import pandas as pd
gasolina_df = pd.read_csv('gasolina.csv', sep=',')

import seaborn as sns
with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
  grafico.set(title="Preço Da Gasolina", xlabel='Dias', ylabel='Preço');