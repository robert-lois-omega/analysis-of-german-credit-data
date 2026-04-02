
import panel as pn
import pandas as pd
import numpy as np
import holoviews as hv
from math import pi
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

def account_balance_risk_bar_chart(df: pd.DataFrame):
    balance_map = {
        1: "No running account",
        2: "No balance or debit",
        3: "Balance between 0 and < 200 DM",
        4: "Balance ≥ 200 DM or active ≥ 1 year"
    }

    df_plot = df.dropna(subset=["Account.Balance", "Creditability"]).copy()
    df_plot["Account Balance Label"] = df_plot["Account.Balance"].map(balance_map)

    df_plot["Risk"] = df_plot["Creditability"].map({
        1: "Good",
        0: "Bad"
    })

    grouped = df_plot.groupby(
        ["Account Balance Label", "Risk"]
    ).size().reset_index(name="Count")

    category_order = list(balance_map.values())
    grouped["Account Balance Label"] = pd.Categorical(
        grouped["Account Balance Label"],
        categories=category_order,
        ordered=True
    )

    grouped = grouped.sort_values("Account Balance Label")

    bars = hv.Bars(
        grouped,
        kdims=["Account Balance Label", "Risk"],
        vdims=["Count"]
    ).opts(
        stacked=True,
        width=650,
        height=300,
        cmap=["#4F94A0", "#2CBBD4"],
        legend_position="top",
        tools=["hover"],
        xlabel="Account Balance",
        ylabel="Number of Customers",
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

def sex_marital_distribution_donut(df: pd.DataFrame):

    sex_map = {
        1: "Male : Divorced/Separated",
        4: "Female : Divorced/Married",
        2: "Male : Single",
        3: "Male : Married/Widowed",
        5: "Female : Single"
    }

    df_plot = df.dropna(subset=["Sex...Marital.Status"]).copy()
    df_plot["Category"] = df_plot["Sex...Marital.Status"].map(sex_map)

    grouped = df_plot["Category"].value_counts().reset_index()
    grouped.columns = ["Category", "Count"]

    grouped["angle"] = grouped["Count"] / grouped["Count"].sum() * 2 * pi
    grouped["color"] = Category20c[len(grouped)]

    p = figure(
        height=300,
        width=500,
        toolbar_location=None,
        tools="hover",
        tooltips="@Category: @Count",
        x_range=(-0.5, 1.0)
    )

    p.wedge(
        x=0, y=1,
        radius=0.4,
        start_angle=cumsum("angle", include_zero=True),
        end_angle=cumsum("angle"),
        line_color="white",
        fill_color="color",
        legend_field="Category",
        source=grouped
    )

    p.circle(x=0, y=1, radius=0.2, color="white")

    p.axis.visible = False
    p.grid.visible = False

    card = pn.Card(
        pn.Column(
            pn.pane.HTML("<h2 style='text-align:center;'>Sex & Marital Status</h2>"),
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

    return card

# IGNORE
def creadibility_vs_loan_duration(df: pd.DataFrame):

    df_plot = df.rename(columns={
        'Duration.of.Credit..month.': 'Duration',
        'Creditability': 'Risk'
    })

    df_plot['Risk'] = df_plot['Risk'].map({
        1: 'Good',
        0: 'Bad'
    }).fillna(df_plot['Risk'])

    box_plot = hv.BoxWhisker(
        data=df_plot,
        kdims=['Risk'],
        vdims=['Duration']
    ).opts(
        width=1000,
        height=300,
        box_fill_color='Risk',
        cmap='Category10',
        tools=['hover'],
        xlabel="Creditability",
        ylabel="Duration (Months)"
    )
    
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