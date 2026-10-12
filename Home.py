# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from streamlit.components.v1 import html as st_html
import style
import sim_data

st.set_page_config(page_title="银发守护 · 概念演示原型", layout="wide")

ARCH_SVG = """
<svg viewBox="0 0 680 430" width="100%" style="max-width:860px;font-family:sans-serif">
  <defs>
    <marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>
  <text x="20" y="18" font-size="14" font-weight="600" fill="#2C2C2A">端–边–云–端 四层协同架构</text>
  <rect x="20" y="34" width="640" height="62" rx="12" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
  <text x="36" y="52" font-size="13" font-weight="600" fill="#085041">感知层（端）</text>
  <text x="150" y="52" font-size="12" fill="#0F6E56">公园 / 广场 / 步行街 · 多模态采集终端</text>
  <rect x="32" y="62" width="196" height="26" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
  <text x="130" y="79" font-size="12" fill="#04342C" text-anchor="middle">摄像头 / 麦克风阵列 / 环境传感器</text>
  <line x1="340" y1="96" x2="340" y2="120" stroke="#5F5E5A" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
  <rect x="20" y="122" width="640" height="72" rx="12" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
  <text x="36" y="140" font-size="13" font-weight="600" fill="#0C447C">边缘智能层（边）</text>
  <text x="150" y="140" font-size="12" fill="#185FA5">Jetson Nano / 树莓派 · 本地实时推理</text>
  <rect x="32" y="150" width="196" height="34" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
  <text x="130" y="171" font-size="12" fill="#042C53" text-anchor="middle">RT-DETR + CLIP 多模态融合</text>
  <rect x="242" y="150" width="196" height="34" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
  <text x="340" y="171" font-size="12" fill="#042C53" text-anchor="middle">跌倒 / 徘徊 / 聚集 识别 &lt;200ms</text>
  <rect x="452" y="150" width="196" height="34" rx="8" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
  <text x="550" y="171" font-size="12" fill="#FFFFFF" text-anchor="middle">SOS 本地快速告警</text>
  <line x1="340" y1="194" x2="340" y2="218" stroke="#5F5E5A" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
  <rect x="20" y="220" width="640" height="72" rx="12" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
  <text x="36" y="238" font-size="13" font-weight="600" fill="#085041">云端服务层（云）</text>
  <text x="150" y="238" font-size="12" fill="#0F6E56">语义理解 · 知识推理 · 服务生成</text>
  <rect x="32" y="248" width="196" height="34" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
  <text x="130" y="269" font-size="12" fill="#04342C" text-anchor="middle">适老化知识图谱</text>
  <rect x="242" y="248" width="196" height="34" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
  <text x="340" y="269" font-size="12" fill="#04342C" text-anchor="middle">LLM 推理（ChatGLM 微调）</text>
  <rect x="452" y="248" width="196" height="34" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
  <text x="550" y="269" font-size="12" fill="#04342C" text-anchor="middle">个性化服务建议 · 加密</text>
  <line x1="340" y1="292" x2="340" y2="316" stroke="#5F5E5A" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
  <rect x="20" y="318" width="640" height="62" rx="12" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
  <text x="36" y="336" font-size="13" font-weight="600" fill="#0C447C">用户交互层（端）</text>
  <text x="150" y="336" font-size="12" fill="#185FA5">「银发守护」小程序 · 三端协同</text>
  <rect x="32" y="346" width="196" height="26" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
  <text x="130" y="363" font-size="12" fill="#042C53" text-anchor="middle">老人端：语音 / 求助 / 导航</text>
  <rect x="242" y="346" width="196" height="26" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
  <text x="340" y="363" font-size="12" fill="#042C53" text-anchor="middle">家属端：查看 / 告警 / 周报</text>
  <rect x="452" y="346" width="196" height="26" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
  <text x="550" y="363" font-size="12" fill="#042C53" text-anchor="middle">管理者端：看板 / 调度</text>
  <text x="20" y="404" font-size="12" fill="#6B6A64">感知–理解–服务 闭环：边缘检出异常 → 云端生成个性化服务建议 → 小程序触达家属并联动处置</text>
</svg>
"""

st.markdown(style.css(), unsafe_allow_html=True)

st.markdown(
    '<div class="sg-card" style="border-left:4px solid #0F6E56">'
    '<div class="sg-h" style="font-size:19px">银发守护 · 城市公共空间适老化智能感知与服务系统</div>'
    '<div class="sg-p" style="margin-top:4px">基于多模态大模型的「感知—理解—服务」一体化解决方案</div>'
    '<div style="margin-top:8px">'
    '<span class="badge b-info">概念演示原型</span>'
    '<span class="badge b-gray">智慧生活与大健康赛道</span>'
    '<span class="badge b-gray">团队：晚晴智守</span>'
    '</div></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="sg-note">本页及后续页面所有节点状态、事件与图表均为 <b>模拟数据</b>，'
    '用于展示系统形态与闭环逻辑，不代表真实运行结果；技术指标为设计目标值，实测进展见「5 技术验证路线」。</div>',
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(style.kpi("2.97 亿", "60岁及以上老年人口（占总人口21.1%）"), unsafe_allow_html=True)
with c2:
    st.markdown(style.kpi("≈4000 万/年", "老年人发生跌倒，约50%在公共场所"), unsafe_allow_html=True)
with c3:
    st.markdown(style.kpi("1.2 万亿元", "2026年中国智慧养老市场规模（预测）"), unsafe_allow_html=True)

st.markdown("#### 系统闭环：感知 → 理解 → 服务")
st.markdown(
    '<div class="sg-flow">'
    '<div class="step"><div class="t">① 感知</div><div class="d">多模态终端实时采集视觉、语音与环境状态，边缘端本地完成跌倒/徘徊/聚集识别。</div></div>'
    '<div class="step"><div class="t">② 理解</div><div class="d">异常事件转为结构化特征，云端 LLM 结合适老化知识图谱进行语义理解与推理。</div></div>'
    '<div class="step"><div class="t">③ 服务</div><div class="d">生成个性化服务建议，经小程序触达家属并联动社区处置，形成主动服务闭环。</div></div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("#### 四层架构")
st_html(ARCH_SVG, height=470)

st.markdown("#### 核心指标（设计目标值）")
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(style.kpi("mAP ≥ 90%", "异常行为检测精度（目标）"), unsafe_allow_html=True)
with m2:
    st.markdown(style.kpi("< 200 ms", "边缘推理响应延迟（目标）"), unsafe_allow_html=True)
with m3:
    st.markdown(style.kpi("12 类", "支持的异常行为识别"), unsafe_allow_html=True)
with m4:
    st.markdown(style.kpi("≈2500 元", "单节点硬件成本"), unsafe_allow_html=True)

st.markdown(
    '<div class="sg-card"><div class="sg-h">商业模式：B2G2C</div>'
    '<div class="sg-p">政府端 SaaS 年费 5000 元/节点（约60%收入）· 家属端增值服务 99 元/年（约25%）· '
    '机构端设备+年费（约10%）· 数据增值报告（约5%，中长期）。</div></div>',
    unsafe_allow_html=True,
)

st.markdown("#### 页面导航")
st.markdown(
    '- **实时监测看板**：多节点运行状态与模拟主监测视图\n'
    '- **事件与处置**：异常事件时间线与云端服务建议\n'
    '- **小程序三端**：老人端 / 家属端 / 管理者端界面原型\n'
    '- **管理者看板**：适老化指数与统计分析\n'
    '- **技术验证路线**：关键技术对照与无硬件替代方案',
)
