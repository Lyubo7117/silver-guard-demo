# -*- coding: utf-8 -*-
"""银发守护 · 概念演示原型 —— 共享样式与小组件"""

BASE_CSS = """
<style>
.sg-card{border:1px solid #E5E2DA;border-radius:12px;padding:14px 16px;background:#FFFFFF;margin-bottom:12px}
.sg-kpi{border:1px solid #E5E2DA;border-radius:12px;padding:12px 14px;background:#F7F6F2;margin-bottom:10px}
.sg-kpi .v{font-size:22px;font-weight:600;color:#0F6E56;line-height:1.2}
.sg-kpi .l{font-size:12px;color:#6B6A64;margin-top:2px}
.badge{display:inline-block;padding:2px 10px;border-radius:999px;font-size:12px;font-weight:500;margin-right:6px}
.b-ok{background:#E1F5EE;color:#085041}
.b-warn{background:#FAEEDA;color:#854F0B}
.b-err{background:#FCEBEB;color:#A32D2D}
.b-info{background:#E6F1FB;color:#0C447C}
.b-gray{background:#F1EFE8;color:#5F5E5A}
.sg-h{font-size:15px;font-weight:600;color:#2C2C2A;margin:0 0 2px}
.sg-p{font-size:12.5px;color:#5F5E5A;margin:0 0 4px}
.sg-note{font-size:12px;color:#854F0B;background:#FAEEDA;border-radius:8px;padding:8px 12px;margin:8px 0}
.sg-flow{display:flex;gap:10px;align-items:stretch}
.sg-flow .step{flex:1;border:1px solid #E5E2DA;border-radius:12px;padding:12px;background:#F7F6F2}
.sg-flow .step .t{font-size:13px;font-weight:600;color:#0F6E56}
.sg-flow .step .d{font-size:12px;color:#5F5E5A;margin-top:4px}
.phone{width:284px;border:1px solid #D9D6CD;border-radius:28px;background:#F4F2EC;padding:14px 12px;margin:0 auto}
.phone .notch{width:84px;height:6px;border-radius:6px;background:#D9D6CD;margin:0 auto 10px}
.phone .screen{background:#FFFFFF;border:1px solid #ECE9E1;border-radius:18px;padding:14px;min-height:470px}
.bigbtn{display:block;text-align:center;background:#0F6E56;color:#fff;border-radius:14px;padding:15px;font-size:16px;font-weight:600;margin:10px 0}
.bigbtn.red{background:#A32D2D}
.rowline{display:flex;justify-content:space-between;font-size:12.5px;color:#2C2C2A;padding:7px 0;border-bottom:1px solid #F0EEE7}
.rowline:last-child{border-bottom:none}
.sg-mini{font-size:12px;color:#6B6A64}
</style>
"""


def css():
    return BASE_CSS


def status_badge(s):
    m = {"在线": "b-ok", "注意": "b-warn", "告警": "b-err",
         "新告警": "b-err", "处理中": "b-warn", "已完结": "b-ok"}
    return '<span class="badge %s">%s</span>' % (m.get(s, "b-gray"), s)


def kpi(value, label):
    return '<div class="sg-kpi"><div class="v">%s</div><div class="l">%s</div></div>' % (value, label)
