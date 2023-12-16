import streamlit as st
from streamlit_echarts import st_echarts

# 将主题更改为黑色
# st.set_page_config(page_title="监控应用", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")
st.set_page_config(layout="wide")
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


    