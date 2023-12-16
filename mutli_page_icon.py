import streamlit as st
from streamlit_echarts import st_echarts
from st_pages import Page, show_pages, add_page_title

st.set_page_config(layout="wide")

# Optional -- adds the title and icon to the current page
# add_page_title("CNSTK INTRA2")
# st.set_page_config(
#     page_title="Hello world",
#     page_icon="chart_with_upwards_trend",
#     layout="wide",
# )

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Page("pages/page1.py", "CNSTK INTRA", "🇨🇳")
    ]
)

# add_page_title()

# 创建外层tab
tabs = st.sidebar.radio("选择监控选项", ("指标一", "指标二", "指标三"))

# 创建不同的指标页面
if tabs == "指标一":
    
    st.title("指标一监控页面")
    col1, col2 = st.columns(2)
    with col1:
      arr = [820, 932, 901, 934, 1290, 1330, 1320]
      option = {
          "title": [
              {"text": "Michelson-Morley Experiment", "left": "center"},
              {
                  "text": "upper: Q3 + 1.5 * IQR \nlower: Q1 - 1.5 * IQR",
                  "borderColor": "#999",
                  "borderWidth": 1,
                  "textStyle": {"fontWeight": "normal", "fontSize": 14, "lineHeight": 20},
                  "left": "10%",
                  "top": "90%",
              },
          ],
          "tooltip": {
              "trigger": 'axis'
          },
          "legend": {
              "data": ['销量2']  # 图例名称，对应 series 中的 name
          },
          "xAxis": {
              "type": "category",
              "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
          },
          "yAxis": {"type": "value", "name": "gain_bps"},
          "series": [{"data": arr, "type": "line"}],
          "splitArea": {"show": True},
          
      }
      
      st_echarts(
          options=option, height="400px", key="echarts-1", width="100%",
      )
    with col2:
      arr = [820, 932, 901, 934, 1290, 1330, 1320]
      option = {
          "xAxis": {
              "type": "category",
              "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
          },
          "yAxis": {"type": "value"},
          "series": [{"data": arr, "type": "line"}],
      }
      
      st_echarts(
          options=option, height="400px", key="echarts-2", width="100%",
      )

elif tabs == "指标二":
    st.title("指标二监控页面")
    # 添加指标二的监控内容

elif tabs == "指标三":
    st.title("指标三监控页面")
    # 添加指标三的监控内容


    

# # 定义每个页面的函数
# def page1():
#     st.header("这是页面 1")
#     # 在这里放置页面 1 的内容

# def page2():
#     st.header("这是页面 2")
#     # 在这里放置页面 2 的内容

# def page3():
#     st.header("这是页面 3")
#     # 在这里放置页面 3 的内容

# # 创建页面字典
# pages = {
#     "页面 1": page1,
#     "页面 2": page2,
#     "页面 3": page3,
# }

# 标题和选择框
# st.title("多页面应用")

# # 创建垂直排列的单选按钮  
# selected_page = st.radio("选择一个页面", list(pages.keys()))

# # 直接调用选择的页面函数
# pages[selected_page]()
