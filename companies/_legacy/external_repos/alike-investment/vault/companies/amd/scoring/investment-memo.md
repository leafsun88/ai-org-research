---
company: Advanced Micro Devices, Inc.
ticker: AMD
memo_level: L4
alike_score: 76
fit_score: 4/5
most_resonant_old_friend: nvidia
date: 2026-04-09
analyst: Alike Investment System L4
data_cutoff: 2026-04-09
---

# AMD (Advanced Micro Devices, Inc.) — L4 Investment Memo

---

## Executive Summary

**一句话 Thesis**

> 市场将AMD定价为"NVIDIA的低配版挑战者"（当前Forward P/E 21.5x vs NVIDIA ~30x），实际上它是一家由工程师CEO Lisa Su领导的"开放AI生态建设者"——在硬件执行力（年度GPU节奏+EPYC CPU 33%份额）已达顶级的基础上，三重业务拐点正在同步展开：(1) MI400/Helios Rack 2026 H2量产，(2) Meta $100B+/OpenAI 6GW超大规模anchor客户锁定，(3) ROCm软件飞轮从"可用"向"首选"迁移——而市场仍在用"CUDA护城河不可突破"的静态叙事定价，这是一个正的认知差窗口。

**关键数字仪表盘**

| 指标 | 数值 | 意义 |
|------|------|------|
| 股价（2026-04-09） | $231.82 | 52周高$267，折让13% |
| 市值 | $377.96B | |
| EV | $354.64B | |
| FY2025营收 | $34.64B | +34.3% YoY |
| Data Center营收（FY2025） | $16.6B | 占总营收48%，+32% YoY |
| FCF（FY2025） | $6.74B | +180% YoY，FCF利润率19.4% |
| 净现金 | $7.33B | 财务弹药充足 |
| Forward P/E | 21.5x | 相对NVIDIA折价约30% |
| Alike Score | 76/100 | 高质量挑战者 |
| 分析师目标价均值 | $289.35 | 46位分析师，隐含涨幅+25% |

**投资评级**：观察偏买入 — MI450/Helios 2026 H2量产是关键验证节点；Meta/OpenAI大单已提供多年营收基底；但ROCm生态成熟度和AMD能否从"挑战者"转变为"开放AI基础设施标准"仍是核心不确定性。

**最大风险**：ROCm与CUDA的性能差距在2026-2027年未能明显收窄，导致hyperscaler将AMD定位为"纯粹备选方案"而非"战略合作伙伴"，压制ASP和市场份额增长空间。

---

## 一、组织穿透

### 1.1 D1-D7 组织评分总览

**是的，MI300/MI400系列是A类Key Bet，原因如下：**

| 维度 | 得分 | 一句话判断 |
|------|------|-----------|
| D1 CEO认知质量 | 4.5/5 | 第一性原理芯片架构判断：2018年，当竞争对手嘲笑chiplet为"glue"时，Lisa Su押注chiplet架构，理由是Moore's Law正在改变，需要不同的差异化路径 |
| D2 Key Leader深度 | 3.5/5 | Mark Papermaster（CTO, EVP Technology & Engineering）：MIT & IBM出身，加入AMD 2011年，已15年 |
| D3 考核激励机制 | 3.5/5 | "Pay for Performance"声明：10-K HR章节明确"we have a strong pay for performance culture"，但具体工程师考核机制完全不可观察 |
| D4 信息架构 | 3.5/5 | 创新与技术委员会（Innovation and Technology Committee）：Board级别的专门委员会负责技术和市场风险的监督，表明技术信息能到达董事会层面 |
| D5 组织熵减能力 | 4.0/5 | ZT Systems收购+12个月出售制造部门：2025年3月以$30亿+收购ZT Systems，同年10月将制造业务出售给Sanmina |
| D6 Talent Density | 4.0/5 | MIT/IBM/Bell Labs基因：Lisa Su本人（MIT PhD半导体）及高管团队（Papermaster来自IBM）的技术背景为工程师文化提供了顶层信号 |
| D7 Key Bet质量 | 4.5/5 | MI300/MI400系列是A类Key Bet——年度硬件节奏追上NVIDIA，Meta $100B+大单和OpenAI 6GW协议证明已进入tier-1 hyperscaler核心训练基础设施，ROCm软件生态是未完成的拼图 |
| **Alike Score** | **76/100** | Fit: 4/5 |

### 1.2 为什么最像NVIDIA？差异在哪里？

**表层共振**：AMD与NVIDIA都是高性能计算GPU公司、工程师CEO领导、年度硬件节奏驱动、数据中心AI是核心增长引擎。但这个表层共振掩盖了本质差异：

**NVIDIA是平台定义者（Paradigm Creator）：**
> *"Jensen Huang的CUDA是20年连续信念的制度化——T5T信息网络、One Architecture承诺均直接从CEO认知转化为组织机制。"*

NVIDIA的护城河是认知+组织+产品的三重compounding：Jensen 2006年在CUDA上的押注当时被认为是疯狂的，但20年的持续投入将一个API变成了数百万开发者的思维框架——这是CUDA真正的护城河，而非H100的算力数字。

**AMD是生态挑战者（Open Ecosystem Challenger）：**

Lisa Su的核心认知不是"我们要复制CUDA"，而是"CUDA是单一供应商的封闭系统，而AI基础设施最终需要开放生态"：

> *"You're right, it was not the obvious strategy. But we had a vision. We had to say, 'What do we think we could be best at?' If you take a look at the five-year arc, not the two-year arc, Moore's law was changing."* — Lisa Su, Christian Investing Substack, 2025-07-03 ([Substack](https://christianinvesting.substack.com/p/research-report-amd-modularity-wins))

**共振的本质不在于相似，而在于生成力的阶段性对应**：AMD 2025年的状态类似于NVIDIA 2016-2018年——GPU已在数据中心获得重要客户，软件生态（ROCm vs CUDA 2015-2018年）仍在追赶，年度硬件节奏刚刚建立。

**AMD与NVIDIA的Alike Score差距（76 vs ~92+）**核心在于：
1. 软件生态compounding已有的年份：CUDA 19年 vs ROCm 9年
2. 制度化程度：Jensen T5T=组织机制 vs Lisa Su"Run towards problems"=文化口号
3. Fit Score：NVIDIA 5.0（算力基础设施=One Architecture完美适配）vs AMD 4.0（Full-stack AI系统方向正确但ROCm软件错配尚未修复）

> *"We are uniquely positioned to deliver across this stack, combining industry-leading CPUs, GPUs and adaptive SoCs with networking, software and system integration expertise."* — AMD 10-K FY2025, Business Section ([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm))

### 1.3 CEO认知进化：从救火到AI时代挑战者定义者

Lisa Su的CEO认知轨迹是Alike框架中最重要的观察维度：

**第一阶段（2014-2018）：救火者认知**
- 核心判断：AMD有高性能CPU+GPU两个核心资产，问题是缺乏清晰战略和执行机器
- 关键决策：聚焦高性能计算（放弃消费移动），chiplet押注（被竞争对手嘲笑时推进）
- 认知特征：第一性原理分析（"从5年维度看，不从2年维度看"），工程师CEO本能

**第二阶段（2019-2022）：挑战者认知**
- 核心判断：EPYC可以赢得服务器市场，半导体行业进入"谁赢得roadmap谁赢得一切"时代
- 关键决策：Xilinx $500亿收购（当时被质疑，现在看是FPGA+AI协同的正确布局）
- 认知特征：从"能执行"升级到"能定义产品类别"

**第三阶段（2023-至今）：AI生态建设者认知**
- 核心判断：AI将不仅需要算力，还需要完整的软件+系统+网络解决方案；开放生态是对抗CUDA封闭护城河的唯一可持续策略
- 关键决策：年度GPU节奏、ROCm开源投入、Meta/OpenAI战略关系、Helios Rack全栈产品
- 认知特征：超越"芯片供应商"，向"AI基础设施伙伴"升维

> *"We believe AI systems will require not only powerful chips, but also full-stack innovation across compute, networking, systems architecture and software."* — AMD 10-K FY2025 ([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm))

**认知边界（需持续观察）**：Lisa Su的认知对ROCm软件优先级的定义是否已内化为"战争级别"的组织承诺？公开表态和招聘数据的匹配度是关键验证点。

### 1.4 组织弱势维度

**D3（3.5/5）：考核激励的结构性问题**
- 薪酬风险评分9/10（Yahoo Finance）暗示激励结构设计存在问题
- 缺乏可识别的"A类原创激励机制"（对比NVIDIA T5T+不裁员承诺体系）
- AMD的"Pay for Performance"声明是目标而非可观察的机制

**D4（3.5/5）：内部信息流转不透明**
- 外部披露质量出色（segment数据精准），但31,000人内部信息如何流转不可观察
- 与NVIDIA T5T全员信号网络的差距在于"制度化而非方向"

**组织穿透评级：B+**（强工程执行力+有待完善的软件文化承诺强度）

---

## 二、投资论点

### Bull Case

**1. MI400/Helios 2026 H2：AMD最大产品发布验证年**

MI450+MI455X+Helios Rack-Scale Platform在2026年H2进入量产——这是AMD自EPYC Zen 2以来最重要的产品发布节点。

- S&P Global预测：MI400系列2026年产生约$7.2B收入，Data Center GPU全年同比增长114%至$15B ([S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/03/amd-s-next-generation-ai-chips-set-to-power-2026-data-center-growth))
- 关键技术参数：CDNA 5架构，HBM4内存，较MI350理论性能提升约3倍（特定AI训练工作负载）
- Helios=完整系统方案，ASP大幅高于单块GPU，是AMD向"系统集成商"转型的验证

> *"Management outlined a 2H FY 2026 inflection as MI450 and Helios rack-scale systems enter volume."* — Futurum Research, 2026-02-05 ([Futurum](https://futurumgroup.com/insights/amd-q4-fy-2025-record-data-center-and-client-momentum/))

**2. Hyperscaler Anchor：Meta+OpenAI大单提供多年营收基底**

- Meta $100B+ AI芯片多年协议（含训练+推理）——这是单一最大的AMD GPU采购承诺，且已被行业媒体确认 ([The Rundown](https://podcasts.apple.com/us/podcast/amd-lands-%24100b-ai-deal-with-meta/id1726048251))
- OpenAI 6GW部署协议（MI450系列为首批GW产能）——AMD从"推理备选"到"训练战略合作伙伴"的身份转变
- Meta/OpenAI的规模化使用意味着ROCm软件已具备frontier model训练能力——这是ROCm飞轮自我验证的开始

**3. EPYC CPU：最稳定、最不依赖ROCm的增长引擎**

- 服务器CPU市场份额33%（all-time high），且Intel份额仍在下滑
- "Venice" CPU 2026 H2发布，延续5th Gen EPYC的市场份额增长势头
- Data Center AI工作负载增长→服务器CPU需求增长→EPYC受益，与GPU业务有正相关性

**4. 开放生态的长期战略优势**

超大规模hyperscaler（Meta/Microsoft/Google/Amazon）都有"避免单一供应商依赖"的结构性需求——CUDA锁定对他们而言既是算力优势也是议价权威胁。ROCm的开源特性为这些客户提供了战略上的"第二选择"价值，即使ROCm的绝对性能低于CUDA，也有部署理由。

> *"长期来看，AMD是'开放生态'的赌注。随着企业寻找NVIDIA封闭系统的替代方案，AMD正在成为开放标准运动的领导者。"* — Simply Wall St Analysis, 2026-01-30

### Base Case

**最可能情景**：AMD Data Center segment在2026-2027年保持50%+增速，MI450 2026 H2如期量产但产能爬坡比预期慢；ROCm生态在2027年底仍明显落后于CUDA但差距开始收窄；EPYC持续份额增长但放缓至年增速15-20%；FCF利润率从19.4%稳步提升至25%+。

全年营收：2026年约$46-47B（+34% YoY），2027年约$60-70B。

### Bear Case

**1. ROCm差距未收窄，AMD被定格为"纯粹备选方案"**

如果2027年ROCm与CUDA的性能差距（目前高并发场景30-67%）未降至<15%，AMD的AI GPU将始终被定位为"备用/压价工具"——定价权受限，ASP难以提升。

> *"CUDA的CUDA Gap Score在30-99之间，意味着软件优化可以等效于硬件性能提升30-99%。"* — AIMultiple CUDA vs ROCm研究, 2026-01 ([AIMultiple](https://aimultiple.com/cuda-vs-rocm))

**2. NVIDIA Blackwell/Rubin架构进一步拉大差距**

NVIDIA的B200/R系列（2025-2026）若在软件优化上继续领先，AMD的年度节奏追赶可能永远落后"一代"——成为永久性的追赶者而非竞争者。

**3. 大客户采购集中度风险**

Meta+OpenAI的超大规模订单造成AMD营收对少数客户的高度依赖——若任一客户削减采购（技术路线变化/自研芯片加速），AMD营收波动将远超预期。

**4. 宏观和出口管制风险**

美国对华芯片出口管制影响AMD MI308等产品在中国市场的销售——Q4 2025已有$390M中国相关MI308销售在指引中未被计入。

---

## 三、基本面概览

| 指标 | FY2025 | FY2024 | FY2023 | FY2022 |
|------|--------|--------|--------|--------|
| 营收 | $34.64B | $25.79B | $22.68B | $23.60B |
| YoY增速 | +34.3% | +13.7% | -3.9% | +43.6% |
| 毛利率 | 49.5% | 49.4% | 46.1% | 44.9% |
| 营业利润率 | 10.7% | 8.1% | 1.8% | 5.4% |
| 非GAAP营业利润率 | ~22.5% | ~22% | ~24% | ~26% |
| 净利润 | $4.33B | $1.64B | $854M | $1.32B |
| FCF | $6.74B | $2.40B | $1.12B | $3.12B |
| FCF利润率 | 19.4% | 9.3% | 4.9% | 13.2% |
| R&D投入 | $8.09B | $6.46B | $5.87B | $5.00B |
| R&D/营收 | 23.4% | 25.0% | 25.9% | 21.2% |
| 员工数 | ~31,000 | ~26,000 | ~25,000 | ~25,000 |
| 人均营收 | $1.12M | ~$990K | ~$900K | ~$940K |
| Rule of 40 | 51.2 | ~23 | ~1 | ~23 |
| 净现金 | $7.33B | $3.41B | $3.31B | $3.39B |

([AMD Financial Data](https://finance.yahoo.com/quote/AMD/))

**业务分段（FY2025全年）**：
| 分段 | FY2025营收 | YoY |
|------|-----------|-----|
| Data Center | $16.6B | +32% |
| Client & Gaming | ~$14.8B | ~+30% |
| Embedded | ~$3.2B | 恢复中 |

**Q4 2025分段（季度）**：Data Center $5.4B（+39%）, Client $3.1B（+34%）, Gaming $843M（+50%）, Embedded $950M（+2.9%）。

([AMD Q4 FY2025 IR Release](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial-results))

**组织效率信号**：
- FCF从FY2024 $2.4B跳升至FY2025 $6.74B（+180%），FCF利润率从9.3%到19.4%——这是AI GPU规模效应开始释放的财务证明
- 人均营收持续提升（$1.12M），与NVIDIA $2M+的差距正在收窄
- SBC占营收4.7%（行业合理水平，不过度稀释）

---

## 四、竞争格局深度分析

### AI GPU市场：定性分析框架

| 维度 | AMD | NVIDIA | AMD相对优势 |
|------|-----|--------|-----------|
| 年度硬件节奏 | 已建立（MI300→MI450→MI500） | 已建立（H100→H200→B200） | 接近对等 |
| 软件生态 | ROCm开源，10年历史，仍追赶 | CUDA 20年，数百万开发者 | NVIDIA大幅领先 |
| 内存带宽 | HBM3E（MI350），HBM4（MI450） | HBM3E（H200），HBM4（B200 2027） | AMD有一定优势（特定场景） |
| 系统解决方案 | Helios（2026 H2） | DGX H100/B200 完整系统 | NVIDIA领先，AMD追赶中 |
| TCO | 同等算力下AMD有竞争力 | 更高ASP | AMD TCO优势明显 |
| 多供应商价值 | hyperscaler战略需求 | 单一供应商锁定 | AMD有独特战略价值 |
| 客户锁定深度 | Meta/OpenAI多年大单 | 生态锁定 | 各有护城河 |

### EPYC vs Intel Xeon：AMD已胜利

EPYC从<1%到33%的市场份额之旅已完成——AMD在服务器CPU市场的转型是过去10年半导体行业最成功的案例之一，也是Lisa Su认知迭代→战略执行→业务验证的最完整证明。

> *"EPYC processors have reached an all-time high of 33% server unit share, continuing to eat into Intel's legacy footprint."* — Simply Wall St, 2026-01-30

---

## 五、估值与预期回报

**当前估值（2026年4月）**：

| 指标 | 数值 | 历史区间 |
|------|------|--------|
| Forward P/E | 21.5x | 历史区间15-60x |
| P/S (TTM) | 10.9x | |
| EV/Revenue | 10.2x | |
| EV/EBITDA | 52.6x（GAAP）| 非GAAP调整后约14-16x |
| Trailing PEG | 0.65 | <1.0=成长被低估 |
| 分析师目标价均值 | $289.35 | 隐含涨幅+24.8% |

**分析师共识**：46位分析师，37 Buy/8 Hold/0 Sell，目标价$220-$365，中位数$290.50。

**认知差来源**：市场仍在用"CUDA护城河不可突破"的静态叙事为AMD AI GPU业务打折，未充分计入：
1. Meta/OpenAI anchor大单提供的多年营收可见性
2. EPYC CPU持续份额增长的复利效应
3. FCF从$2.4B到$6.74B的质变（从成长公司到现金生成机器）
4. 年度GPU节奏建立后的产品迭代确定性

**简易估值框架（基于FY2027E）**：

| 情景 | FY2027E营收 | FCF利润率 | FCF | EV倍数 | 目标价 |
|------|-----------|---------|-----|--------|--------|
| Bull（ROCm突破，MI500验证） | $70B | 22% | $15.4B | 30x EV/FCF | ~$280+ |
| Base（稳步推进，没有黑天鹅） | $60B | 20% | $12B | 22x EV/FCF | ~$210-240 |
| Bear（ROCm停滞，大客户减单） | $45B | 16% | $7.2B | 15x EV/FCF | ~$115-130 |

---

## 七、风险、催化剂与时间线

### Top风险

| 风险 | 概率 | 影响 | 组织层面关联 |
|------|------|------|-----------|
| ROCm性能差距未收窄（2027仍>20%） | 40% | HIGH | D7软件Bet未能成为A类；定价权受限 |
| MI450/Helios 2026 H2交付延迟 | 25% | HIGH | 年度节奏破功；市场信心受损 |
| 大客户（Meta/OpenAI）自研芯片加速 | 20% | MEDIUM-HIGH | 营收集中度风险暴露 |
| 出口管制进一步扩大 | 30% | MEDIUM | 中国市场~15%营收受影响 |
| Lisa Su离职（<2028） | 5% | VERY HIGH | D1单点风险；无明确接班人 |
| 半导体周期下行 | 25% | MEDIUM | Embedded/Client拖累，Data Center延缓 |

### 催化剂

**正面催化剂**：

| 催化剂 | 时间 | 概率 | 逻辑 |
|--------|------|------|------|
| MI450/Helios开始量产交付 | 2026 Q3 | 75% | 验证年度节奏承诺 |
| Data Center Q2 2026 >$6B | 2026年7月 | 65% | AI GPU拐点继续向上 |
| ROCm benchmark改善（差距<25%） | 2026年底 | 50% | 软件飞轮开始转动 |
| EPYC "Venice" CPU正式发布 | 2026 H2 | 90% | 服务器CPU份额继续扩张 |
| FY2026 FCF利润率突破22% | 2027年初 | 60% | FCF质变持续 |

**负面催化剂**：

| 催化剂 | 时间 | 概率 |
|--------|------|------|
| MI450量产延迟至2027 | 2026 Q3 | 20% |
| Meta减少AMD订单（加速内建AI芯片） | 2026-2027 | 15% |
| 进一步出口管制扩大至MI350 | 2026年 | 25% |

### 时间差窗口

```
组织变化（2023-2024）          战略验证（2025-2026）         业务兑现（2027-2028）
年度GPU节奏制度化              MI350→MI450量产               Data Center >60%年增速实现
ROCm软件投入加速              Meta/OpenAI大单执行           ROCm生态飞轮验证/失败
Helios全栈战略确立            EPYC "Venice" 发布             FCF利润率25%+
        |                           |                           |
     <12-24月->                 <12-24月->                 ← 股价重评估
```

当前处于"战略验证期中段"——组织已设定年度节奏，客户大单已锁定，但MI450/Helios的量产和ROCm生态的软件进展将在2026年H2至2027年提供决定性验证。

---

## 八、投资结论与信息缺口

**投资决策**：观察偏买入

- **建仓条件**：MI450开始向Meta/OpenAI交付（2026 Q3新闻验证）+ Data Center Q2 2026 >$5.5B
- **加仓条件**：ROCm与CUDA差距在PyTorch基准测试中收窄至<20% + FY2026年化Data Center营收 >$25B
- **减仓/止损条件**：MI450量产延迟超过2个季度 + 任一hyperscaler客户缩减AMD订单超过30%

**情景分析**

| 情景 | 概率 | 结果 | 目标价区间 | 驱动因素 |
|------|------|------|-----------|--------|
| 多头 | 25% | ROCm突破，MI500提前，AI PC爆发 | $350-$400 | 软件飞轮验证+估值重评 |
| 基准 | 50% | 年度节奏维持，ROCm缓慢改善，FCF持续增长 | $240-$290 | 分析师共识区间 |
| 空头 | 25% | ROCm停滞，大客户减单，周期下行 | $130-$160 | 多供应商故事失败 |
| **期望价值** | | | **$240-$270** | 加权（净现金$7.33B提供底部支撑） |

**信息缺口**

| 缺失信息 | 重要性 | 建议下一步 |
|---------|-------|----------|
| ROCm工程团队实际规模和投入 | VERY HIGH | GitHub commit数据+LinkedIn招聘分析 |
| Meta实际部署进展和ROCm使用情况 | VERY HIGH | 每季度earnings call追踪 |
| Lisa Su内部工作机制（T5T类似机制？） | HIGH | 离职高管访谈+Glassdoor深度分析 |
| MI450性能基准测试数据 | HIGH | 2026 Q2-Q3技术发布会+第三方评测 |
| C-suite以下VP层Xilinx整合后质量 | MEDIUM | LinkedIn org-scan |
| 内部考核机制（D3深度验证） | MEDIUM | 前员工博客+社区访谈 |

---

## 附录：研究材料索引

### L1 Discovery层（原始数据）

| 文件 | 日期 | 信源级别 |
|------|------|--------|
| `discovery/sources/earnings/2026-02-04_10-K.md` | 2026-02-04 | S5 |
| `discovery/sources/earnings/2025-11-05_10-Q.md` | 2025-11-05 | S5 |
| `discovery/sources/earnings/2025-08-06_10-Q.md` | 2025-08-06 | S5 |
| `discovery/sources/earnings/2025-05-07_10-Q.md` | 2025-05-07 | S5 |
| `discovery/sources/earnings/2026-03-27_DEF 14A.md` | 2026-03-27 | S5 |
| `discovery/financials.md` | 2026-04-09 | S5 |
| `discovery/financials_detailed.md` | 2026-04-09 | S5 |
| `discovery/profile.md` | 2026-04-09 | S4 |
| `discovery/organization/_org_scan_report.md` | 2026-04-09 | S4 |
| `discovery/sources/founder_voice.md` | 2026-04-09 | S3 |

### 外部参考（S2-S3）

| 来源 | 标题/内容 | 日期 |
|------|---------|------|
| Stratechery (Ben Thompson) | AMD CEO Lisa Su interview | 2024-06-06 |
| Christian Investing Substack | AMD Modularity Wins研究报告 | 2025-07-03 |
| AIMultiple | CUDA vs ROCm 2026比较 | 2026-01-22 |
| S&P Global Market Intelligence | AMD Next-Gen AI Chips 2026展望 | 2026-03-17 |
| AMD IR (S5) | Q4 FY2025 Earnings Release | 2026-02-03 |
| AMD IR (S5) | Q3 FY2025 Earnings Release | 2025-11-04 |
| Futurum Research | AMD Q4 FY2025分析 | 2026-02-05 |
| Simply Wall St | AMD数据中心分析 | 2026-01-30 |
| Pear VC | Lisa Su Leadership Lessons | 2025-10-30 |
| Chief Executive Group | CEO of the Year: Lisa Su | 2024-10-23 |

### L2-L3分析层

| 文件 | 类型 |
|------|------|
| `scoring/alike-memo.md` | L2 Alike Score (76/100) |
| `scoring/org-inflection.md` | L3 Org Inflection |
| `scoring/biz-inflection.md` | L3 Biz Inflection (ABCD) |

### 校准参照

| 文件 | 用途 |
|------|------|
| `vault/old-friends/_calibration.json` | D1-D7校准矩阵 v2.0 |

---

*生成日期：2026-04-09 | 信息截止：2026-04-09 | 分析师：Alike Investment System L4 | 校准版本：v2.0*

*This is research and analysis only, not personalized financial advice. Consult a qualified financial advisor before making investment decisions.*
