# venues_and_sources.md
# 论文来源地图：去哪里找什么

不同主题应该去不同的地方找论文。
这个文件帮助 Claude 在推荐搜索渠道时给出准确建议。

---

## 核心会议（按主题）

### AI in Education / 教育 AI
| 会议 | 全称 | 特点 |
|------|------|------|
| **AIED** | International Conference on Artificial Intelligence in Education | 教育 AI 最核心的会议，系统、算法、学习效果都有 |
| **EDM** | Educational Data Mining | 偏数据和算法，学习分析、知识追踪 |
| **LAK** | Learning Analytics & Knowledge | 学习分析，偏应用和数据驱动教学 |
| **ITS** | Intelligent Tutoring Systems | 专注智能辅导系统，理论和工程并重 |

### 学习科学 / 教学设计
| 会议 | 全称 | 特点 |
|------|------|------|
| **ICLS** | International Conference of the Learning Sciences | 学习科学最重要的会议，理论扎实 |
| **AERA** | American Educational Research Association | 教育研究综合性大会，实证研究多 |
| **ISLS** | International Society of the Learning Sciences | ICLS 主办方，也有 CSCL 子会议 |
| **CSCL** | Computer-Supported Collaborative Learning | 技术支持下的协作学习 |

### HCI / 交互设计
| 会议 | 全称 | 特点 |
|------|------|------|
| **CHI** | ACM Conference on Human Factors in Computing Systems | HCI 最顶级会议，有大量教育/学习类研究 |
| **CSCW** | Computer-Supported Cooperative Work | 协作和社会计算，含在线学习社区研究 |
| **IDC** | Interaction Design and Children | 专注儿童和青少年的交互设计 |
| **UIST** | User Interface Software and Technology | 偏工具和界面创新 |

### CS 教育 / 编程教育
| 会议 | 全称 | 特点 |
|------|------|------|
| **SIGCSE** | ACM Technical Symposium on Computer Science Education | CS 教育最重要的会议 |
| **ICER** | International Computing Education Research | CS 教育研究，实证导向 |
| **ITiCSE** | Innovation and Technology in Computer Science Education | 偏欧洲，创新教学实践 |

---

## 核心期刊（按主题）

### 教育技术 / EdTech
| 期刊 | 特点 |
|------|------|
| **Computers & Education** | 最广泛引用的教育技术期刊，实证研究强 |
| **British Journal of Educational Technology (BJET)** | 英国为主，教育技术应用 |
| **Educational Technology & Society** | 开放获取，亚太区研究多 |
| **Journal of Educational Technology & Society** | 同上 |

### 学习科学 / 认知
| 期刊 | 特点 |
|------|------|
| **Journal of the Learning Sciences** | 学习科学理论和实证的顶级期刊 |
| **Cognition and Instruction** | 认知科学和教学的交叉 |
| **Learning and Instruction** | 欧洲为主，教学和学习研究 |
| **Educational Psychologist** | 教育心理学理论综述 |

### AI / 计算机科学
| 期刊 | 特点 |
|------|------|
| **International Journal of Artificial Intelligence in Education** | AIED 的官方期刊 |
| **User Modeling and User-Adapted Interaction** | 用户建模和自适应系统 |
| **IEEE Transactions on Learning Technologies** | 技术导向，IEEE 出版 |

---

## 数据库 / 搜索平台

| 平台 | 最适合 | 特点 |
|------|--------|------|
| **Google Scholar** | 所有主题，覆盖最广 | 无官方 API，但搜索语法强大，适合浏览器手动搜索 |
| **Semantic Scholar** | 所有主题 | 官方免费 API，可看引用图谱，很多免费 PDF（脚本主力） |
| **ACM Digital Library** | HCI / CS 教育 | CHI、SIGCSE、CSCW 等会议全文 |
| **arXiv (cs.AI, cs.HC, cs.CY)** | AI / 系统 | 预印本，最新研究，全部免费（脚本支持） |
| **ERIC** | K-12 教育研究 | 美国教育资源信息中心，教育政策和实践 |
| **PsycINFO** | 教育心理学 | 需要机构授权，心理学文献权威 |
| **JSTOR** | 人文社科 / 教育历史 | 需要机构授权 |

---

## Google Scholar 使用指南

Google Scholar 没有官方 API，不适合脚本化。但它覆盖最广（含灰色文献、书籍、会议论文），
适合作为**浏览器入口**，配合高级搜索语法使用。

### 直接搜索链接生成

Claude 在输出问题翻译卡时，应同时生成可点击的 Google Scholar 搜索链接。

**链接格式**：
```
https://scholar.google.com/scholar?q=QUERY&as_ylo=YEAR
```

**示例**：
- 关键词：`formative assessment AI feedback`，2020年起
  → `https://scholar.google.com/scholar?q=formative+assessment+AI+feedback&as_ylo=2020`

- 组合搜索：`"metacognitive monitoring" AND "AI tutor"`
  → `https://scholar.google.com/scholar?q=%22metacognitive+monitoring%22+AND+%22AI+tutor%22`

**参数说明**：
| 参数 | 含义 | 示例 |
|------|------|------|
| `q=` | 搜索关键词（空格用+，引号用%22） | `q=formative+assessment` |
| `as_ylo=` | 起始年份（year low） | `as_ylo=2020` |
| `as_yhi=` | 截止年份（year high） | `as_yhi=2024` |
| `scisbd=1` | 按日期排序（最新优先） | `scisbd=1` |
| `as_sdt=0` | 包含所有类型文章 | `as_sdt=0` |

### 高级搜索语法

在搜索框直接输入，无需进入高级搜索页面：

| 语法 | 用途 | 示例 |
|------|------|------|
| `"短语"` | 精确匹配短语 | `"formative feedback"` |
| `author:姓名` | 找特定作者 | `author:"john hattie"` |
| `intitle:词` | 只在标题里搜 | `intitle:metacognition` |
| `source:期刊名` | 限定期刊/会议 | `source:"computers education"` |
| `AND` / `OR` | 布尔逻辑 | `scaffolding AND "AI tutor"` |
| `-词` | 排除某个词 | `feedback -peer` |

### 推荐操作流程（浏览器手动）

```
1. 用生成的链接打开 Google Scholar
2. 点左侧 "Since [Year]" 过滤近期论文
3. 排序选 "Relevance"（不是 "Date"，除非要找最新）
4. 找到感兴趣的论文后：
   - 点 "Cited by N" → 看引用这篇的后续研究
   - 点 "Related articles" → 找相似论文
   - 点 "All N versions" → 找免费 PDF 版本
5. 拿到论文标题后，用 Semantic Scholar 或 scripts 找 PDF
```

### 给 Claude 的输出规则

在问题翻译卡末尾，针对每个主要关键词组合，生成一个 Google Scholar 链接：

```
【直接搜索入口】
🔗 [formative assessment AI feedback（2020-）]
   https://scholar.google.com/scholar?q=formative+assessment+AI+feedback&as_ylo=2020

🔗 ["metacognitive monitoring" AND "AI tutor"]
   https://scholar.google.com/scholar?q=%22metacognitive+monitoring%22+AND+%22AI+tutor%22
```

链接数量：每次翻译卡给 2-3 个链接，对应最重要的关键词组合，不要超过 3 个。

---

## 主题 → 推荐渠道 速查表

| 用户想找的主题 | 优先去这里 |
|--------------|-----------|
| AI 教育系统 / AI tutor | AIED → Semantic Scholar → arXiv cs.AI |
| 学习分析 / 教育数据 | LAK, EDM → Computers & Education |
| 元认知 / 自我调节学习 | ICLS, Cognition and Instruction → Google Scholar |
| 反馈设计 / 形成性评估 | Computers & Education, BJET → Google Scholar |
| 编程教育 / CS 教育 | SIGCSE, ICER → ACM Digital Library |
| HCI / 学习界面设计 | CHI, CSCW → ACM Digital Library |
| 协作学习 | CSCL, CSCW → Google Scholar |
| 儿童学习 / K-12 | IDC, AERA → ERIC |
| 动机 / 游戏化 | Learning and Instruction → Google Scholar |
| 最新 AI 研究（系统类） | arXiv cs.AI, cs.HC, cs.CY |

---

## 免费获取策略

```
优先级：
1. arXiv — 完全免费，适合 AI/CS 类
2. Semantic Scholar — 很多论文有直接 PDF 链接
3. 作者个人主页 / ResearchGate — 作者上传版
4. Unpaywall 浏览器插件 — 自动找开放版本
5. Google Scholar → 点"所有版本" — 有时有免费版

使用本 skill 的 scripts：
  python scripts/search_semantic_scholar.py "关键词" --limit 5
  python scripts/search_arxiv.py "关键词"
  python scripts/fetch_pdf.py --from-json results.json
```
