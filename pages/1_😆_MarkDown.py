import streamlit as st

st.set_page_config(page_title="MarkDown", page_icon="😱")

st.markdown("""
### 杨宸
#### 爱学习
***人生***若**只如***初见*.

---
##### 列表
- [Streamlit](https://streamlit.io/) <https://streamlit.io/>
- [Gradio](https://www.gradio.app/) <https://www.gradio.app/>
- [PyWebIo](https://github.com/pywebio/PyWebIO) <https://github.com/pywebio/PyWebIO>

---
##### 表格
| 第一列    |                    第二列                    | 第三列 |
| :-------- | :------------------------------------------: | -----: |
| Streamlit |      [Streamlit](https://streamlit.io/)      |   不错 |
| Gradio    |      [PyWebIo](https://www.gradio.app/)      |   不错 |
| [PyWebIo  | [Gradio](https://github.com/pywebio/PyWebIO) |   不错 |

---
##### 引用
> Streamlit 是一个开源的 Python 库，可以轻松创建和共享用于机器学习和数据科学的精美自定义 Web 应用。只需几分钟，您就可以构建和部署功能强大的数据应用。让我们开始吧！
>> [Streamlit](https://streamlit.io/)&emsp;<https://streamlit.io/>
>>> <https://streamlit.io/>

> Gradio是演示机器学习模型的最快方法，它具有友好的Web界面，因此任何人都可以在任何地方使用它！
>> [Gradio](https://www.gradio.app/)&emsp;<https://www.gradio.app/>
>>>  <https://www.gradio.app/>

> PyWebIO提供了一系列命令式的交互函数来在浏览器上获取用户输入和进行输出，将浏览器变成了一个“富文本终端”，可以用于构建简单的Web应用或基于浏览器的GUI应用。
>> [PyWebIo](https://github.com/pywebio/PyWebIO)&emsp;<https://github.com/pywebio/PyWebIO>
>>> <https://github.com/pywebio/PyWebIO>

---
##### 代码块
```python
import streamlit as st
st.set_page_config(page_title="MarkDown", page_icon="😱")
st.markdown()
```

---
#### 任务列表
- [x] GFM task list 1
    - [ ] GFM task list 1-1
- [ ] GFM task list 2
    - [ ] GFM task list 2-1
---

<font color=blue>蓝色</font>  <br /> 
<font color=orange>橙色</font>  <br /> 
<p style="color:#42F3EF;font-size:30px;">人生若只如初见</p>
<p style="text-align:center;font-family:仿宋;">heading 1-人生</p>
<hr />
""",  unsafe_allow_html=True)

col1, col2 = st.columns(2)
table = """
##### 表格
| 第一列    |                    第二列                    | 第三列 |
| :-------- | :------------------------------------------: | -----: |
| Streamlit |      [Streamlit](https://streamlit.io/)      |   不错 |
| Gradio    |      [PyWebIo](https://www.gradio.app/)      |   不错 |
| [PyWebIo  | [Gradio](https://github.com/pywebio/PyWebIO) |   不错 |
"""
col1.markdown(table)
col2.markdown(table)

