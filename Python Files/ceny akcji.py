import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_miedz = pd.read_csv('ca_c_f_d.csv')
df_KHGM = pd.read_csv('kgh_d.csv')

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
sns.lineplot(x='Data', y='Zamkniecie', data=df_KHGM, color='blue')
plt.title('KGHM')
plt.xticks(df_KHGM['Data'].dt.to_pydatetime(), df_KHGM['Data'].dt.strftime('%Y-%m-%d'), rotation=45)


plt.subplot(2, 1, 2)
sns.lineplot(x='Data', y='Zamkniecie', data=df_miedz, color='Red')
plt.title('Miedź')
plt.xticks(np.arange(0, 1000, 100))

plt.show()
