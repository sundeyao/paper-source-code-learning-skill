# Paper & Model Source-Code Learning Skill

面向团队协作的 Codex Skill：逐步阅读深度学习论文、追踪真实源码、解释张量数据流、区分训练与推理，并评估模型迁移方案。

## 目录

```text
paper-source-code-learning/
├── SKILL.md
├── README.md
├── agents/openai.yaml
├── references/
│   ├── source-reading.md
│   ├── tensor-tracing.md
│   ├── training-inference.md
│   ├── model-adaptation.md
│   └── output-templates.md
├── evals/test-cases.md
└── scripts/validate_skill.py
```

## 推荐：团队级安装

把整个目录复制到团队仓库根目录的 `.agents/skills/paper-source-code-learning/`，并提交到 Git。成员拉取仓库后，在该工作区打开 Codex 即可共享同一套规则。

### Windows PowerShell

在项目根目录执行，假设 ZIP 已解压到 `$HOME\Downloads\paper-source-code-learning`：

```powershell
New-Item -ItemType Directory -Force ".agents\skills" | Out-Null
Copy-Item -Recurse -Force "$HOME\Downloads\paper-source-code-learning" ".agents\skills\paper-source-code-learning"
```

### macOS / Linux

```bash
mkdir -p .agents/skills
cp -R ~/Downloads/paper-source-code-learning .agents/skills/paper-source-code-learning
```

确保最终路径为 `.agents/skills/paper-source-code-learning/SKILL.md`，不要多套一层同名目录。

## 个人级安装（可选）

- macOS / Linux：`~/.agents/skills/paper-source-code-learning/`
- Windows：`%USERPROFILE%\.agents\skills\paper-source-code-learning\`

团队共享仍建议使用项目级 `.agents/skills/` 并提交到版本控制。

## 在 Codex / VS Code 中使用

1. 打开包含 `.agents/skills/` 的项目根目录。
2. 在 Codex 输入框使用 `$` 技能选择/提及功能，选择 `paper-source-code-learning`；也可以明确要求使用该 Skill。
3. 如果技能列表没有更新，重启 Codex 或重新打开工作区。
4. 提供论文、源码仓库、关键文件或配置。Skill 不会自动获得不可访问的源码。

推荐启动提示：

> 使用 `$paper-source-code-learning`。先检查当前仓库和配置，告诉我模型整体执行流程、入口函数、主要模块及关键张量；先不要展开每个模块的内部细节。所有实现结论都要根据当前源码核验。

## 验证

### 静态检查

在 Skill 根目录运行：

```bash
python scripts/validate_skill.py
```

成功时应显示 `PASS`。

### 行为测试

按 `evals/test-cases.md` 在 Codex 中执行测试。检查是否：
- 先检查当前仓库和配置；
- 给出真实文件路径与函数名；
- 解释张量维度与实际运算；
- 区分训练匹配与推理后处理；
- 不编造未确认的实现。

团队建议至少两位成员在不同工作区测试同一组用例。把 Skill 与测试用例一起做代码评审。

## 原则

真实源码优先；按需读取辅助资料；不混用框架/版本；不确定时明确说明。
