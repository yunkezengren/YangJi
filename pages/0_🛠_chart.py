import streamlit as st
import pandas as pd
import numpy as np
import numpy as np
from bokeh.plotting import figure, show
from bokeh.plotting import figure, show
from bokeh.models import Spinner, ColorPicker
from bokeh.layouts import row, column

st.set_page_config(page_title="Chart", page_icon="🛠")

tab0, tab1, tab2, tab3, tab4 = st.tabs(["第零", "第一", "第二", "第三", "第四"])
tab1.write("人生若只如初见")
tab2.write("何事秋风悲画扇")

chart_data1 = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
chart_data2 = pd.DataFrame(np.random.randn(100, 2), columns=['a', 'b'])
chart_data3 = pd.DataFrame(np.random.randn(50, 3),columns=["a", "b", "c"])

tab1.line_chart(chart_data1)
tab2.area_chart(chart_data2)
tab3.bar_chart(chart_data3)

col1, col2 = tab4.columns(2)
col1.line_chart(chart_data3)
col2.bar_chart(chart_data3)


x = np.random.rand(50)
y = np.random.rand(50)

p = figure(title="人生若只如初见",  # 表标题
           width=600, height=600,  # 自动调整到屏幕宽度sizing_mode="stretch_width",
           x_range=(-0.1, 1.1), y_range=(-0.1, 1.1),
           x_axis_label="x轴", y_axis_label="y轴",
           # tools=[BoxZoomTool(), ResetTool(), HoverTool()],
           tools="pan,box_zoom,"  # xpan 鼠标拖动上下左右移动
                 "wheel_zoom,"
                 "xwheel_pan,ywheel_pan,"  # xwheel_pan滚轮控制上下左右移动
                 "tap,hover,reset,save",
           active_scroll="wheel_zoom",
           # tooltips="(@x, @y)",
           tooltips=[("(x,y)", "($x, $y)")],
           )
p.line(x, y, color="#20b2aa", line_width=0.5, legend_label="Temp")
points = p.circle(x=x, y=y, size=20,
                  fill_color="turquoise", fill_alpha=1,
                  line_color="lightsalmon", line_width=1)
spinner1 = Spinner(title="大小", value=20,
                   low=1, step=1, high=200, width=80)
spinner1.js_link('value', points.glyph, 'size')
spinner2 = Spinner(title="填充透明度", value=1, low=0, step=0.1, high=1, width=80)
spinner2.js_link('value', points.glyph, 'fill_alpha')
spinner3 = Spinner(title="线条宽度", value=1, low=0, step=0.1, high=80, width=80)
spinner3.js_link('value', points.glyph, 'line_width')
picker1 = ColorPicker(title="填充颜色", color="turquoise", aspect_ratio=2, width=80)
picker1.js_link('color', points.glyph, 'fill_color')
picker2 = ColorPicker(title="线条颜色", color="lightsalmon", aspect_ratio=2, width=80)
picker2.js_link('color', points.glyph, 'line_color')
# show(row(column(spinner1, spinner2, spinner3, picker1, picker2, width=100), p))
layout = row(column(spinner1, spinner2, spinner3, picker1, picker2, width=100), p)
tab0.bokeh_chart(layout)  # use_container_width=True
st.markdown("""---""")

col1, col2= st.columns(2)
if col1.button('Say hello'):
    col1.write('Why hello there')
else:
    col1.write('Goodbye')

agree = col2.checkbox('I agree')
if agree:
    col2.write('Great!')
else:
    col2.write('No!')
st.markdown("""---""")

col1, col2= st.columns(2)
genre = col1.radio("What's your favorite movie genre",
                 ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    col2.write('You selected comedy.')
else:
    col2.write("You didn't select comedy.")
st.markdown("""---""")

col1, col2= st.columns(2)
options = col1.multiselect('What are your favorite colors',
                         ['Green', 'Yellow', 'Red', 'Blue'],['Yellow', 'Red'])
st.write('You selected:', options)

