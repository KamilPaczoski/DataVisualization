from dash import dcc
from dash import html
import plotly.graph_objects as go


def render_tab3(df):
    df_sales_by_type = df.groupby([df['tran_date'].dt.dayofweek, 'Store_type'])[
        'total_amt'].sum().reset_index()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df_sales_by_type['day_of_week'] = df_sales_by_type['tran_date'].map(lambda x: weekdays[x])

    fig = go.Figure()
    for store_type in df_sales_by_type['Store_type'].unique():
        store_type_data = df_sales_by_type[df_sales_by_type['Store_type'] == store_type]
        fig.add_trace(go.Bar(x=store_type_data['day_of_week'], y=store_type_data['total_amt'], name=store_type))
    fig.update_layout(barmode='group', xaxis_title='Dzień tygodnia', yaxis_title='Ilośc sprzedaży')

    layout = html.Div([html.H1('Kanały sprzedaży na przestrzeni dni tygodnia', style={'text-align': 'center'}),
                       dcc.Graph(id='bar-sales-by-store-type', figure=fig)])

    return layout
