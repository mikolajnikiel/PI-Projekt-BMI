import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data_text = pd.read_csv('test_text1.txt', delimiter='\t')
data_input = pd.read_csv('test_input1.txt', delimiter='\t')

bmi_ranges = [0, 16.00, 17.00, 18.50, 25.00, 30.00, 35.00, 40.00, float('inf')]

data_text['BMI'] = data_text['BMI'].astype(float)
data_input['BMI'] = data_input['BMI'].astype(float)

data_text['BMI Category'] = pd.cut(data_text['BMI'], bins=bmi_ranges, labels=range(len(bmi_ranges)-1))
data_input['BMI Category'] = pd.cut(data_input['BMI'], bins=bmi_ranges, labels=range(len(bmi_ranges)-1))

colors = ['#000080', '#4169E1', '#98FB98', '#9ACD32', '#CCFF33', '#CC9933', '#CC3333', '#990000']

plt.figure(figsize=(10, 6))
sns.scatterplot(x='wzrost', y='masa', hue='BMI Category', data=data_text, s=75, palette=colors)
sns.scatterplot(x='wzrost', y='masa', hue='BMI Category', data=data_input, s=200, palette=colors)

plt.ylim(25, 200)
plt.title('Porównanie danych użytkownika z danymi z tabeli')
plt.legend(title='Kolory BMI', loc='upper right', labels=[f'{bmi_ranges[i]}-{bmi_ranges[i+1]}' for i in range(len(bmi_ranges)-1)])
plt.show()
