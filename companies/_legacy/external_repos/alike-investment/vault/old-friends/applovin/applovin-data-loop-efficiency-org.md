# AppLovin: 海量闭环数据和极致效率组织驱动的算法机器 [Final] 副本

## Executive Summary

> AppLovin做的效果广告的本质是一场广告竞价拍卖中的预测精度之争。效果广告主分配渠道预算的决策逻辑高度简单：哪个平台带来的ROAS更高，预算就流向哪里；Publisher选择接入哪个变现平台的逻辑同样如此：哪个平台带来的eCPM更高，流量就给谁。
> 访谈与行业调研印证了这一点。广告主侧，AppLovin的ROAS表现——尤其是D28优化窗口下的长周期用户质量——是其从Meta、Google和其他中小玩家手中持续抢占预算份额的核心驱动力；Publisher侧，MAX在游戏类App中已达到70-80%的市占率，核心原因是其相对AdMob平均10-30%的eCPM提升。**算法效果是这个生意中最关键的竞争门槛——效果领先则预算与流量正向集聚**。
> 决定算法效果的是两个更底层的结构性支撑：闭环数据提供了高质量的数据燃料，组织机制保障了实验的高频产出和算法迭代速度。
> **支柱一：海量闭环数据**
> AppLovin通过3个产品构建了一套其他广告平台难以复制的数据获取体系。MAX作为供给侧SSP，持续输入发布商流量和拍卖成交价信号；AppDiscovery作为需求侧DSP，回传广告主出价行为和竞对竞价水位；Adjust作为归因MMP，提供从广告曝光到用户购买的全链路转化数据；广告主与发布商的真实市场行为则作为第四路信号，持续校准模型对创意效果和用户行为的判断。
> **这三类型数据形成 "数据密度↑→算法模型精度↑→广告主的ROAS↑→广告主预算↑ 和 开发者收益↑ →数据密度↑" 的自强化飞轮。**这一飞轮的起点，在于算法本身的精度提升：更好的算法意味着MAX能为开发者（Publisher）带来更高的eCPM，从而吸引更多开发者将自己的广告库存迁移至MAX，推动其在Mediation领域的市占率持续提升；与此同时，更高的ROAS也驱动广告主将更多预算集中投入AppDiscovery，进一步巩固其在Ad Network中的竞争地位。供给与需求两端的双重扩张，带来了更大体量的行为数据和转化信号，反哺AXON迭代出更精准的算法——形成一个难以从外部打破的正反馈闭环。。
> **支柱二：组织机制：以Pod为单元、算法迭代为核心的极简工程驱动型组织**
> 数据闭环决定了AXON能获得多少数据，组织机制决定这些数据能被以多快的速度转化为算法迭代和最终算法效果的提升。
> - **极致精简的组织原则 + 技术决策高度集中**：AXON2.0的模型框架、排序算法、产品路线图和实验工具体系，全部由Gio（CPEO）一人拥有决策权。CTO Basil提供基础设施底座。在其他科技大厂，同等范围可能需要10-15个VP，每个决策都需跨VP协调。产品方向由CTO和CPEO直接决策，工作流仅3-4层，市场信号可在数小时内从高层传导至执行工程师。
> - **”Pod“制小团队 x Full-stack能力要求 ****—> ****极快的算法迭代速度**：150名核心工程师分散在约20个自治Pod中，每个Pod专注单一指标、拥有端到端所有权。每位工程师被要求独立掌握特征工程、建模和业务逻辑的完整技术栈，最大程度消除跨人依赖，确保单个工程师即可独立推进一个完整实验。同一模型可同时有多名工程师在各自Pod内独立训练不同版本，将实验并行密度放大至传统组织难以企及的量级。
> - **Engineering-driven**，**去PM化，扁平决策链：**无PM的摩擦意味着一个算法改进想法从产生到上线A/B测试，可压缩至数天完成。这种安排的逻辑是：当产品的核心竞争力是算法效果时，最懂算法的人最应该决定产品方向，而不是信息二手转手之后的PM。
> - **Revenue-Driven Autonomy驱动自下而上的主动性，工程师绩效与Revenue Impact直接挂钩**，且被期望自主识别收入机会并直接执行，不等待上级指令。
> - **将人才换血制度化**：当算法范式发生转变时，组织有能力同步完成自我更新。
> 两个支柱共同作用的结果，是AXON引擎在实时竞价场景中交付的持续领先的ROAS。这是广告主选择AppLovin、加大预算投入的直接理由。

## Key Bet：组织能力能复用来解决电商广告挑战

> AppLovin从游戏广告向电商广告的扩张，面临数据基础、信号处理和模型架构三个层面的根本性技术挑战：数据从游戏的简洁链路变为多源异构，转化信号从清晰的安装事件变为模糊的间接指标，模型需处理海量动态SKU与多模态素材。
> **电商广告的扩张阶段是一个"快速试错、逼近正确解"的过程。不知道什么模型架构、什么特征组合、什么信号处理方式对电商最有效，唯一的方法是大量实验、快速淘汰、复合迭代。**AppLovin组织机制是为最大化ML实验通量而设计的，以及现有调研证据验证了机制的有效性。
> - 决策权集中与工程师全栈闭环使关键技术选择（如将间接信号作为标签而非优化目标）得以快速落地，避免了大厂常见的跨团队论证周期。
> - 可复用的ML基础设施使20-30人的电商团队在数月内将北美ROAS效率提升至Meta的70-80%水平。
> - Temu、SHEIN、AliExpress等广告主的投放占比均呈上升趋势，初步验证了算法的实战效果。

## 投资决策思考

> 基于行业访谈和广告主调研，构建了AppLovin的估值模型和情景分析框架：
> - Base Case假设游戏广告增速从FY25的48%放缓至2028E的10%，电商广告以~56% CAGR（2025-2027）渐进式扩张，驱动总收入从FY25的$5.48B增长至2027E的$10.4B，EBITDA margin从82%扩张至83%，对应2027E EPS $22.06。以28x/20x的2026E/2027E P/E定价，Base Case指向$441-446，与当前股价（~$435）基本持平。
> - Upside Case假设电商self-serve全面开放后adoption加速（E-com YoY从70%提升至100%），总收入增至2027E的$11.5B、EPS $24.48，以30x/22x P/E定价指向$501-539。
> 投行中位目标价$735所隐含的46.5x高于当前市场隐含的27.5x 2026E P/E的原因是：AppLovin的收入增速（48%）约为Meta（17%）和Google（14%）的3倍、EBITDA margin（84%）约为两者的2倍、且没有Reality Labs或Other Bets等非广告业务的利润拖累，PEG ratio 0.75反而是三者中最低的。市场的核心分歧在于电商增长的速度和可持续性：看多方认为AXON的ROAS表现和self-serve portal将驱动广告主快速adoption，看空方担忧Meta数据壁垒、SEC调查以及规模扩大后ROAS能否维持。
> <u>基于组织机制的深度理解，个人判断电商adoption速度更可能接近Upside Case（E-com YoY 100%）而非Base Case（70%）——但不至于达到投行隐含的极端乐观情景</u>。在当前价位（~$435）可以少量建仓观察，目标价$500-540（+15-24% upside），若叠加Multiple修复可达$560-640（+29-47%）。**若股价因市场动荡回落至$400以下（对应25x 2026E P/E，几乎抹去电商期权价值），建议大幅加仓：该价位下即便电商增长弱于预期，仅游戏广告稳态增长即可支撑估值，而电商+CTV+新场景构成免费的上行期权。**
> 下一个关键验证节点为Q1 2026财报（预计5月发布），重点跟踪电商算法团队变化、电商self-serve上线后的广告主数量和spend增速。

## 1. AppLovin构建的数据闭环生态和算法飞轮

### 1.1 AppLovin的业务定位：聚焦In-App广告市场

| **数字广告细分** | **全球市场规模 (2026E)** | **主要玩家** | **全球 No.1 Player及份额** | **北美 No.1 Player及份额** | **AppLovin 渗透难度与现状** |
| --- | --- | --- | --- | --- | --- |
| **搜索广告 (Search)** | ~$185B | Google, Bing | **Google** (~80%+) | **Google** (~74%) | **不触达****。** 搜索基于“用户意图”，AppLovin暂无此类第一方数据 |
| **社交媒体 (Social)** | ~$155B | Meta (IG/FB), TikTok, Snap | **Meta** (~60%*) | **Meta** (~55%) | **不触达****。** 社交媒体是围墙花园。AppLovin难以渗透其内部流量，但AppLovin正在通过更优的转化率抢夺其广告主的**预算份额**。 |
| **零售媒体 (Retail Media)** | ~$180B | Amazon, Walmart, Instacart | **Amazon** (~36%) | **Amazon** (~75%) | **不触达。** 亚马逊等电商站内广告，闭环生态 |
| **其他应用内展示 (In-App)** | **~$190B** | AdMob, **AppLovin**, Unity, Mintegral | **AdMob** (~25%) | **AppLovin** (~22%**) | **主战场。** AppLovin在游戏领域已是统治者，正从游戏向电商和DTC广告扩张 |
| **联网电视 (CTV)** | ~$45B | YouTube TV, Hulu, Roku, Wurl | **YouTube** (~25%) | **Hulu/Disney** (~20%) | **刚进入。** <u>AppLovin通过收购</u><u>Wurl</u><u>切入</u>。目标是利用 AXON 算法让电视广告像移动广告一样“可测量、可转化” |

*注意：* 全球份额剔除中国市场数据；** 指在非 Google/Meta 的第三方应用流量中的份额。*

### 1.2 AppLovin怎么在广告巨头Google和Meta下崛起

**AppLovin抓住了Meta和Google不重视的长尾APP流量市场：**除了 Meta（Facebook/Instagram）和 Google（YouTube/搜索）这种超级 App，移动端有数以百万计的中小 App（特别是游戏）。广告主不可能一家一家去谈广告位。AppLovin 的 MAX 平台充当了“超级包租婆”，它把全球数万个 App 的广告位聚合在一起。你只需通过 AppLovin，就能瞬间触达全球海量的分散流量。

**                                                                               美国市场移动端APP流量结构**

| **排名** | **App名称** | **应用类别** | **DAU（million)** | **平均用户时长 (min)** | **流量占比（用户时长）** |
| --- | --- | --- | --- | --- | --- |
| 1 | YouTube（Google） | 长视频 / 流媒体 | 157 | 65 | 8.76% |
| 2 | Spotify | 音频流媒体 / 播客 | 53 | 140 | 6.37% |
| 3 | Netflix | 长视频流媒体 | 81 | 63 | 4.40% |
| 4 | TikTok | 短视频 / 社交娱乐 | 88 | 54 | 4.08% |
| 5 | Facebook（Meta） | 综合社交网络 | 135 | 33 | 3.83% |
| 6 | Instagram（Meta） | 视觉社交 / 短视频 | 105 | 33 | 2.98% |
| 7 | Snapchat | 即时通讯 / 社交 | 100 | 31 | 2.66% |
| 8 | WhatsApp（Meta） | 即时通讯 | 81 | 36 | 2.50% |
| 9 | X | 社交媒体 / 资讯 | 56 | 34 | 1.64% |
| 10 | Reddit | 社区论坛 / 图文 | 53 | 28 | 1.27% |
|  | **Top 10合计占比** |  |  |  | **38.49%** |
|  | **其他App** |  |  |  | **61.51%** |

*Source：根据DataReportal统计，截至2025年11月，美国整体互联网络用户规模约为3.20亿人*

**AppLovin 自己下场做游戏积累的数据，打造出最好的游戏广告模型**

- **第一方数据的积累：** Meta 和 Google 没有自己的重度游戏矩阵，但 AppLovin 在早期疯狂收购和成立了大量游戏工作室（如 Lion Studios）。在巅峰期，AppLovin 自己拥有几百款游戏，每天有数千万 DAU。
- **喂养 AI 的养料：** 这些自家的游戏成了 AppLovin 最完美的数据燃料。算法知道了用户玩什么关卡容易卡住、什么时候会冲动充值、对什么颜色的按钮最敏感。这些海量且合规的第一方数据，完成了 AXON 1.0 的“冷启动”。

**重要业务决策构建了集成的广告平台闭环数据生态，在苹果ATT之后优势凸显**

- **收购 MAX，这是最关键的一步（2018）**。当时行业还在用落后的“瀑布流”模式，MAX推出了透明的应用内实时竞价（In-App Bidding）。开发者发现用 MAX 赚得更多，纷纷接入。
- **外部市场助力和收购Adjust的关键决策（2021）：**苹果推出 ATT 隐私政策，重创了依赖跨App追踪的Meta。同一年，AppLovin 花了10 亿美金买下了归因测量平台 **Adjust**，加上自家的 MAX，瞬间在“无 IDFA 时代”完成了自洽的数据闭环。
- **数据和技术积累迎来爆发（2023-2026）：**利用前期积累的所有优势（控制了拍卖场、拥有了归因结果、沉淀了几年第一方数据），AppLovin 推出搭载最新 AI 强化学习的 AXON 2.0，带来收入增长从2023年开始进一步加速。**                                                       **

### 1.3 Applovin的垂直集成的闭环生态，建立了一个极高壁垒的数据护城河，这是驱动算法持续领先的关键

- **供给侧 (MAX):** MAX作为广告中介平台（Mediation）， 直接对接Publisher。开发者（比如《开心消消乐》的开发商）在自己的 App 里接入 MAX 的 SDK。MAX 帮开发者把App里的广告位拿出来，向全世界的广告网络（包括 AppDiscovery、Meta、Google 等）公开拍卖。
- **需求侧 (AppDiscovery):** AppDiscovery作为投放平台**，**直接对接广告主。广告主（比如某游戏公司、Shein）在这里开设账户，设定预算和目标（比如“我要买新用户，每个愿意出 10 美元”），然后 AppDiscovery 负责去全网买量。
- **监测侧 (Adjust):** Adjust作为归因与分析平台，对接广告主。广告主在自己的 App 里接入SDK，用来监测“用户下载 App 后到底干了什么”（比如是否注册、是否充值、买了什么商品）。
- **AXON 2.0 (底层 AI 算法大脑)：** 不直接对接外部客户，它是 AppLovin 内部的核心引擎。它接收来自 **MAX** 的海量环境数据（用户正在玩什么、点击频率），接收来自 **Adjust** 的转化结果数据（用户最后买没买）。综合这些数据后，AXON 指挥 **AppDiscovery** 去精准出价。

<u>这种“既当拍卖行、又当买家、还当公证员”的角色，让它在后隐私时代（IDFA 失效后）拥有比 Meta 更好的第一方数据反馈回路</u>。

![](https://xhs-doc.xhscdn.com/104004dg31t74nd5c560775kfg0?imageView2/2/w/1600)

AppLovin通过3个产品构建了一套其他广告平台无法复制的数据获取体系。MAX作为供给侧SSP，持续输入发布商流量和拍卖成交价信号；AppDiscovery作为需求侧DSP，回传广告主出价行为和竞对竞价水位；Adjust作为归因MMP，提供从广告曝光到用户购买的全链路转化数据。

**这三类型数据形成 "数据密度↑→算法模型精度↑→广告主的ROAS↑→广告主预算↑ 和 开发者收益↑ →数据密度↑" 的自强化飞轮。**<u>这一飞轮的起点，在于算法本身的精度提升：更好的算法意味着MAX能为开发者（Publisher）带来更高的eCPM，从而吸引更多开发者将自己的广告库存迁移至MAX，推动其在Mediation领域的市占率持续提升；与此同时，更高的ROAS也驱动广告主将更多预算集中投入AppDiscovery，进一步巩固其在Ad Network中的竞争地位。供给与需求两端的双重扩张，带来了更大体量的行为数据和转化信号，反哺AXON迭代出更精准的算法——形成一个难以从外部打破的正反馈闭环</u>。

三类数据的密度、实时性和覆盖广度直接决定了模型的预测精度上限，直接影响投放的ROAS。 这也是为什么AppLovin在2021年花费14亿美元收购Adjust（获取转化链路数据）、同年收购MoPub（扩大供给侧数据覆盖）——MoPub的收购使AppLovin可触达的广告库存规模扩大逾十倍，接入了数以万计的非游戏应用及其7亿日活用户，这是训练更强大AXON所需的关键数据燃料。 **这套数据基础设施需要数年时间积累，是护城河中时间壁垒最高的部分。**

                                                                           **  AppLovin的数据和算法飞轮**

![](https://xhs-doc.xhscdn.com/104004dg31tmitegtmo020tbhes?imageView2/2/w/1600)

### 1.4 算法带来的广告效果提升驱动广告主持续扩大在AppLovin的广告预算，以及开发者迁移到MAX平台

**广告主端**

调研的多家游戏广告主（米哈游、三七互娱等）反馈，<u>AppLovin 的ROAS并不弱于Meta和Google，其核心优势在于长效回收周期的优化策略。 Google 和 Meta 往往侧重于较短的优化窗口（如 D0、D7），而 AppLovin 在两三年前就推出了 D28（转化窗口的优化功能）。</u>

- 以D0/D7 ROAS评估，AppLovin 的初期ROAS可能略低；但由于D28模型专门针对高留存、长线高价值用户进行优化，在 D7 到 D28 的周期内，AppLovin 用户的价值增长呈现指数级优势。

**AppLovin AXON 算法优势带来ROAS的不断提升，导致广告主预算份额往AppLovin迁移：**目前全球广告网络市场高度集中度在不断提升，AppLvoin过去几年的高速增长主要源于蚕食了包括 Meta、Google，以及Unity 等中小玩家的广告主预算份额。

> *"AppLovin 拥有MAX 聚合平台。游戏公司既是广告主也是开发者，通过接入 MAX 的 SDK，AppLovin 能够掌握用户在游戏内深度的 Runtime 运行数据（如下载、激活、何时暂停、何时充值、完成什么任务等长线行为）。广告主考核 Day 7 或 Day 28的ROAS时，AppLovin 能够基于长线行为标签，精准捕捉具有“高粘性、高付费意愿、高频次”属性的用户。游戏客户在追求长期LTV时，AppLovin 的效果表现更优，其预算占比呈上升趋势。"      **——  中国游戏公司出海代理商**华扬联众专家*    *                *

> *”AppLovin的广告预算占比从早期的3-5%上升到2025年的7%，预计2027年占比达到10%。主要由于AXON 2.0算法升级，匹配更精准，30天 ROAS 已从之前的 1.8 显著跃升至 2.1。“  ——  米哈游广告投放总监*

**开发者端**

<u>2021/2022 年起，大量游戏publisher以及部分非游戏publisher开始将主要广告中介平台从AdMob 迁移至 MAX</u>。**促成这一趋势的驱动力是Max变现能力高于AdMob**。2024-2025 年间，全球范围内开发者从 AdMob 迁移至 MAX 的速度明显加快。 访谈的AppLovin专家提到，<u>2026年1-2 月，全球约有2179家发行商完成了从 AdMob 到 MAX 的全量迁移。同期从 MAX 流向 AdMob 的非游戏发行商约195家</u>。

- AdMob仍主要依赖“传统瀑布流（Waterfall）+ 有限实时竞价”模式。除Google自身资源外，对第三方广告源的出价次数和效率较低。
- A/B 测试通常显示 MAX 能带来 10%-15%（甚至高达 30%）的整体收入提升。

<u>Publisher的选择完全取决于商业回报（即算法带来的更高eCPM），不存在绝对的“平台忠诚度”</u>。即使存在排他性锁定合同，竞争对手往往会通过补贴方式来打破壁垒。平台迁移不存在直接的资金成本，仅涉及技术团队整合新 SDK 和网络配置的时间与资源。

> *"I had an Italian client that had a lot of utility apps and they were on AdMob and they tested on one MAX. They saw higher results and they decided to move the entire portfolio."  ——  AppLovin, Manager of Business Development*

## 2. 复盘AppLovin的业务技术升级和组织演变：组织和算法/业务同频迭代

> **复盘AppLovin从成立以来的重大业务和技术升级发现：AppLovin的重大组织变化时点都是业务和算法的迭代关键点，组织随算法的需求迭代。**
> 2022年以前，公司的核心工程组织仍以传统AdTech方式运行——Axon 1.0建立在监督学习和强化学习的传统算法模型之上，工程团队也多为公司创立以来的"老人"。然而，外部冲击的叠加彻底打破了这一状态：其一，2021年苹果推行IDFA政策（ATT），切断了移动广告的关键数据源，导致AppLovin的老数据集几近"失效"；其二，Meta和Google早已在神经网络与Transformer架构上深耕多年，AppLovin的传统建模能力与竞争对手之间出现了明显代差。CTO Vasil主导了2022-23年间一次彻底的组织重建——大规模替换无法适应新技术栈的老员工，从Meta、Google等公司以及顶尖院校引入新鲜血液，全力构建以深度神经网络和推荐系统为核心的Axon 2.0架构。
> 2024年，当自有游戏数据对算法价值不大时，砍掉自有游戏团队，精简组织，人员数量减少55%，全面专注Software Platform。

| **时间节点** | **关键业务与技术升级** | **Mediation 市占率 (供给端/库存控制)** | **Ad Network 市占率 (需求端/买量预算份额)** | **竞争力的提升** |
| --- | --- | --- | --- | --- |
| **2012-17年** | 纯 Ad Network，算法积累期 | **0%**<br>完全依赖第三方瀑布流 | **< 5%**<br>属于中腰部买量渠道，远落后于 Google、Meta 及当时的 IronSource | 处于被动地位，无法获取全局竞价数据，算法优化受限于自身极其有限的转化样本 |
| **2018-21年** | **2018-2020**<br>收购 MAX，推出应用内竞价，收购 MZ 开发AXON 1.0 | **10% - 20%**<br>通过 In-App Bidding 开始抢夺供给侧话语权 | **10% - 15%**<br>跻身头部买量渠道（“三足鼎立”：AppLovin, IronSource, Unity） | 首次打破规则。MAX 带来的全局视野，为随后诞生的 AXON 1.0 提供了海量且实时的多维度训练数据 |
|  | **2021-2022**<br>ATT 落地；收购 MoPub、Adjust，整合生态 | **~45%**<br>吸收 MoPub 盘子，与 Unity 形成绝对双寡头 | **20% - 30%**<br>大幅承接 Meta 因苹果 ATT 政策流失的精准定向预算 | 闭环形成。在竞争对手因隐私政策“致盲”时，AppLovin 依靠 MAX 的上下文数据和 Adjust 的归因数据，实现了逆势超车 |
| **2023 至今** | 推出 **AXON 2.0**，全面拥抱 AI 大模型预测 | **50%+ (近乎垄断)**<br>大幅甩开合并后的 Unity (U+IS) | **30%+ (应用内买量霸主)**<br>成为移动游戏甚至部分泛应用领域 ROAS最高的第一大买量渠道 | AXON 2.0 极大提升了精准匹配率和广告主 ROAS，不仅通吃中重度游戏预算，并开始切入电商等非游戏广阔市场 |

### 2.1 2012-17年：早期创立与预测推荐引擎

AppLovin 成立于 2012 年。彼时移动广告市场充斥着简单的展示网络，AppLovin从第一天起就定位为效果导向的推荐引擎（Recommendation Engine）。早期算法主要是基于协同过滤和基础机器学习的预测模型。它通过分析用户的设备信息、已安装的应用以及历史点击行为，来预测“这个用户最有可能下载哪款新游戏”。早期的算法依赖于相对静态的历史数据积累。随着移动生态的爆炸式增长，数据处理的延迟和维度的单一性开始成为瓶颈。

### 2.2 2018-21年：算法从传统Ad-tech转向ML驱动，通过收购构建出闭环数据版图

**2018年收购 MAX，拥有广告中介平台（Mediation Platform），获得用户一手数据**

- 在 MAX 之前，移动App变现主要采用“传统瀑布流（Waterfall）”模式。开发者必须根据历史 eCPM手动对各个广告网络（包括 AppLovin）进行排序。这种方式极其低效，Ad Network只能“排队”等待展示机会，不仅开发者收益受损，AppLovin 也无法看到全局的广告库存，导致其算法缺乏足够的数据喂养。
- MAX 首创并推广了应用内竞价（In-App Bidding）。它打破了排队模式，让所有广告网络在同一时间、对同一次展示机会进行实时竞价。 MAX 让 AppLovin 获得了“平等的牌桌”。AppLovin 自家的广告网络（AppDiscovery）能够看到平台上所有的展示机会。这极大地丰富了 AppLovin 算法能够摄取的数据量，为其后续算法的爆发奠定了数据基础。

**2020年收购 Machine Zone，转型成ML驱动的Ad-tech公司**

- 在此之前，AppLovin 主要是传统的 AdTech 平台，算法虽然有效，但在处理超大规模实时并发数据（毫秒级反馈）时面临技术天花板。收购后，引入了 Machine Zone 的机器学习团队，开始将产品向“ML 驱动的 AdTech”转型。
- MZ 团队的加入，直接促成了 AppLovin 核心机器学习引擎 **AXON 1.0 的诞生**。
  - MZ 将其强大的实时并发数据流处理技术与 AppLovin 的推荐引擎融合。算法从“基于静态批处理分析”进化为“基于超大规模图网络和实时数据的深度学习”。AXON 能够以毫秒级的速度，在数十亿的事件中精准匹配广告主和用户，极大地提升了 ROI 和转化率。这也标志着 AppLovin 从一家广告网络公司，正式蜕变为一家纯粹的 AI 技术驱动公司。
  - 此时使用的是 **Axon 1.0**，基于传统的机器学习方法（监督学习、强化学习），依赖人工特征工程（约 2 万+特征）。

**2021年收购 Adjust，构建数据闭环，具备归因分析：**2021年4月以约10亿美元收购Adjust

- AppLovin作为广告平台，需要知道广告投放的效果（用户是否下载、是否付费）。在此之前，AppLovin 必须依赖第三方的 MMP（移动测量合作伙伴，如 AppsFlyer、Branch 或 Adjust）来回传归因数据。这意味着数据链路有一部分掌握在别人手中。
- 这次收购恰逢苹果推出 ATT 政策（限制 IDFA 追踪）的前夕。整个行业的精准定向能力遭到毁灭性打击。Adjust 补齐了AppLovin生态的最后一块拼图——**归因与分析**。它让 AppLovin 拥有了强大的第一方分析能力。在行业内其他广告网络因为苹果新规失去方向时，AppLovin 能够通过 Adjust 提供的高级分析工具、聚合数据模型以及转化值管理，在保护隐私的前提下继续优化其AXON算法，从而在后 IDFA 时代实现了逆势增长。

**2021年收购 MoPub，确立供给侧绝对霸主：**2021年10月宣布从 Twitter 手中以10.5亿美元收购，2022年1月正式完成整合。

- MoPub 曾是 MAX 在市场上的最大竞争对手。通过收购并强制 MoPub 上的开发者迁移到 MAX 平台，AppLovin 完成了移动广告变现领域的“大一统”。 这次收购让 MAX 的市场份额呈垄断之势。更多的开发者意味着更多的广告展示机会（海量供给） -> 这些数据喂给升级后的 AXON 算法 -> AXON 投放更加精准，广告主获得更高 ROI（需求增加） -> 开发者在 MAX 上赚到更多钱（eCPM 提高） -> 吸引更多开发者加入。

### **2.3 2022-23年：算法技术跃迁，组织大换血，招细分技术专才，面临人才困境时Leader下场自己干**

**苹果IDFA政策切断数据源，算法技术与竞争对手出现代差：**苹果推行IDFA隐私新政，导致旧的数据获取方式失效，AppLovin的数据一度变得“过时”，旧模型难以精准预测安装量。之前为了解决 IDFA 后的归因和数据断层问题，收购 MMP 公司 Adjust，并开发 AppDiscovery。虽然有了新数据源，但此时模型仍停留在旧架构上，整合需要时间，导致 2022 年期间虽然有点击（Hits）但缺乏安装（Installs）转化，效率未达预期。

> *"Google and Meta were deeply driven by neural networks and transformer models and we were on very much the traditional modeling techniques... And there were major gaps in terms of how our competitors were doing training and modeling of some of the models"   —— AppLovin, ML Engineer *

**为了推动算法升级，组织大换血**：<u>在市场低迷背景下，CTO Basil Shukin 推动了根本性的技术栈重构。解雇了大量依赖传统工具的老员工（包括 ML、运营、发布管理团队）。大量招聘来自 </u><u>Meta </u><u>和 </u><u>Google</u><u> 的工程师，以及高校毕业生。新团队彻底抛弃传统ML 模型，全面转向</u><u>深度神经网络 (Deep Neural Networks)</u><u> 和 </u><u>Transformer</u><u> 架构</u>。利用新架构处理更复杂的非结构化数据（上下文、创意元数据），而不仅仅是简单的用户 ID。

> "* In 2022, the market had a very big dump and a lot of companies really pulled back. The company kind of really started reorganizing and rebuilding some of the entire engineering org. And t***hey let go almost all of the old people that etc. at the company and they brought in a completely knew set of people, from Meta and Google and they hired a lot more new graduates*** as  from all the top universities."*   *—— AppLovin, ML Engineer *

**专才优先，而非通才**：在AXON 2 转型关键期，AppLovin 的招聘理念与Google等大厂存在根本性差异。 <u>Google和 Palantir 遵循的是 " 招聘优秀的通才型工程师，让他们在入职后学习特定领域知识 " 的逻辑 —— 入职时不预设技术方向，以计算机科学基础能力和潜力为核心选拔维度。</u>**AppLovin聚焦于招聘有行业经验和特定领域知识的资深工程师， 明确要求候选人在进入特定团队之前就已深度掌握该团队的技术栈。 **

> *"以 C++ 开发为例， AppLovin 的候选人必须在面试时就能使用 C++ 作答，并能深入讲解 C++ 从 2015 到 2022 年的语言演变、多线程特性等细节 —— 这类知识只有在长期实践 C++ 的工程师身上才能找到。 如果你不熟悉你所面试的团队的技术栈和底层基础技术，你被录用的概率是零。 这一标准显著提高了面试通过的门槛，同时也压缩了招聘池的规模。" —— AppLovin Hiring Manager*

**当时的人才困境：**2023年之前AppLovin不算是一家“有前景”的创业公司。一方面规模不大，其次当时普遍认为Google和Meta已经做得非常成熟了，Ad-tech行业机会小，所以难招到最顶级的人才。当时AppLovin尝试过很多方法，都不是特别有效，后来就认清了现实，那时候就是利用团队现有的资源，先把东西做出来。

> *"AppLovin从上到下的技术Leader都非常hands-on，这也是很多大厂没有的优势，当想做一个新东西却找不到合适的人去做时，技术Leader是可以亲自下场写代码去完成这件事。" —— AppLovin Chief Product and Engineer Officer 葛小川*

### **2.4 2024年后，砍掉自营游戏（员工数减少一半），****组织再次精简；**转向内部快速培养新人而非外部空降

AppLovin最初收购游戏工作室，是为了训练其机器学习模型，服务于广告优化。随着外部开发者涌入MAX平台，第三方数据的规模和多样性开始超过自营游戏能提供的，飞轮不再依赖自家游戏就能转起来，<u>创始人Adam在2024年出售了重度人力的游戏业务，将核心人员全部集中在高毛利的软件平台（Software Platform）上。员工人数从2023年的1,745 人暴降近 55%至2024年的788 人；但同年总营收却涨 43%（达 47.1亿美元）</u>。

> *”Seven years ago, we began acquiring gaming studiosto help train our earliest machine learning models, an invaluable step in shaping the Al that underpins our AXON platform. However, we've never been a game developer at heart.“                                             —— AppLovin CEO Adam Foroughi *

**AppLovin在2024年之后招聘重心彻底转向新人**：<u>在AXON 2.0已经建立领先技术优势之后，AppLovin发现</u><u>经验的价值</u><u>在AppLovin的目前的业务模式下</u><u>被高估，</u><u>外部招聘的高管往往带有前公司的思维定势，并且难以适应AppLovin的文化。</u><u>随后</u><u>彻底放弃对业界资深候选人的关注，转向大幅招聘大学刚毕业的或者毕业之后在业界工作2年以内的年轻人，并在内部快速培养提拔，内部培养的管理者效率更高</u>。

- AppLovin BD团队的Entry-level员工（如BD业务的分析师）画像是24-25岁的大学毕业生，学习能力强、适应速度快，极度渴望成功（Hungry）、抗压能力强、具备企业家精神。

> *"如果你管理一家公司，想解决一个问题，而这个问题已经被其他公司解决了，你潜意识里最直接的方法可能就是从那个擅长的公司挖一个Director过来，让他重新组建团队，觉得问题就能解决了。但如果你仔细去历史中寻找案例，你会发现大部分这样的尝试其实都是失败的。但我认为对于真正的优秀人才，学习能力是最重要的，过去所有的经验并不代表一个人的学习能力，它只代表这个人已有的知识。*
> *你招一个人过来，他能够快速成长，能够figure out一些他以前不知道的事情，这种能力的价值，要远远高于脑子里已经沉淀好的已有知识的价值。我们这边做事情的方式是希望打破常规，很多时候已有的知识反倒会成为一种阻碍，所以从2024年开始，我们的招聘哲学就转变了。"*
> *—— AppLovin Chief Product and Engineering Officer 葛小川 (Giovanni)*

> *"Rewarding and promoting the people within the company at higher positions instead of recruiting those higher positions from the get-go. Regarding the recruiting process, they are looking for entry levels, freshly out of universities, at 24 or 25, who are eager, motivated and can learn quick and can adapt very quick. "   —— AppLovin, Manager of Business Development*

## 3. 以Pod为单元、极致精简的Engineering-driven型组织

### 3.1  极致精简的组织原则 + 技术决策高度集中

**极致精简是核心组织原则。** 创始人Adam把精简视为战略选择——他认为增加人手会稀释人才密度、阻碍沟通、抑制适应性。AppLovin极力避免用“堆人头”来换取营收增长，Adam认为盲目扩张 headcount会直接稀释团队的人才密度。

> *"I constantly get asked, 'You're an advertising business. You have tons of revenue opportunity in front of you to grow. Why don't you go hire a bunch of people?' And the simple answer to that for me is I've got a lot of great people. The second I hire a bunch of people, when it becomes bunches or you think about hiring quotas, you dilute the intelligence around you."*
> * —— Adam Foroughi, Goldman Sachs Builders and Innovators Summit, October 2025*
> *"We believe our culture is unique. ***By staying lean and retaining key contributors, we have built an exceptionally high-performing team of subject matter experts capable of innovating faster and more effectively than those at other companies***."*  *— Adam Foroughi, Q1-2024 Earnings Call*

维持“10人初创团队”的建设者环境 (The Builder's Environment)：在业务规模持续扩张过程中，Adam思考的是如何不让繁文缛节毁掉公司的创新能力。

> *"Why does companies become less efficient when they scale? Why is there more process when companies scale? So we wanted to build a culture that inspired that same entrepreneurial spirit as it scaled, and that is predicated on building a team of doers, getting process out of their way and allowing them to execute as if the company was still 10 people."*
> *—— Adam Foroughi, Nasdaq London Investor Conference, December 2024*

**技术决策权高度集中于CTO和CPEO，而非分散在多个VP和委员会中：**AppLovin采用双工程领导结构驱动算法能力和基础设施能力同步演进。CTO Basil管理分布式系统、训练平台、数据pipeline和serving基础设施，在2022-2023年主导了底层技术栈的全面重建和核心ML团队的人员大换血。 Giovanni（Chief Product and Engineering Officer）负责模型框架、排序算法、创意智能和产品路线图，是AXON 2.0的核心贡献者，从IC起步一路晋升。两人分别向CEO汇报，在广告系统上共担责任，确保"做什么模型"和"用什么基础设施训练和部署"之间没有组织断裂。在<u>其他科技大厂，CPEO Giovanni一个人覆盖的范围可能需要10-15个VP各自负责，每个架构决策都需要跨VP协调和妥协。AppLovin因为只有一个核心产品、决策权集中在极少数人手中，架构的统一性可以被维护，算法需求和基础设施供给之间没有摩擦</u>。

                                                                            **AppLovin的工程团队架构**

![](https://xhs-doc.xhscdn.com/104004dg31u260ehgh80e5sgphg?imageView2/2/w/1600)

![](https://xhs-doc.xhscdn.com/104004dg31u261m3p0s08eb2fi0?imageView2/2/w/1600)

*注：以上图片根据专家访谈内容整理*

### 3.2  ”Pod“制小团队 x Full-stack能力要求 —> 极快的算法迭代速度

**AppLovin核心工程团队~150人，分布在~20个功能性Pod中。每个Pod的典型配置是：1名VP级技术负责人、1名Tech Lead、2-4名工程师，加上若干数据科学家，几乎不设PM岗位**。<u>每个Pod独立负责明确定义的技术子系统（Subsystem）或业务目标，对其负责的系统拥有端到端的所有权（End-to-End Ownership），每个Pod聚焦于一个核心指标（One Metric），围绕该指标制定专属路线图，开展快速实验与迭代。</u>

- **最小依赖原则。** 如果一个Pod对其他团队存在过多依赖，则被视为功能边界设计存在缺陷，需要重新划分。这一原则从设计层面消除了跨团队协调的摩擦，使每个Pod能够以最快速度推进迭代。

**全栈（Full-stack）能力减少配合协调时间：** 当一个Pod只有6-8人，却要端对端负责一个子系统时，每个工程师必然需要掌握特征工程、建模、业务逻辑等多个层面。AppLovin内部盛行"Full-Stack"文化——每个工程师被要求独立掌握"整个技术栈"（Feature Engineering、Modeling、Business Side），这使得个体之间的依赖降至最低。**Pod制设计的精妙之处在于它适配了ML领域的实验逻辑（大量A/B test找到最优算法），这种设计可以实现并行实验密度最大化。** **Pod制下，单个工程师就可以独立推进一个完整实验，而无需等待其他团队的配合，时间效率最高**。而绝大多数科技公司，检索、重排和排序由不同团队负责，且使用不同的代码类，想做任何横向优化都会被卡住。任何改动都需要协调对齐，实验密度受到严重压制。

> *“同一个模型可能同时有10名工程师在独立训练10个不同版本，其中有人做A/B测试，有人做参数校准，有人做性能验证——这10组实验是并行推进的，而不是串行排队的。”  —— AppLovin, ML Engineer *

广告ML模型的优化不像传统软件那样有明确的对错——无法在写代码阶段就确定一个改动会提升还是降低业务指标。模型的效果只有在真实数据和真实流量上测试后才能验证。**ML的"实验速度"等于"算法进化速度"**。

![](https://xhs-doc.xhscdn.com/104004dg31u0vgmjogs019a69ig?imageView2/2/w/1600)

**AppLovin模式**：

- 同一个Pod内的4位工程师，每人拥有从假设到上线的完整链路，在同一套共享ML基础设施（3个主类、PyTorch、FeatureStore、GPU集群）上各自独立推进不同的ML实验。比如，工程师A的embedding改进已进入A/B测试阶段，B的模型校准正在训练，C的强化学习探索在做原型，D在构思新特征实验
- 四条泳道并行不阻塞，且任何一条泳道的成果（因为底层只有3个代码主类）都能立即传播到数十个模型

**传统大厂模式**：

- 同样的ML迭代被拆成研究→训练→部署→评估四个独立团队，每次交接都产生排队等待和上下文切换成本
- 四个团队各自维护不同的代码库和模型类，一个团队的改进无法自动惠及其他团队

                                                      **AppLovin vs. Meta//Linkedin的算法团队的执行效率对比**

| **维度** | **AppLovin** | **Meta/Linkedin** |
| --- | --- | --- |
| 单人并行A/B测试 | >1个/人 | 整队~1个 |
| 想法到上线 | 约1周 | 数月至1年 |
| 基础设施建设 | 几周 | 数月至1年 |
| 跨团队协调 | 无需（全栈拥有） | 大量协调成本 |

*注：以上基于在Meta和AppLovin工程师的访谈*

### 3.3 Engineering-driven，去PM化的决策机制

在绝大多数互联网公司，产品方向由PM（产品经理）主导，工程师是需求的执行者。AppLovin完全颠覆了这一逻辑，PM在AppLovin的职责范围被严格限定在内部工具、内部报表和流程优化等领域。任何直接影响广告主、发行商或用户体验的产品功能，均由CTO Basil、CPEO Giovanni等工程领导层直接与各VP团队协作决策，完全绕过PM环节。

这种安排的逻辑是：**当产品的核心竞争力是算法效果时，最懂算法的人最应该决定产品方向，而不是信息二手转手之后的PM。** CEO Adam本人是技术出身，其核心精力集中于业务增长、产品战略与顶层市场判断；CTO Vasil是技术决策的最终权威，直接参与各VP团队的日常站会，对技术进展保持一线感知。整个决策链路是：市场信号 → Adam/Vasil的直接判断 → 传达给工程VP → Pod执行，中间几乎没有缓冲层。这种"识别市场信号 → 工程快速响应 → 直接上线验证"的链路，正是AppLovin在算法迭代速度上能够甩开大公司的核心原因之一。

- 比如，访谈专家提到2021年NFT市场出现明显机会时，Adam直接组建了一个小型内部工作组，在两个月内从零上线了一个区块链NFT广告展示平台，全程无传统PM介入。

对应地工程师被明确要求具备商业理解能力（Business Acumen）——要能理解广告技术的商业逻辑、客户价值主张和市场动态。当工程师本身具备足够的业务判断力时，PM作为信息中介的必要性自然消失，决策链条因此大幅缩短。

> *”Best thing about this place? Zero red tape. No bloated middle management. If you have an idea that can boost ROAS, you code it, run an A/B test, and if the metrics are green, it ships to production. You don't need 5 PMs to sign off on a doc."  —— AppLovin, ML Engineer *

### 3.4 以Revenue Impact为核心指标考核Engineer团队

AppLovin不是以代码数量或者质量考核工程师，**绩效的核心指标是Revenue Impact。**AppLovin极其看重数据验证和实验驱动，不同岗位的工程师有不同且高度量化的考核标准：

- 机器学习 (ML) 工程师： 考核模型带来的业务提升（Model Lift）以及 ROAS（广告支出回报率）的增长转化。
- 基础设施 (Infra) 工程师： 考核系统的低延迟、高吞吐量以及成本效率。
- 广告投放 (Ads/Serving) 工程师： 考核竞价拍卖（Auction）的吞吐量速度、广告填充率以及新广告主的接入效率。
- SDK 工程师： 考核系统集成的性能、可靠性（无异常中断）以及真实环境下的到达率。

比如，如果工程师只是在一个小角落做优化，只影响系统的一个节点，那么其收入贡献自然有限；但如果某个改动能够触达10个不同的系统模块，产生的收入归因就会成倍放大。这种激励设计天然驱使工程师追求更高影响半径的系统性改进，而不是局部修补。

Revenue Impact是一种自主驱动机制（Revenue-Driven Autonomy）：工程师被期望自己思考如何创造更多收入、并直接执行这些想法，而不是等待自上而下的指令。这意味着实验的发起权在个人而非管理层——工程师不是被分配"去优化这个模型"，而是自己识别收入机会后主动立项、设计实验、验证效果。这解决了科技大厂常见的两个问题：一是目标分裂（研究员追求学术指标、工程师追求技术指标），二是等待瓶颈（好想法被卡在PM排期或管理层审批中）。

### 3.5 通过高薪吸引和快速验证和淘汰，维持高人才密度

A**ppLovin维持高人才密度的机制：通过高薪吸引顶尖人才→极短的观察窗口→快速淘汰不适配者**。**第一，高薪吸引。** 公司以远超广告技术行业水平的薪酬（Staff级可达$62万以上）锁定顶尖人才，股权在薪酬包中占比极高，使得高薪成为员工在高压环境下仍愿加入的首要杠杆。**第二，”No Ramp-up“。** 公司不提供系统性入职培训，新人从第一天起即被期望独立找到方向并产出成果，能否留下几乎完全取决于能否在极短时间内自证价值。**第三，快速淘汰低绩效。** AppLovin对绩效不达标的容忍度极低，一旦发现不适合，会相对迅速地做出处理，通常会提供相对丰厚的离职补偿。 这种淘汰机制在外部观察者看来可能显得冷血，但在公司内部是作为维持团队高质量密度的必要手段被接受的。

> *"Diluting a team with too many average hires slows down the best performers and creates unnecessary bureaucracy."
> — Adam Foroughi, Goldman Sachs Builders and Innovators Summit *

> *"对于新员工，公司期望其在入职后两个月内就能交付完全面向客户的功能，没有传统意义上的"ramp-up"期" —— AppLovin, ML Engineer *

**把薪酬提到硅谷最高水平，同时对应高强度工作**：在AI领域之外，AppLovin是硅谷薪酬最高的公司，薪酬高于Meta和Google的同业务岗位。有BD员工在访谈中提到在AppLovin的每天工作时长12-14小时，周末每天工作3-5小时。

> *“There is zero work-life balance with a constant carrot and stick. You will be messaged on nights, weekends, and holidays... It's basically Amazon but without the brand name."*   *——  Taro内部员工匿名评论*

### 3.6 Underdog Mindset，反会议、反流程文化（Anti-Meeting, Anti-Process）

**AppLovin 的组织文化可以理解为一种刻意维持的"受控混乱"：用极少的会议和流程换取决策速度，用频繁的方向调整换取市场适应性，用 Underdog心态抵抗大公司病。**

AppLovin内部依赖Slack沟通解决绝大多数问题，会议被视为生产力的天敌。但也有员工提到这种反会议文化导致了团队间沟通透明度的严重不足。

> *"AppLovin relies heavily on Slack to resolve issues, minimizing the need for synchronous meetings. Meetings should always have a clear agenda and purpose; if a topic can be resolved over chat, it should be."
> — Adam Foroughi, 20VC Podcast with Harry Stebbings*
> *"They hate time-wasting group meetings. This was one of my favorite aspects of AppLovin culture. Things tend to move fast. Stuff gets done."  — Glassdoor,  前员工评价*

创始人Adam认为CEO的核心工作是清除拖慢优秀工程师的"臃肿和流程"。访谈的HR提到，Adam之前招过一个Chief People Officer ，不到一年便离职了，Adam直接接管了HR相关工作。 AppLovin对HR官僚流程零容忍，以及对 "HR拖慢业务节奏 " 的强烈反感。

> *"A CEO's job in a growing company is to remove the 'bloat' and 'process' that slows down talented engineers."
> — Adam Foroughi, Nasdaq London Investor Conference*

Underdog Mindset 和Adam的成长和创业经历相关，AppLovin的发展中经历了多次"差点死掉"的故事：早年无法获得风投、仅靠$4M 天使资金起步，2022年市值从高点暴跌90%至$30亿，在 Apple 隐私政策变化的冲击下被广泛认为将成为又一个广告技术行业的殉葬品。Adam将这种濒死经历内化为组织基因，他在公开的访谈中表示自己从不觉得是房间里最聪明的人，最大的优势就是比别人更拼；他警告一旦觉得舒服了就是在滑向自满。

> *"It's a story about how culture and organizational design allowed a scrappy tech company to overcome enormous odds, survive multiple potentially fatal blows, and ultimately build one of the most impressive companies we've seen."
> — WCM Investment Management*

## 4. Key Bet：组织能力能复用来解决增量电商广告业务的难题

### 4.1从游戏广告算法模型到电商广告算法模型的技术挑战和路线

**模型优化目标变了：不预测意图，预测经济价值**

- **电商模型不试图理解“用户想要什么”（Intent）**，**预测“什么能带来最大经济价值”（Economic Value）**：Axon 的目标是预测哪种广告素材（Creative）组合能最大化广告主的经济回报（ROAS/CPA）。
- **关注宏观波动（Volatility）与业务动态**：模型会捕捉由于地缘政治、大型活动（如疫情、战争等）导致的市场波动。帮助电商客户理解在特定情景下（如库存积压、价格调整、突发事件），如何调整广告策略以保持业务稳定或增长。不依赖单一用户的长期画像，而是通过大量的实时实验（Real-time Experimentation）和归因（Attribution）数据来驱动决策。

> *“We don’t want to predict what the user wants. We want to predict what ad creative combination can drive maximum economic value — what campaigns can this business run using Axon to drive revenue in scenarios of uncertainty and challenge” —— AppLovin, ML Engineer *

**数据基础的重构**

- 游戏数据：链条简洁集中：点击→安装→付费，事件格式统一、归因清晰，模型用简单的用户嵌入和事件信号就能完成训练。
- 电商数据："极度分散且难以整合"。数据来源包括曝光、素材元数据、转化率、用户互动、地理上下文等，分散在不同渠道、不同时间节点、不同格式中，没有一条清晰主线。从ML角度看，特征工程的复杂度指数级上升——模型输入从标准化的事件序列，变成需要对齐、清洗、融合的多源异构数据。

*AppLovin在2021年苹果IDFA隐私政策变更后就经历过数据危机，先后通过收购Adjust、开发AppDiscovery、整合MAX和MoPub来补充数据来源。电商场景将这个挑战再次放大——不仅要解决"有没有数据"，还要解决"数据如何统一表达"。*

**信号处理的转变：*** ***这是一个在ML层面关键的设计选择。**

- 游戏中，"是否安装了App"是一个干净的学习信号，模型直接以此为优化目标训练。电商中，信号含义更模糊且间接——一次曝光未必带来转化，一次点击也不代表购买意愿。如果直接拿这些间接信号当优化目标，模型会被噪音干扰，训练效果反而变差。
- <u>因此AppLovin选择将曝光（Impression）、素材元数据（Creative Metadata）、转化率（Conversion Rate）、用户参与度（Engagement）、地理/非地理上下文作为标签（Label）而非学习信号处理信号作为输入特征附加到模型中</u>，而非作为损失函数的优化目标，告诉模型："这些信息要纳入考量，但不要直接对着它们优化。"

> *"We treat each of these signals as a label rather than a learning signal."  —— AppLovin, ML Engineer *

**模型架构的全面升级：**数据收集到了、信号处理方式定了，模型要能真正"理解"这些数据才有用，这就是"表征"（AI把原始信息转化为它能计算和比较的内部语言）

- **产品嵌入（Product Embeddings）**：电商建模"最重要的组件"。游戏产品端简单（几万款游戏，品类有限，特征固定），电商涉及海量SKU，每个商品有独特属性组合且随时间动态变化。模型需要为每个商品生成高维向量表示，并持续更新。
- **多模态编码器（Multi-modal Encoders）**：游戏素材相对标准化，电商广告涉及图片、视频、文案等多种模态。模型需要同时"看懂"不同类型的内容，判断哪种素材组合对特定受众最有效。
- **向量架构（Vector Architecture）：**产品嵌入解决了"理解商品"，多模态编码器解决了"理解素材"，而向量架构是将两者与用户连接起来的桥梁，将用户、商品、广告素材全部映射到同一个高维向量空间中，然后通过向量之间的距离或相似度来实时计算最优匹配——哪个用户、在什么场景下、看到哪个商品的哪种素材，最有可能产生转化。电商场景的特殊性在于匹配维度更多（用户×商品×素材×上下文），且需要在毫秒级的竞价窗口内完成计算
- 此外，这套架构还需要具备**跨垂直领域可扩展性**——游戏就是一个品类，电商涵盖服装、电子、美妆等无数品类，每个品类的用户行为和决策逻辑都不同。模型不能为每个品类单独训练，需要构建可灵活适配不同D2C品牌的统一框架。专家提到公司通过大量A/B测试和快速迭代来实现这种适配。

![](https://xhs-doc.xhscdn.com/104004dg31u3q8gaahs02n82gf0?imageView2/2/w/1600)

### 4.2 组织能力怎么复用来解决电商广告挑战？

**从游戏广告到电商广告，不变的是底层的ML竞价逻辑，变化的是数据、信号和表征的复杂度。** 访谈的Technical Staff和Research Scientist都指出，两个场景共享同一套技术骨架：多阶段架构（检索→粗排→精排）完全通用，探索策略直接可迁移，校准技术跨领域适用，竞价策略和Market Guide Model的核心逻辑相同。变化的部分如上述4.1讨论的内容。

**电商广告的扩张阶段是一个"快速试错、逼近正确解"的过程。不知道什么模型架构、什么特征组合、什么信号处理方式对电商最有效，唯一的方法是大量实验、快速淘汰、复合迭代。**AppLovin组织机制是为最大化ML实验通量而设计的，在这个阶段拥有速度优势。

- **决策权集中使得技术路线能被快速确定并执行。** 电商广告与游戏广告在ML层面有若干根本性的设计选择——比如，电商中的曝光、点击等间接信号应该作为"学习信号"还是"标签"来处理？这类影响整个训练范式的决策，在大厂需要研究、工程、产品多方论证数周到数月，在AppLovin由Gio一人拥有全部决策权，极短时间内确定并执行。
- **Full-stack拥有权使得电商模型的"假设→验证"在单人闭环内完成。** 产品嵌入该怎么设计？加入图像编码器还是融合文本特征？这些试探性实验由同一位工程师从假设提出→沙箱原型→全量训练→A/B测试→上线全程负责，不存在跨团队交接延迟。访谈的Research Scientist给出做了一个对比：Meta的"经常一起购买"模型从概念验证到上线花了一年，AppLovin一个好想法一周就能上线——差距不在工程师能力，而在组织结构消灭了交接环节。
- **共享ML基础设施和可插拔架构使得电商模型可以"站在游戏模型的肩膀上"起步。**多阶段架构（检索→粗排→精排）完全通用，探索策略直接可迁移，校准技术跨领域适用，竞价策略核心逻辑相同。系统采用可插拔设计，电商通过插入新训练数据和模型版本接入，不需要重建基础设施——训练平台、feature store、SuperBatch、自动化A/B测试系统，电商团队从第一天起直接使用。这是20-30人的电商团队能在数月内产出有竞争力结果的基础设施前提。

### 4.3 行业访谈和广告主Channel Check中的主要信号

#### **AppLovin内部访谈**

- 访谈的Technical Staff表示：北美市场的电商ROAS效率目前约为Meta的70-80%，差距主要是规模问题而非算法问题。
- 访谈的Research Scientist提到：AppLovin开始电商业务仅数月后就接近Meta的效果表现——Meta在此领域投入了数千人多年开发，AppLovin电商团队仅20-30人。这一追赶速度本身就是组织效率优势的最直接证据。

#### **电商广告主Channel Check**

- <u>从Temu、SHEIN、AliExpress三家中国跨境电商广告主的访谈来看，AppLovin已从2023年的边缘测试渠道迅速成长为各家的增量渠道。三家广告主在AppLovin上的投放占比均呈持续上升趋势</u>——Temu从几乎为零增至2026年预计的7%（7亿美金），SHEIN从约2%跃升至约13%（约2.3亿美金），AliExpress从约3%增至约8%（2.3亿美金）。
- AppLovin的核心竞争力在于转化效率高、目前在早期阶段的获客成本低，且其AXON AI算法在精准推荐和程序化买量方面表现突出。
- 三家也指出了共性隐忧：边际效果随投放时间递减（Temu称效果已较高点下降20%-30%）。整体来看，AppLovin正处于电商广告的快速渗透期，但其在Meta、Google主导的格局中仍属补充性角色，占比提升空间受限于流量天花板和广告主风险分散策略。

![](https://xhs-doc.xhscdn.com/104004dg31u3rkt021m115ernrk?imageView2/2/w/1600)

## 5. 当下股价Price in的预期和投资决策

### 5.1 基于行业访谈的财务模型预测

#### **Base Case（电**商渐进式扩张+游戏稳健但放缓**）**

- 游戏广告业务从2025A的48%增长逐步放缓至2028E的10%，反映AXON 2.0 eCPM优化驱动的自然增长但TAM逐步成熟。电商广告业务以2025A→2027E约55.6%的CAGR扩张，驱动E-com Gross Ad Spend从$4.5B增长到$10.7B，核心假设是H1 2026 self-serve portal全面上线后的渐进式adoption。Revenue从FY25的$5.48B增长到2027E的$10.4B（CAGR ~38%），EBITDA margin从82%扩张至83%，Net Income从$3.4B增至$7.2B。
- **以28x 2026E P/E定价得$446、以20x 2027E P/E定价得$441，对应当前股价基本是fair value——upside仅+1-3%。这意味着，如果电商按预期节奏推进、游戏业务不出意外，当前股价已经充分反映。**

![](https://xhs-doc.xhscdn.com/104004dg31u4gper1is0emtoje0?imageView2/2/w/1600)

#### **Upside Case（电商加速+游戏超预期）**

-  游戏增速在新应用垂类（社交、工具类）的拓展下小幅上行（2026E 25% vs. Base 21%），电商在self-serve全面开放后adoption加速，E-com YoY Growth从Base的70%提升至100%（2026E）。Revenue从FY25的$5.48B增长到2027E的$11.5B（CAGR ~45%），EBITDA扩张至2027E的$9.6B。
- 以30x 2026E P/E定价得$501（+15%）、以22x 2027E P/E定价得$539（+24%）。**这一场景成立的前提是：AXON在电商垂直领域的ROAS快速逼近Meta水平、self-serve portal带来的广告主数量显著超预期、以及游戏业务在非游戏App内广告上打开新增量。对应的2027股价上行空间是23.8%**。

![](https://xhs-doc.xhscdn.com/104004dg31u4g4kdj1m12ue9cio?imageView2/2/w/1600)

*详细的业务逻辑和Model见文档*[AppLovin的业务逻辑和财务模型](https://docs.xiaohongshu.com/doc/63d75fcbe39c141a53ddc25919334dfd)

### 5.2 市场对电商/DTC广告业务的分歧点

**分歧的核心是：电商广告能以多快的速度成为AppLovin的第二增长引擎，以及这个增长的可持续性有多强。**

**为什么投行给AppLovin的Multiple远高于Meta和Google？**

投行给予AppLovin的**目标价格中位数对应的2026E P/E为46.5x**（vs. Meta 24.2x和 Google 29.8x）。投行给出这种倍数差异原因是：

- **增速差异。** AppLovin 2025年收入增速70%、一致预期2026年增速48%，而Meta 2025年增速约19%（预期2026E约15-17%），Google约14%（预期2026E约12-15%）。AppLovin的PEG ratio为0.75 ，低于1.0，说明即使在当前高倍数下，增速仍然足以"买单"。Meta的PEG约0.88，Google约1.1。从PEG角度看，AppLovin的增速相对于其估值倍数反而是三者中最便宜的。
- **利润率差异放大了P/E倍数的合理性。** AppLovin的EBITDA margin为84%、net margin约63%，远高于Meta的EBITDA margin约52%和Google的约38%。高利润率公司的收入增长对EPS的杠杆效应更大，因此愿意给予更高的P/E。

**为什么投行目标价远高于当前股价？** 投行中位数PT约$735，隐含从当前$435上涨约+69%。**差距来自Multiple重估——投行认为当前28x 2026E P/E不合理地压缩了，应回到40-50x的"正常"水平（考虑增速+margin组合）**。

![](https://xhs-doc.xhscdn.com/104004dg31u4mcm9ais0cksn6ho?imageView2/2/w/1600)

### 5.3 投资决策

**当前定价与估值判断：**截至2026年3月25日，AppLovin股价约$435，对应2026E P/E 27.5x、2027E P/E 21.3x。这一估值水平已充分反映了电商渐进式扩张叠加游戏稳健放缓的Base Case情景（我们模型的Base Case P/E定价指向$441-446，与当前股价基本持平）。投行中位目标价$735（隐含46.5x 2026E P/E）与市场定价之间存在约+69%的gap，反映的是对电商增长速度和Multiple合理水平的判断分歧。我们的Upside Case（E-com YoY 100%、30x/22x P/E）指向$501-539，定位在市场定价与投行乐观预期之间。

**我们的差异化认知：**通过外部访谈和广告主Channel Check，我们获得了三个市场不具备的关键判断依据：（1）电商ROAS在可比支出水平下已达Meta的70-80%，差距是规模问题而非算法问题——这直接回答了"AppLovin电商能不能打"的核心疑问；（2）2-5天的模型迭代周期背后是一套可拆解的组织机制（决策权集中、Full-stack拥有权、三个主类统一架构、自建A/B测试系统），且已在电商场景中被验证有效；（3）可插拔架构使电商扩张的边际成本极低，支撑margin在规模扩大时不被稀释。<u>基于组织机制的深度理解，有理由认为电商adoption速度更可能接近Upside Case（E-com YoY 100%）而非Base Case（70%）——但不至于达到投行隐含的极端乐观情景</u>。

**投资建议**

**当前价位（~$435）可少量建仓。** 在此价位买入，上行空间来自两层叠加：EPS上修（电商adoption快于一致预期）+ Multiple从当前被压缩的27.5x向30-35x修复。若电商按Upside Case节奏推进，对应$501-539目标价，即+15-24% upside；若市场情绪回暖叠加Q1/Q2电商数据超预期，Multiple进一步修复至35-40x（仍远低于投行隐含的46x），对应$560-640区间，即+29-47% upside。

**若股价回落至$400以下，建议大力加仓。** $400以下对应2026E P/E约25x、2027E P/E约19.6x，这一估值水平意味着市场几乎完全抹去了电商增长的期权价值，仅为游戏广告的稳态增长定价。这是一个显著的错误定价，原因如下：

- **基本面确定性极高**。FY2025收入$5.48B（+70% YoY）、EBITDA margin 84%、FCF margin 68%——这是全球广告科技行业中利润质量最高的公司之一。即便电商业务完全不及预期，仅游戏广告业务的自然增长（AXON 2.0 eCPM持续优化）也能支撑每年15-20%的收入增长和持续扩张的利润率。$400以下的价格对应的是一个"电商缓慢增长"的情景，访谈证据显示这一情景的概率极低。
- **组织机制赋予了这家公司突破新领域的可复制能力**。AppLovin的历史已经多次验证了这一点：2021年IDFA危机后，公司用不到两年时间完成了从传统ML到神经网络+Transformer的全面技术转型，收入从低谷翻了数倍；2023年剥离游戏工作室后，用一年时间将电商ROAS做到Meta的70-80%。这种"极小组织×极快迭代×单一引擎聚焦"的模式，使得每一次进入新领域都不是从零开始，而是在已验证的基础设施和文化之上做增量拓展。电商之后，CTV（已通过收购Wurl布局）、亚太社交网络（已启动）等新场景都可能成为下一个增长曲线。$400以下买入，相当于以游戏业务的稳态价值获得了电商+CTV+新场景的免费期权。
- 从历史股价模式看，AppLovin的每一次大幅回调都被证明是买入机会。2022年初股价从IPO后高点跌去90%至~$10，随后在AXON 2.0驱动下反弹70倍；2025年2月短卖报告导致单日暴跌12%，此后数月收复全部失地。市场对这家公司的短期定价反复出现过度反应，而长期基本面持续超预期。

### 附录1：可比公司估值

![](https://xhs-doc.xhscdn.com/104004dg31u4nd14k1s065gko44?imageView2/2/w/1600)

### 附录2：AppLovin分部门人员构成（AppLovin Core + Adjust + Wurl）

![](https://xhs-doc.xhscdn.com/104004dg31u22hgrjh809kb1dek?imageView2/2/w/1600)

*注：以上信息基于Linkedin检索，公司公开文件，专家访谈整理之后的推测数据*

### 附录3：外部访谈概览

| **访谈对象所属公司** | **访谈对象背景** |
| --- | --- |
| AppLovin | Technical Staff at AppLovin (Jan 2020 – Present) |
| AppLovin | Former Staff Research Scientist at AppLovin (Apr 2024 – Jan 2025) |
| AppLovin | Former BD Manager of at AppLovin (Jan 2024 – Jan 2025) |
| AppLovin | Former Senior BD Manager at AppLovin (Jan 2022 – Sep 2025) |
| AppLovin | Former Senior Manager of Engineering Recruiting at AppLovin (Sep 2021 – May 2024) |
| 米哈游 | 米哈游平台负责人 |
| 莉莉丝 | 手游广告投放经理 |
| 华扬联众 | 媒体副总经理 |
| Temu | 高级电商运营经理 |
| Shein | 高级品牌经理/主管 |
| AliExpress | 市场总监 |

