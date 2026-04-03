import panel as pn
import holoviews as hv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.models import HoverTool

from dashboard.charts import *

hv.extension('bokeh')

def create_home(data):
    no_of_credible = data[data['Creditability'] == 1]['Creditability'].sum()
    average_credit_amount = data['Credit.Amount'].mean()
    percentage_of_employed_clients = (data[data['Occupation'] == 1]['Occupation'].sum() / data['Occupation'].sum()) * 100

    home_content = pn.Column(
        "<h1>Analytics</h1>",
        pn.Row(
            pn.Card(
                pn.pane.HTML(f""" <h4 style="text-align: center">No. of Creditable Clients</h4> 
                                <h1 style="text-align: center">{no_of_credible}</h1> """),
                collapsible=False,
                hide_header=True,
                styles={'background': 'white'},
                margin=(3, 3)
            ),
            pn.Card(
                pn.pane.HTML(f""" <h4 style="text-align: center">Average Credit Amount</h4> 
                                <h1 style="text-align: center">DM {round(average_credit_amount, 2)}</h1> """),
                collapsible=False,
                hide_header=True,
                styles={'background': 'white'},
                margin=(3, 3)
            ),
            pn.Card(
                pn.pane.HTML(f""" <h4 style="text-align: center">Percentage of Unemployed Clients</h4> 
                                <h1 style="text-align: center">{round(percentage_of_employed_clients)}%</h1> """),
                collapsible=False,
                hide_header=True,
                styles={'background': 'white'},
                margin=(3, 3)
            )
        ),
        pn.Row(
            loan_duration_vs_credibility_line_chart(data),
        ),
        pn.Row(
            account_balance_risk_bar_chart(data),
            years_emmployed_vs_credibility_line_chart(data),
        ),
    )
    return home_content

def create_demographics(data):
    average_clients_age = data['Age..years.'].mean()

    demographic_dashboard_content = pn.Column(
        "<h1>Client Demographics</h1>",
        pn.Row(
            pn.Card(
                pn.pane.HTML(f""" <h4 style="text-align: center">Average Client's Age</h4> 
                                <h1 style="text-align: center">{round(average_clients_age)}</h1> """),
                collapsible=False,
                hide_header=True,
                styles={'background': 'white'},
                margin=(3, 3)
            ),
        ),
        pn.Row(
            demographic_dashboard(data),
            sex_marital_distribution_donut(data),
        ),


    )
    return demographic_dashboard_content


def create_form(widgets, remarks, confidence):
    submit_btn = widgets.pop("submit")

    fields = list(widgets.values())

    grid = pn.Card(
    pn.GridBox(
        *fields,
        ncols=3,
    ),
    pn.Row(
        submit_btn, align="center",
        styles={
            "margin-top": "10px"
        },
    ),
    styles={
        "border-radius": "12px",
        "box-shadow": "0 4px 12px rgba(0,0,0,0.08)",
        "padding": "20px",
        "margin": "5px",
        "background": "white"
    },
    collapsible=False,
    hide_header=True,
    )

    return pn.Column(
        "# Risk Analysis",
        pn.Row(remarks, confidence, sizing_mode="stretch_width"),
        grid,
        sizing_mode="stretch_width",
        margin=20
    )
