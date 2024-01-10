import pandas as pd
import cufflinks as cf
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df_miedz = pd.read_csv('ca_c_f_d.csv')
df_miedz['Data'] = pd.to_datetime(df_miedz['Data'])
df_miedz = df_miedz.set_index('Data')
df_KGHM = pd.read_csv('kgh_d.csv')
df_KGHM['Data'] = pd.to_datetime(df_KGHM['Data'])
df_KGHM = df_KGHM.set_index('Data')

fig = make_subplots(rows=3, cols=1, subplot_titles=['KGHM', 'Miedź', 'Tabela'], shared_xaxes=True)
fig.add_trace(df_KGHM.iplot(kind='scatter', mode='lines', asFigure=True, colors=['blue'])['data'][3], row=1, col=1)
fig.add_trace(df_miedz.iplot(kind='scatter', mode='lines', asFigure=True, colors=['red'])['data'][3], row=2, col=1)
fig.update_layout(height=800, width=800, showlegend=False)
fig.update_xaxes(showticklabels=False, row=1, col=1)
years = [str(year) for year in df_miedz.index.year]
fig.update_xaxes(row=2, col=1, tickmode='array', tickvals=df_miedz.index.year, ticktext=years)
table = go.Table(
    header=dict(values=['Data', 'KGHM', 'Miedź']),
    cells=dict(values=[df_KGHM.index.date, df_KGHM['Zamkniecie'], df_miedz['Zamkniecie']]),
    columnwidth=[40, 80, 80]
)
fig2 = go.Figure(data=[table])
fig2.update_layout(height=600, width=800)
fig2.write_html("fig2.html")
# fig.add_table(table)
# fig.add_trace(fig2['data'][0], row=3, col=1)
fig.add_trace(table)
fig.write_html("fig.html")

