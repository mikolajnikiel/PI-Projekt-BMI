def plik(waga, wzrost, BMI):
    file = open("tabela wynikow2.txt", "a")

    Lp = 0

    file.write("Lp\tWaga\tWzrost\tBMI\n")
    file.write(f"{Lp + 1}\t")
    file.write(f"{waga}\t{wzrost}\t{BMI:.2f}\n")

    file.close()


def bmi_input():
    if jednostki == 1:

        waga = input("Podaj swoją wagę (w kilogramach):\n")
        if waga.lower() == "przerwij program":
            print("Program został przerwany.")
            exit()
        waga = float(waga)

        wzrost = input("Podaj swój wzrost (w centymetrach):\n")
        if wzrost.lower() == "przerwij program":
            print("Program został przerwany.")
            exit()
        wzrost = float(wzrost)

        BMI = waga / ((wzrost / 100) ** 2)
        print(f"Twój wskaźnik BMI wynosi: {BMI:.2f}")

    elif jednostki == 2:

        waga = input("Podaj swoją wagę (w funtach):\n")
        if waga.lower() == "przerwij program":
            print("Program został przerwany.")
            exit()
        waga = float(waga) * 2.20462

        wzrost = input("Podaj swój wzrost (w calach):\n")
        if wzrost.lower() == "przerwij program":
            print("Program został przerwany.")
            exit()
        wzrost = float(wzrost) * 2.54

        BMI = waga / ((wzrost / 100) ** 2)
        print(f"Twój wskaźnik BMI wynosi: {BMI:.2f}")

    else:
        print("Błędny wybór systemu jednostek.")

    if BMI < 16.0:
        print(
            "Kategoria: wygłodzenie,\nRyzyko chorób towarzyszących otyłości: ryzyko minimalne,\n ale zwiększony poziom wystąpienia innych problemów zdrowotnych")
    elif 16.0 < BMI < 16.99:
        print(
            "Kategoria: wychudzenie,\nRyzyko chorób towarzyszących otyłości: ryzyko minimalne,\n ale zwiększony poziom wystąpienia innych problemów zdrowotnych")
    elif 17.0 <= BMI <= 18.49:
        print(
            "Kategoria: niedowaga,\nRyzyko chorób towarzyszących otyłości: ryzyko minimalne,\n ale zwiększony poziom wystąpienia innych problemów zdrowotnych")
    elif 18.5 <= BMI <= 24.99:
        print("Kategoria: pożądana masa ciała,\nRyzyko chorób towarzyszących otyłości: minimalne")
    elif 25.0 <= BMI <= 29.99:
        print("Kategoria: nadwaga,\nRyzyko chorób towarzyszących otyłości: średnie")
    elif 30.0 <= BMI <= 34.99:
        print("Kategoria: otyłość I stopnia,\nRyzyko chorób towarzyszących otyłości: wysokie")
    elif 35.0 <= BMI <= 39.99:
        print("Kategoria: otyłość II stopnia (duża),\nRyzyko chorób towarzyszących otyłości: bardzo wysokie")
    elif BMI >= 40.0:
        print(
            "Kategoria: otyłość III stopnia (chorobliwa),\nRyzyko chorób towarzyszących otyłości: ekstremalny poziom ryzyka")

    plik(waga, wzrost, BMI)


print("Program liczy BMI. Użytkownik musi podać swój wzrost oraz wagę aby dowiedzieć się jaki ma wskaźnik BMI.")
print("Naciśnij 1, aby wybrać system metryczny, a 2, aby imperialny.")
print("Aby przerwać działanie programu, wpisz: 'przerwij program'.")

while True:
    jednostki = input("Twój wybór: ")

    if jednostki in ('1', '2'):
        jednostki = int(jednostki)
        break
    elif jednostki.lower() == "przerwij program":
        print("Program został przerwany.")
        exit()
    else:
        print("Nie ma takiego systemu jednostek...\nWybierz 1 lub 2.")

while True:
    bmi_input()