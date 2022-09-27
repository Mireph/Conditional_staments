budjet = float(input())
statisti = int(input())
price_dress = float(input())
decor = budjet * 0.1
if statisti >= 150:
    sum_obleklo = statisti * price_dress - (statisti * price_dress * 0.1)
else:
    sum_obleklo = statisti * price_dress
sum_za_film = decor + sum_obleklo
if sum_za_film > budjet:
    print(f"Not enough money!")
    print(f"Wingard needs {sum_za_film - budjet :.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {budjet - sum_za_film :.2f} leva left.")