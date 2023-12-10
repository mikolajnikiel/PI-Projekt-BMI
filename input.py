def bmi_calculator():
    print("Wybierz jednostki: \n1. Metryczne \n2. Imperialne")
    # wybieramy jednostki
    unit_choice = int(input("Wybierz 1 lub 2: "))

    # wprowadzamy ilość obserwacji
    num_obs = int(input("Ile obserwacji chcesz wprowadzić? "))

    with open("plik.txt", "w") as f:
        f.write("Wyniki BMI\n")
        for i in range(num_obs):
            # wprowadzamy wagę i wzrost
            if unit_choice == 1:
                wzrost = float(input("Podaj wzrost w metrach: "))
                masa = float(input("Podaj wagę w kilogramach: "))
            elif unit_choice == 2:
                wzrost = float(input("Podaj wzrost w calach: "))
                masa = float(input("Podaj wagę w funtach: "))
            else:
                print("Nieprawidłowy wybór jednostek.")
                return

            # liczymy BMI
            bmi = masa / (wzrost ** 2)

            f.write(f"Obserwacja {i+1}: {bmi:.2f}\n")

    print("Wyniki zostały zapisane do pliku plik.txt")


bmi_calculator()
