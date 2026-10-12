# 部署指南：GitHub + Streamlit Cloud

本目录已初始化为独立 Git 仓库并完成首次提交。按下面步骤即可上线。

## 1. 在 GitHub 创建仓库

1. 登录 GitHub → 右上角 **+** → **New repository**；
2. Repository name 建议 `silver-guard-demo`；
3. 可见性：**Private**（含商业计划数据，推荐）或 **Public**（便于分享演示链接）；
4. **不要**勾选 "Add a README / license / gitignore"（保持空仓库，避免推送冲突）；
5. 点击 **Create repository**。

## 2. 关联远程并推送（PowerShell，在本目录执行）

```powershell
git remote add origin https://github.com/Lyubo7117/silver-guard-demo.git
git branch -M main
git push -u origin main
```

> - 推送时会弹出 GitHub 登录/授权，按提示完成。
> - GitHub 已不支持账号密码推送，若认证失败，请使用 **Personal Access Token（PAT）** 作为密码，
>   或改用 SSH：`git@github.com:Lyubo7117/silver-guard-demo.git`。
> - 若你的 GitHub 用户名不是 `Lyubo7117`，请把上面 URL 中的用户名替换成你自己的。

## 3. 在 Streamlit Cloud 部署

1. 访问 https://share.streamlit.io ，用 GitHub 账号登录并授权；
2. 点 **New app**；
3. 配置：
   - Repository：`Lyubo7117/silver-guard-demo`
   - Branch：`main`
   - Main file path：`Home.py`
4. （可选）Advanced settings 选择 Python 版本（不选则用默认，兼容本项目）；
5. 点 **Deploy**，等待 1–3 分钟构建完成，得到 `https://xxxx.streamlit.app` 链接。

## 4. 日常更新

改动代码后：

```powershell
git add -A
git commit -m "update: 说明你的改动"
git push
```

Streamlit Cloud 检测到推送会自动重新部署。

## 常见问题

- **部署后 ModuleNotFoundError**：确认 `requirements.txt` 已随仓库提交、入口为 `Home.py`。
- **push 认证失败**：使用 PAT（GitHub → Settings → Developer settings → Personal access tokens）或配置 SSH。
- **私有仓库部署**：Streamlit Cloud 需在授权时允许访问该私有仓库。
- **主题调整**：编辑 `.streamlit/config.toml`。
