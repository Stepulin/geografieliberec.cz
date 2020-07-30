# %%
from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, ContinuousColorMapper, LogColorMapper, Legend, LegendItem
from bokeh.palettes import brewer, viridis
import pandas as pd
import geopandas as gpd
import json
###
shapefile = '/var/www/html/mapy/published/01-bokeh/data/countries_110m/ne_110m_admin_0_countries.shp'
datafile = '/var/www/html/mapy/published/01-bokeh/datafinal2.csv'
# shapefile = 'data/countries_110m/ne_110m_admin_0_countries.shp'
# datafile = 'datafinal2.csv'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
gdf.columns = ['country', 'country_code', 'geometry']
df = pd.read_csv(datafile)
df_1953 = df[df['midperiod'] == 1953]
merged = gdf.merge(df_1953, left_on = 'country_code', right_on = 'iso_3', how = 'left')
merged.fillna('No data', inplace = True)
merged_json = json.loads(merged.to_json())
json_data = json.dumps(merged_json)
### DELETE ANTARCTICA
gdf = gdf.drop(gdf.index[159])

# %%
geosource = GeoJSONDataSource(geojson = json_data)
palette = brewer["Purples"][7]
palette = palette[::-1]
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 70, nan_color = '#d9d9d9')
tick_labels = {"0": "0", "10": "10", "20":"20", "30":"30", "40":"40", "50":"50", "60":"60", "70":"70"}
color_bar = ColorBar(color_mapper = color_mapper, label_standoff = 8, width = 500, height = 20,
                     border_line_color = None, location = (0,0), orientation = "horizontal", major_label_overrides = tick_labels)
p = figure(title = 'Úmrtnost v roce X', plot_height = 720, plot_width = 1280, toolbar_location = "right")
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.patches('xs','ys', source = geosource,fill_color = {'field' : 'umrtnost', 'transform' : color_mapper}, line_color = 'black', line_width = 0.25, fill_alpha = 1)
p.add_layout(color_bar, 'below')
output_notebook()
show(p)

# %%
from bokeh.io import curdoc, output_notebook
from bokeh.models import Slider, HoverTool, formatters, Axis, BasicTickFormatter, WheelZoomTool, BoxSelectTool, ResetTool, PanTool, SaveTool
from bokeh.layouts import widgetbox, row, column
def json_data(selectedYear):
    yr = selectedYear
    df_yr = df[df['midperiod'] == yr]
    merged = gdf.merge(df_yr, left_on = 'country_code', right_on = 'iso_3', how = 'left')
    merged.fillna('No data', inplace = True)
    merged_json = json.loads(merged.to_json())
    json_data = json.dumps(merged_json)
    return json_data
geosource = GeoJSONDataSource(geojson = json_data(1953))
palette = brewer["Purples"][7]
palette = palette[::-1]
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 70, nan_color = '#d9d9d9')
tick_labels = {"0": "0", "10": "10", "20":"20", "30":"30", "40":"40", "50":"50", "60":"60", "70":"70"}
color_bar = ColorBar(color_mapper = color_mapper, label_standoff = 8, width = 500, height = 20, border_line_color = None, location = (0,0), orientation = "horizontal", major_label_overrides = tick_labels)
hover = HoverTool(tooltips = [('Stát','@country'),('Úmrtnost.', '@umrtnost')])
p = figure(title = 'Úmrtnost v roce X', plot_height = 720, plot_width = 1280, toolbar_location = "right", tools = [hover, ResetTool(), BoxSelectTool(), PanTool(), SaveTool()])
p.add_tools(WheelZoomTool())
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.patches('xs','ys', source = geosource,fill_color = {'field' : 'umrtnost', 'transform' : color_mapper}, line_color = 'black', line_width = 0.25, fill_alpha = 1)
p.add_layout(color_bar, 'below')
def update_plot(attr, old, new):
    yr = slider.value
    new_data = json_data(yr)
    geosource.geojson = new_data
    p.title.text = 'Úmrtnost v roce %d' %yr
slider = Slider(title = 'Rok',start = 1953, end = 2098, step = 5, value = 1953)
slider.on_change('value', update_plot)
layout = column(p,widgetbox(slider))
curdoc().add_root(layout)
output_notebook()
show(layout)

# %%
