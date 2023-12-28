import numpy as np
import matplotlib.pyplot as plt
import numpy_financial as npf

cena = 120000
oprocentowanie_banku = 0.12 / 12
lata = 5
wzrost_ceny = 0.05

finalna_cena_mieszkania = cena * ((wzrost_ceny + 1) ** lata)

miesieczna_skladka = -npf.pmt(oprocentowanie_banku, lata * 12, 0, finalna_cena_mieszkania)

czas = np.arange(0, lata * 12 + 1, 1)
wartosc_mieszkania = cena * (1 + wzrost_ceny / 12) ** czas
wartosc_lokaty = -npf.fv(oprocentowanie_banku, czas, miesieczna_skladka, 0)

plt.plot(czas, wartosc_mieszkania, label='Mieszkanie')
plt.plot(czas, wartosc_lokaty, label='Lokata')
plt.legend()
plt.show()
