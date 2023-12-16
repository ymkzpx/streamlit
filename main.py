# import streamlit as st

# # 设置页面标题和布局
# st.set_page_config(page_title='监控Dashboard')

# # 创建一个选择器在sidebar上，作为最顶层的选项
# primary_selection = st.sidebar.radio("选择监控类型", ["系统状态", "性能指标"])

# # 根据顶层选择，展示不同的二级层次选项和内容
# if primary_selection == "系统状态":
#     with st.container():
#         # 创建二级层次
#         st.header("系统状态监控")
#         # 可以用`st.expander`来显示或隐藏进一步的详细信息
#         with st.expander("CPU状态"):
#             st.write("CPU使用率")
#             # 展示CPU使用率指标的代码
            
#         with st.expander("内存状态"):
#             st.write("内存使用情况")
#             # 展示内存使用指标的代码

# elif primary_selection == "性能指标":
#     with st.container():
#         # 创建二级层次
#         st.header("性能指标监控")
#         # 使用`st.expander`来显示或隐藏详细信息
#         with st.expander("网络性能"):
#             st.write("网络吞吐量和延迟")
#             # 展示网络相关指标的代码
            
#         with st.expander("磁盘性能"):
#             st.write("磁盘读写速率")
#             # 展示磁盘使用指标的代码

import streamlit as st

# 自定义边框样式
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# 你也可以直接在这里写入CSS字符串
sidebar_css = """
        <style>
            .css-1d391kg {
                border: 2px solid #009688;
                border-radius: 5px;
            }
        </style>
        """

# 添加CSS到侧边栏
st.markdown(sidebar_css, unsafe_allow_html=True)

# 使用 sidebar
st.sidebar.header('侧边栏标题')

# 其他内容 ...
