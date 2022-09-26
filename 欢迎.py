import streamlit as st

st.set_page_config(page_title="杨宸爱学习",page_icon="👋")

st.write("# 👋 欢迎使用Streamlit!")

st.sidebar.success("选择一个上方的demo")
st.markdown(
    """
    Streamlit 是一个专为机器学习和数据科学项目构建的开源应用程序框架。\n
    人生若只如初见
    **👈 看看左侧边栏** 看看Streamlit可以做什么的一些例子！
    ### 想要了解什么?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community forums](https://discuss.streamlit.io)
    ### 看更多的演示!
    - Use a neural net to [analyze the Udacity Self-driving Car Image Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)