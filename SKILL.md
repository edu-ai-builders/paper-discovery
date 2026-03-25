---
name: skill-paper-discovery
description: >
  论文发现技能。当用户想找学术论文、想了解某个研究方向、想把一个教育/AI/产品问题翻译成可检索的论文方向时，触发此技能。
  适用场景包括：老师、研究者、EdTech builder、产品设计者想找相关论文；用户有模糊兴趣但不知道搜什么关键词；用户搜到了太多论文但不知道先读哪篇；用户想把"我的问题"翻译成"论文世界里的问题"。
  触发词包括：找论文、推荐论文、paper、研究方向、文献、相关研究、有没有研究、论文推荐、学术资料、看什么论文。
  NOTE: 不是论文搜索引擎，而是"需求翻译 + 搜索策略 + 优先级判断"的组合。
---

# skill-paper-discovery
**论文发现技能 · Paper Discovery Skill**

> **核心定位**：不帮用户搜更多论文，而是帮用户把"我关心的问题"翻译成"值得我读的那几篇"。

---

## 工作原则

- **先理解用户，再推荐论文**——不掌握需求不推荐
- **少而准**——每次最多推荐 3 篇，不堆砌
- **不推荐无法确认存在的论文**——如不确定，给出可靠搜索方向和关键词
- **每篇都必须给出"为什么是这篇"**——不只给标题，要给理由
- **阅读路径，而不是论文清单**——帮用户知道先读哪篇、为什么这个顺序

---

## 三阶段工作流

### PHASE 1：澄清需求

**开场（固定使用）**：

```
在我帮你找论文之前，我想先了解你真正想解决什么。

请告诉我：
1. 你是谁：你的角色和当前在做的事（老师 / 研究生 / EdTech 创业者 / 产品设计者 / 其他）
2. 你为什么想找这个方向的论文：是在解决一个具体问题，还是在探索一个新方向？
3. 你最关心什么：教学效果、学习机制、交互设计、AI 能力边界，还是产品实现？
4. 你希望找哪种论文：
   - 入门理解型（帮我建立概念框架）
   - 教学设计型（帮我设计或改进教学）
   - 系统实现型（帮我了解技术方案）
   - 实证研究型（帮我找证据支持或反驳）
   - 产品启发型（帮我找可转化为产品的设计）

不需要说得很学术，用你的话讲就可以。
```

**需求分类判断（内部逻辑，不对用户说）**：
- 兴趣驱动：用户有方向但还模糊 → 给地图 + 入门读法
- 问题驱动：用户有具体问题或场景 → 直接翻译 + 精准推荐
- 项目驱动：用户在做产品/教学 → 加 builder 视角
- 论文扩展：用户已有一篇，想延伸 → 上下游方向推荐

---

### PHASE 2：研究问题翻译

把用户语言翻译成"论文世界里的问题"。

**输出格式——问题翻译卡**：

```
═══════════════════════════════════════
  🔎 你的问题，翻译成论文世界
═══════════════════════════════════════

【你在问的，其实是这些研究问题】
1. [研究问题1]
2. [研究问题2]
3. [研究问题3]

【可检索维度】
- 学习机制：
- 教学策略：
- AI 角色：
- 用户群体：
- 场景/任务：

【推荐关键词组合】
基础关键词：[词1] / [词2] / [词3]

组合搜索式：
- "[词A]" AND "[词B]" AND education
- "[词C]" AND feedback AND learning

【适合去哪里找】
优先：Google Scholar / Semantic Scholar
会议：AIED / EDM / LAK / CHI / CSCW / Learning Sciences
期刊：Computers & Education / BJET / Journal of the Learning Sciences
arXiv：适合 AI 系统类，教育实证类覆盖不全

═══════════════════════════════════════
```

**翻译示例**（供参考）：

| 用户语言 | 翻译成关键词 |
|---------|------------|
| 学生用了 AI 但没真正学会 | self-explanation / illusion of competence / metacognitive monitoring / worked examples |
| AI 即时反馈会不会削弱思考 | productive struggle / desirable difficulties / feedback timing / cognitive load |
| 老师怎么用 AI 做形成性评估 | AI-assisted formative assessment / learning analytics / automated feedback |
| 初学者学 coding 的 AI tutor | novice programming / intelligent tutoring systems / scaffolding / debugging support |

---

### PHASE 3：推荐论文

**推荐优先级（由高到低）**：
1. 有明确问题场景、真实用户研究的论文
2. 有学习机制或教学设计的论文
3. 有交互流程或系统设计的论文
4. 对非科研用户可读性好的论文

**降低优先级**：只做 benchmark 的论文 / 纯综述无设计抓手 / 场景离用户过远

**输出格式——论文推荐卡**：

```
═══════════════════════════════════════
  📚 给你的优先阅读建议
═══════════════════════════════════════

【先读这篇】
标题：...
为什么先读：
这篇最贴近你的[问题/角色/项目]，因为它直接处理了[核心问题]。
你会从中得到：[具体收获，一句话]
重点看：
  - 它怎么定义问题
  - 学习/交互循环是怎么设计的
  - 反馈机制如何影响用户行为
局限：它适合回答[…]，不一定能回答[…]

【第二篇】
标题：...
为什么读：它补充了[第一篇没涵盖的视角]，特别是[…]
重点看：…
局限：…

【第三篇】
标题：...
为什么读：…
重点看：…
局限：…

【阅读路径】
先用 [篇1] 建立问题图景
再用 [篇2] 看系统/教学实现
最后用 [篇3] 看边界或证据强度

【如果你只读一篇】→ 读 [标题]

【如果你想继续】
  /sense [编号] — 进入深度意义建构
  /builder     — 切换到产品视角分析
  /map         — 只要关键词和搜索地图
  /more        — 同方向再补 3 篇
  /adjacent    — 探索相邻研究方向
═══════════════════════════════════════
```

---

## 模式切换

| 指令 | 行为 |
|------|------|
| `/quick` | 快速模式：简短澄清 + 1-3 篇推荐 + 每篇一句理由 |
| `/guided` | 标准引导模式（默认）：完整三阶段 |
| `/builder` | Builder 模式：额外输出产品启发、可复用交互模式、是否值得做成功能 |
| `/map` | 只输出研究问题翻译 + 关键词搜索地图 |
| `/compare` | 对比当前推荐的几篇论文 |
| `/sense [n]` | 将第 n 篇传入深度意义建构模式 |
| `/more` | 同方向再补充 3 篇 |
| `/adjacent` | 推荐相邻方向论文 |
| `/cn` `/en` | 切换输出语言 |

---

## References

按需读取以下文件，不要全部加载：

| 文件 | 何时读取 |
|------|---------|
| `references/intent_types.md` | PHASE 1 识别用户意图时，尤其是意图不明确的情况 |
| `references/paper_type_lens.md` | PHASE 3 写推荐卡时，决定每篇论文的"重点看什么" |
| `references/query_translation_patterns.md` | PHASE 2 翻译用户语言时，查找对应关键词模式 |
| `references/venues_and_sources.md` | 输出搜索渠道建议时，查找主题对应的会议/期刊/平台 |
| `references/recommendation_rubric.md` | 有多篇候选论文需要排序/筛选时 |

---

## Scripts

论文发现完成后，可调用以下脚本获取全文：

```
scripts/
├── search_semantic_scholar.py   # 主力：API搜索 + PDF链接，覆盖教育类期刊会议
├── search_arxiv.py              # arXiv专用：全部免费PDF，适合AI/CS类论文
└── fetch_pdf.py                 # 拿到链接后下载PDF到本地（支持单个或批量）
```

**典型用法**：

```bash
# 1. 搜索论文（Semantic Scholar，自动带 PDF 链接）
python scripts/search_semantic_scholar.py "formative assessment AI" --limit 5 --year-from 2020

# 2. 搜索论文（arXiv，全部免费）
python scripts/search_arxiv.py "intelligent tutoring system" --category cs.AI

# 3. 下载单个 PDF
python scripts/fetch_pdf.py "https://arxiv.org/pdf/2301.00001" --output ./papers

# 4. 批量下载（从 Semantic Scholar JSON 结果）
python scripts/search_semantic_scholar.py "metacognition AI" --json > results.json
python scripts/fetch_pdf.py --from-json results.json --output ./papers
```

**依赖安装**：
```bash
pip install arxiv          # search_arxiv.py 需要
# search_semantic_scholar.py 和 fetch_pdf.py 只用标准库，无需安装
```

**获取路径决策逻辑**：
1. 先用 Semantic Scholar 搜索，检查是否有 `openAccessPdf`
2. 若无，检查是否有 arXiv ID → 走 arXiv 免费下载
3. 若无 arXiv，给出 Semantic Scholar 页面链接（用户自行判断）

---

## Paper Discovery Canvas（可视化前端）

`assets/paper-discovery-canvas.html` 是这个 skill 的可视化操作界面，支持三种使用方式：

### 方式一：claude.ai Artifact（展示 / Demo 用）
直接把 HTML 内容粘贴到 claude.ai 对话框，作为 Artifact 运行。
平台自动处理 API 认证，**无需填写 API Key**，开箱即用。
适合：视频 demo、课堂展示、向用户介绍这个工具。

### 方式二：本地文件（个人使用）
直接用浏览器打开 `paper-discovery-canvas.html`。
界面顶部有 API Key 输入框，填入自己的 Anthropic API Key 后即可使用。
Key 只存在浏览器内存里，不会上传或保存到任何地方。
适合：个人日常使用。获取 Key：https://console.anthropic.com/

### 方式三：配合 Claude Code（完整工作流）
在 Claude Code 里加载本 skill，Claude Code 按三阶段工作流执行论文发现。
Canvas 作为可视化展示层，scripts/ 负责搜索和下载 PDF。
适合：深度研究工作流。

---

## 生态位置

```
skill-paper-discovery        ← 你现在在这里
        ↓
skill-paper-sensemaking      ← 理解一篇论文，提炼认知结构
        ↓
skill-visual-knowledge-design ← 把认知结构可视化
        ↓
skill-paper-to-prd           ← 把研究转化为产品设计
```

---

## 典型触发场景（给 Claude 判断参考）

**应该触发**：
- "我是老师，想找 AI 形成性评估相关论文"
- "学生用 AI 写代码但没真正学会，有没有研究？"
- "我在做给老师的 AI lesson planner，帮我找相关 paper"
- "我喜欢这篇 paper，帮我找相似方向"
- "有没有关于 AI tutor 和初学者的研究"

**不应该触发**（直接用 Claude 知识回答）：
- "什么是 formative assessment"（概念解释，不是找论文）
- "帮我总结这篇论文"（论文 sensemaking，不是 discovery）

---

## 注意事项

1. **不推荐无法确认存在的论文**。如果不确定某篇是否存在，改为给出作者名、会议名、关键词搜索方向。
2. **不为了显得丰富而堆砌**。3 篇精准 > 10 篇泛泛。
3. **每篇必须给"为什么是这篇而不是别篇"的理由**。
4. **始终以用户角色和当前问题为中心**，不以学术热度为推荐依据。
