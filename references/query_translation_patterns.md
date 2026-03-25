# query_translation_patterns.md
# 用户语言 → 论文关键词 翻译模式库

这个文件收录常见的"用户说的话"到"论文关键词"的翻译模式。
Claude 在做 PHASE 2 翻译时，先查这里，再结合用户具体情况调整。

---

## 翻译模式库

### 学习效果 / 学没学会

| 用户说 | 翻译成关键词 |
|--------|------------|
| 学生答对了但没学会 | illusion of competence / shallow learning / surface processing / metacognitive accuracy |
| 学生用了 AI 但没真的理解 | AI-assisted learning / over-reliance / self-explanation / conceptual understanding |
| 学生会做题但不会迁移 | transfer learning / near transfer / far transfer / worked examples |
| 学生用了 AI 就不思考了 | cognitive offloading / productive struggle / desirable difficulties / over-reliance on AI |
| 怎么知道学生真的学会了 | formative assessment / learning analytics / knowledge tracing / assessment validity |

---

### 反馈 / 评估

| 用户说 | 翻译成关键词 |
|--------|------------|
| 即时反馈会不会削弱思考 | immediate feedback / delayed feedback / desirable difficulties / retrieval practice |
| 怎么给学生有用的反馈 | formative feedback / elaborated feedback / corrective feedback / feedback timing |
| AI 自动批改/评分 | automated essay scoring / automated feedback / NLP in education / writing feedback |
| 让学生相互评价 | peer assessment / peer feedback / collaborative learning / calibration |
| 形成性评估 | formative assessment / assessment for learning / embedded assessment / learning analytics |

---

### 元认知 / 自我调节

| 用户说 | 翻译成关键词 |
|--------|------------|
| 学生不知道自己不会 | metacognitive accuracy / calibration / Dunning-Kruger / self-assessment |
| 帮学生反思 | metacognitive scaffolding / reflective learning / self-regulated learning / prompting reflection |
| 学生不会规划学习 | self-regulated learning / SRL / goal setting / learning strategies |
| 帮学生监控自己的学习 | metacognitive monitoring / self-monitoring / learning analytics / dashboard |

---

### AI / 技术角色

| 用户说 | 翻译成关键词 |
|--------|------------|
| AI 辅导系统 | intelligent tutoring system / ITS / adaptive learning / AI tutor |
| AI 给学生提示/脚手架 | scaffolding / hints / adaptive feedback / zone of proximal development |
| AI 帮老师 | teacher-facing AI / learning analytics dashboard / instructional support |
| AI 写代码辅导 | AI programming tutor / code feedback / debugging support / Copilot in education |
| 对话式 AI 教学 | conversational agent / chatbot in education / dialogue-based tutoring |
| AI 个性化学习 | adaptive learning / personalization / learner modeling / mastery learning |

---

### 教学方法

| 用户说 | 翻译成关键词 |
|--------|------------|
| 脚手架 / scaffolding | scaffolding / ZPD / guided practice / fading |
| 项目式学习 | project-based learning / PBL / problem-based learning |
| 合作学习 | collaborative learning / CSCL / peer learning / group work |
| 翻转课堂 | flipped classroom / blended learning / pre-class preparation |
| 间隔练习 | spaced repetition / spacing effect / retrieval practice / distributed practice |
| 做中学 | learning by doing / experiential learning / constructivism |
| 游戏化 | gamification / game-based learning / educational games / motivation |

---

### 用户群体

| 用户说 | 翻译成关键词 |
|--------|------------|
| 初学者 / 新手 | novice learners / beginners / prior knowledge / expertise reversal effect |
| 编程初学者 | novice programmers / CS1 / introductory programming / computational thinking |
| K-12 学生 | K-12 education / school students / primary education / secondary education |
| 大学生 | higher education / undergraduate / college students |
| 成人学习者 | adult learning / andragogy / professional development / lifelong learning |
| 老师 | teacher professional development / teacher learning / instructional design |

---

### 动机 / 情感

| 用户说 | 翻译成关键词 |
|--------|------------|
| 学生没有动力 | motivation / self-determination theory / intrinsic motivation / engagement |
| 学生有学习焦虑 | learning anxiety / math anxiety / stereotype threat / emotional regulation |
| 学生容易放弃 | persistence / grit / growth mindset / failure response |
| 让学习更有意思 | engagement / interest development / situational interest / flow |

---

### 产品 / 系统设计

| 用户说 | 翻译成关键词 |
|--------|------------|
| 怎么设计学习系统 | learning system design / educational technology design / UX for learning |
| 怎么设计反馈循环 | feedback loop / formative feedback / assessment design / iterative feedback |
| 怎么设计 onboarding | onboarding / user onboarding / novice support / tutorial design |
| 怎么让用户坚持用 | retention / habit formation / nudge / behavior change |
| 学习数据怎么用 | learning analytics / educational data mining / dashboard / data-driven instruction |

---

## 翻译规则（给 Claude 用）

```
翻译时的优先级：
1. 先找机制关键词（描述学习/认知过程）
2. 再找策略关键词（描述教学/系统设计）
3. 最后找场景关键词（描述用户群体和任务类型）

一个用户问题，通常对应 3-5 个关键词组合。
不要只给1个，也不要给超过6个。

翻译后，构建 2-3 个组合搜索式：
- "[机制关键词]" AND "[场景关键词]"
- "[策略关键词]" AND education AND "[用户群体]"
```

## Google Scholar 链接生成规则

翻译卡末尾必须附上 2-3 个可直接点击的 Google Scholar 链接。

**生成规则**：
- 空格替换为 `+`
- 引号替换为 `%22`
- 默认加 `as_ylo=2019`（近5年）
- 精确短语用 `%22词组%22` 包裹

**示例对照**：

| 搜索式 | 生成链接 |
|--------|---------|
| `formative assessment AI` | `https://scholar.google.com/scholar?q=formative+assessment+AI&as_ylo=2019` |
| `"metacognitive monitoring" education` | `https://scholar.google.com/scholar?q=%22metacognitive+monitoring%22+education&as_ylo=2019` |
| `scaffolding AND "novice programmers"` | `https://scholar.google.com/scholar?q=scaffolding+AND+%22novice+programmers%22&as_ylo=2019` |

**输出格式**（加在翻译卡末尾）：
```
【直接搜索入口 · Google Scholar】
🔗 [关键词组合描述]
   https://scholar.google.com/scholar?q=...

🔗 [关键词组合描述]
   https://scholar.google.com/scholar?q=...
```

---

## 没有直接模式时怎么办

如果用户的问题在上面找不到对应模式：

1. 识别用户问题的核心动词（学习、设计、评估、反思、动机...）
2. 识别核心对象（学生、老师、系统、内容...）
3. 识别核心情境（课堂、在线、AI辅助、自主学习...）
4. 组合这三层生成关键词

然后在推荐时注明："这个方向的关键词是我根据你的问题推导的，建议也尝试以下搜索式：..."
