# Paper & Model Source-Code Learning Skill — V2

面向团队复用的通用 Codex Skill：阅读不同领域论文、核实源码、追踪数据流、理解训练/推理与实验，并评估任务迁移。

## V2 改进

- 通用核心不预设任何一种模型架构。
- 每次研究新项目都重新识别论文、仓库、版本和配置，防止沿用旧项目假设。
- 目标检测、LLM/Transformer、扩散模型、检索/RAG 分开维护并按需参考。
- 增加通用论文/实验分析和跨领域测试。
- 新增分析模态编码器、跨模态融合、动态路由、模态权重、蒸馏与联合训练。
  
## 目录

```text
paper-source-code-learning-skill-v2/
├── SKILL.md
├── README.md
├── agents/openai.yaml
├── references/
│   ├── source-reading.md
│   ├── tensor-tracing.md
│   ├── training-inference.md
│   ├── paper-analysis.md
│   ├── experiment-analysis.md
│   └── output-templates.md
├── domains/
│   ├── object-detection.md
│   ├── llm-transformer.md
│   ├── diffusion-models.md
│   └── retrieval-rag.md
├── evals/
│   ├── general-tests.md
│   ├── detection-tests.md
│   └── llm-tests.md
└── scripts/validate_skill.py
```

## 安装到 Codex 项目

推荐团队共享路径：`your-repo/.agents/skills/paper-source-code-learning/`。把本目录内容复制到该位置并提交 Git。确保最终路径是 `.agents/skills/paper-source-code-learning/SKILL.md`，不要额外嵌套 V2 文件夹。

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force ".agents\skills" | Out-Null
Copy-Item -Recurse -Force `
  "$HOME\Downloads\paper-source-code-learning-skill-v2\*" `
  ".agents\skills\paper-source-code-learning"
```

### macOS / Linux

```bash
mkdir -p .agents/skills/paper-source-code-learning
cp -R ~/Downloads/paper-source-code-learning-skill-v2/. \
  .agents/skills/paper-source-code-learning/
```

按当前 Codex 客户端的 Skill 发现机制，在工作区重新加载/重启 Codex，并通过 `$` 技能选择器或明确名称调用。

## 更新现有 GitHub 仓库（网页操作）

你现有的仓库是 `paper-source-code-learning-skill`，根目录已有旧版文件。

1. 下载并解压 V2 ZIP。
2. 打开现有仓库 `Add file` → `Upload files`。
3. 进入解压后的 `paper-source-code-learning-skill-v2` 文件夹，选中里面的**全部内容**，上传到仓库根目录；不要把外层 V2 文件夹套进去。
4. 检查 GitHub 是否将同名文件作为更新处理。若提示冲突或不允许覆盖，逐个打开旧文件，使用铅笔图标编辑替换，或改用 GitHub Desktop / Git 更新。
5. 确认新增 `domains/` 和三个 `evals/` 文件出现在提交列表中。
6. 提交说明填写 `Upgrade to domain-neutral paper learning Skill V2`，点击 `Commit changes`。
7. 检查仓库首页：`SKILL.md` 已更新，`domains/` 已出现，`evals/` 下有三个新测试文件。

**注意：** 上传新文件不会自动删除仓库里不再使用的旧文件。若旧的 `evals/test-cases.md` 仍存在，确认新测试文件已提交后，再手动删除旧文件；不要在新版本未确认完整前删除。

## 验证

在本目录运行 `python scripts/validate_skill.py`。它只检查文件结构、元数据和引用，不会验证 Codex 的实际行为。

按 `evals/` 中的提示词测试：通用测试用于所有项目；检测和 LLM 测试只在相应领域运行。建议用一篇检测论文和一篇 LLM 论文分别验收。

## 维护原则

通用规则放在 `SKILL.md` 和 `references/`；领域专属知识放在 `domains/`；领域案例放在对应 `evals/`。新增领域时，先添加领域参考和测试，再在主 Skill 的按需选择列表中登记。
