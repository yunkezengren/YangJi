import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="文本格式", page_icon="👋")

# 输入--------------------------------------------------------------------------------
st.write(1234)  # 可以多参数
st.write('1 + 1 = 2')
st.write({'第一列': [1, 2], 
          "杨宸": {'一': [1, 2], '二': [10, "20"]}, 
          "鸡哥": ["爱学习",[1, 2]]
          })
st.write(1, '+', 1, '=', 2)
data_frame = pd.DataFrame({
    '第一列': [1, 2],
    '第二列': [10, 20],})
st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')

# magic
x = 10
'x', x

st.markdown('Streamlit is **_really_ cool**.')
st.markdown("""
        # h1
        ## h2
        ### h3
        Love **is** *bold*.
        Love __is__ _bold_.
        | Syntax      | Description | Test Text     |
        | :---        |    :----:   |          ---: |
        | Header      | Title       | Here's this   |
        | Paragraph   | Text        | And more      |
        """)


st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')
st.caption('This is a string that explains something above.')
st.text('This is some text.')

code = '''
def hello():
    print("Hello, Streamlit!")
for i in range(10):
        print(i)
        '''
st.code(code, language='python')
st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# 显示交互式小部件-------------------------------------------------------------------------------------------------------------------------
st.button('Click me')
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
# st.download_button('Download file')  # 有问题
# st.camera_input("Take a picture")
st.color_picker('Pick a color')

st.metric('My metric', 42, 20)

# 将小部件添加到侧边栏-------------------------------------------------------------------------------------------------------------------------
# Just add it after st.sidebar:
a = st.sidebar.radio('Select one:', [1, 2])
# Or use "with" notation:
with st.sidebar:
    st.radio('Select one:', ["+", "-"])

# 列-------------------------------------------------------------------------------------------------------------------------
# Two equal columns:
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")
# Three different columns:
col1, col2, col3, col4, col5 = st.columns([2, 1, 2, 1.5, 1])  # col1 is larger.
col1.write("This is column 1")
col2.write("This is column 2")
col3.write("This is column 3")
col4.write("This is column 4")
col5.write("This is column 5")
# # You can also use "with" notation:
# with col1:
#     st.radio('Select one:', [1, 2])

# 选项卡制表符-------------------------------------------------------------------------------------------------------------------------
# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("人生若只如初见")
tab2.write("何事秋风悲画扇")
# # You can also use "with" notation:
# with tab1:
#     st.radio('Select one:', [1, 2])

# form-------------------------------------------------------------------------------------------------------------------------
with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')

# 显示进度和状态-------------------------------------------------------------------------------------------------------------------------
with st.spinner(text='In progress'):
    time.sleep(2)
    # st.balloons()
# # st.progress(progress_variable_1_to_100)
# # st.success('Success message')
st.info('Info message')
st.warning('Warning message')
st.error('Error message')
# st.snow()

