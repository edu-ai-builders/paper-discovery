# skill-paper-discovery

**A paper discovery skill for the edu-ai-builders ecosystem.**

> Not a search engine. A translator — from your question to the papers worth reading.

[中文版本](#中文介绍) · [English](#english-introduction)

---

## 中文介绍

### 这个 skill 是做什么的

`skill-paper-discovery` 不是论文搜索引擎的替代品。

它解决的是一个更根本的问题：**大多数人不是不会搜论文，而是还没把自己的问题翻译成"论文世界里的问题"。**

这个 skill 帮助老师、研究者、EdTech builder、产品设计者，从一个模糊的兴趣、具体的教学困惑或产品想法出发，找到现在最值得读的那几篇论文。

```
你的问题 → 研究问题 → 关键词 → 值得读的论文 → 阅读路径
```

### 核心能力

- **需求澄清**：在推荐论文之前，先识别用户的意图（入门探索 / 解决问题 / 教学设计 / 产品开发 / 研究验证 / 论文延伸）
- **问题翻译**：把用户的自然语言翻译成可检索的研究问题和关键词组合
- **精准推荐**：每次最多推荐 3 篇，每篇都必须说明"为什么是这篇而不是别篇"
- **阅读路径**：不是论文清单，而是有顺序和理由的阅读路线
- **搜索入口**：自动生成 Google Scholar 可点击链接
- **PDF 获取**：通过 Semantic Scholar API 和 arXiv 搜索并下载开放获取论文

### 三种模式

| 模式 | 适合场景 | 输出 |
|------|---------|------|
| **Guided**（默认） | 大多数用户 | 完整三阶段：需求澄清 → 关键词翻译卡 → 论文推荐卡（含阅读路径） |
| **Quick** | 时间有限，已有方向 | 直接给 1-3 篇推荐，每篇一句理由 |
| **Builder** | 做产品 / 工具的人 | 在标准输出基础上额外给出产品启发、可复用交互模式 |

### 文件结构

```
skill-paper-discovery/
├── SKILL.md                              # 主逻辑：三阶段工作流 + 指令系统
├── references/
│   ├── intent_types.md                   # 六种用户意图 + 识别规则
│   ├── paper_type_lens.md                # 六种论文类型 + 对应阅读视角
│   ├── query_translation_patterns.md     # 用户语言 → 关键词翻译模式库
│   ├── venues_and_sources.md             # 会议/期刊/平台速查 + Google Scholar 指南
│   └── recommendation_rubric.md         # 五维推荐评分框架
├── scripts/
│   ├── search_semantic_scholar.py        # Semantic Scholar API 搜索（官方免费）
│   ├── search_arxiv.py                   # arXiv 搜索 + 免费 PDF 直链
│   └── fetch_pdf.py                      # 单个 / 批量 PDF 下载
└── assets/
    └── paper-discovery-canvas.html       # AI-powered 可视化前端
```

### Paper Discovery Canvas（可视化界面）

`assets/paper-discovery-canvas.html` 是这个 skill 的前端界面，支持三种使用方式：

**① claude.ai Artifact（推荐展示用）**
在 claude.ai 里作为 Artifact 运行，平台自动处理认证，无需任何配置。

**② 本地文件**
用浏览器直接打开，填入 Anthropic API Key 即可使用。
Key 仅存在浏览器内存，不会上传。获取：[console.anthropic.com](https://console.anthropic.com)

**③ 配合 Claude Code**
加载本 skill，Claude Code 执行完整工作流，scripts/ 负责搜索和下载 PDF。

### 快捷指令

| 指令 | 行为 |
|------|------|
| `/quick` | 切换到快速推荐模式 |
| `/builder` | 切换到产品视角模式 |
| `/map` | 只输出关键词和搜索地图 |
| `/more` | 同方向再补充 3 篇 |
| `/adjacent` | 推荐相邻研究方向 |
| `/compare` | 对比当前推荐的几篇 |
| `/sense [n]` | 将第 n 篇传入深度意义建构 |

### 生态位置

```
skill-paper-discovery        ← 你在这里：找到值得读的论文
        ↓
skill-paper-sensemaking      ← 深度理解一篇论文
        ↓
skill-visual-knowledge-design ← 把认知结构可视化
        ↓
skill-paper-to-prd           ← 把研究转化为产品设计
```

### 依赖安装

```bash
pip install arxiv          # search_arxiv.py 需要
# search_semantic_scholar.py 和 fetch_pdf.py 只用 Python 标准库
```

### 适合谁用

- 教师：想用学习科学研究改进教学设计
- 研究者 / 研究生：需要快速锁定值得精读的文献
- EdTech builder：想把学术研究转化为产品功能
- 教育产品设计者：需要研究依据支撑设计决策

---

## English Introduction

### What this skill does

`skill-paper-discovery` is not a paper search engine.

It solves a more fundamental problem: **most people don't fail to find papers because they can't search — they fail because they haven't yet translated their question into the language of academic research.**

This skill helps teachers, researchers, EdTech builders, and product designers go from a vague interest, a specific teaching challenge, or a product idea, to the specific papers most worth reading right now.

```
Your question → Research question → Keywords → Papers worth reading → Reading path
```

### Core capabilities

- **Intent clarification**: Before recommending anything, identifies what the user actually needs (exploration / problem-solving / instructional design / product development / hypothesis validation / extending a known paper)
- **Query translation**: Converts natural language into searchable research questions and keyword combinations
- **Focused recommendations**: Maximum 3 papers per session, each with an explicit "why this one and not others" rationale
- **Reading paths**: Not a list, but an ordered sequence with reasons — read A to build context, B for design patterns, C for evidence or edge cases
- **Search links**: Auto-generates clickable Google Scholar URLs for each keyword combination
- **PDF retrieval**: Searches Semantic Scholar API and arXiv, downloads open-access PDFs

### Three modes

| Mode | Best for | Output |
|------|----------|--------|
| **Guided** (default) | Most users | Full 3-phase flow: intent clarification → keyword translation card → paper recommendation card with reading path |
| **Quick** | Time-constrained, already have direction | 1-3 direct recommendations, one-line rationale each |
| **Builder** | Product / tool builders | Standard output + product implications, reusable interaction patterns |

### File structure

```
skill-paper-discovery/
├── SKILL.md                              # Main logic: 3-phase workflow + command system
├── references/
│   ├── intent_types.md                   # 6 user intent types + detection rules
│   ├── paper_type_lens.md                # 6 paper types + reading lens for each
│   ├── query_translation_patterns.md     # Natural language → keyword translation patterns
│   ├── venues_and_sources.md             # Conferences/journals/platforms + Google Scholar guide
│   └── recommendation_rubric.md         # 5-dimension recommendation scoring framework
├── scripts/
│   ├── search_semantic_scholar.py        # Semantic Scholar API search (free, official)
│   ├── search_arxiv.py                   # arXiv search + direct PDF links
│   └── fetch_pdf.py                      # Single / batch PDF downloader
└── assets/
    └── paper-discovery-canvas.html       # AI-powered visual frontend
```

### Paper Discovery Canvas

`assets/paper-discovery-canvas.html` is the visual interface for this skill. Three ways to use it:

**① claude.ai Artifact (recommended for demos)**
Run as an Artifact in claude.ai. Platform handles auth automatically — no configuration needed.

**② Local file**
Open directly in any browser. Enter your Anthropic API Key to activate.
Key is stored only in browser memory and never transmitted anywhere.
Get a key: [console.anthropic.com](https://console.anthropic.com)

**③ With Claude Code**
Load the skill in Claude Code for the full workflow. Scripts handle search and PDF download.

### Commands

| Command | Action |
|---------|--------|
| `/quick` | Switch to quick recommendation mode |
| `/builder` | Switch to product-focused mode |
| `/map` | Output only keyword map and search links |
| `/more` | 3 more papers in the same direction |
| `/adjacent` | Papers in neighboring research areas |
| `/compare` | Comparative analysis of current recommendations |
| `/sense [n]` | Pass paper n to deep sensemaking |

### Ecosystem

```
skill-paper-discovery        ← you are here: find papers worth reading
        ↓
skill-paper-sensemaking      ← deeply understand a single paper
        ↓
skill-visual-knowledge-design ← visualize cognitive structure
        ↓
skill-paper-to-prd           ← translate research into product design
```

### Installation

```bash
pip install arxiv          # required for search_arxiv.py
# search_semantic_scholar.py and fetch_pdf.py use Python standard library only
```

### Who this is for

- **Teachers** who want to ground instructional design in learning science research
- **Researchers / graduate students** who need to quickly identify what's worth reading carefully
- **EdTech builders** who want to translate academic findings into product features
- **Education product designers** who need research backing for design decisions

---

*Part of the [edu-ai-builders](https://github.com/edu-ai-builders) open-source AI education OS.*
*作者：爱思考的伊伊子 · 播客：教育AI智造者*
