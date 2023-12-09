import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_text = pd.read_csv('bmi-text.txt', delimiter='\t')
data_input = pd.read_csv('bmi-input.txt', delimiter='\t')


sns.scatterplot(x='masa', y='wzrost', data=data_text, label='Dane z tabeli')
sns.scatterplot(x='masa', y='wzrost', data=data_input, label='Dane użytkownika')
plt.title('Porównanie danych użytkownika z danymi z tabeli')
plt.show()
