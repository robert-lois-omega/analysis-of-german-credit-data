
import panel as pn
import pandas as pd
import numpy as np
import holoviews as hv
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.models import HoverTool


def years_emmployed_vs_credibility_line_chart(data):

    df = data.dropna(subset=["Length.of.current.employment"]).copy()
    df["Length.of.current.employment"] = df["Length.of.current.employment"].astype(str)
    grouped = df.groupby("Length.of.current.employment")["Creditability"].agg([
        "count", "sum"
    ]).reset_index()

    grouped["bad_rate"] = (grouped["count"] - grouped["sum"]) / grouped["count"]
    x_factors = grouped["Length.of.current.employment"].tolist()

    if len(x_factors) == 0:
        return pn.pane.HTML("<b>No data available for Employment Duration</b>")

    source = ColumnDataSource(grouped)

    p = figure(
        x_range=x_factors,
        height=300,
        tools="pan,wheel_zoom,reset"
    )

    p.line(
        x="Length.of.current.employment",
        y="bad_rate",
        source=source,
        line_width=3
    )

    p.scatter(
        x="Length.of.current.employment",
        y="bad_rate",
        source=source,
        size=8
    )

    hover = HoverTool(
        tooltips=[
            ("Years Employed", "@{Length.of.current.employment}"),
            ("Credibility", "@bad_rate{0.0%}"),
            ("Total Clients", "@count")
        ]
    )

    p.add_tools(hover)

    p.yaxis.axis_label = "Credibility"
    p.xaxis.axis_label = "Years Employed"

    return pn.Card(
        pn.Column(
            pn.pane.HTML("<h2 style='text-align:center;'>Years Employed VS Credibility</h2>"),
            p
        ),
            styles={
                "border-radius": "12px",
                "box-shadow": "0 4px 12px rgba(0,0,0,0.08)",
                "padding": "10px",
                "margin": "5px"
            },
            collapsible=False,
            hide_header=True,
    )

def loan_duration_vs_credibility_line_chart(data):

    df = data.dropna(subset=["Duration.of.Credit..month."]).copy()
    df["Duration.of.Credit..month."] = df["Duration.of.Credit..month."].astype(int)

    grouped = df.groupby("Duration.of.Credit..month.")["Creditability"].agg([
        "count", "sum"
    ]).reset_index()

    grouped = grouped.sort_values(by="Duration.of.Credit..month.")
    grouped["bad_rate"] = (grouped["count"] - grouped["sum"]) / grouped["count"]
    grouped["Duration.of.Credit..month."] = grouped["Duration.of.Credit..month."].astype(str)

    x_factors = grouped["Duration.of.Credit..month."].tolist()

    if len(x_factors) == 0:
        return pn.pane.HTML("<b>No data available for Employment Duration</b>")

    source = ColumnDataSource(grouped)

    p = figure(
        x_range=x_factors,
        width=1300,
        height=300,
        tools="pan,wheel_zoom,reset"
    )

    p.line(
        x="Duration.of.Credit..month.",
        y="bad_rate",
        source=source,
        line_width=3
    )

    p.scatter(
        x="Duration.of.Credit..month.",
        y="bad_rate",
        source=source,
        size=8
    )

    hover = HoverTool(
        tooltips=[
            ("Loan Duration", "@{Duration.of.Credit..month.}"),
            ("Credibility", "@bad_rate{0.0%}"),
            ("Total Clients", "@count")
        ]
    )

    p.add_tools(hover)

    p.yaxis.axis_label = "Credibility"
    p.xaxis.axis_label = "Loan Duration"

    return pn.Card(
        pn.Column(
            pn.pane.HTML("<h2 style='text-align:center;'>Loan Duration VS Credibility</h2>"),
            p
        ),
            styles={
                "border-radius": "12px",
                "box-shadow": "0 4px 12px rgba(0,0,0,0.08)",
                "padding": "10px",
                "margin": "5px"
            },
            collapsible=False,
            hide_header=True,
            sizing_mode="stretch_width",
    )

def account_balance_risk_bard_chart(df: pd.DataFrame):

    df_plot = df.dropna(subset=["Account.Balance", "Creditability"]).copy()

    df_plot["Risk"] = df_plot["Creditability"].map({
        1: "Good",
        0: "Bad"
    }).fillna(df_plot["Creditability"])

    grouped = df_plot.groupby(["Account.Balance", "Risk"]).size().reset_index(name="Count")

    bars = hv.Bars(
        data=grouped,
        kdims=["Account.Balance", "Risk"],
        vdims=["Count"]
    ).opts(
        stacked=True,
        width=600,
        height=400,
        cmap="Category10",
        legend_position="top",
        tools=["hover"],
        xlabel="Account Balance Category",
        ylabel="Number of Customers",
        title="Account Balance vs Credit Risk"
    )

    card = pn.Card(
        pn.Column(
            pn.pane.HTML("<h2 style='text-align:center;'>Account Balance vs Risk</h2>"),
            bars
        ),
        styles={
            "border-radius": "12px",
            "box-shadow": "0 4px 12px rgba(0,0,0,0.08)",
            "padding": "10px",
            "margin": "5px"
        },
        collapsible=False,
        hide_header=True,
    )

    return card



def demographic_dashboard(df):

    hist, edges = np.histogram(df["Age..years."], bins=10)

    source = ColumnDataSource(data=dict(
        top=hist,
        left=edges[:-1],
        right=edges[1:]
    ))

    p = figure(
        title="",
        height=300,
        width=600,
        tools="pan,wheel_zoom,reset"
    )

    p.quad(
        top='top',
        bottom=0,
        left='left',
        right='right',
        source=source
    )

    # Hover tool
    p.add_tools(HoverTool(
        tooltips=[
            ("Age Range", "@left{0} - @right{0}"),
            ("Count", "@top")
        ]
    ))

    return pn.Card(
        pn.Column(
            pn.pane.HTML("<h2 style='text-align:center;'>Age Distribution</h2>"),
            p
        ),
            styles={
                "border-radius": "12px",
                "box-shadow": "0 4px 12px rgba(0,0,0,0.08)",
                "padding": "10px",
                "margin": "5px"
            },
            collapsible=False,
            hide_header=True,
    )

# IGNORE
def creadibility_vs_loan_duration(df: pd.DataFrame):

    # Rename columns for cleaner plotting (optional but recommended)
    df_plot = df.rename(columns={
        'Duration.of.Credit..month.': 'Duration',
        'Creditability': 'Risk'
    })

    # Map Creditability to readable labels (optional)
    df_plot['Risk'] = df_plot['Risk'].map({
        1: 'Good',
        0: 'Bad'
    }).fillna(df_plot['Risk'])

    # Create box plot
    box_plot = hv.BoxWhisker(
        data=df_plot,
        kdims=['Risk'],
        vdims=['Duration']
    ).opts(
        width=1000,
        height=400,
        box_fill_color='Risk',
        cmap='Category10',
        tools=['hover'],
        xlabel="Creditability",
        ylabel="Duration (Months)"
    )

    # Wrap in Panel Card
    card = pn.Card(
        pn.Column(
            pn.pane.HTML(
                "<h2 style='text-align:center;'>Loan Duration vs Risk</h2>"
            ),
            box_plot
        ),
        styles={
                "border-radius": "12px",
                "box-shadow": "0 4px 12px rgba(0,0,0,0.08)",
                "padding": "10px",
                "margin": "5px"
            },
        collapsible=False,
        hide_header=True,
    )

    return card