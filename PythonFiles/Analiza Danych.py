import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('HRDataset.csv')

df_plot = df.groupby(['ManagerID', 'PerformanceScore']).size().reset_index().pivot(columns='PerformanceScore', index='ManagerID', values=0)
df_plot.plot(kind='bar', stacked=True)

plt.show()

#done in notebook as it was more description based task