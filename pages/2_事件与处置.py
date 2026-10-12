# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import pandas as pd
import style, sim_data

st.markdown(style.css(), unsafe_allow_html=True)
st.title("异常事件与处置")
st.caption("异常事件列表 · 感知-理解-服务时间线 · 云端服务建议（数据为模拟）")

if "events" not in st.session_state:
    st.session_state.events = sim_data.gen_events()
events = st.session_state.events

df = pd.DataFrame(events)[["event_id", "type", "node", "date", "time", "confidence", "status"]]
st.subheader("事件列表")
st.dataframe(
    df, use_container_width=True, hide_index=True,
    column_config={"confidence": st.column_config.ProgressColumn("置信度", format="%.2f", min_value=0, max_value=1)},
)

ids = [e["event_id"] for e in events]
sel = st.selectbox("选择事件查看详情", ids)
ev = next(e for e in events if e["event_id"] == sel)

st.markdown(
    '<div class="sg-card"><div class="sg-h" style="font-size:16px">事件详情 · %s %s</div>'
    '<div style="margin-top:6px">'
    '<span class="badge b-info">%s</span>'
    '<span class="badge b-gray">%s</span>'
    '<span class="badge b-gray">%s %s</span>'
    '<span class="badge b-gray">置信度 %s</span>'
    '</div></div>' % (ev["event_id"], style.status_badge(ev["status"]), ev["type"],
                      ev["node"], ev["date"], ev["time"], ev["confidence"]),
    unsafe_allow_html=True)

st.subheader("处置时间线（感知—理解—服务）")
tl = [
    ("T0 边缘检出", "<200ms 本地推理识别异常，触发本地告警"),
    ("T1 本地脱敏", "人脸模糊化，仅上传行为特征向量"),
    ("T2 云端理解", "LLM 结合知识图谱进行语义理解与推理（约1.5s，模拟）"),
    ("T3 生成建议", "输出结构化个性化服务建议"),
    ("T4 触达联动", "通知家属 / 派单社区 / 联动处置"),
    ("T5 处置完结", "记录归档，纳入适老化指数统计"),
]
for t, d in tl:
    st.markdown('<div class="rowline"><span><b>%s</b></span><span class="sg-mini">%s</span></div>' % (t, d),
                unsafe_allow_html=True)

st.subheader("云端服务建议（模拟 LLM 输出）")
sug = sim_data.suggestion_for(ev["type"])
cols = st.columns(2)
for i, (k, v) in enumerate(sug):
    with cols[i % 2]:
        st.markdown('<div class="sg-card"><div class="sg-h">%s</div><div class="sg-p">%s</div></div>' % (k, v),
                    unsafe_allow_html=True)

st.markdown('<div class="sg-note">该事件已本地人脸脱敏，云端仅保存行为特征向量；数据采用 AES-256 加密存储。</div>',
            unsafe_allow_html=True)

st.subheader("处置操作（模拟）")
b1, b2, b3 = st.columns(3)


def set_status(s):
    for e in st.session_state.events:
        if e["event_id"] == sel:
            e["status"] = s
    st.rerun()


with b1:
    if st.button("通知家属", use_container_width=True):
        st.toast("已通知家属（模拟）")
with b2:
    if st.button("派单社区", use_container_width=True):
        st.toast("已派单至社区（模拟）")
with b3:
    if st.button("标记已完结", use_container_width=True):
        set_status("已完结")
