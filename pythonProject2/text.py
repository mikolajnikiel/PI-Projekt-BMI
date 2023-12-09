import pandas as pd

książka='C:/Users/Tomasz/Documents/GitHub/PI-Projekt-BMI/Książka 1 (1).xlsx'
excel_tabelka=pd.read_excel(książka)

print("BMI posczegolnych osob wynosi: ")
excel_tabelka['BMI']=excel_tabelka['waga']/((excel_tabelka['wzrost'])/100)**2

excel_tabelka['ryzyko'] = excel_tabelka['ryzyko'].astype('object')
excel_tabelka['wagaciala'] = excel_tabelka['wagaciala'].astype('object')


excel_tabelka.loc[excel_tabelka['BMI'] < 18.5, 'wagaciala']= 'Niedowaga'
excel_tabelka.loc[excel_tabelka['BMI'] > 18.5, 'wagaciala']= 'waga optymalna'
excel_tabelka.loc[excel_tabelka['BMI'] > 25, 'wagaciala']= 'nadwaga'
excel_tabelka.loc[excel_tabelka['BMI'] > 29.99, 'wagaciala']= 'otylosc'
excel_tabelka.loc[excel_tabelka['BMI'] < 18.5, 'ryzyko']= 'powiekszony poziom problemow zdrowotnych'
excel_tabelka.loc[excel_tabelka['BMI'] > 18.5, 'ryzyko']= 'minimalne'
excel_tabelka.loc[excel_tabelka['BMI'] > 25, 'ryzyko']= 'srednie'
excel_tabelka.loc[excel_tabelka['BMI'] > 29.99, 'ryzyko']= 'wysokie'
excel_tabelka.loc[excel_tabelka['BMI'] > 34.99, 'ryzyko']= 'bardzo wysokie'

print(excel_tabelka[['Imie i nazwisko', 'BMI', 'wagaciala', 'ryzyko']])



plik= 'bmi.txt'
excel_tabelka[['Imie i nazwisko', 'BMI', 'wagaciala', 'ryzyko']].to_csv(plik, index=False, sep='\t')

print("Dane zapisano do pliku: {plik}")