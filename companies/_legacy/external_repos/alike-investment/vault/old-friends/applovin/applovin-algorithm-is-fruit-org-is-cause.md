# AppLovin：算法是果，组织是因

> **Executive Summary：**
> **AppLovin是全球领先的AI广告科技平台，以AXON引擎为核心，从移动游戏广告向全品类电商广告扩张：**组织是S级组织——约400人核心算法与工程团队驱动超40亿美元EBITDA，人均贡献约1,000万美元利润；全公司共900+人还原广告收入后人效超1800万美元，是同行业公司的10倍以上。
> **在手游广告时代，AppLovin解的题是"后ATT时代的精准获客"，差异化bet是预测概率而非识别意图：**23年AppLovin通过一次技术组织重构，葛小川重新搭建的技术组织完成了从AXON 1.0到AXON 2.0的算法升级——这不是渐进式升级，而是从底层推翻重建。技术路线上最大的差异化bet是，放弃了对用户身份图谱（IDFA）的依赖，转而基于实时行为信号和上下文预测"用户此刻会做什么"的概率。支撑这套算法的基建是创始人在2017-2022年通过一系列关键收购构建的全栈闭环：MAX聚合平台、AppDiscovery竞价引擎、Adjust归因平台。三者构成了"闭环数据三角"——从出价、竞拍、展示到转化归因，全部在自有体系内完成，不依赖广告主回传，反馈延迟被压缩到极限。AXON 2.0推出后效果立竿见影：广告主ROAS显著提升，游戏广告市占率达30%，iOS仅次于苹果，安卓仅次于Google，全面超越Meta。
> **通过组织穿透发现，AppLovin并不是一家靠"更好的算法"赢的公司，而是一家靠"更快产出和迭代算法的组织"赢的公司：**
> **极简架构 + 反会议文化——消灭理解摩擦**
> 整个AXON算法仅用3个主Class支撑数十个模型，任何工程师都能快速理解整个系统，而Meta需要数百个类文件。同时，AppLovin制度化地推行"反会议"——每周仅一次团队会议，日常依赖文字和数据看板的静默协作。公司架构从C-level到IC极致精简，一人多岗。前研究科学家的量化对比最直观：在AppLovin 5天完成从想法到上线的事，在其他公司需要上月；其他公司十人团队同时只能跑一个AB测试，AppLovin人均并行超过一个。
> **No PM + Entire Stack Engineer——消灭协作等待**
> 全面推行"一人一Feature"模式，每个工程师独立负责从想法到生产的全部环节，不需要写PRD、不需要跨部门对接、不需要代码review。没有PM，因为拥有深厚领域知识的工程师本身就是产品经理。这种设计从根本上消除了大公司常见的"排队等配合"问题。
> **人才密度飞轮 + "永远是Underdog"——消灭组织退化**
> Adam对扩张团队规模有近乎执念的抵触，对"组织越大越慢"的退化规律有着深刻的认知。人才哲学上寻找不循规蹈，永远保持饥饿感，敢于挑战常规的工程师，坚信十倍工程师配合AI工具成为百倍工程师，这种高筛选标准创造了自我强化的正循环：最强的人维持最高要求的文化，这套文化又自然排斥不匹配的人。
> **今天的AppLovin在用这套"老组织"解一道新题——电商广告能否规模化：**
> 电商广告是4-5倍的天花板拓展，但难点在于归因链路断裂，AppLovin的解题路径清晰：先与平台级自营电商共建数据优化算法，再通过Shopify集成打通mid-size DTC品牌市场。2026H1是最大验证节点——Self-serve Ad Manager全量上线+视频素材生成产品落地将同时验证"产品自动化能否替代人工销售"和"素材瓶颈能否被AI突破"两个核心卡点。若验证通过，电商广告有望复现AXON 2.0在游戏领域的爆发曲线。
> **投资结论：有条件买入，核心逻辑是"算法是果，组织是因"——AppLovin的真正资产不是AXON算法本身，而是一套极度自洽的组织哲学**：超高人才密度、Simplicity、反会议文化、Engineering-driven、No PM、Entire Stack Engineer，以及由此产生的极速迭代基础设施，构成了竞争对手无法在短期内弥合的结构性差距。估值层面需要耐心，理想的介入窗口在估值回调至1,000亿美元左右（对应约17x 26E EV/EBITDA），届时风险收益比显著改善，3年2倍的回报预期更具备吸引力。

## 1. Why Interesting

AppLovin（后称“APP”）是一家容易被误解的公司。表面上看，它做的是全球的“网盟流量”、"手游广告"，——一个听起来既不性感也不前沿的生意。但如果深入拆解，就会发现他将一个被忽视的生意做成了一个“极度克制”的千亿美金业务。而且他可能是当前美股市场上"AI落地变现"最纯粹、最高效的案例。

- **高收入增速和夸张的利润率**：2021年-2025年软件平台收入从6.7亿美元增长到55亿美元，复合增长52%；2026年公司收入目标80亿美元，同比增长45%。2025年运营利润率高达76%，利润率高达61%。

![](https://xhs-doc.xhscdn.com/104004dg31tp5pru3mq00gik6dg?imageView2/2/w/1600)

- **在巨头夹击下赢得了“数据与信号”优势**：市场曾认为Meta和Google不可战胜，但APP通过对MAX（流量聚合平台）的控制，拿到了全市场超50%的聚合平台竞价流量（～15亿DAU），拥有了比Meta更深的用户可见度。这使本身没有流量池的APP，在全球范围内（除中国），成为继两大”wall-garden“ Google和Meta之后的第三级。

> “Meta does not have access to full mediation. APP runs the mediation stack for 50+% of the auctions... That's less of a technology advantage, more of a** data and signal advantage**.”——ex Meta Head of Product

- **反直觉的极致人效与盈利杠杆**：APP是市场上将AI技术转化为财务回报效率最高的公司。支撑公司98% EBITDA的核心业务团队仅约400人，人均创收和利润冠绝硅谷。2025年人效超600万美元，是Netflix的2倍以上，Shopify的4-5倍。如果横向对比广告业务公司，还原广告收入（APP收入赚的是差价部分，还原广告收入相当于广告主gross billings）后人效超过1800万美元，是国内互联网巨头的10倍以上。

> “The core business that drives 98% of the EBITDA is about 400 people... The EBITDA of the company I think is run rate well over 4 billion now, so if you just translate that as $10 million a head...” ——CEO Adam Foroughi

- **算法驱动业务，模型即产品：**核心人员大部分指CPEO葛小川领导的算法中台（约400人，包含核心100人神经网络团队，其他如工程师团队、广告创意团队以及电商与创新团队），围绕AXON 2.0 AI模型基座，打造了一系列商业化产品。商业化团队只有250人服务2000个头客（包括代理），在收入和团队规模上做了取舍，不做苦生意。

> "We don't have a big salesforce. We think the product is so good it should be able to sell itself, and we end up with **engineers building code to expand revenue**." ——CEO Adam Foroughi
> “APP的生意是算法驱动的，我们全球只有2000个客户，不做苦生意。”“因为流量的匹配和分配策略完全内化在算法里，销售无法左右资源分配，所以最后实际上就剩一两个客户效果没那么好，我们就去给他们做一些比如画饼、搞个方案、心智传播等，（销售）就是一个兜底的作用。”——APP 大中华区销售总监

- **从手游到电商，算法驱动下实现了Sale-less Scale up**：手游广告市占领先，iOS仅次于苹果，安卓仅此于谷歌。24年下半年开始扩展到电商，手游广告（~$43B全球TAM）到电商广告（$75-150B全球TAM），TAM又扩大了4-5倍。电商业务启动第一年软件平台收入就达到6.2亿美元（还原广告gross billing约15亿美元），2026年目标19亿美元收入。

> "For the past 13 years, we’ve been deep-seated in the gaming developer ecosystem—a relatively niche market—where we’ve perfected our ROI models to solve the ultimate challenge: how to spend one dollar and generate the highest possible profit." "Addressable market outside gaming: 5x to 10x the size of the gaming market."——Adam Foroughi

> "Our team working on e-commerce is less than **10 people**."（指的是电商的算法和工程师团队，据HR称目前也不足20人）——CEO Adam Foroughi

- **资本市场将游戏领域的成功归因到的简单的叙事：**外界看到的是一个符合逻辑的简单叙事，在AXON 1.0引擎基础上->做自营游戏->积累一方数据->持续训练算法->算法进化到AXON 2.0->性能强引爆市场。但多方校验的事实上，资本市场很大程度上低估了缔造AXON2.0背后的掌舵人——葛小川（Gio），一个从Meta过来的IC，用了两年半成为了公司的CPEO，实际意义上的二号位，以及他所打造的这个工程师为主导的技术组织。

> "外界总是希望找到简单的解释，让成功看起来比较简单，实际上不是的，游戏数据对核心算法也没那么重要，电商算法完全是重新创业，唯一的差别是多了一年试错经验（2023年做应用市场算法AXON 2.0，2024年H2开始做电商市场算法）。如果有一天外界的评价是这个团队特别厉害，做任何事情都能做成，我反而会不适应。"“实际上唯一的优势就是我们的团队，今天没做大语言模型是因为投资回报率不合适，如果有一天需要，我们也能很快成为第一梯队的玩家。”——葛小川接受硅谷101访谈，2025年底

从技术团队内部看，APP前研究科学家Oren Sar Shalom（前 AXON 2.0早期团队成员之一（1/11），Now at LinkedIn，ex-APP, Meta, Prime Researcher）给我描述了一种在大厂完全不可想象的工作速度：

> **"At APP, you can do even from idea to production in five days, which is impossible at LinkedIn, Google, Meta, any other company.**""Something that now takes me even months to do at LinkedIn — at APP I would finish it in less than two weeks, because I would face no barriers."——Oren Sar Shalom, APP Former Research Scientist

- **现在的 APP 看起来不便宜，26E PE 30 倍、EV/EBITDA 24 倍。但别忘了，这是一家25年增速 70%的高成长标的，且天花板更高的电商广告业务已经撬开了大门：**市场现在很纠结，一方面质疑电商扩展的确定性，一方面又在按图索骥寻找简单的成功叙事。诚然，目前的电商算法还没达到 AXON 2.0 23年的inflection point。但我对 APP 的兴趣在于，这个公司的核心护城河，不是外界看到的某种单一算法，而是被大多数人低估的、能高效解题的“组织能力”。

## 2.考古APP的关键拐点

### 2.1 起源与早期（2011-2018）：解题"手游获客"

**创始人的底色：移民家庭的生存本能**

APP由Adam Foroughi于2011年创立。理解这家公司，必须先理解创始人。Adam 1980年出生于伊朗德黑兰，其父亲曾是伊朗最大的房地产开发商之一。1979年伊斯兰革命后，全家被迫逃离，先到法国，1984年辗转移民美国南加州，父亲失去所有财产，从零开始。

> "When you grow up and you see the loss that your parents faced and then you see that your dad had to give up a business that he built, has sort of lost a big part of himself and given that up for your benefit, you don't really have much of a choice but to push yourself when you get into life."——Adam Foroughi, Goldman Sachs Builders and Innovators Summit (2025.10)

这种"曾经拥有一切却瞬间归零"的家族集体记忆，烙印在Adam的潜意识里，塑造了两个关键特质：一是对现金流和盈利能力的极度关注（而非外界的掌声），二是一种永远不认为自己已经成功的危机感。

> "The biggest asset I had—because I never did feel like I was the smartest person in most the rooms I was in—was work harder than everyone else around me.""I wake up between 5:15 and 5:30 every morning with the immediate thought that the company might go bankrupt, prompting me to check statistics before I can calm down and start my day."——Adam Foroughi

Adam在UC Berkeley学经济学，毕业后做过衍生品交易员，之后有两次Ad Tech创业经历——LifeStreet Media（2005年创立，专注桌面端应用内广告）和Social Hour（2008年创立，移动社交营销）。两次创业都成功退出，但更重要的是积累了一个核心认知：

> "Because I had a desktop advertising company in the 2000-2010 era, I could start seeing the beginnings of all the traffic shifting to mobile... Facebook hadn't launched on mobile yet, their monetization platform. So, like, at the time, people weren't realizing that all the consumption was shifting really, really quickly."——Adam Foroughi, Goldman Sachs Builders and Innovators Summit (2025.10)

**创业的冷启动：被40家VC拒绝后的自力更生**

2012年3月，Adam与John Krystynak和Andrew Karam共同创立APP。

> "We couldn't spend the dollars intelligently, and I ended up looking at that and saying there's going to be a lot of developers that are going to exist in this economy... I felt like we could actually pivot what we were working on and just go right back into performance advertising."——Adam Foroughi, Goldman Sachs Builders and Innovators Summit (2025.10)

Adam被超过40家风险投资机构拒绝，反而成了一个关键的组织基因塑造事件：因为融不到钱，Adam只能走冷启动路线，在没有外部资金支持的情况下，硬生生把公司带到了盈利状态（2012年9月，创立仅6个月即实现盈利）。

> "But what we do want across the board is that every single person with every dollar that they spend thinks about the dollars that they're spending as their own."——Adam Foroughi

早期的APP是一个相对标准的移动广告网络，同时也运营自有手游工作室（200+款游戏），既是广告买方也是卖方。自有游戏组合的价值在于：它是AXON 1.0 算法的训练场和测试场。

> "实际上，APP自创建以来就经历了多个重大转型。最初成立时，它是一家应用推广公司，这一核心业务与现在有些相似，但当时其技术并不是现代化的推荐算法，而是基于一些社交图谱的规则引擎。"——葛小川, APP CPEO

### 2.2 关键收购期（2018-2022）：构建全栈垄断

APP真正的战略转型始于一系列精准的M&A。2018年7月，KKR以4亿美元投资APP，估值从14亿提升至约20亿美元。Herald Chen（KKR TMT负责人）加入董事会，后来出任总裁兼CFO——这标志着公司从创业阶段进入战略扩张阶段。

**（1）2018年收购MAX——整个故事中最关键的一笔**

MAX是一个应用内广告聚合（mediation）平台，核心创新是用实时竞价（real-time bidding）替代传统的waterfall拍卖（每次展示需要30-40次调用）。APP于2018年9月收购MAX，从此从一个"竞拍者"变成了"既是拍卖师又是竞拍者"——这是后续所有竞争优势的根基。

> "第一轮收购包括了两家广告汇聚平台的公司——Max和MoPub，其中MoPub是从推特收购而来……APP又收购了一家游戏公司，名为MachineZone。MachineZone对APP的意义不仅在于增加了自家开发的游戏，还因为其内部有一个广告投放团队，等于引入了一个买方平台"——葛小川, APP CPEO

**（2）2021年2月收购Adjust（$10亿）**

移动归因和反欺诈平台，在苹果ATT（App Tracking Transparency）政策推出后尤为关键，帮助APP内化了测量能力，完成了数据闭环。

**（3）2021年10月收购MoPub（$10.5亿，来自Twitter）**

这是一笔"消灭竞争对手+整合市场"的经典操作。MoPub在鼎盛期服务超过50,000个应用，是最大的独立mediation平台。APP将MoPub的客户迁移至MAX，然后直接关停MoPub。到2025年上半年，MAX聚合了超过9,000款应用，在头部手游中的mediation份额达到55%。

**（4）2022年收购Wurl（$4.3亿）**：CTV（联网电视）广告平台，为未来扩展至电视端预留了入口。

**（5）2022年尝试收购Unity（~$176亿），后放弃**：这笔交易如果成功，会创造从游戏引擎到广告变现的全链路垄断。APP在风险收益恶化后果断放弃，展示了资本配置纪律。

**（6）2025年尝试收购Tiktok，后失败：**2025年Adam提到其竞购Tiktok的方案比其他对手（如甲骨文、亚马逊或财团）更强，因为他提出的不是剥离美国业务，而是将 APP 与 TikTok 除中国以外的全球业务进行合并。

> "TikTok is doing roughly $20 billion in ad revenue outside of China, but it is severely undermonetized. By integrating our AXON engine, we believe that revenue could scale to $80 billion or more, aligning its monetization efficiency with the likes of Meta." ———CEO Adam Foroughi

### 2.3 AXON 2.0与利润爆发（2023-2024）：AI引擎的"iPhone时刻"

**2022年的至暗时刻：大环境与内部危机叠加**

2021年4月，APP以$80/股在纳斯达克IPO，首日即跌破发行价。但真正的危机不只是股价——2021年4月，苹果正式实施ATT（App Tracking Transparency）政策，要求每个App必须弹窗征求用户同意才能追踪其跨应用行为。全球平均opt-in率仅约25%，这意味着广告平台一夜之间失去了约75%用户的精准身份标识（IDFA）。

ATT对整个移动广告生态是一次地震级打击，但对不同玩家的影响程度截然不同。彼时的市场领导者Meta受创最深——其Audience Network（MAN其网盟业务）产品因采取"双重授权"合规策略（用户需同时在Meta和发布商App两端授权），iOS可触达受众接近归零：

> "Supply wasn't lost because publishers walked away from Audience Network. Supply was just not serviceable by Meta Audience Network because of the fact that this double opt-in was… single opt-in is hard enough to get. Double opt-in made it even slimmer. You effectively lost your audience overnight.""Meta chose to comply even at the cost of its Audience Network iOS serviceability." ——Meta Director of Product Management

IDFA消失带来的其实是两个不同问题：一是"找准人"（知道用户是谁以投放广告），二是"算清账"（将转化归因回广告）。Meta数年前通过AEM和概率建模解决了“算清账”，但“找准人”花费了远更长的时间，导致MAN 22年退出市场后近期26年才重新回来。

> "It took much longer to solve the issue for identity for ad delivery than it took to solve for identity for ad conversion attribution… It required a lot of internal policy conversations, not just a technical conversation."——Meta Director of Product Management

在这个背景下，APP的AXON 1.0同样举步维艰。2022年，移动游戏公司削减广告支出，APP软件业务连续三个季度收入持平。2022年12月28日，股价跌至历史低点。核心问题不仅仅是宏观环境，更是AXON 1.0的技术架构本身已经不适应后ATT时代：

> "Back to 2021-2022, when Axon 1.0 was built out… the traditional machine learning techniques didn't really materialize into significant penetration into all different areas and different gaming apps or the ecosystem that they built around, so they were not able to effectively measure the output."——Shubham Agrawal, APP ML Core Engineer

**危机中的重生：组织重构先于技术重构**

AXON 2.0的成功不是从技术开始的，而是从组织开始的。2023年是APP组织史上变动最剧烈的一年——而正是Adam这次"先换人、再换技术"的决定，为后续的技术飞跃创造了前提条件。

> "In 2023, there was a major shift in terms of how the company restructured and realigned their team structure… Most of them were let go and they hired a lot more young folks who were actually super energetic about building some of these advanced systems… they kind of hired a lot more people from Meta and Google, and then they revamped the whole engineering initiatives in order to actually align with what the next generation Axon 2.0 would look like."——Shubham Agrawal, APP ML Core Engineer

葛小川的角色至关重要——他从Meta的IC直接被Adam带入APP，而他的工作从根本上改变了公司的技术和组织。

> "AXON 2.0 is only due to Gio. The culture of APP is based on Gio. He changed the company. The company owes him a lot. The greatness of Adam was to understand this is the right thing to do and to give Gio all of the power he needs. It's extremely non-trivial to take someone who was just an IC at Meta and to turn him into a senior VP in no time."——Oren Sar Shalom, APP Former Staff Research Scientist

**AXON 2.0的技术本质：为后ATT时代重写算法基模**

AXON 2.0不是AXON 1.0的渐进升级，而是一次从底层推翻重建的bold bet。技术路线发生了根本性变化：

**从监督学习到深度神经网络**

AXON 1.0是基于传统机器学习（监督学习）的系统，预测效果有限，AXON 2.0全面转向深度学习和神经网络。

> “Back then they had a very old mechanism that it used to, it was only extra boost. Okay, no deep learning. So Gio said we need to throw away everything and build from scratch. This is AXON 2.0, completely new. Everything is new so that's not actually AXON. “We went from supervised to deep learning and neural networks. That was the current Tech of the focus."——Oren Sar Shalom, APP Former Staff Research Scientist

**从身份图谱到行为预测与上下文信号**

这是理解AXON 2.0为什么能在后ATT时代胜出的关键。传统广告平台（尤其是Meta）的核心逻辑是依赖IDFA构建用户身份图谱——"知道你是谁，所以知道你想要什么"。IDFA消失后，这套架构的根基坍塌了。而AXON 2.0走了一条完全不同的路：不依赖"你是谁"，而是基于用户实时行为和上下文信号来预测"你此刻会做什么"。（通过多年内部积累的用户标签数据，今天的APP也已经知道“你是谁”了）。

> "APP's performance-first with a closed loop with LTV learning means that it's not as susceptible to changes in privacy, whereas Meta, for example, has been hit the hardest... because APP are not as reliant on IDFA identifiers, for example, they more based on predictive modeling, contextual signals or cohort approaches as well, they do have a clear edge here."——APP前业务发展经理

**模型按用户行为分类，而非按游戏品类**

另一个反直觉的设计是，AXON 2.0的模型不是按"休闲游戏/中核游戏/RPG"这种品类来分的，而是按用户行为来分——安装率模型、结账模型、订阅模型。

> "We have one model based upon the type of thing that we expect the user to perform. For a user, if you want the user to install an APP, then we will have an install rate model. If you want the user to do a checkout activity within the APP, then we would have the checkout model… We just put them into a cluster of specific type of apps."——Shubham Agrawal, APP ML Core Engineer

这种基于行为的建模方式天然与IDFA无关——它不需要知道"你是谁"，只需要知道"你是一个高概率会完成结账行为的用户"。这使得AXON 2.0的算法逻辑从出生第一天起就是为后ATT原生的。

**效果爆发——在后ATT时代解了别人解不了的题**

AXON 2.0在2023年中期推出后，效果立竿见影。广告主的ROAS显著提升 → 广告主愿意出更高的价格 → CPM上升 → APP收入和利润同时暴增。

> "在我加入之后，APP面临许多需要解决的问题。我们重新构建了APP的广告算法，外界称之为AXON 2.0。随着时间推移，广告在公司收入中的占比不断提高。我最初加入时广告收入占公司营收的约20%，而上个月已上升至80%。现在，我们游戏业务已出售，广告收入几乎占据了100%。"——葛小川, APP CPEO

本质上，AXON 2.0在后ATT时代解了一道别人还在挣扎的题：当整个行业因为IDFA消失而手足无措时，APP打破了旧范式（依赖身份图谱的监督学习），从零构建了一套基于行为预测和上下文信号的新基模（深度神经网络+Transformer）。

**凭借 AXON 2.0 算法在构建的游戏广告统治力**

得益于 AXON 2.0 算法的代际领先，APP 在移动游戏广告领域展现出极强的竞争优势。目前，其整体游戏广告支出市占率约达 30%，在 iOS 和安卓市场均稳居第二，仅次于系统层级的苹果（ASA）和谷歌（AdMob），已全面超越 Meta。

我们可以从两个维度拆解 AXON 2.0 的算法竞争力：

**1）和数据围墙类公司如Meta Advantage+竞争：**算法层还有一处关键差异，Meta输出的是预测准确率，AXON 2.0输出的是策略成功率。实际上AXON 2.0是端到端模型，但为了方便比较，可以把AXON 2.0想象成两层模型，第一层和Meta输出一样都是预测准确率，但APP输入是以用户行为+上下文为主，用户信息为辅，Meta是纯用户信息为输入。AXON 2.0在第一层基础上还有一层策略模型，这由其DSP商业模式决定，当算清楚预测准确率后，AXON 2.0还可以决定要不要拿下。

这就好比一场德扑，Meta和APP都是牌手，对目前自己的胜率有所计算后，AXON 2.0还可以决定“玩不玩”，可以Fold。Meta由于都是自己流量需要“每把都玩”。这就是为什么对于大多数游戏广告主而言（通常要求30天ROAS达到1.2即可放量），APP的普遍ROAS都要高于Meta，Meta是个更广的广域流量池“每把都玩”，AXON 2.0是在更垂的流量池里“控制入池”。一个典型的AXON 2.0场景如下：

1. App Discovery基于广告主回报阀值，广告主愿意支付CPI为 $4.0
2. 基于MAX聚合的“网盟流量”中，AXON算法找到了最适配的广告位，输入是SDK回传的用户行为数据等，输出翻译成人话大概是“对这个广告位和这个用户，我出价$2.6大概率能拿下，但该用户LTV价值为$6.0” 这个策略成功概率是xx%
3. App Discovery为这个广告位出价$2.6并最终拿下，MAX支付流量成本$2.6给下游发行商
4. 广告主支付$4.0，拿到预期LTV$6.0的客户，赚取$2.0的经济净值（1.5 ROAS）
5. APP赚取差价$1.4，对应（广告主spending的）抽成率35%（APP的均值）

**2）和Unity等相同模式（DSP+SSP模式）的网盟流量公司类的竞争：**如果说和自有流量池玩家竞争，Meta等依旧可以在效果略差的情形下，靠广域的流量池和APP竞争广告主预算，那么在网盟流量竞争中，APP则处于绝对的统治地位。相同模式下，各方算法大的逻辑基本相同，区别在于算法层面对于上述例子中“出价$2.6大概率能拿下”和“该用户LTV价值为$6.0”的预测准确度差异巨大，甚至在产品上Applvoin也领先3年。另一个体现APP算法的领先程度数字是，APP在投放端的take rate可以达到40-45%（综合35%是被Max部分收入10-12% TR拉低），行业其他DSP平台平均take rate在20%左右（给广告主效果更好，自己还更赚钱）。

> "APP 的AXON 2.0被评价为'跑什么都能达标'……Unity目前主要依赖广告平台回传数据，Day28 LTV产品其实是刚开始半年不到，Runtime（引擎端）数据尚未正式投入算法学习，预计2026年才会开始尝试获取授权并使用，……APP学的时间比较早，采纳的数据源，包括数据的维度丰富度也会碾压。"——Unity（“网盟市场”中的第二名） Expert

## 3.核心护城河

### 3.1 MAX Mediation的"拍卖行"垄断

MAX在头部手游中的mediation份额估计为55%，是Unity LevelPlay的两倍以上。到2025年上半年，MAX聚合了超过9,000款应用。这个位置赋予APP三个结构性优势：

（1）免佣优势：MAX对第三方DSP收取约5%的聚合费用，但APP自己的AppDiscovery竞拍器免除此费——在同等出价下，AppDiscovery天然有5%的成本优势。（MAX平台的竞标成功中，APP的App Discovery占比超50%）

（2）数据保真度优势：

> "Meta does not have access to full mediation. APP runs the mediation stack for 50+% of the auctions. Because consolidating supply to that level means you just have that much more visibility into users… of course, your models are going to learn better. That's less of a technology advantage, more of a data and signal advantage."——Meta Director of Product Management

（3）广告服务与延迟优势：直接技术集成让AppDiscovery的广告渲染更流畅、延迟更低——对于"可玩广告"这种需要即时互动的格式尤为重要。

**Adam的远见：2017-18年不计成本推MAX，"当时没人懂"**

MAX的今日垄断并非自然形成，而是Adam在2017-2018年就开始布局、全力押注的结果。当时公司将BD团队的核心KPI全部压在MAX的市占率上，而非短期盈利。

> "实际上真正的MAX推广，应该是从差不多17-18一直到21-22年，在推这个事情的时候，市占率占的特别高。但是现在回头想起来之后，这个好处是巨大的，当年大家其实都没有完全了解到。"
> "基本上大家都装MAX了，该装都装了，应装尽装了。"这意味着MAX的推广期已经结束，进入了收割期。——APP商业化专家

当时市场的共识是：做"二手流量贩子"不可能做成一家真正伟大的公司，TikTok和Facebook都在打造自己的流量池。没有人认为一个中间商能成为giant。但Adam恰恰在所有人看不起的赛道上，用最激进的方式抢占了基础设施层的位置。

**设备级SDK安装：MAX带来的不只是拍卖权，更是即时数据反馈的"协议层"入口**

MAX的战略价值远不止于Mediation市场份额本身。理解MAX的真正护城河，需要理解一个关键机制：当开发者接入MAX时，实际上是在设备层面安装了APP的SDK——这不是简单的"软件集成"，而是一个协议层级的数据通道。通过这个SDK，APP获得了设备级别的实时用户行为数据反馈（还包括竞价逻辑、广告渲染等核心功能），而不需要像其他平台那样依赖广告主回传一方数据。

> "你看抖音就是我们在国内这些厂商，就大家也要求广告主回传一方数据，但是他是直接不需要回传了，这是一个最深层次的SDK级别的一些机会。那这个东西我觉得就是他的这个认知和决策最牛逼的地方。"——APP商业化专家

换言之，抖音、Meta、小红书等平台的数据获取方式是"请求广告主配合回传"——这取决于广告主的意愿和技术能力，数据质量和时效性都有损耗。而APP通过MAX的SDK直接部署在设备上，数据的采集是协议层面的、实时的、不依赖广告主配合的。

基于应用内SDK协议层面的全域用户行为一方数据回传，MAX带来的裁判视角下的竞价透明度数据，以及Adjust带来的SSP聚合数据和byIP数据。这三层数据共同构成了APP在后IDFA时代独一无二的数据闭环。MAX的垄断地位意味着，竞争对手即使有能力搭建类似的算法，也无法复制这个数据采集的基础设施层——因为SDK已经装在了15亿设备上。

**切换成本的真正来源不在于技术替换难度，而在于市场地位带来的心理惯性**

> "Mediation platform只能装一家，技术上替换并不难，但广告主担心切换后效果不确定、开发流程受破坏，且APP流量规模更大，这种'不想冒险'的惯性才是真正的壁垒。"——APP商业化专家
> "你站在广告主的角度来讲，因为你的MAX如果跑得好好的，你切过去，很可能你跑得好，但别的不一定跑得好，对吧？再一个的话，整个开发流程……它会破坏你整个开发流程嘛……所以这个护城河不来源于技术的替代成本，而在于市占率。"——APP商业化专家

### 3.2 AXON的数据飞轮

AXON每天处理数十亿次竞价、展示和安装后事件。在有机数据上APP并无结构性优势，但凭借算法领先赢得更多竞标，从而形成更强的用户反馈数据飞轮，这是数据层面护城河。

> "从这一角度来看，即便我们拥有MAX平台，我们获取的有机数据与其他竞价者是完全相同的……像Google和Meta有他们自己的数据，比如Meta在Facebook上的用户数据，这是我们无法获得的。但这逐渐成为了APP的一项优势。因为我们的算法非常出色，而现在的平台购买力强，能获取更多用户的曝光量……就像一个飞轮，你赢得的越多，获得的反馈数据就越多、质量也越高。"——葛小川, APP VP Engineering

Adam上将这种飞轮效应提炼为一个极简的增长公式——通过定向模型增强（directed model enhancements）和持续的递归学习（recursive learning），算法本身就能驱动baseline的持续增长：

> "几年前设定这个基准时，市场甚至不相信APP能有20%的增长。但这只是一个用于对齐投资者预期的底线。过去几年，由于技术的初期红利和数据的飞轮效应，实际增速远超于此。随着拓展电商等新领域，模型获取的数据更多，飞轮效应将持续叠加。"——Adam Foroughi

AXON已经转化为可量化的增长基准，算法通过每一次竞价的胜负结果进行递归学习，模型在无人工干预的情况下自动变得更好——这即是Adam说到的即使不做任何新功能开发，仅靠现有飞轮的惯性，也能维持20-30%的baseline增长。

## 4. 组织穿透：APP最被低估的护城河

如果只允许用一个词解释APP为什么赢，不是"算法"，而是"组织"。正如葛小川说的，算法理论上可以被复制，但产生这种算法的组织形态极难被复制。

> "即使将谷歌的算法复制到另一家公司，六个月后，该公司也无法与谷歌相提并论。人的因素和文化对产品的影响是深远的。"——葛小川，APP CPEO

### 4.1 极致扁平的组织所带来的极致效率

我过去访谈了超过十位APP现员工和离职员工，提及率最高的词便是“Lean Organization”和“Move Fast”，这种对于极致扁平的追求来源于创始人对人才密度理念近乎执念的追求：

> "I constantly get asked, 'You're an advertising business. You have tons of revenue opportunity in front of you to grow. Why don't you go hire a bunch of people?' And the simple answer to that for me is I've got a lot of great people. The second I hire a bunch of people, when it becomes bunches or you think about hiring quotas, you dilute the intelligence around you."—— Adam Foroughi

APP的C-level只有5个人：CEO Adam Foroughi（兼COO和CMO职能）、CPEO（兼CPO和CTO for AI）、CTO Basil Shikin负责基础设施、CFO Matt Stumpf、CALO Victoria Valenzuela负责行政、HR、法务。

> "无COO，Adam直接抓运营执行；无CMO，Adam本人出任品牌与公关核心发言人；战略决策均由Adam主导；亲自跑SQL参与研究团队核心数据分析，2022年以前要终面每一个员工，目前仍负责审批每一个HC。"——APP HR总监

这种扁平化不仅存在于顶层，而是贯穿整个组织。同时，将决策权充分授权给一线，为move fast打造了高失败容忍度的文化。

> "I’d rather have an engineer push code that breaks the system and we lose a few million dollars, but we can roll it back in 10 minutes, than have a culture where people are too afraid to move fast because of a process."——*Adam Foroughi*
> "我们的director，他的预算决定范围权就已经能够到百万美元……在业务的驱动等等这些决策，我们是将大量的自主权放，比如说中国的大陆地区，我们的研发是不需要再找回到美国，然后帮他去做支持的。"——APP人力资源经理

APP的Move fast本质上是组织架构在根基层面消除了一切减速因素后自然产生的结果。前研究科学家给出了最直观的量化对比：

> "At APP, you can do even from idea to production in five days, which is impossible in LinkedIn, Google, Meta, any other company."
> "Something that now takes me even months to do at LinkedIn — at APP I would finish it in less than two weeks, because I would face no barriers."
> "At LinkedIn, the response prediction team — about ten people, just about the size of (2023) APP research team — we on average got just one AB test at any given time. APP got almost ten."——Oren Sar Shalom, APP Former Staff Research Scientist
> "Each one of the employees on average got more than one AB test at any given point of time."——Oren Sar Shalom, APP Former Staff Research Scientist

这种速度的基础设施由三根支柱支撑：

**支柱一：AppDiscovery + MAX + Adjust的闭环数据三角**

Move Fast的前提是反馈的即时性。APP同时拥有需求侧（AppDiscovery）、供给侧（MAX）和归因侧（Adjust），这意味着从"模型出价→赢得拍卖→用户行为→效果归因"的完整闭环全部在自有体系内完成，没有任何外部依赖。一个新模型上线后，能在几小时内就拿到真实的效果反馈，而不需要等待广告主回传数据或第三方归因平台出报告（通常需要几周甚至一个月时间）。

对比Meta或Google：它们的归因依赖外部MMP或自归因，数据回传存在延迟和损耗；模型优化需要跨团队协调（广告产品组、数据科学组、平台组），每次迭代周期天然更长。APP的闭环三角把反馈延迟压缩到极限，让"fail fast"从口号变成了日常。

**支柱二：模型纯净性——用模型解决问题，拒绝Post-Processing**

APP选择在模型内部解决所有问题，让每一次模型改进都产生清晰可归因的收益变化：

> "APP doesn't have post-processing. They say that if you do post-processing you just hide all of the deficiencies in the model. We solve it with the model alone and only. This is a completely novel idea that they thought about by themselves. It involved thousands of lines of code across the entire stack and they did it in three weeks."——Oren Sar Shalom, APP Former Staff Research Scientist
> "一种是直接的方法，手动纠正缺陷；另一种则是相信只要把模型做好，就能最终弥补缺陷……我们不去过度优化短期收益，而是专注于如何建设好的模型……从长远来看，这导致了我们的模型非常清晰……某种改变对我们的模型是有利的，通过直觉和线下测试来验证，然后在上线测试中获取最终收益，这一系列操作之间具有极高的相关性。"——葛小川, APP CPEO

这种"模型纯净性"直接加速了迭代：当你知道每一次改动的因果关系是清晰的，你就敢大胆试、快速试。相反，如果模型被层层post-processing包裹，你对每次改动的效果就无法预判，迭代速度自然降下来。

**支柱三：极简代码架构——3个Class支撑数十个模型**

速度最底层的基础设施是代码架构的极简。整个AXON算法仅用3个主Class支撑数十个模型（涵盖retrieval、re-ranking、多目标、iOS/Android双端等），与Meta数百个类文件的层级架构形成代差：

> "For the code, at APP, there are three main classes, that's it. Everything is built around three main classes in terms of the modeling. In Meta, we would have hundreds and hundreds of files. So the beauty of APP is simplicity."——Oren Sar Shalom, APP Former Staff Research Scientist

极简架构意味着：任何一个工程师都能快速理解整个系统，而不需要花数周熟悉复杂的代码依赖树。这与全栈工程师的组织设计形成完美互锁——当代码足够简单、人足够全栈时，一个人就能从想法到上线独立完成全部工作，不需要"排队"等其他团队配合。

APP的算法优势不来自原创发明，而来自比任何公司都快地把学界最新成果转化为生产验证：

> "If there is a new paper, something cool that was published that is relevant, someone from APP will be on it. They will try it immediately, they will fail fast, they will try it — if they see it doesn't serve any good results, they will move on. But they will try it in no time."
> "They didn't invent anything. They just experimented — so which one works well and moved on."
> "We can maintain a small team, keep it simple and we will move exponentially faster than any other company."——Oren Sar Shalom, APP Former Staff Research Scientist

闭环数据三角决定了反馈速度，模型纯净性决定了迭代质量，极简架构决定了组织执行摩擦。三者共同作用的结果是——APP在速度维度上构建了一条竞争对手无法简单复制的护城河。

### 4.2 反会议文化：静默协作与异步通信

APP可能是硅谷最"反会议"的公司。这不是一种偏好，而是一种制度化的设计。

> "There was a no-meeting policy. There was just one meeting per week for the team, that's it. Once there are no meetings, that means that whenever you do need to brainstorm with someone or ask questions, you will slack them and you will immediately get a response because the other person is not in the meeting. So everything moves super fast."——Oren Sar Shalom, APP Former Staff Research Scientist
> "我们鼓励的是静默协作（依赖文字和数据看板的异步协作模式），以及异步同步……不需要靠开会或者同步沟通来对齐，浪费大量时间在这上面，我们直接通过数据看板、评审或者产品的数据反馈来进行协作……每个人或者每个团队直接负责你这个模块，拥有这个模块的全部决定权。"——APP人力资源经理

葛小川从管理者视角解释了为什么会议是效率的敌人：

> "如果一个事情需要安排会议去讨论，这件事情大概率是不重要的……如果你真的觉得这个事情重要，应该直接去找相关的人聊一下。很多会议的标准时长是30分钟，但实际上很少有人会说这个会议开了五分钟就结束，通常大家还是要把这30分钟熬过去。""通过文字沟通可以减少反复交流的次数，强迫自己提高沟通方式……由于采用这种沟通习惯，大家能够以简单的几句就达成很好的默契。"——葛小川, APP CPEO

### 4.3 Entire Stack工程师与No-PM架构

**不仅是Full Stack Engineer，而是Entire Stack Engineer**

> “Employees(Research and Engineering team) are expected to master the 'entire stack,' including feature engineering, modeling, and the business side. This makes each individual completely independent and reduces dependencies on other team members.”——Oren Sar Shalom, APP Former Staff Research Scientist

2025年起，APP全面推行"一人一Feature"的全栈工程师模型——一个人负责某个Feature的全部开发，不需要写PRD，不需要跨部门对接，不需要代码review和QA环节。

> "我们在25年就开始已经在测试，现在已经全量推的，就是一个人在研发层面就只负责一个feature的全部，所以都是全栈工程师……你不会的地方，肯定有人还不是全栈……那这些可以让AI来完成，我们是接受的。所以这个人负责某feature的开发，他不需要写PRD，不需要跨部门的对接、代码的review、QA这些环节都不用。"——APP人力资源经理

**No PM？因为工程师自己就是PM——他们拥有足够的领域知识来判断什么该做**

> "There is no PM, no product manager. Because each one of the team got tons of domain knowledge, they don't feel they need another non-technical person, the PM, to tell them what to do. They find themselves the next best thing."——Oren Sar Shalom, APP Former Staff Research Scientist

葛小川将这种模式与大厂组织病做了对比——在大公司里，PM的存在往往是因为工程师不了解业务，但这种分工本身就制造了效率损耗和政治博弈：

> "我们苹果能够避免这个问题，是因为团队规模相对较小，且不推崇纯管理的角色。所有想要晋升的工程师必须是在技术上最优秀的人，能够读懂他们的代码，这样就不需要通过制造叙事来提升自己，因为他们的工作会被真实的结果所认可。"——葛小川, APP CPEO

### 4.4 人才哲学：密度优先、AI优先、Underdog文化

**Headcount极度克制**

Adam多次公开表达了对扩张团队规模的抵触。并不是为了"省钱"，而是对组织退化规律有差异化认知：

> "I never understood why these same people who have exceptional ability end up churning out of companies when those companies scale. Why does companies become less efficient when they scale? Why is there more process when companies scale? So we wanted to build a culture that inspired that same entrepreneurial spirit as it scaled, and that is predicated on building a team of doers, getting process out of their way and allowing them to execute as if the company was still 10 people."——Adam Foroughi

Adam在MS会议上也表达了AI对人效的影响：

> "The reality of generative AI and LLMs is that they act as a force multiplier. A 10x engineer, when armed with these tools, becomes a 100x engineer. However, a 1x engineer only becomes a 2x engineer. The gap between the best and the average isn't closing; it's expanding exponentially."——Adam Foroughi

APP的裁员节点往往是股价最高位，与传统的"困境裁员"完全相反，本质上是AI提升人效后的结构性瘦身。如2024年11月，APP市值刚突破1000亿美元大关，却在这波“高股价”背景下进行了裁员。此外，2022年6月（约300人）的最大规模裁员也属于这一逻辑的延伸，2021年并购Adjust曾让公司人数从902人“虚胖”至1594人，在2022至2024年的持续整合期内，大量相关岗位逐步被APP本体或AI工具所替代。

CFO Stumpf明确表示，未来新增headcount将以几十人为单位，而非规模化扩张。

**选人标准：Underdog偏好**

APP选人不迷信名校或大厂背景，更看重行业深耕、潜力与特定资源经验。

> "有很多技术强、职业上有雄心壮志的人，他们更关注解决问题本身，而非解决问题的方法。这种候选人与我们之间可能更容易产生文化上的共鸣。""名校毕业生就是一个标志，这证明了他们聪明且勤奋。此外，毕业后选择加入一家不那么知名的公司工作一到两年，但自身发展非常快速，最终发现无法再被这个环境所容纳。这样的候选人来到这里后，往往会取得非常显著的成功。"——葛小川, APP CPEO
> "超过60%的岗位来自内推，利用属性相近的人带属性相近的人的裂变效应保证执行力标签一致；招聘时明确要求游戏BD候选人必须真正玩过游戏，纯懂广告不够。"——APP销售总监

**高淘汰率与极速晋升并存**

Leader预期非常快就带来影响，没有所谓的转岗或缓冲期。但另一面是，如果你表现出色，晋升速度极快：

> "Leaders are expected to show impact within the first two months, without a lengthy ramp-up period." ——Shubham Agrawal, APP ML Core Engineer
> "At APP, if you're good, your manager will call you and say, 'Congratulations, you got promoted.' You will be passive about it as an employee. In other companies there is a committee, you submit a package, you need to show that your performance is expected from the next level for at least six months — so it takes years until you get promoted."——Oren Sar Shalom, APP Former Staff Research Scientist

### 4.5 文化底色：技术信仰、Extreme Ownership与"永远是underdog"

贯穿APP所有组织设计的底层文化可以概括为三个关键词：

**技术信仰——一切决策以技术和数据为准绳，而非关系、层级或直觉。**

> "我们的文化首先是比较偏技术信仰，大家都是优先相信技术，也就是技术跟数据……这种心智是纯工程师纯理科生。"——APP销售总监

**Extreme Ownership——赋予每个人全部决策权和责任，容忍失败但不容忍不作为。**

> "If you allow them to take ownership responsibility and take action without fear of downside, that team develops to have more responsibility, more ownership and more pride in what they're doing because they have the ability to take those shots and learn from them."——Adam Foroughi
> "我们的审批流程也是非常短的……很多我们可以不需要审批，或者是一些小客户，可以快速地先批了先跑，然后后审，就跟广告一样先上了之后再先发后审，这种迭代文化还是比较明显。"——APP销售总监

**永远是underdog**——**无论市值多大，都维持创业公司的饥饿感和危机感。**

> "On culture, we embrace being underestimated. A skeptical market sharpens our focus and pushes our teams to execute. Our revenue per employee remains among the highest in the world because we build the best and most scalable products in our category."——Adam Foroughi
> "大部分人都非常聪明，并且非常刻苦……大家都有勇气去挑战常规，不会因为做出与他人不同的选择而感到焦虑。"——葛小川, APP CPEO

## 5.今天的APP在解什么关键问题

### 5.1 电商广告能否规模化

**电商的归因链路比游戏更复杂**

> "In gaming, the loop is very tight. A user clicks, installs, and plays—all within the app ecosystem. E-commerce is a different animal. You have a customer seeing an ad in a mobile app, but the conversion happens on a mobile web browser or even a desktop."

电商的漏斗更长、更复杂，中间的影响因素也更多。分为：

1. 发现层（Discovery）——Meta是典型代表；

2. 搜索与转化层（Bottom of funnel）——搜索广告，未来还会有基于大语言模型（LLM）的广告；

3. CRM用户存量运营。

这三层各自对应不同的数据需求和技术挑战。在游戏中，APP靠MAX SDK的闭环数据三角就能覆盖从展示到付费的全部链路。但在电商场景中，用户从"看到游戏内广告"到"在品牌官网完成购买"中间跨越了App和Web两个世界——数据链路断裂了，电商的挑战在于信号的稀疏性。

> "The challenge with e-commerce is the sparsity of signals. When you move outside of gaming, you’re dealing with a much longer conversion funnel and a lot more noise in the attribution data. The feedback loop for the AI is inherently slower because the data is more fragmented."——Adam Foroughi

**重建电商数据三角是第一优先级**

APP进入电商的第一步不是去优化算法，而是重建数据闭环。其产品演进路径清晰地反映了这个优先级——从"有信号"的场景出发，逐步向"无信号"的场景推进：

- 第一步是通用候选模型（Universal Candidate），一年半前推出，依赖"曾有互动行为"信号，技术难度最低。
- 第二步是新客活动（Prospecting Campaigns），去年10月推出，瞄准"访问过网站但从未下单"的潜在客户——模型开始依赖AXON Pixel和Adjust的跨域身份映射能力。
- 第三步是新访客活动（Discovery Campaigns），26年2月推出，直接为广告主获取"从未访问过其网站"的纯增量新客——这是广告界最具价值也最困难的转化形式。

在数据重建过程中，Axon Pixel的部署速度是关键指标，尽管Pixel没法像SDK一样彻底解决闭环数据问题：

- 可以理解Axon Pixel在DTC客户中扮演着SDK在游戏客户中的作用，可以绕过网页Cookie，Serve-to-serve将关键事件回传给APP，让APP在Last Click逻辑下确认归因。Pixel需要广告主（尤其是Shopify商家，现在可以一键部署）在建站时安装。
- Axon Pixel回传的核心数据有三类：1）行为漏斗：产品浏览、加购、发起结账、购买；2）商业价值：SKU类目、AOV；3）用户匹配数据：脱敏邮箱、IP地址等。
- 与游戏的SDK回传相比，信号更弱、特征深度更深：Pixel回传用户IP或脱敏邮箱，算法要通过概率去推测“你是谁”，要通过游戏/工具流量中行为来预测用户的电商行为，而且未来行为是多元行为（是否加购、客单价），Pixel回传的特征不局限于概率而是“SKU”级深度。

**商业化路径从平台自营电商开始优化算法，到mid-size DTC规模化**

**第一阶段（23H2-至今）：合作头部平台级自营电商如Shein、Temu等，共建数据优化算法。**

平台级自营电商预算体量足够大、品类覆盖足够广、且愿意和APP共建算法。目前已经完全跑通，电商客户一般会在ROAS达标基础上持续放量，直到ROAS迫近渠道目标，广告主分渠道ROAS要求会不同，跟渠道的定位以及产品（拉新、唤活、高质量客户等）相关。

> "我们应该是整个平台体系上首批去尝试的商家……23年下半年开始试运营，以独立的高端子品牌作为试水对象。24年上半年基本我们就进入快速放量期了。"“APP在新人群的投放表现是比较可观的，Shein对它定位是一个增量的渠道，拉新 ROAS 稳定在5.5+，显著高于 Meta 的3~4.5x。”“整体预算分配，试水阶段3%，24年提升到7%，25年接近10%，预计26年持续提升，长期预算预估Meta 26%、Google 24%、TK 20-25%、APP 15-18%”——Shein，投放渠道运营总监，202603
> “25年2月，开始数据共建，两个维度。第一个是归因数据——你要把你的归因数据给我。第二个是算法整合——我们认为我们用什么样的算法更合适，你要允许我参与到你给我投放广告的算法共建里。”“Temu24年试水投放几千万美元，总投放70亿美元；25年放量2亿美元，总投放81亿美元；26年预估7亿美元，总投放大比例增加到139亿美元（国内少投300亿人民币，temu多投300亿人民币，除非有监管限制）”“新客获取成本CPA大概要比Meta低20%左右……但回本周期上并没有比Meta有优势，做Hold out实验不是很理想，没有带来新客户但也有可能是我们北美新客都触达至少一遍了。”——Temu，投放运营总监，202603

APP 2025年电商收入6亿，对应广告主支出18亿美元，主要由平台自营电商贡献，其中头客Shein和Temu两家25年贡献广告主支出就8亿美元，仅两家目前26年年框就增长到13.5亿美元，同比增长69%，平台自营电商的基本盘可预期地稳定增长。

**第二阶段（25H1-至今）：从平台电商到mid-size DTC品牌，规模化胜负手**

中国跨境电商出口规模3,400亿美元，其中DTC模式1,200美元且增速远超大盘，欧洲市场DTC规模1,460亿美元，北美市场DTC规模2,350亿美元，全球DTC市场基本保持10%同比增速。DTC商家投流费比基本在20-30%之间，意味着全球DTC市场5000亿左右GMV下，投流费空间可以达到1250亿美元，对于APP来说是规模化的胜负手。

GTM上，打通Shopify应用和归因集成，快速打开DTC市场，AXON pixel部署量从2025年9月底的几乎为零，快速增长至2026年1月初的约22,000个广告主域名。

> “我们花了大量时间完善 Shopify 应用和归因集成。现在，电商商家接入我们的门槛几乎为零。这是算法能够跑通的大前提。” —— Adam Foroughi，UBS AI Conference，202512

**要攻克mid-size DTC市场，素材自动化能力是胜负手**

**视频素材将成为"新定向"**

APP来做电商广告的定向逻辑从传统电商广告如Meta的"人群标签"转向"素材信号"，它不试图预测用户想买什么，而是寻找创意组合与经济价值的最优匹配。换言之，在AXON 2.0的算法范式下，你拍什么样的视频就会吸引什么样的人——AI根据素材产生的第一波用户反馈信号，自动在10亿+流量中寻找更多类似的人。

> "Signals are the key driver of performance, I would say now, as opposed to targeting settings... creative then just becomes so much more important, and the variety of creative becomes important... to feed the algorithms and feed these signals to let the creative do the targeting."——Brian, Gymshark数字营销负责人（APP customer）
> "We are not trying to predict what this user wants to buy, but it's more about understanding that if we kind of showed this kind of ad… what kind of combination will maximize certain value …APP is not there to understand like what kind of products that the user is interested in buying from the business."——Shubham Agrawal, APP ML Core Engineer

电商客户的素材短板是瓶颈，Adam认为生成式AI技术本身会迅速普及成为一种Commodity，真正的胜负手在于测试和反馈的绝对速度。而APP的AXON竞价引擎与素材生成引擎在同一个底层运转，将“AI生成 -> 投放 -> 获取转化信号 -> 调整生成参数”的循环压缩到了极致，有天然的优势。

> "游戏开发者非常精明，一个Campaign能测试50,000个广告素材；而电商等新客户最多只有1,000个。这种巨大的素材多样性鸿沟限制了推荐系统的发挥。APP构建了基于LLM的Multi-Agent（多智能体）架构来生成静态图片和视频广告。静态图片生成已在试点中，视频模型即将推出。"——Adam Foroughi, Morgan Stanley TMT Conference (2026.3)
> "Everyone has generative AI tools now, including Google and Meta. Our advantage is not just the ability to generate a video; it’s the closed-loop integration with AXON. We can take a GenAI-produced video and test it across two million auctions per second. Within ten minutes, our system knows if that creative is a winner. If it’s not, it’s discarded; if it is, we instantly flood it with scale."——Adam Foroughi

目前基于LLM的Multi-Agent（多智能体）架构来生成静态图片广告的产品刚刚上线，视频广告自动生成产品预计在26Q2上线。

**Adam更大的野心：从Discovery到CRM，做电商客户的全链路**

从创始人的隐晦表态和现员工的访谈中，可以预料APP不满足于只做电商广告的"发现层"（这是Meta的主场），而是试图沿着漏斗向下延伸，最终触达DTC品牌的CRM和存量运营。

这一野心已经有了产品层面的布局。APP通过Shopify集成切入电商商家安装AXON Pixel后，APP开始积累品牌的全域用户行为数据（访问、加购、下单、复购、邮箱/IP），这些数据正是CRM运营的基础原料。

> "With the Shopify integration, it's a **'**set-it-and-forget-it' model. Historically, these brands had to hire expensive agencies or large internal teams to manage CRM and UA. Now, they just click a button, give us access to their signals, and AXON optimizes the full lifecycle from discovery to repeat purchase. We’re turning marketing from a labor-intensive cost into a fully automated arbitrage."——Adam Foroughi

从投资视角来看，电商三层漏斗中，Discovery层的竞争最激烈（Meta、TikTok、Google都在），但CRM层的竞争相对稀薄。如果APP能凭借Pixel + Adjust的数据基础设施，从"帮品牌获客"延展到"帮品牌运营存量用户"，其单客户ARPU和粘性将大幅提升。

**电商广告的进展信号（截至2026年初）**

-  Jefferies 4Q25对30个电商客户广告调查显示：在已使用APP的电商广告主中，APP已占其4Q25预算的14%，成为明确的"第三大渠道"（仅次于Meta ~31%和Google ~32%，领先TikTok ~6%）。
- 这些广告主预计2026年将APP的预算份额进一步提升至14.5%。30家调查对象中仅2家计划降低APP份额。
- Northbeam数据显示，APP在DTC品牌中的ROAS比Meta高约45%，比次级平台高约74%。（初始状态，参考性低）
- 87%的调查广告主已试用Prospecting Campaigns，60%表示带来了显著或中度的新客收入增长。
- 自动化产品Self-serve Ad Manger 和GenAI视频素材生成产品预计26年Q2推出。

### 5.2 供给侧扩容是APP的10x Bet

拆解一下APP在买量端市占率30% = 流量端自有平台MAX市占55% x Appdiscovery竞胜约为50% + 非自有平台市占45% x Appdiscovery竞胜10%。这也意味着在整个“网盟流量”里，APP已经将30%的“优质量”竞胜拿下，成功扩展电商领域，理论上可以提高每个潜在request的eCPM（游戏大R一直推游戏广告会到转化瓶颈，但推电商广告可以增加潜在转化），但流量天花板依旧是100%网盟流量，而APP已经拿下30%。

这也是为什么公司竞购TikTok，对APP而言意味着巨大的自有流量池。竞购失败后APP提出了雄心勃勃的“Inverted Meta Model”社交应用战略：

> “In a world where AI lowers the cost of creation, content will explode. Our goal is to build a platform that doesn't just host content, but uses our decentralized AI infrastructure to solve the discovery problem from day one.”——Adam Foroughi
> “我们正在架构一个下一代社交平台的数字骨干，它是AI原生的，并且在设计上是去中心化的。”“在第三方平台就是杀出重围确实非常困难的...但我觉得这就像一个在一个harsh环境里面长出来的植物，虽然你遇到很多困难，但这些困难本身是让你变得更加的坚韧。我觉得AppLovin在这种第三方平台厮杀这么多年，其实我们的技术、我们的文化其实都变得非常非常坚韧。那么现在再去打造这样一个自有流量平台，我自己其实是抱有非常非常乐观的一个愿景。”——葛小川, APP CPEO

## 6.投资Thesis

1. **游戏基本盘：稳定增长**

  a. 算法飞轮带来的Baseline增长是结构性的，不依赖外部市场增长，年baseline提升20-30%；
  b. 每年全球游戏市场的内生增长～10%，投变一体的游戏广告主eCPM自然增长～5-10%；
  c. 结合市场结构性优化，APP的手游核心业务每年30-40%的增长确定性高。

> “Currently, we have a 1.3% conversion rate... but we model a 5% ceiling for the platform.”——Adam Foroughi

2. **电商广告：路径验证，规模化已见曙光**

  a. 头部客户强信号，平台自营电商跑通，APP成为继Meta、Google、Tiktok之后的第四大渠道，头部平台级客户的budget份额可以作为全市场budget分配终局的核心参考；
  b. 打通DTC规模化的基建逐渐到位，数据闭环Pixel、自动化投放Self-serve Ad Manager、GenAI素材生成SparkLabs，战略聚焦突破核心卡点——素材自动生成能力，26Q2上线的视频广告生成产品将加速电商广告规模化；
3. **组织穿透：算法是果，组织是因**

  a. APP的组织内生特征——超高人才密度、Simplicity、反会议文化、Engineering-driven、No PM、Entire Stack Engineer以及其带来的极速迭代的基础设施无法轻易克隆，构成了投资AppLovin最大的护城河；
  b. 人才密度策略创造了正向自我强化循环——Adam坚定用AI把最强的工程师的产出放大100倍，也不愿意用规模换组织退化；
  c. 这是一个"越用越强"的飞轮，而竞争对手面对的是"越大越慢"的困境，APP的组织设计从根本上消灭了一切减速机制，让最强的人解最难的题。
4. **估值框架：不是一道简单题，需要等待合适的价格**

  a. 估值层面需要耐心。APP的市场估值1,492亿美元，对应约为26E PE 30x、EV/EBITDA约 23x，对于一家70%增速的公司并不算贵，但也没有明显的安全边际
  b. 若游戏业务维持25%年化增长、电商业务2026-2028年每年增长70%（参考AXON 2.0后的游戏广告增长），2028E总收入可达约145亿美元、EBITDA约120亿美元，按20x EV/EBITDA对应约2,400亿美元企业价值——3年约60%的上行空间。理想的介入窗口在估值回调至1,000亿美元左右（对应约17x 26E EV/EBITDA），届时风险收益比显著改善，3年2倍的回报预期更具备吸引力。

**Appendix：**

| 指标 | 2024A | 2025A | 2026E | 2027E | 2028E |
| --- | --- | --- | --- | --- | --- |
| 总收入（$M） | 3,224 | 5,481 | 8,000 | 10,830 | 14,500 |
| *YoY增速* | 75% | 70% | 42% | 35% | 34% |
| 其中：Gaming（$M） | 3,224 | 4,861 | 6,100 | 7,600 | 9,500 |
| 其中：电商（$M） | - | 620 | 1,900 | 3,230 | 5,000 |
| Adj. EBITDA（$M） | 2,412 | 4,433 | 6,362 | 8,900 | 12,035 |
| *EBITDA Margin* | 75% | 81% | 83% | 83% | 83% |
| Gross Ad Spend（$B） | 9.2 | 15.7 | 21.9 | 30.9 | 41.4 |
| *电商收入占比* | 2% | 8% | 17% | 30% | 34% |

**Reference：**

| **Type** | **Notes** |
| --- | --- |
| **NotebookLM（欢迎对话）** | [https://notebooklm.google.com/notebook/14c4af1f-478b-4a98-830b-b2711956a1fb/preview](https://notebooklm.google.com/notebook/14c4af1f-478b-4a98-830b-b2711956a1fb/preview) |
| **Previous Study** | [Applovin‘s Org](https://docs.xiaohongshu.com/doc/514f6012e3be2f339d917cce3b422e72)<br>[AppLovin核心问题和主要事实](https://docs.xiaohongshu.com/doc/703faa299bcc16e9ba383b203658562b)<br>[Applovin AI Value Add 桌面研究](https://docs.xiaohongshu.com/doc/12135cbc2fa059927513a4d25f6d321a) |
| **Mangement Interviews** | [✅Applovin‘s Adam Foroughi](https://docs.xiaohongshu.com/doc/30527ad692bf59ed14fd95ce4d108fa2)<br>[Applovin‘s 葛小川汇总](https://docs.xiaohongshu.com/doc/f5111acb9f639eadd7a768d666c00dc2)<br>[MS Conf. Applovin keynote](https://docs.xiaohongshu.com/doc/5afd547777f72f5e38c0512a0ccf4a42) |
| **Employee Interviews** | [AppLovin - Former Staff Research Scientist](https://docs.xiaohongshu.com/doc/6a53b8aa457323903f308329b474b421)<br>[Applovin-Alex Head of BD LATAM-20260318](https://docs.xiaohongshu.com/doc/65a8cc9a7bb9a9ff770294b702922226)<br>[Applovin-国内算法Research scientist-20260315](https://docs.xiaohongshu.com/doc/6aac05e380814453bd611fec1dc4e2a2)<br>[Applovin-销售总监-20260309](https://docs.xiaohongshu.com/doc/f77500d734721176e421fa28af00087c)<br>[Applovin-Member of Technical Staff Shubham Agrawal-20250309](https://docs.xiaohongshu.com/doc/7b1ef935a8b33c62f14fe24f3cd871c2)<br>[Applovin-HR专家-20260309](https://docs.xiaohongshu.com/doc/67cfab9e1adbf27226eac5ea1b926340)<br>[Applovin-商业化专家-20260310](https://docs.xiaohongshu.com/doc/2ed0d2c9c955f3c80d5a7b3fb73c8d4b) |
| **Competitor Interviews** | [✅Meta Audience Network: Spotlight on Competitive Threat to AppLovin and Unity](https://docs.xiaohongshu.com/doc/b04a79c737009e81e149e2a848435f20)<br>[Unity专家纪要-20251216](https://docs.xiaohongshu.com/doc/f7c0867c2421c999104bb1487664a05d) |
| **Customer Interviews** | 自营平台级电商客户（头部广告主）：<br>[Shein专家：投放渠道运营总监-20260317](https://docs.xiaohongshu.com/doc/30567f60167f9c88db2f41d919e385b3)<br>[拼多多Temu专家：中台运营总监-20260318](https://docs.xiaohongshu.com/doc/d9b43adddac5895519f4528f68925dcb)<br>DTC电商客户（mid-sized广告主）：<br>[Gap-Global Media Channel Strategy & Center of Excellence Leader-20260319](https://docs.xiaohongshu.com/doc/47e54445995e3efb0329691370a15a5b)<br>[Applovin: Self-Serve AXON Ads Manager Launch, Margin Maintenance, Non-Gaming Ad Moat](https://docs.xiaohongshu.com/doc/86bde0a499e427b066a33104ec537115)<br>[AS Beauty-VP of Growth-20260319](https://docs.xiaohongshu.com/doc/2554f8dc934e685d0c9d7d41e8685ceb) |

