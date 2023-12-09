import pandas as pd

książka='C:/Users/Tomasz/Documents/GitHub/PI-Projekt-BMI/Książka 1.xlsx'
excel_tabelka=pd.read_excel(książka)

print("BMI posczegolnych osob wynosi: ")
excel_tabelka['BMI']=excel_tabelka['waga']/((excel_tabelka['wzrost'])/100)**2

print(excel_tabelka[['Imie i nazwisko', 'BMI']])

plik= 'bmi.txt'
excel_tabelka[['Imie i nazwisko', 'BMI']].to_csv(plik, index=False, sep='\t')

print("Dane zapisano do pliku: {plik}")