# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
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

# ---------------- Hero 首屏 ----------------
st.markdown(
    '<div class="sg-hero">'
    '<div class="eyebrow">SMART CITY · 智慧生活与大健康赛道</div>'
    '<div class="t">银发守护 · 城市公共空间适老化智能感知与服务系统</div>'
    '<div class="s">基于多模态大模型的「感知 — 理解 — 服务」一体化解决方案：'
    '在公园、广场、步行街等公共空间部署多模态感知终端，边缘端本地完成跌倒 / 徘徊 / 聚集等异常行为识别，'
    '云端结合适老化知识图谱生成个性化服务建议，经「银发守护」小程序触达家属并联动社区处置。</div>'
    '<div class="tags">'
    '<span class="badge b-primary">概念演示原型</span>'
    '<span class="badge b-info">多模态大模型</span>'
    '<span class="badge b-info">端边云协同</span>'
    '<span class="badge b-gray">团队：晚晴智守</span>'
    '</div>'
    '<div class="meta"><span>第十二届中国研究生智慧城市技术与创意设计大赛</span>'
    '<span>队长：刘宇博</span><span>队员：尚金凌 · 张烨</span></div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown(style.note(
    '本原型所有节点状态、事件与图表均为 <b>模拟数据</b>，用于展示系统形态与闭环逻辑，'
    '不代表真实运行结果；技术指标为设计目标值，预估依据见「6 指标预估依据」。'),
    unsafe_allow_html=True)

# ---------------- 社会价值 ----------------
st.markdown(style.section("为什么做这件事", "社会价值与市场空间"), unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(style.kpi("2.97 亿", "60岁及以上老年人口", "占总人口 21.1%，已进入中度老龄化社会"), unsafe_allow_html=True)
with c2:
    st.markdown(style.kpi("≈4000 万/年", "老年人发生跌倒", "约 50% 发生在公共场所，救治不及时后果严重"), unsafe_allow_html=True)
with c3:
    st.markdown(style.kpi("1.2 万亿元", "2026年智慧养老市场规模", "预测值，公共空间适老化是增量蓝海"), unsafe_allow_html=True)

# ---------------- 系统闭环 ----------------
st.markdown(style.section("系统闭环", "感知 → 理解 → 服务"), unsafe_allow_html=True)
st.markdown(
    '<div class="sg-flow">'
    '<div class="step"><div class="n">1</div><div class="t">感知</div>'
    '<div class="d">多模态终端实时采集视觉、语音与环境状态，边缘端本地完成跌倒 / 徘徊 / 聚集识别，原始画面不出域。</div></div>'
    '<div class="step"><div class="n">2</div><div class="t">理解</div>'
    '<div class="d">异常事件转为结构化特征，云端 LLM 结合适老化知识图谱进行语义理解与风险推理。</div></div>'
    '<div class="step"><div class="n">3</div><div class="t">服务</div>'
    '<div class="d">生成个性化服务建议，经小程序触达家属并联动社区处置，形成主动服务闭环。</div></div>'
    '</div>',
    unsafe_allow_html=True,
)

# ---------------- 四层架构 ----------------
st.markdown(style.section("总体架构", "端 – 边 – 云 – 端 四层协同"), unsafe_allow_html=True)
st.iframe(ARCH_SVG, height=470)

# ---------------- 核心指标 ----------------
st.markdown(style.section("核心指标", "设计目标值 · 预估依据见「6 指标预估依据」"), unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(style.kpi("mAP ≥ 90%", "异常行为检测精度", "目标值，非实测"), unsafe_allow_html=True)
with m2:
    st.markdown(style.kpi("< 200 ms", "边缘推理响应延迟", "目标值，非实测"), unsafe_allow_html=True)
with m3:
    st.markdown(style.kpi("12 类", "支持的异常行为识别", "封闭类别集 + 零样本兜底"), unsafe_allow_html=True)
with m4:
    st.markdown(style.kpi("≈ 2500 元", "单节点硬件成本", "Jetson Nano 级方案"), unsafe_allow_html=True)

# ---------------- 商业模式 ----------------
st.markdown(style.section("商业模式", "B2G2C · 收入结构预估"), unsafe_allow_html=True)
st.markdown(
    '<div class="sg-card">'
    '<div class="sg-p">以政府端 SaaS 订阅为基本盘，家属端增值服务提升粘性，机构端与数据增值服务拓展中长期空间。</div>'
    '<div class="sg-barrow">'
    '<div class="item"><div class="lab"><span>政府端 SaaS 年费（5000 元/节点）</span><b>约 60%</b></div>'
    '<div class="sg-bar"><i style="width:60%"></i></div></div>'
    '<div class="item"><div class="lab"><span>家属端增值服务（99 元/年）</span><b>约 25%</b></div>'
    '<div class="sg-bar"><i style="width:25%"></i></div></div>'
    '<div class="item"><div class="lab"><span>机构端设备 + 年费</span><b>约 10%</b></div>'
    '<div class="sg-bar"><i style="width:10%"></i></div></div>'
    '<div class="item"><div class="lab"><span>数据增值报告（中长期）</span><b>约 5%</b></div>'
    '<div class="sg-bar"><i style="width:5%"></i></div></div>'
    '</div></div>',
    unsafe_allow_html=True,
)

# ---------------- 页面导航 ----------------
st.markdown(style.section("演示导航", "左侧边栏可切换，建议按序演示"), unsafe_allow_html=True)
nav = [
    ("📹", "实时监测看板", "多节点运行状态 + 模拟主监测视图（检测框 / 扫描线 / SOS 告警）"),
    ("🚨", "事件与处置", "异常事件列表、感知—理解—服务时间线、云端服务建议与处置流转"),
    ("📱", "小程序三端", "老人端 / 家属端 / 管理者端高保真界面原型，可切换查看"),
    ("📊", "管理者看板", "适老化指数、事件趋势、类型分布与响应时长统计"),
    ("🧭", "技术验证路线", "关键技术设计目标 vs 当前状态、无硬件替代方案、12 个月路线"),
    ("📐", "指标预估依据", "四项核心指标的预估推导链条与公开基准来源"),
]
rows = [nav[0:3], nav[3:6]]
for row in rows:
    cols = st.columns(3)
    for col, (ico, t, d) in zip(cols, row):
        with col:
            st.markdown(
                f'<div class="sg-navcard"><div class="ico">{ico}</div>'
                f'<div class="t">{t}</div><div class="d">{d}</div></div>',
                unsafe_allow_html=True,
            )

st.markdown(style.footer(), unsafe_allow_html=True)
