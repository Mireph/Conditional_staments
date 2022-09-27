price_vac = float(input())
pazzel = int(input())
kukli = int(input())
meche = int(input())
minjon = int(input())
truks = int(input())
suma = pazzel * 2.6 + kukli * 3 + meche * 4.1 + minjon * 8.2 + truks * 2
broi_porachani_igr = pazzel + kukli + meche + minjon + truks
if broi_porachani_igr >= 50:
    kraina_cena = suma - (suma * 0.25)
else:
    kraina_cena = suma
naem = kraina_cena * 0.1
pechalba = kraina_cena - naem
if pechalba >= price_vac:
    print(f"Yes! {pechalba-price_vac :.2f} lv left.")
else:
    print(f"Not enough money! {price_vac-pechalba :.2f} lv needed.")