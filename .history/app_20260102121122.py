import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("pink_morsels_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f4f6f8",
        "padding": "30px"
    },
    children=[
        html.H1(
            "Soul Foods – Pink Morsels Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "20px"
            }
        ),

        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "8px",
                "boxShadow": "0 4px 10px rgba(0,0,0,0.1)",
                "marginBottom": "20px"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        "fontWeight": "bold",
                        "marginBottom": "10px",
                        "display": "block"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginBottom": "10px"}
                ),
            ]
        ),

        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "8px",
                "boxShadow": "0 4px 10px rgba(0,0,0,0.1)"
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# Callback for filtering data
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        title="Pink Morsels Sales Over Time",
        labels={
            "Date": "Date",
            "Sales": "Total Sales"
        }
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app = dash.Dash(__name__)

    app.run(debug=True)
