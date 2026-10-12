# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from streamlit.components.v1 import html as st_html
import style

st.markdown(style.css(), unsafe_allow_html=True)
st.title("「银发守护」小程序 · 三端原型")
st.caption("老人端 / 家属端 / 管理者端界面原型（静态高保真示意，数据为模拟）")


def phone(inner):
    return ('<div class="phone"><div class="notch"></div>'
            '<div class="screen">%s</div></div>' % inner)


t1, t2, t3 = st.tabs(["老人端", "家属端", "管理者端"])

with t1:
    elder = phone(
        '<div style="text-align:center;font-size:15px;font-weight:600;color:#2C2C2A">下午好，王奶奶</div>'
        '<div class="sg-mini" style="text-align:center;margin-bottom:8px">中山公园 · 东门广场</div>'
        '<div class="sg-card" style="background:#E1F5EE;border-color:#9FE1CB;margin-bottom:8px">'
        '<div class="sg-h" style="color:#085041">当前状态：安全</div>'
        '<div class="sg-p">周边人流正常，无需担心</div></div>'
        '<div class="bigbtn red">一键求助 SOS</div>'
        '<div style="display:flex;gap:8px;margin-top:6px">'
        '<div class="sg-card" style="flex:1;text-align:center;margin:0"><div class="sg-h">语音交互</div><div class="sg-mini">说话即可</div></div>'
        '<div class="sg-card" style="flex:1;text-align:center;margin:0"><div class="sg-h">服务导航</div><div class="sg-mini">就近休息点</div></div>'
        '</div>'
        '<div class="sg-card" style="margin-top:8px"><div class="sg-h">今日提醒</div>'
        '<div class="sg-p">下午4点社区义诊，步行约300米</div></div>'
    )
    st_html(elder, height=560)

with t2:
    family = phone(
        '<div class="sg-card"><div class="sg-h">张爷爷 · 78岁</div>'
        '<div style="margin:6px 0"><span class="badge b-ok">状态：安全</span>'
        '<span class="badge b-gray">幸福里社区广场</span></div>'
        '<div class="rowline"><span>今日步数</span><b>3,240</b></div>'
        '<div class="rowline"><span>今日事件</span><b>1 次（已处置）</b></div></div>'
        '<div class="sg-card" style="border-left:4px solid #A32D2D">'
        '<div class="sg-h" style="color:#A32D2D">异常告警推送</div>'
        '<div class="sg-p">14:32 检测到【长时间静止】，已自动核验并通知您</div>'
        '<div class="bigbtn red" style="margin-top:8px">查看实时定位</div></div>'
        '<div class="sg-card"><div class="sg-h">健康周报</div>'
        '<div class="sg-p">本周活动规律，建议增加午间休息</div></div>'
    )
    st_html(family, height=560)

with t3:
    admin = phone(
        '<div style="display:flex;gap:8px">'
        '<div class="sg-kpi" style="flex:1;margin:0"><div class="v">18</div><div class="l">今日事件</div></div>'
        '<div class="sg-kpi" style="flex:1;margin:0"><div class="v">96%</div><div class="l">设备在线</div></div></div>'
        '<div class="sg-card" style="margin-top:8px"><div class="sg-h">待处置事件</div>'
        '<div class="rowline"><span>跌倒 · 运河公园南门</span><span class="badge b-err">新</span></div>'
        '<div class="rowline"><span>独自徘徊 · 颐年苑花园</span><span class="badge b-warn">处理中</span></div>'
        '<div class="rowline"><span>异常聚集 · 人民广场</span><span class="badge b-warn">处理中</span></div></div>'
        '<div class="sg-card"><div class="sg-h">设备管理</div>'
        '<div class="rowline"><span>感知终端</span><b>6 在线 / 0 离线</b></div>'
        '<div class="rowline"><span>边缘算力负载</span><b>正常</b></div></div>'
        '<div class="bigbtn">进入数据看板</div>'
    )
    st_html(admin, height=560)
