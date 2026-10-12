# -*- coding: utf-8 -*-
import sys, os, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from streamlit.components.v1 import html as st_html
import style, sim_data

st.markdown(style.css(), unsafe_allow_html=True)
st.title("实时监测看板")
st.caption("多节点运行状态 · 模拟主监测视图 · SOS 本地快速告警（数据为模拟）")

if "seed" not in st.session_state:
    st.session_state.seed = 0

ctrl1, ctrl2 = st.columns([1, 2])
with ctrl1:
    if st.button("立即刷新", use_container_width=True):
        st.session_state.seed += 1
        st.rerun()
with ctrl2:
    st.checkbox("模拟实时推送（每 3 秒）", key="live")
if st.session_state.get("live"):
    time.sleep(3)
    st.session_state.seed += 1
    st.rerun()

nodes = sim_data.gen_nodes(st.session_state.seed)
online = sum(1 for n in nodes if n["status"] == "在线")
alarm = sum(1 for n in nodes if n["status"] == "告警")
people = sum(n["people"] for n in nodes)
avg_lat = round(sum(n["latency_ms"] for n in nodes) / len(nodes))

k1, k2, k3, k4 = st.columns(4)
k1.markdown(style.kpi("%d/%d" % (online, len(nodes)), "在线节点"), unsafe_allow_html=True)
k2.markdown(style.kpi(str(alarm), "告警节点"), unsafe_allow_html=True)
k3.markdown(style.kpi(str(people), "当前监测人数"), unsafe_allow_html=True)
k4.markdown(style.kpi("%d ms" % avg_lat, "平均推理延迟（模拟）"), unsafe_allow_html=True)

for n in [x for x in nodes if x["sos"]]:
    st.error("SOS 本地快速告警：%s 检测到【挥手呼救】，边缘端 <200ms 本地触发，未经云端。" % n["name"])

st.subheader("节点状态")
cols = st.columns(3)
for i, n in enumerate(nodes):
    with cols[i % 3]:
        st.markdown(
            '<div class="sg-card">'
            '<div class="sg-h">%s %s</div>'
            '<div class="sg-p">%s · %s场景</div>'
            '<div class="rowline"><span>当前人数</span><b>%d</b></div>'
            '<div class="rowline"><span>最近行为</span><b>%s</b></div>'
            '<div class="rowline"><span>推理延迟</span><b>%d ms</b></div>'
            '<div class="rowline"><span>隐私</span><b>已本地脱敏</b></div>'
            '</div>' % (n["name"], style.status_badge(n["status"]), n["id"], n["type"],
                        n["people"], n["behavior"], n["latency_ms"]),
            unsafe_allow_html=True)

st.subheader("主监测视图（模拟）")
labels = ["%s（%s）" % (n["name"], n["id"]) for n in nodes]
sel = st.selectbox("选择节点", labels)
node = nodes[labels.index(sel)]
view = (
    '<div style="position:relative;width:100%%;max-width:640px;height:340px;border-radius:12px;'
    'overflow:hidden;border:1px solid #E5E2DA;background:#2C2C2A">'
    '<div style="position:absolute;left:0;top:0;right:0;padding:8px 12px;color:#fff;font-size:12px;'
    'background:rgba(0,0,0,.35)">%s · 模拟画面（人脸已本地脱敏）</div>'
    '<div style="position:absolute;left:12%%;top:38%%;width:120px;height:150px;border:2px solid #97C459;'
    'border-radius:6px"><span style="position:absolute;top:-18px;left:0;color:#97C459;font-size:11px">person 0.94</span></div>'
    '<div style="position:absolute;left:52%%;top:52%%;width:110px;height:120px;border:2px solid #EF9F27;'
    'border-radius:6px"><span style="position:absolute;top:-18px;left:0;color:#EF9F27;font-size:11px">%s 0.88</span></div>'
    '<div style="position:absolute;left:78%%;top:60%%;width:70px;height:90px;border:2px solid #85B7EB;'
    'border-radius:6px"><span style="position:absolute;top:-18px;left:0;color:#85B7EB;font-size:11px">person 0.91</span></div>'
    '<div style="position:absolute;left:0;bottom:0;right:0;padding:8px 12px;color:#fff;font-size:12px;'
    'background:rgba(0,0,0,.35)">检测目标 %d · 主导行为 %s · 延迟 %d ms</div>'
    '</div>' % (node["name"], node["behavior"], max(2, node["people"] % 5), node["behavior"], node["latency_ms"])
)
st_html(view, height=360)
