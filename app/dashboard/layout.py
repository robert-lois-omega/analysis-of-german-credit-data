import panel as pn

def create_layout(home, form, demographics):

    BG = "#ffffff"
    CARD = "#f5dddd"

    header = pn.Row(
        pn.pane.Image('./img/logo.jpg', width=120),
        sizing_mode="stretch_width",
        height=100,
        styles={
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "background-color": "white",
            "padding": "10px 20px"
        }
    )

    tabs = pn.Tabs(
        ("Home", home),
        ("Demographics", demographics),
        ("Risk Analyzer", form),
        dynamic=True,
        tabs_location="above",
        sizing_mode="stretch_both",
        stylesheets=[
            """
            .bk-tab {
                font-size: 14px !important;
                padding: 12px 20px !important;
            }
            """
        ]
    )
    content = pn.Column(
        pn.Card(
            tabs,
            styles={
                "border-radius": "12px",
                "box-shadow": "0 4px 12px rgba(0,0,0,0.08)",
                "padding": "10px",
                'background': "#ffffff"
            },
            collapsible=False,
            sizing_mode="scale_both",
            hide_header=True,
        ),
        margin=10,
    )

    main_area = pn.Column(
        header,
        content,
        styles={"background": BG},
        sizing_mode="stretch_both"
    )

    layout = pn.Row(
        main_area,
        sizing_mode="stretch_both"
    )

    return layout