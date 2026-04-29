# Anthropic 的黄金年代_20260325 副本

在中期文档 [Anthropic Overview_20260313](https://docs.xiaohongshu.com/doc/ea6ab54610a9768e4627d3d96e0bd405) 的基础上，新增了部分观点

*注：本文 95% 由 Claude Project 完成，人工修改的部分约占 5%（主要包括错别字的校准、Topic Sentence的修改等，全程大概耗时 10min）*

### **Reference**

*较中期文档有12个新增的source*

| **Employees** | [Anthropic RL Engineer ex-Meta_20260213](https://docs.xiaohongshu.com/doc/32201921e6cc17347210c79c5933bfd0)<br>[Anthropic Member of Technical Staff_20260315](https://docs.xiaohongshu.com/doc/e62fdbdd480556ffee8842987782fb37)*（新增）* |
| --- | --- |
| **Competitors** | [OpenAI Agentic RL Researcher_20260325](https://docs.xiaohongshu.com/doc/7dbac2459d4a0235d03665e7191d8520)*（新增）*<br>[Minimax Co-Founder Yeyi & 田渊栋_20260322](https://docs.xiaohongshu.com/doc/701f6666b1e86c2e2cac8666c2520982)*（新增）*<br>[Ex-MSL Post-training Researcher_20260316](https://docs.xiaohongshu.com/doc/aa8001e69539f2ce8772a689129dece6)*（新增）*<br>[OpenAI Infra Engineer_20260318](https://docs.xiaohongshu.com/doc/1fed61a9aa2174593d7c742c899687ea)*（新增）*<br>[xAI Coding Lead_20260322](https://docs.xiaohongshu.com/doc/0221bd64877c95d89400824d33f7e60d)*（新增）*<br>[xAI Coding Researcher_20260315](https://docs.xiaohongshu.com/doc/da064786edd4661f8837a95dfbfbf5e1)*（新增）*<br>[Bytedance Agent Platform PM Lead_20260123](https://docs.xiaohongshu.com/doc/aa65823b36258df6cdcc1c9eeb17ab55)<br>[Bytedance Agent Platform PM Lead（第2次）_20260213](https://docs.xiaohongshu.com/doc/b7390ccad45fda61ba00fc95aa99a7ac)<br>[ex-Doubao PM, Consumer Agent Founder_20260213](https://docs.xiaohongshu.com/doc/1b03e993854fd868e582e42eaecccb4d)<br>[Minimax Coding Post-training Researcher_20260207](https://docs.xiaohongshu.com/doc/c1caa04fa94c13a86a48ac3aecfb2e7d)<br>[阶跃星辰_办公 Agent PM Lead（千问PM)_20260206](https://docs.xiaohongshu.com/doc/736ecb9cc2a1b7cc67a94fb3d1f3617a) |
| **Clients & Users** | [贾扬清  & 黄东旭 Dinner Talk（1/2）_20260321](https://docs.xiaohongshu.com/doc/201ee885f92d506dbc066be4085e1103)*（新增）*<br>[Apple Siri Machine Learning Engineer_20260313](https://docs.xiaohongshu.com/doc/d5c9261063fbd88822b3ab6b3fa95f2f)*（新增）*<br>[Amazon Post-Training Researcher_20260317](https://docs.xiaohongshu.com/doc/7eec084979aa35d7d5c2e7a4ad31cd4e)*（新增）*<br>[Firework RL Engineer_20260317](https://docs.xiaohongshu.com/doc/173910a5017fd4c026250ea861b8430b)*（新增）*<br>[Meta VP of Engineer_20260310](https://docs.xiaohongshu.com/doc/11540c10e662c42f49a8999315811b8d)<br>[Meta AI Platform Engineer_20260308](https://docs.xiaohongshu.com/doc/bc3f7228b3850067a3b66ab318b1c676)<br>[光年之外AI PM_20260129](https://docs.xiaohongshu.com/doc/059cd7a2f925c798a243a0424797640f) |
| **Ecosystems** | [Composio Founder_20260307](https://docs.xiaohongshu.com/doc/bdf6a6e5e38b0108bde8495692ff1dbc)<br>[ASW Corp Dev Deal Lead_20260318](https://docs.xiaohongshu.com/doc/0806016e49e16df232577ac1c54059c3)*（新增）* |
| **Investors** | [Sequioa LLM Investor_20260304](https://docs.xiaohongshu.com/doc/1b812473bffe6b6dee8a3fbfac9f3c16)<br>[Lollapaloza Capital Investor/ 王慧文家办 _20260306](https://docs.xiaohongshu.com/doc/0caa19c52078cf14015aba56d6d0f559)<br>[Monolith Public Equity Partner_20251230](https://docs.xiaohongshu.com/doc/7fc5941ca56eec55bd13126ea29fc1d9)<br>[拾象 co-founder_20251118](https://docs.xiaohongshu.com/doc/29ae6185f9e7d04440bc2f1ec4146b3b) |

### **一、组织**

#### **Cowork 用 Claude 写 Cowork，每天一个 feature 的节奏来自于闭环本身**

Claude Cowork 从去年 3 月开始做，能做这么快就是因为一套极紧的迭代 loop：内部员工就是核心用户，有 idea 直接做，做完立刻拿到 feedback 和 data，再继续迭代。从写到发布，内部测试一两天，没有人 complain 就直接 push。这不是产品管理能力，是系统设计——把最短的反馈路径内建进组织。

> *“*最想去的是Anthropic,他们的自动化程度最高。整个* Developer flow *里面，写代码只是其中一部分，还有* compile*、*run*、*verification*，然后去监控。就是整个软件公司的运行，包括非常多的层面。大部分人还只是在写代码这一小部分。其他的部分，也要交给* AI*。--- xAI Coding Lead，2026年3月

这套机制的飞轮效应已经可测：Anthropic 内部的 Claude Code 比外部版本快 10 倍。一位内部 researcher 的原话是"很简单朴素"——内部用的模型远比市面上好，用这个模型来构建下一代模型，就是 compounding，就能一直领先。对比字节：Seed 的人跑到抖音楼下去蹲数据，刀耕火种训模型，因为用的不是最好的模型来训下一代模型，飞轮根本转不起来。

Anthropic 定义了一个 Idea Journey，专门规定了怎么把一个好的 idea 落成一个产品

> Anthropic内部有一个'Demo Book'机制：员工觉得什么东西好玩、有价值，直接写进去，不需要任何人批准，只要跟**manager**通个气。Manager的工作是跟上级一起从Demo Book里筛选：哪些是好idea、哪些现在不成熟、哪些可能半年后有大爆发。这套机制充分发挥了底层员工的创造力——那些觉得自己有两下子、不愿意被上级瞎指挥的人，在这里有直接的idea输出通道。

#### Pass/No Pass 的绩效设计，把内耗压到最低

Anthropic 的绩效评估只有 pass / no pass，故意没有 3 档、5 档的层级。原因很直接：细分层级会让人去抢功劳、去规避那些"对公司重要但不帮我升职"的 project。晋升的决定权从绩效周期解绑——manager 看你的工作耀眼到无法忽视，直接提拔，不需要等任何 review cycle。

具体案例：一个人 2024 年底加入，25 岁，一手从零建了一个 project，2025 年就升了 manager；另一个人 2025 年 9 月入职，25 岁，今年 2 月就当了 manager——从入职到 manager 只花了 5 个月。还有一个人 26-27 岁，去年连升两级到 L8，相当于大厂的 principal 级别。

> *“*他自己建了好几个组，建了好几个完全不同、完全没有人想要的方向*……*他做这些东西不是为了* promote *而* promote*，而是为了把这件事做成。在这里，做成是最重要的事情。*”*--- Anthropic Member of Technical Staff，2026年3月

Manager 在 Anthropic 不是 pure people manager，而是同时做 IC。"活太多了，你如果只做 people management，你就只是在指挥别人，实际上你这个组的进展完全看不懂。"这意味着 manager 本身的技术判断是真实的，而非空洞的。Job security 比大厂好很多，大脑里没有这个威胁，就能专注在工作本身。

#### 面试有一轮其他 lab 没有的 Culture Interview，在筛 Mission Fit

Anthropic 的面试流程中有一个专门的 Culture Interview，问的不是 system design，而是"讲一个你职业生涯中处于 ethically conflicted 境地时的选择"。它在筛选的是：你在公司利益和个人意志冲突时，能否 serve the mission。

> *“*他会选一些就是愿意是* team player*，他不会选那种个人英雄主义的。有个做* health AI *做的很强的* researcher*，他面试的时候说*"*我是这方面最强的人，没有人比我更强*"*，然后就因为这个被挂了，虽然他后来去* OpenAI *管了一个很大的* Health AI *团队。*Anthropic *喜欢那种* serve the organization*、*sacrifice the mission *的人，就是我的目的是要* serve *这个组织，而不是凌驾于组织之上。*”*--- Anthropic Member of Technical Staff，2026年3月

一位 Apple Siri ML 工程师反馈，technical round 过了，culture round 被挂，因为面试官在看的是"这个人有没有 philosophical / profound 的思考方式"。不是要假装 altruistic，而是要检验你是否真的对 AI safety 这件事有过认真的思考，还是只把它当 checkbox。整个流程还多了一轮 technical 和 Project Dive（讲你之前做过的项目），由 hiring committee 的 panel 做最终决策。

#### 去年 1000 人，现在两三千人，增量主要在 FDE 和 enterprise sales

Anthropic bar 很高但招人速度依然很快，每次 orientation 都有几百人加入。去年 3 月还是 1000 人，现在可能已经两三千人了，增量主要在 forward deployment 和 sales 团队——这直接对应企业战略的转向。Anthropic 已经不需要 intern 了，需要的是能 manage agent、把事情推动起来的有经验的人。Research 那边招人相对慢一些。

#### 从 CIA 招安全专家，代码跨组隔离，信息封闭是护城河的一部分

Anthropic 专门从 CIA 招了安全专家来管信息安全，代码在不同组之间是隔离的——做 post-training 的人看不到 pre-training 的代码。不同 team 之间无法互看代码，各组进展相互不透明。从竞争角度看，外部几乎无法通过人员流动逆向还原 Anthropic 的训练 recipe——只能从模型表现推断，信息优势受到结构性保护。

> *“*他们公司好像就是比较封闭，据说就是* code *好像都不是所有人都能看到的，不同组可能就看不到别的另外一个组的* code*。他们还招了个* CIA *的人专门看怎么把公司的信息安全做好。*”*--- xAI Researcher，2026年3月

Anthropic 已经把给新员工的股权形式从 stock options 切换成 RSU。公司估值飞升（从面试时的 70 亿到入职时翻了好几倍），strike price 已经高到员工根本付不起 exercise 的钱了。RSU 相比 options 杠杆更低——但也意味着风险更小，且估值折扣从原来的约 70 折（strike price = 市场价 × 70%）变成 0 折。相比 OpenAI 给 research 全员发 100～200 万美金 retention bonus 来抗衡 Meta TBD lab 挖人，Anthropic 的应对方式更被动——employee 只能等 IPO。这种"绑定感"双面起作用：留住了核心员工，但也让潜在候选人在 total comp 对比中觉得 upside 不如 OpenAI 直观。

> "现在他们给 RSU 了，不给期权了。就是因为公司变大了以后，这个估值很高了，你要去 exercise 的话，根本就不够钱去买完所有的股。现在是 RSU，等于你付出股数会少一点，但它这个没有杠杆了。"
> --- Anthropic Member of Technical Staff, 2026年3月

### 二、技术与模型

#### Pre-training 是 Anthropic 的真正地基，Post-training 是相对弱项但正在追赶

从外部视角看，Anthropic 的 pre-training 被认为是行业顶尖水准，而 post-training 是相对弱的地方。一位 OpenAI agentic RL researcher 的判断：Anthropic 从 RL 追到现在，刚刚还不错，但他们的 Post-train RL 的 scale 一直都比较小，包括整个 infra 和 recipe 在内。他们之前的 Post-train 都不是特别 work，Opus 4.5 发的时候就是这个情况，但因为 Pre-train 做得很好，所以也不耽误。

> *“*我觉得核心是多搞数据，特别是* Mid-Train *的数据，就是因为* Mid-Train *和* Pre-Train *足够强，所以才没那么依赖* RL*。另外一个论据是他们的* long horizon task *做得不如* Codex*，按理说是应该能做得更好的，可能就是* Post-train *弱了一点。*”*--- OpenAI Agentic RL Researcher

一位 Apple Siri ML 工程师的观察印证了这一判断：大家都觉得 Anthropic 的后训练很强。之前跟一个 DeepMind 的人聊，他说如果把 DeepMind 的 pre-training 跟 Anthropic 的后训练放在一起，这模型会非常强。DeepMind 和 OpenAI 在 RL 上都很强，但投 RL environment 很多人投 Anthropic，因为之前 Anthropic post-training 那帮人全部在搞 Inner。

#### Agentic RL 的 recipe 空白是当前最大的技术代差来源，Anthropic 是发明者

Reasoning model 的训练范式（COT trace、GRPO 等）经 DeepSeek 开源后已成公知，但 coding agent 的 agentic RL recipe 目前没有公认标准。Anthropic 是 coding agent 这个范式的发明者——第一个让人只用英语写 code、自己去跑 job、自行 debug 的产品。但 OpenAI 开始做起来之后，一两个月就追上来了，这正说明 recipe 一旦被复制，领先优势会快速压缩。

> *“Coding agent *可能有一些最新的菜谱，大家没有* share *出来嘛。以过去的* SOTA *就是那个* reasoning model*，*DeepSeek *已经把它接入了，大家都知道怎么搞，但现在是* agentic RL *就是没有一个* recipe*，就是* coding agent *的这个* recipe *可能最详细的没有* share *出来*……*就是相当于炒菜一样。炒菜就是假设这个大模型就是一盘菜，然后那个厨子就是这些* researcher *每天训练这个模型的。他同样的菜，同样的* ingredients*，同样的肉，不同的人他就做就会得到不同的效果嘛。*”*--- ex-MSL Post-Training Researcher，2026年3月

Anthropic 最早拿到 coding 相关的真实数据。Cursor 默认使用 Claude 模型，相当于从全球最大的 coding 工具中持续获取海量真实数据。用户在 Cursor 中的所有对话（代码问题、debug 过程、报错信息）默认被用于训练，除非主动关闭该设置。对比 Meta：Llama 没有足够的 C 端 coding 用户，缺少真实 coding 数据是 Meta AI 在 post-training 上最难弥补的结构性缺陷。

#### Post-training 工作流的 agentic 化，是 Anthropic ARR 爆炸增长的核心驱动

整个 post-training 工作流正在被 agentic 化：先用 Claude 生成大量样本数据，做自己的 post-training 实验，看在某个 benchmark 上能达到什么上界；把 recipe 留下来，换一个可以商用的 backend（千问、DeepSeek 等）重新生成数据；数据出来之后 agent 自动质检，发现问题自动修复，再进入下一轮迭代。每次迭代都要大量调用 Claude API，这是 Anthropic ARR 爆炸增长的核心原因之一。

> *“*这套* workflow *都是* agentic *的：数据出来之后* agent *自动质检，发现问题自动修复，再进入下一轮迭代。每次迭代都要大量调用* Claude API*，这是* Anthropic ARR *爆炸增长的核心原因。*”*--- Amazon Post-Training Researcher，2026年3月

#### 算力上有结构性劣势，但 AWS 深度绑定保障推理供给

Anthropic 目前用的是 H 系列 GPU，在卡的数量上不如 OpenAI（更不如 xAI），Google 的 TPU 被认为是基础设施最强的。这是 Anthropic 的相对劣势——如果有更多卡，模型提升速度会更快。在大模型训练端，实际上只有两种方案：TPU 和 NVIDIA GPU。Cerebras、AMD ROCm 等其他选项在主流实验室中没有实际采用。

> *“*我觉得* OpenAI *和* xAI *的这个卡是最多的，*Google *应该是最最好的。*Anthropic *如果有卡的话会更好，会好很多，会更强。*”*--- Anthropic Member of Technical Staff，2026年3月

### 三、战略

#### Anthropic 是所有模型公司里定价最高的，这是 enterprise positioning 的主动选择

Anthropic 内部员工直接承认："我们的这个 price 已经这么高了，你肯定不会再看免费的 model 了。我们是所有 model 里面最贵的。"这个高定价背后有两层逻辑：第一，Anthropic 主要关注 enterprise API，不需要打价格战来争 DAU；第二，即便被国产低价模型蒸馏、被 Gemini Flash 低价竞争，Anthropic 在 premium users 上的领先会持续。

> *“*我们这个* price *已经这么高了，你肯定不会再看免费的* model *了，我们是所有* model *里面最贵的。对于竞争，我们当然会更* concern Google *和* OpenAI*，而不是中国的那些便宜模型。*”*--- Anthropic Member of Technical Staff，2026年3月

收入结构：Enterprise API 占 85%，Consumer Subscription 占 15%。Claude Code 属于 Enterprise API，占 Enterprise 部分的 18%。整体年化 ARR 最近一周 run rate 已达 30 亿美元。

#### Anthropic 正在激进地做 Palantir——挖走 AWS 半个 BD 团队，打 5 亿美金以上大单

Anthropic 近期从 AWS 挖走了大量 BD 和 GTM 人才，专注做 5 亿美金以上的超大订单，对标 Palantir 的企业服务模式。这帮人是 sales/BD 出身，擅长做大客户关系，被认为"非常激进"。未来服务战略客户占 60%，针对 2000~3000 万美金的大单，会与 Palantir 正面竞争，可能会收购 30~60 人的小咨询公司，组建咨询团队，需要分给咨询公司 40% 的利润。

在过去一年，Anthropic 从 1000 人扩张至两三千人，新增人员大部分是 FDE（现场部署工程师）和企业销售。这是从模型公司向企业服务公司演进的重要信号，也是 ARR 快速增长的直接驱动力。

> *“Anthropic *的企业级动作*——*多招人、拿下基座客户、做更高* Margin *的客户，这几个点都是在为上市做铺垫。全面拥抱企业和国家客户，把* ToB *做得更重、更深。*”*--- Lollapaloza Capital Partner，2026年3月

#### 与 AWS 深度绑定是战略资产，但 10 年后云厂商会变成今天的 Cisco 和 HP

Anthropic 与 AWS 的关系是行业最深度的模型公司-云厂商绑定：AWS 保障了推理卡供给，GCP 流量约占 Anthropic 总流量的 1/3，是最大的分发渠道之一。但从长期视角看，模型公司和云厂商之间存在结构性张力。

> *“*我对云厂商都不太看好。我觉得它死不了，但是* in ten years time *就变成今天的* HP *了。就是大家还是会用你，你也还会涨，但是整体* business *没那么* sexy *了。我们以后可能就变成给这些模型公司搭* data center *的人了，这就没有意思了。今天我们的* margin *主要还是来自于我们* offer *的云之上的* service*。但如果以后大家不用了，模型指哪打哪，那我们以后多被动。*”*--- AWS Corp Dev，2026年3月

Cisco 和 HP 是上一波基础设施红利的最大受益者，但随着软件层价值崛起，它们的估值倍数一路压缩，从成长股变成价值股，最终变成无聊的 infrastructure 生意。模型公司建自己的 data center 和芯片只是时间问题——现在所有的钱都让芯片给赚到了，所有人都是在给英伟达打工，云厂商夹在芯片和模型之间，两侧都在被压缩利润。

> *“*有一天所有的模型会在所有的* cloud *上，就是不会有任何人。我觉得是有一致性的关系，时间长了，因为你的利益根本就是不一致的，所以你是保持不了的，只能短期内做朋友。*”*--- AWS Corp Dev，2026年3月

### 四、客户

#### Meta 是 Anthropic 最大的客户，每月 API 消耗约 4000 万美金

Meta 停工一周、全员学习 AI——公司把所有最好的工具都开放给员工，Claude、Gemini、ChatGPT 全都有，还有几千个内部 skills。那一两周整个公司写了几万个 skills，几千个放到 work 里，一周乘以 50，就能理解他们的 API 消耗——Anthropic 的 ARR 涨了约 60 亿美金，意味着每月 API 收入涨了约 5 亿美金，Meta 可能贡献了其中约 1/10，即一个月 4000 万美金。

Meta 的具体 use case：AI 平台（管理 GPU 集群的）正在变成 Agent-driven。以前训练一个任务跑 3-4 个小时，得过一会回去看跑好没有。现在 Agent 帮你监控——如果 Job Failed 是简单原因，Agent 直接帮你修了重跑；复杂的就帮你 debug，给出潜在的 3 个原因。这种非常基础的抠型类工作，Agent 是 100% 能替代的。

> *“*我之前可能是有* 20 *个项目，每个项目都要开会讨论，但现在我这几个项目不开会了，把它列出来哪些是项目负责人，然后每周三五点钟，所有人在一个* Doc update *一下进展，不用开会。然后如果有人没填，*agent *会去* remind *一下。搞完之后给我个总结，整体需要配个* action*。我们可以半小时把所有项目过一遍，给他们反馈一下。我就不需要开那么多会了，以前我觉得大部分时间都在开会，现在我真的可以做点其他事情了。*”*--- Meta VP of Engineer

#### Amazon 内部、安全创业者、投资机构：Claude 企业渗透路径清晰

在 Amazon 内部，研究员用 Claude Code 完全接管了之前因不懂 Java 而无法操作的工作：把 codebase 丢给 Claude Code，说清楚想实现什么功能，它自己搞定。AWS 账号切换、权限认证、提交 batch job、改参数设置，以前要打开网页一步步操作，现在就在 terminal 小窗口里跟它说。Routine 级别的功能开发和环境配置，Claude Code 已经几乎没有问题。

一位在安全公司做了 8 年的工程师，把毕生所学写成几个 skills 塞进 Claude，做了一个 security agent，效果超出他用过的所有产品，于是决定出来创业。他说把毕生所学都贡献给 Anthropic 了。他出来创业的逻辑：现在大家都在 vibe coding，所有软件都有很大的安全问题，Claude 只负责实现，不负责安全，这个需求是 vibe coding 需求的二阶导，非常大；而且模型非常适合做安全检测——就像警察进了犯罪现场，需要不断生成 hypothesis，模型在这件事上很擅长。

> *“Claude 4.6 *出来之后* verification *能力变得很强，之前* agent *做任务会偷懒漏掉一些，*4.6 *之后会强制把所有* task *都做完，结果非常好。这已经是我听到的第四个因为* Claude *模型变强而决定创业的人了。*”*--- Anthropic Member of Technical Staff，2026年3月

#### Claude Cowork 是最接近白领 agent OS 的产品，Google DeepMind 员工可用但其他 Google 员工不能

Claude Cowork 接入了更多信息源——公司内部文档、Google Meet 的 transcript 等，有更多 context，也会主动问 clarification question。它会在后台持续运行好几个小时，做完 deep dive 几天后还会再给你一个 update。在 Anthropic 内部，Cowork 是统一的一个 bot，但不同 org 有不同的专属 Coworker，敏感信息不会跨 org 流通。

一个有趣的竞争信号：Google 员工都想用 Claude Cowork，但公司不让——具体规则是 DeepMind 的员工可以用，DeepMind 以外的 Google 员工不能用。字节全公司都不能用。这种封禁本身就说明 Claude Cowork 已经成为了一个 mission-critical 的工具，其他公司才会认真对待这个威胁。

### 五、行业格局

#### Codex 由 PM Tibo 全闭环 lead，赛马机制跑出来的，是 Anthropic 最强竞争信号

OpenAI 把所有精力、所有人、所有卡都 all-in 在 coding，这是结构性的资源倾斜。Codex 有一个关键的组织因素：由 PM Tibo 来 lead，全闭环管产品、research 和 engineer，产品侧约 30 人，training 侧（post-train 阶段做 coding 的）有十个出头。product-first 的结构——research team 和 third party team 都是服务产品的——被认为是 Codex 能做成的关键。Tibo 之前做过模型，very tactical。

Codex 是 OpenAI 内部多个团队赛马的结果：内部有多个做类似 Codex 的组，最终 Tibo 那个组赢了，兼并了其他所有组，大一统。这套赛马机制让正确的方向自然浮现。从 GPT 1.3 开始，coding 训练已并入主训练流，不再单独训练。

体感上 Claude Code 和 Codex 的分歧已经出现。Codex 在"给一个 goal，自己不停 iterate，几个小时达到这个 goal"这种 long horizon 的 task 上更强；Claude Code 在 tool-use 场景更强，就是你设计很多工具，让它去调用和编排的时候是独一档。这不是 Anthropic 输了，而是两者已经形成了各自有优势的使用场景——这个局面会让高粘度用户两个都用。

> *“*他们现在知道会这么赚钱，他就也要把* coding *这块给做大。他把所有的精力、所有的人、所有的钱都用在* Codex *上，他是比我们晚* launch *了几个月，但结果上来看他没有什么理由会做的比我们差。*”*--- Anthropic Member of Technical Staff，2026年3月

#### Llama 4 失败解剖：sliding window attention 代码有 bug，选错架构一条路走到黑

LLAMA 4 的 pre-training 存在底层架构缺陷：虽然 context window 理论上可达 1B token，但输出长度无法超过 8K——超过则模型退化。根源是：当时内部对比了两种 attention 架构，其中 sliding window attention 的实现代码有 bug，导致实验结果显示 chunk attention 更优，最终选错了方向，一条路走到黑。在 reasoning 能力上，LLAMA 4 同样失误：Meta 的 reasoning 团队没有构造 COT trace 数据，错过了这波关键能力的跟进窗口。

> *“*那个是* context*，就是* LLAMA4 context *可以达到一个* billion*、*10 *个* billion*，但是它输，它的输出超过没有办法达到* 8K*。超过* 8K *就会变成傻瓜，那是一个底线的失误，一个底线的问题。我们测的时候，当时还有另外一个模型架构，就是现在大家都用的那个，就是做那个* long context *一个架构，我们当时也考虑了，但是我们选的我们那个叫* chunk *的，然后现在大家公认就是要那个* sliding window*。然后我们当时做实验的时候，虽然说* sliding window *写的是有* bug *的，所以就证明出来我们的那个* chunk *的效果更好，然后就一条路走到黑了。*”*--- ex-MSL Post-Training Researcher，2026年3月

Meta 工程文化的系统性问题：训练 codebase 缺乏 guardrail，所有人都可以随意写入，周五能跑通的代码周一必挂。500 个 engineer 共用一套 codebase，周五提交周一必崩。Impact 考核制度催生了严重的政治内斗，Zuckerberg 本人对此负有直接责任：他定了错误的 timeline、选了错误的领导层、催生了错误的文化。Meta 缺乏两类关键数据：没有大规模真实 coding user data（无人用 Meta AI 写代码），以及没有跟上最新 agentic RL 的 recipe。

#### xAI 已经比"人人自危"还高一个程度，算力有人有钱但 Infra 架构不够 AI native

xAI 有算力、有人、也花了很多钱买数据，Elon 也花了很多时间在 coding model 上，但依然没做好。内部从去年开始大力做 coding，依然没赶上。核心问题是：xAI 的 Infra 架构不够 AI native，从 Google 来的时候 copy 了 Google 的那一套，但实际上已经不适用于现在了。能蒸馏也是一个自己的能力问题，他们连 Claude Sonnet 4.6 都比不过。

> *“*你就想象成一个封建社会就行了。一个土皇帝，身边有几个太监。大部分人都是太监的。底下大部分人都是瑟瑟发抖。就在这个公司，你做的越多，错的越多。因为他没有* promotion *和* reward *机制，只有* penalty *机制，所以大家都会被* hacked *成尽量苟着。只要少做就可以了。*”*--- xAI Coding Lead，2026年3月

SpaceX 那边过来的人直接接管公司，把 coding 核心团队拆散，核心成员相继离职。高流动性反而降低了人才锁定：xAI 员工每半年可卖一次股票，有人工作一年卖出 700 万美元后离职。获利后的核心人员更容易离开，进一步削弱 team 稳定性。这与 Anthropic 的封闭策略形成鲜明对比。

#### OpenAI 是 reactive 的组织，被 Anthropic 的 coding 先发优势逼出了战略转向

OpenAI 长期聚焦两件事：最大化消费者规模，以及追求 raw intelligence 指标——而非优化 enterprise 实际使用场景。Anthropic 在 enterprise 侧的领先更多是 post-training 阶段调优方向的战略差异，而非纯粹的模型智能差距。Claude Code team 保持每天一个 feature 的发布节奏，而 OpenAI 则是每次发布一大批更新但节奏不稳定。

一个结构性优势：Google 内部禁止使用 Codex（因 OpenAI 是 Google 的竞争对手），Amazon 同样被限制使用 Codex 而只能采用自家产品。这意味着两大超大规模云和企业服务生态对 Codex 存在系统性准入壁垒。Claude Code 没有类似的竞争关系约束，在企业客户端的可及性更强。

Sam Altman 在内部跟 OpenAI 的人说，如果今年 Anthropic 的收入超过我们，你们也不要感到意外，我们的收入也会追上来的。这个表述本身说明 Anthropic 已在 coding 收入上对 OpenAI 形成实质威胁。

> *“OpenAI is a highly reactive organization. The pivot toward coding is a response to Anthropic's lead with Claude Code, not a forward-looking strategic choice. The speed at which Anthropic accelerated — Claude Code represented a massive leap over prior versions — genuinely surprised the market and forced OpenAI's hand.”*--- OpenAI Infra Engineer，2026年3月

### 六、估值判断

#### 最近一个月估值涨了 100B——这 100B 贵吗？

100B 美金在 20x P/S 的估值逻辑下，意味着多了 50 亿美金的 ARR，对应多了 4 亿美金/月的 API 收入。从微观体感来看这个数字是否合理：Meta 最近三个月整体的 API 收入只有 6000 万美金，但四五千万都是在最近 1 个月，其中可能 3500 多万美金都是在最近 1-2 周。

这就是指数爆炸的前期。从 Meta 的数据可以合理推断：光 Meta 4 月 API 支出就能到 1 亿美金，5 月就是 2 亿美金——完全可能，因为企业的 workflow 跑上了是不会停的。Meta 一年花三四百亿美金在员工工资上，马上就要裁员 20%，也就是六七十亿美金的工资省出来了，难道不能每个月多花 2 亿美金给 Anthropic？完全合理，而且比我们想象得更快。

M7 每年发薪水 4000-5000 亿美金，我们纠结的 100B 估值只相当于员工成本的 1%

美国 M7 的公司，每年给员工发薪水要发 4000 亿 - 5000 亿美金。我们纠结的 100B 估值，在 20x P/S 下只相当于 50 亿美金的 ARR，也就是 M7 员工成本的 1%。如果这 1% 的工资省出来，能换来生产力的大幅提升，这笔账显然是合算的。在这个框架下，"贵不贵"这个问题本身就问错了方向——这是一个结构性替代，不是一次性成本。

M7 每年给员工发薪水要发 4000 亿 - 5000 亿美金，我们纠结的 100B 估值，其实只相当于 50 亿美金的 ARR。也就是 M7 的员工成本的 1%，所以 doesn't matter at all——只要 Anthropic 能替代 M7 里 1% 的工作，这个估值就撑得住。

#### 一个微观 case：Palo Alto Networks 10 年 security 经验，两天变成一个 agent

周五在朋友家聚会聊到一个案例。一位在 Palo Alto Networks 做了 10 年的 Security 工程师，把他在 PA 10 年的 security 经验写了几个 skills，做了一个 agent，能看所有网站的安全状况。前天立刻现场帮 3 个 founder 找到了他们产品的安全漏洞。他说这个事情之前需要他一个 senior manager 带着 2 个 junior 工作 2 周，现在 Opus 4.6 安全搞定了。

这个案例的意义不只是"又一个 AI 替代人力"的故事。它说明的是：人类专家 10 年积累的领域 know-how，可以通过 skills 被 codify 成一个 agent，并在新的语境中无限复用。这是整个企业 AI 采用曲线背后的机制——每一个 senior expert 都是一个潜在的 skills 供应者，每一次 workflow 跑通都是一次不可逆的 adoption。

#### 今年是战略拐点年：大客户 BD、FDE 规模化、Sam 内部表态同时发生

三个同时发生的信号共同指向一个拐点：第一，Anthropic 挖了 AWS 战略大客户 BD 团队一半以上的人，同时和埃森哲合作，将 2.5 万的销售变成类似 Palantir 的前端销售，做大客户生意，单人合同金额可以到 5-10M USD；第二，今年多招了 1000 多人做 FDE 模式——这是 Anthropic 规模化企业服务能力的直接体现；第三，Sam 在内部跟 OpenAI 的人说，如果今年 Anthropic 的收入超过我们，你们也不要感到意外，我们的收入也会追上来的。

这三个信号叠加在一起，说明的是：Anthropic 已经不再只是一家模型公司，它正在向企业服务公司转型，而这个转型的速度和力度远超市场预期。FDE 模式本质上是在把 Palantir 的方法论嫁接到模型公司上——用深度的现场部署和定制化，把客户的 workflow 锁进来，形成高粘性的企业合同。

#### 对 Codex/Gemini 竞争的担忧：coding 有没有壁垒，看 xAI 的例子

最大的不确定性：Codex 会不会迎头追上？Gemini 也会追起来。Coding 模型有没有壁垒？

反驳这个担忧最好的证据是 xAI 的案例。今年又有一家掉队了，就是 xAI——他们内部从去年开始大力做 coding，依然没赶上，有算力、有人、也花了很多钱买数据，Elon 也花了很多时间在 coding model 上，但依然没做好。因为 SpaceX 的人去管 xAI，团队被割裂开了，很多人离职。这说明 coding 模型不是"有钱有人就能做好"的事——recipe、数据飞轮、组织稳定性，缺一不可。

Anthropic 的人觉得 OpenAI 依然是强劲的对手，GPT 5.4 效果不错、Codex 效果不错。假设比较差的情况，Anthropic 不会是领跑者，未来几年三家交替领先——但这依然不重要。原因是：即便假设未来御三家平分秋色（对 Anthropic 最差的情况），前面关于组织递归、企业渗透、数据飞轮的论据依然成立。御三家格局 ≠ Anthropic 失去商业价值，它依然是那个"进入 500 万亿 agent GDP 盘子"的唯一验证者。

#### 660B 的 Anthropic 不是共识，ARR 30B 还是信息差，这个差很快会被抹平

3800 亿美金的 Anthropic 是共识，但 660B 的 Anthropic 还不是共识——看看 Citi 这个 supply 多久都没卖掉了，今天我们能在 660B 上投 Anthropic 依然是很难但也挺牛的决策的。这个 660B 不是共识的原因是：目前 30B 的 ARR 还不是共识，还有一点信息差。这个信息差可能也马上就会被抹平。

假设今天 The Information 写了一篇报道，说 Anthropic 的 ARR 已经达到了 30B，我们还能买得到 600B 的 Anthropic 吗？大概率买不到。ARR 本身不重要，但 ARR 决定了 supply 的价格，和我们的成本。今天已经是过去三年最贵的时候，但依然是未来三年最便宜的时候——Anthropic 7 天年化的 ARR 已经到 30B 了，年底可能到 100B。

#### 就像当年云计算的大 Beta，只投 2000 万美金是不够的

这就很像，今天有一个云计算的大的 Beta 在这里，AWS 也可以，Microsoft 也可以，GCP 也可以。我们在美国大模型这件事情上，只在 Google 上买了 2000 万美金，这个 Beta 只买了 2000 万美金是完全不够的——那波云计算的红利，你只买了 2000 万美金意味着你几乎没有买。

在这种指数的发展下，我们因为 5 亿美金/月的收入就 pass 掉 Anthropic 是不合理的。Anthropic 7 天年化的 ARR 已经到 30B 了，年底可能到 100B。如果真的认为未来三年大模型会继续爆发，那今天任何不够重的仓位，都是一种低估。

**最后的最后，我发自内心想了下，根据我在硅谷的体感，我自己愿不愿意投?愿不愿意投百万 RMB 以上的 cash？我觉得我依然非常愿意，因为我觉得一万亿美金没有任何问题。**

