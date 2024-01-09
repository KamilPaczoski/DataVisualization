import pandas as pd

data = pd.read_html(
    'https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/',
    header=0)
df = pd.DataFrame(data[0])
df = df.rename(columns={'POS': 'POZYCJA', 'ARTIST': 'ARTYSTA', 'TITLE': 'TYTUŁ', 'YEAR': 'ROK', 'HIGH POSN': 'MAX POZ'})
ilosc_artystow = len(df['ARTYSTA'].unique())
print(ilosc_artystow)
najczesciej_wystepujace = df['ARTYSTA'].mode().tolist()
print(najczesciej_wystepujace)
df.columns = [col.capitalize() for col in df.columns]
df = df.drop(columns=['Max poz'])
najwiecej_albumow = df['Rok'].mode().tolist()
print(najwiecej_albumow)
ilosc_albumow = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)].count().iloc[0]  # uzywac iloc[0]
print(ilosc_albumow)
najmlodszy_album = df['Rok'].max()
najwczesniejsze_albumy = df.groupby('Artysta')['Rok'].min().sort_values()
print(najwczesniejsze_albumy)
najwczesniejsze_albumy.to_csv('najwczesniejsze_albumy.csv', sep=';')
