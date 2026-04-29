---
company: Google (Alphabet)
status: old_friend
paradigm: "大象转身范式——通过DeepMind大一统+创始人回归，用组织集中化释放技术存量，在存量帝国内部重新点燃pre-train scaling的战斗力"
last_updated: 2026-04-07
---

# Google — Old Friend Profile

## 这家公司发明了什么范式？

Google发明了"大象转身"范式：一个拥有7个20亿MAU产品的巨型组织，在面临ChatGPT的存亡级威胁时，通过Hassabis主导的DeepMind大一统、创始人Sergey回归做关键决策（重视pre-train而非post-train雕花）、产品组织的"洋务运动"（权力下放到Director级、招类Meta的PM），实现了从分散内斗到集中力量办大事的组织转型。核心逻辑是：用组织架构的集中化来释放被内耗浪费的技术存量（pre-train scaling能力+TPU算力+7大产品的Universal Context）。

## D1-D7 校准锚点

### D1 CEO认知质量 — 3.5/5

Sundar Pichai本人并非此次觉醒的核心驱动者。真正做出关键决策的是创始人Sergey Brin——回归后发信要求"重视pre-train，少在post-train雕花"，以及Hassabis推动DeepMind大一统。Pichai的角色更像是允许这些变化发生，而非主动驱动。员工反馈"Google更看likability，不是metrics"、"knowledge isolation"等问题都指向CEO层面的历史欠账。但Pichai的功劳在于：在危机时刻没有阻挡变革，让Hassabis拿到了整个公司最核心的scope。

### D2 Key Leader深度 — 4/5

- **Demis Hassabis**：把整个谷歌训模型的scope集中进DeepMind，"Gemini-First"战略的执行者
- **Sergey Brin**：创始人回归，做了重视pre-train的战略性决策
- **Noam（Transformer八子之一）**：从Character AI回归，灵光一现解决pre-train架构bug，"一次修改就值回四年薪资"
- **Josh（Google Labs负责人）**：洋务运动的执行者，砍VP、拉平team、招类Meta PM，Nano Banana爆款背后的推手
- **Oriol团队**：Nano Banana / Imagen模型核心成员，推动Veo与Imagen团队合并

### D3 考核激励机制 — 2.5/5

Google的考核机制是这次转型中最大的组织债。历史上"likability占50%以上权重"，focus on likability而非impact，导致不敢take risk、不敢launch。直到最近才开始引入数字考核（"真正考number是从去年才开始的"）。Meta两周做完的实验在Google要三个月，quarterly才有一次insight。这些都是制度层面的深层问题，正在改但远未解决。

### D4 信息架构 — 2/5

员工原话："Google的organization最重要的作用是knowledge isolation。"层层拆解让员工只能做份内事，leadership开会把presentation关掉不让基层看。与Jensen的T5T、Tobi的GSD形成鲜明对比。DeepMind大一统后有改善（cross-team的friction减少了），但整体信息架构依然是大公司病的重灾区。

### D5 组织熵减能力 — 3.5/5

正在觉醒。2023年完全混乱（"300个人出现在agent项目第一周"、"两个Chatbot、两套LLM infra"），但2024-2025年通过Hassabis大一统实现了显著的熵减：Google Brain从"drop innovation"变成"Serve Gemini"、Veo和Imagen团队合并、NotebookLM终于集成进Gemini App。Josh的6人攻坚小组+做完就transfer的模式也是有效的熵减机制。但post-train依然有2000人在做、方向分散，"连让一个model converge都很难"。

### D6 Talent Density — 4/5

DeepMind聚集了全球顶级的AI研究人才。Noam回归后一个修改解决困扰已久的bug，团队投入到"direct report和女朋友分手了"的程度。Nano Banana背后有天才researcher用two sets of tokens解决了"抽象vs无损"的矛盾。但大公司整体的talent density被稀释——Google Translate几百号人没事做到处"流窜"，很多senior leader/VP还是旧思维。Josh在招"类Meta"的PM来提升产品侧密度。

### D7 Key Bet质量 — 4.5/5

三个Key Bet都极其有力：
1. **Gemini pre-train scaling**：一年3次大规模pre-train（vs Anthropic 1次），且还没撞墙，post-train空间巨大
2. **TPU**：内部共识"100%的人都用TPU不用GPU"，OCS光互联是降维打击，正在从防守牌变进攻牌
3. **GCP做AI Cloud**：Vertical Integration（最好的芯片+最好的模型），startup覆盖率90%+

## Fit Score — 4/5

Google的业务本质是"全球信息的组织和分发"，AI时代变成"全球信息的理解和生成"。从Search到Gemini是自然延伸，TPU+模型+7大产品的纵向整合与业务本质高度适配。减分项：组织从分散走向集中还在进行中，post-train的组织问题是"草下的萝卜"，释放需要时间。

## Step 0: 业务本质 -> 组织形态推导

**业务本质**：全球最大的信息入口（Search）+ AI基础设施（TPU/GCP）+ 大模型（Gemini）的三位一体。本质上是一家"算力+模型+分发"的纵向整合公司。

**理想组织形态**：需要极强的技术集中力（不能让多个team各自训模型）、极快的产品迭代（AI产品寿命短、需ship fast）、极深的算力积累（TPU需要十年级别的持续投入）。当前组织正在从"分散的研究院联盟"向"以Gemini为核心的集中作战体"转型。

## "学我者生，似我者死"边界

**学Google者生**：
- 技术存量释放的组织方法论——当一个大公司有分散的技术团队时，通过"大一统"集中scope可以释放巨大的组织红利
- 创始人回归做关键判断的模式——Sergey重视pre-train的决策，一个人的判断胜过千人的内卷
- Josh式的"洋务运动"——在大公司内部创造startup式的小团队，砍VP层级、6人攻坚+transfer

**似Google者死**：
- 不能复制"7个20亿MAU产品"的护城河——Universal Context是Google独有的
- 不能复制TPU十年积累——这是不可逆的时间壁垒
- 不能复制"算力无限"的前提——Google一年3次pre-train是因为有TPU，其他公司做不到
- 大象转身的前提是"你得先是大象"——对中小公司无意义

## 关键原声引用

> "23年完全混乱的，23年为什么Gemini那么烂，是因为所有的团队打得真的一塌糊涂......300多人，全都来挤在一个芝麻大的事上......竞争对手搞不死你，内部先把你搞死。"

> "有时候你觉得只这一次修改就值回四年的薪资。" —— 关于Noam回归后解决pre-train架构问题

> "Google很强大，而且已经醒了。" —— 段永平

> "OpenAI越想变得profitable，他们的基座模型能力就越跟不上。如果他们基座做不起来，到头来可能连中国做的都不如。"

> "我甚至觉得之前Google的organization最重要的作用是knowledge isolation，刻意让你对一些事情不知道。"
