# Paper & Model Source-Code Learning Skill — V3

通用论文/源码学习 Skill，新增**交互式网络架构网页生成**能力。适用于 Codex / VS Code 中的 Codex；团队可通过 Git 仓库共享同一版本。

## V3 新增内容

- 生成可本地打开的独立 HTML 架构探索器。
- 点击模块查看来源、输入输出、张量形状、具体计算步骤和上下游连接。
- 高亮数据流；区分数据流与训练/损失连接。
- 使用 JSON 保存网络配置，支持导入、导出和后续更新。
- 使用固定模块 ID，让整体架构、源码细节和变量追踪保持一致。
- 强制建立架构节点 → 源码位置 → 变量/张量 → 下游消费者的对应关系。
- 未核实的源码位置、形状和连接必须标记为待验证。
- 增加多模态学习参考指南和交互式网页测试。

## 目录

```text
paper-source-code-learning-skill-v3/
├── SKILL.md
├── README.md
├── agents/openai.yaml
├── domains/
│   ├── object-detection.md
│   ├── llm-transformer.md
│   ├── diffusion-models.md
│   ├── retrieval-rag.md
│   └── multimodal-learning.md
├── references/
│   ├── source-reading.md
│   ├── tensor-tracing.md
│   ├── training-inference.md
│   ├── paper-analysis.md
│   ├── experiment-analysis.md
│   ├── output-templates.md
│   └── model-config-schema.md
├── templates/paper_network_explorer.html
├── examples/
│   ├── model-config.example.json
│   └── paper_network_explorer-demo.html
├── evals/
│   ├── general-tests.md
│   ├── detection-tests.md
│   ├── llm-tests.md
│   └── interactive-architecture-tests.md
└── scripts/
    ├── validate_skill.py
    └── build_explorer.py
```

## 使用方式

### 1. 安装 Skill
将整个 Skill 目录安装到 Codex 能识别的 Skill 目录。确认 `SKILL.md` 直接位于 `paper-source-code-learning/` 下，不要多套一层目录。团队使用时，可把 Skill 放在团队仓库的 `.agents/skills/paper-source-code-learning/` 并提交 Git。

### 2. 在 Codex 中开始学习
在含有论文、源码和配置的工作区中调用 Skill，然后只需输入：

> 开始学习这篇论文。

Skill 会先识别当前论文/仓库，建立整体架构与源码映射，并在文件创建可用且材料足够时生成第一版交互式网页。后续深入模块后，可以要求它更新同一份 JSON/HTML；不必重新输入完整工作规范。

### 3. 生成网页的文件位置
建议输出到当前项目：

```text
artifacts/<paper-slug>/
├── paper_model_config.json
├── paper_network_explorer.html
└── architecture-evidence.md   # 可选
```

HTML 是独立文件，双击即可在现代浏览器中打开。JSON 是可编辑的结构数据，供后续更新和重新生成网页。

### 4. 手动构建网页
若 Codex 没有自动运行脚本，可在 Skill 包目录或适当路径执行：

```bash
python scripts/build_explorer.py \
  --config artifacts/<paper-slug>/paper_model_config.json \
  --output artifacts/<paper-slug>/paper_network_explorer.html
```

Windows PowerShell 也可以使用单行命令：

```powershell
python scripts/build_explorer.py --config artifacts\<paper-slug>\paper_model_config.json --output artifacts\<paper-slug>\paper_network_explorer.html
```

脚本仅使用 Python 标准库。它会检查模块 ID、坐标、上下游引用和连线端点，并将 JSON 嵌入 HTML。它不负责验证研究内容是否正确；内容真实性仍需对照论文和源码核实。

### 5. 验证
在 Skill 包目录运行：

```bash
python scripts/validate_skill.py
python scripts/build_explorer.py --config examples/model-config.example.json --output /tmp/paper-explorer-test.html
```

结构验证通过不等于已完成浏览器视觉测试。必要时在浏览器打开输出 HTML，测试模块点击、搜索、上下游导航和 JSON 导入导出。

## 更新 GitHub 仓库

将 V3 解压后**内部所有文件和目录**上传到现有仓库根目录，检查同名文件被更新、新增的 `templates/`、`examples/` 和 `domains/multimodal-learning.md` 已出现，然后提交。上传不会自动删除旧文件；确认新版本完整后再清理弃用文件。

## 维护原则

- 通用学习规则放在 `SKILL.md` 和 `references/`。
- 领域知识放在 `domains/`，按当前论文按需读取。
- 网页交互界面放在 `templates/`，模型专属节点与连线放在生成的 JSON。
- 不要把某篇论文的模块、形状或源码路径写成所有论文都通用的事实。
