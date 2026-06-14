# Dynamicycle Docs

BetterDocs 文档同步仓库，管理与 dynamicycle.com/docs/ 的文档内容。

## Codex 连续执行

任何 Codex 或自动化代理开始工作前，应先读取：

1. `AGENTS.md`：项目强制规则
2. `PROJECT_STATE.md`：最近一次执行结果与下一步
3. `PROJECT_HISTORY.md`：追加式执行历史

每次完成任务后，更新状态和历史并推送当前工作分支，以便切换账号或
设备后继续执行。

## 目录结构

```
batterDocs/          # 按分类组织的 markdown 文档
sync/                # Python 同步工具
klaviyo/             # Klaviyo 源文档缓存（待开发）
```

## 同步命令

```bash
# 安装依赖
pip3 install -r sync/requirements.txt

# 从 BetterDocs 拉取到本地
python3 sync/sync.py pull

# 查看本地与远程差异
python3 sync/sync.py status

# 推送本地修改到 BetterDocs
python3 sync/sync.py push
```

## 认证

在 `.env` 文件中配置 WordPress Application Password：

```
WP_SITE_URL=https://dynamicycle.com
WP_USERNAME=<username>
WP_APP_PASSWORD=<password>
```
