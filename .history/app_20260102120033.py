import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("pink_morsels_sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsels Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Dash app setup
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods Pink Morsels Sales Visualiser",
            style={"textAlign": "center"}
        ),

        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
