import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('HRDataset.csv')

# sns.countplot(x='ManagerID', hue='PerformanceScore', data=df)

df_plot = df.groupby(['ManagerID', 'PerformanceScore']).size().reset_index().pivot(columns='PerformanceScore', index='ManagerID', values=0)
df_plot.plot(kind='bar', stacked=True)
plt.title('Zależność między ManagerID a PerformanceScore')

plt.show()

# sns.barplot(x='RecruitmentSource', y='DaysLateLast30', data=df, estimator=np.mean)
# plt.xticks(rotation=45)
# plt.title('Średni czas pracy w zależności od źródła pozyskania pracownika')
# plt.show()