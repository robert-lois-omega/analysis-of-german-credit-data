import panel as pn
import holoviews as hv

from data.loader import load_data
from model.train import train_model
from dashboard.widgets import create_widgets
from dashboard.callbacks import create_callback
from dashboard.views import create_home, create_form, create_demographics
from dashboard.layout import create_layout

hv.extension('bokeh')

data = load_data()
model = train_model()

widgets = create_widgets()

remarks = pn.pane.Markdown("<b style='font-size:16px;'>Credit: </b>")
confidence = pn.pane.Markdown("<b style='font-size:16px;'>Confidence: </b>" \
"<span style='color:gray;'>0.00%</span>")

callback = create_callback(model, widgets, remarks, confidence)
widgets["submit"].on_click(callback)

home = create_home(data)
form = create_form(widgets, remarks, confidence)
demographics = create_demographics(data)

dashboard = create_layout(home, form, demographics)

dashboard.show()