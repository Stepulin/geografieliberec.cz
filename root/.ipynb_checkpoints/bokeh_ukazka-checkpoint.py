# %%
from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, ContinuousColorMapper, LogColorMapper, Legend, LegendItem
from bokeh.palettes import brewer, viridis
import pandas as pd
import geopandas as gpd
import json
###
shapefile = '/var/www/html/mapy/ukazky/01-bokeh/data/countries_110m/ne_110m_admin_0_countries.shp'
datafile = '/var/www/html/mapy/ukazky/01-bokeh/datafinal.csv'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
gdf.columns = ['country', 'country_code', 'geometry']
df = pd.read_csv(datafile)
df_2019 = df[df['time'] == 2019]
merged = gdf.merge(df_2019, left_on = 'country_code', right_on = 'iso_3', how = 'left')
merged.fillna('No data', inplace = True)
merged_json = json.loads(merged.to_json())
json_data = json.dumps(merged_json)
### DELETE ANTARCTICA
gdf = gdf.drop(gdf.index[159])

# %%
geosource = GeoJSONDataSource(geojson = json_data)
palette = brewer["YlGnBu"][8]
palette = palette[::-1]
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 40000000, nan_color = '#d9d9d9')
tick_labels = {"0": "0", "5000000": "5,000,000",
 "10000000":"10,000,000", "15000000":"15,000,000",
 "20000000":"20,000,000", "25000000":"25,000,000",
 "30000000":"30,000,000", "35000000":"35,000,000",
 "40000000":"40,000,000+"}
color_bar = ColorBar(color_mapper = color_mapper, label_standoff = 8, width = 500, height = 20,
                     border_line_color = None, location = (0,0), orientation = "horizontal", major_label_overrides = tick_labels)
p = figure(title = 'Celkový počet obyvatel v roce 2019', plot_height = 720, plot_width = 1280, toolbar_location = "right")
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.patches('xs','ys', source = geosource,fill_color = {'field' : 'pocet_ob', 'transform' : color_mapper}, line_color = 'black', line_width = 0.25, fill_alpha = 1)
p.add_layout(color_bar, 'below')
output_notebook()
show(p)

# %%
from bokeh.io import curdoc, output_notebook
from bokeh.models import Slider, HoverTool, formatters, Axis, BasicTickFormatter, WheelZoomTool, BoxSelectTool, ResetTool, PanTool, SaveTool
from bokeh.layouts import widgetbox, row, column
def json_data(selectedYear):
    yr = selectedYear
    df_yr = df[df['time'] == yr]
    merged = gdf.merge(df_yr, left_on = 'country_code', right_on = 'iso_3', how = 'left')
    merged.fillna('No data', inplace = True)
    merged_json = json.loads(merged.to_json())
    json_data = json.dumps(merged_json)
    return json_data
geosource = GeoJSONDataSource(geojson = json_data(2019))
palette = brewer["YlGnBu"][8]
palette = palette[::-1]
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 40000000,  nan_color = '#d9d9d9')
tick_labels = {"0": "0", "5000000": "5,000,000",
 "10000000":"10,000,000", "15000000":"15,000,000",
 "20000000":"20,000,000", "25000000":"25,000,000",
 "30000000":"30,000,000", "35000000":"35,000,000",
 "40000000":"40,000,000+"}
color_bar = ColorBar(color_mapper = color_mapper, label_standoff = 8, width = 500, height = 20,
                     border_line_color = None, location = (0,0), orientation = "horizontal", major_label_overrides = tick_labels)
hover = HoverTool(tooltips = [ ('Stát','@country'),('Počet ob.', '@pocet_ob')])
p = figure(title = 'Celkový počet obyvatel v roce 2019', plot_height = 720, plot_width = 1280, toolbar_location = "right", tools = [hover, ResetTool(), BoxSelectTool(), PanTool(), SaveTool()])
p.add_tools(WheelZoomTool())
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.patches('xs','ys', source = geosource,fill_color = {'field' : 'pocet_ob', 'transform' : color_mapper}, line_color = 'black', line_width = 0.25, fill_alpha = 1)
p.add_layout(color_bar, 'below')
def update_plot(attr, old, new):
    yr = slider.value
    new_data = json_data(yr)
    geosource.geojson = new_data
    p.title.text = 'Celkový počet obyvatel v roce %d' %yr
slider = Slider(title = 'Rok',start = 1950, end = 2019, step = 1, value = 2019)
slider.on_change('value', update_plot)
layout = column(p,widgetbox(slider))
curdoc().add_root(layout)
output_notebook()
show(layout)

# %%
