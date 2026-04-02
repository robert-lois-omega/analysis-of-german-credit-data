import panel as pn
import holoviews as hv

from data.loader import load_data
from model.train import train_model
from dashboard.widgets import create_widgets
from dashboard.callbacks import create_callback
from dashboard.views import create_home, create_form
from dashboard.layout import create_layout

hv.extension('bokeh')

# Load
data = load_data()
model = train_model()

# Widgets
widgets = create_widgets()

# Output panes
remarks = pn.pane.Markdown("<b style='font-size:16px;'>Credit: </b>")
confidence = pn.pane.Markdown("<b style='font-size:16px;'>Confidence: </b>" \
"<span style='color:gray;'>0.00%</span>")

# Callback
callback = create_callback(model, widgets, remarks, confidence)
widgets["submit"].on_click(callback)

# Views
home = create_home(data)
form = create_form(widgets, remarks, confidence)

dashboard = create_layout(home, form)

# Run
dashboard.show()