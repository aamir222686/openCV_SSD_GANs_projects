from bokeh.plotting import output_file, show, figure
from bokeh.models import HoverTool, ColumnDataSource
from cv2_motion_detector import df

df['Start_string'] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
df['End_string'] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

f = figure(x_axis_type='datetime', height=400, width=1000, title='Motion Graph')
f.yaxis.minor_tick_line_color=None

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
f.add_tools(hover)

q = f.quad(left='Start', right='End', bottom=0, top=1, color='green', source=cds)

output_file('graph.html')
show(f)
