# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import style, sim_data

st.markdown(style.css(), unsafe_allow_html=True)
st.title("管理者数据看板")
st.caption("适老化指数 · 事件趋势 · 类型分布 · 响应分析（数据为模拟）")

k1, k2, k3, k4, k5 = st.columns(5)
k1.markdown(style.kpi("128", "本月异常事件"), unsafe_allow_html=True)
k2.markdown(style.kpi("21", "其中跌倒事件"), unsafe_allow_html=True)
k3.markdown(style.kpi("1.8 min", "平均响应时长"), unsafe_allow_html=True)
k4.markdown(style.kpi("94%", "处置及时率"), unsafe_allow_html=True)
k5.markdown(style.kpi("82 / 100", "城市适老化指数"), unsafe_allow_html=True)

st.subheader("事件趋势（近30天，模拟）")
trend = sim_data.gen_trend()
fig_trend = px.bar(
    trend, x="date", y=["跌倒", "其他异常"],
    color_discrete_map={"跌倒": "#A32D2D", "其他异常": "#EF9F27"},
    barmode="stack", height=300,
)
fig_trend.update_layout(legend_title_text="", margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_trend, use_container_width=True)

col_a, col_b = st.columns(2)
with col_a:
    st.subheader("事件类型分布")
    dist = sim_data.gen_type_dist()
    fig_type = px.bar(dist, y="类型", x="次数", orientation="h", height=300,
                      color="次数", color_continuous_scale=["#9FE1CB", "#0F6E56"])
    fig_type.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_type, use_container_width=True)
with col_b:
    st.subheader("各节点事件数")
    nb = sim_data.gen_node_bar()
    fig_node = px.bar(nb, y="节点", x="事件数", orientation="h", height=300,
                      color="事件数", color_continuous_scale=["#B5D4F4", "#185FA5"])
    fig_node.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_node, use_container_width=True)

col_c, col_d = st.columns(2)
with col_c:
    st.subheader("城市适老化指数")
    gauge = go.Figure(go.Indicator(
        mode="gauge+number", value=82,
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#0F6E56"},
               "steps": [{"range": [0, 60], "color": "#FCEBEB"},
                         {"range": [60, 80], "color": "#FAEEDA"},
{"range": [80, 100], "color": "#E1F5EE"}]},
    ))
    gauge.update_layout(height=300, margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(gauge, use_container_width=True)
with col_d:
    st.subheader("告警响应时长分布（模拟）")
    rng = np.random.default_rng(3)
    resp = rng.lognormal(mean=np.log(110), sigma=0.35, size=400).astype(int)
    fig_resp = px.histogram(resp, nbins=24, height=300,
                            color_discrete_sequence=["#1D9E75"])
    fig_resp.update_layout(xaxis_title="响应时长（ms）", yaxis_title="频次",
                           margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_resp, use_container_width=True)

st.markdown('<div class="sg-note">指数综合设施覆盖率、事件密度、响应时长与处置及时率等维度，'
            '用于政府端城市适老化治理评估（当前为模拟值）。</div>', unsafe_allow_html=True)
