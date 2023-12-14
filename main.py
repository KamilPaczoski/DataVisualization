fertility_rate = [1.3, 1.95, 2.466, 1.6, 2.952, 1.801, 1.34, 1.34, 1.63, 2.326, 2.436, 6.563, 1.283, 1.43, 1.988,
                  1.61, 1.921, 2.4, 1.495, 4.705]
life_expectancy = [76.84878, 81.40732, 77.57895, 74.16341, 68.84907, 73.88595, 75.26829, 76.26098, 80.57244,
                   65.46259, 67.5482, 55.02451, 76.2799, 82.29024, 69.80695, 81.40112, 82.19756, 74.22683, 80.12888,
                   45.55095]
srednia_lf = sum(life_expectancy) / len(life_expectancy)
life_expectancy.sort()
mediana_lf = life_expectancy[len(life_expectancy) // 2]
dominanta_lf = max(set(life_expectancy), key=life_expectancy.count)
print(
    f'Średnia: {srednia_lf}, Mediana: {mediana_lf} Dominanta: {dominanta_lf} (występuje {life_expectancy.count(dominanta_lf)} razy)')
wariancja_lf = sum((i - srednia_lf) ** 2 for i in life_expectancy) / (len(life_expectancy) - 1)  # -1?
odchylenie_lf = wariancja_lf ** 0.5
print(f'Wariancja: {wariancja_lf}, Odchylenie standardowe: {odchylenie_lf}')
srednia_fr = sum(fertility_rate) / len(fertility_rate)
suma = 0
for i in range(len(fertility_rate)):
    suma += (fertility_rate[i] - srednia_fr) * (life_expectancy[i] - srednia_lf)
kowriencja = suma / (len(fertility_rate) - 1)
wariancja_fr = sum((i - srednia_fr) ** 2 for i in fertility_rate) / (len(fertility_rate) - 1)  # -1?
odchylenie_fr = wariancja_fr ** 0.5
korelacja = kowriencja / (odchylenie_fr * odchylenie_lf)
print(f'Kowariancja: {kowriencja}, Korelacja: {korelacja}')
odchylenie_std_populacji = 9.09
poziom_ufnosci = 0.95
margines_bledu = 1.96 * (odchylenie_std_populacji / (len(life_expectancy) ** 0.5))
przedzial_ufnosci = [srednia_lf - margines_bledu, srednia_lf + margines_bledu]
print(f'Przedział ufności: {przedzial_ufnosci}')