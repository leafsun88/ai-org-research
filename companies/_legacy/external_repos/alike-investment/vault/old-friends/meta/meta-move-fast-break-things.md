# META 组织穿透：Move Fast and Break Things 副本

> Move Fast 是一种能力，背后是：
> - ** Focus on impact** 的管理方法论，对员工的评价基本只看numbers，崇尚"one line fix"，如果通过改一行代码和一千行代码有一样的效果，评价上也是一样的，从**评价机制上把 impact的生产效率最大化**
> - **Facebook内部有一个Facebook（用社交媒体做管理工具）**，绩效review的时候也看发了多少个post，每个post有多少人看到了、评论了，使得一线员工的信息触点增多、一线员工拥有几乎透明的全局context，去中心化的”mini决策们“得以涌现;  **Meta的HR系统有8-9层，也并不扁平，但它的信息系统让整个公司的信息overhead大大减少，部门间的silo减少**
> - **前两个因素使得员工可以“Damn the Org Chart“** ：让更多Senior IC直接决策，绩效管理上“**激励ROI而不是absolute impact”，**也降低了管理者扩张团队的动机
> - **Service Leadership：**由于透明的信息系统（员工有信息权）和focus on impact（员工只对结果负责），manager无法垄断员工的信息权和评价权，体现在manager也不分配任务、不催进度，更多是赋能与服务
> - Move Fast的过程里非常鼓励 throw ideas 和 break things：文化手册里写“员工违章去天台搭了半层楼，大家又多了几个工位”的案例
> 反映在管理上，就是 Meta 其实只有三层架构：
> - 最低的一层，是下至一线员工上至director级别的所有人，特点是**impact驱动去中心化管理**
> - 最上层是Zuckerberg一个人，典型的**benevolent dictator**；
> - 中间的一层，是Zuck三级汇报圈范围内的VP们。主要负责将Zuck的意志KPI化，核心能力其实是在**Zuck的意志面前超高效的协同合作的能力**
> 如何评价？
> - 优点是在“**已知的未知**”上的进步有效前进、迭代飞快，但整个组织在数字的短期驱动下极为刚性，对“**未知的未知”**缺乏有效手段
> - 解决方法是靠组织的中心节点（founder/CEO) 来下大棋布大局（比如小扎在Metaverse上的all-in），但带来的问题是如果中心节点误判了，组织缺乏有效的自我纠正机制
> - 且这种move fast、focus on numbers的“葵花宝典”也不适合Metaverse和Llama，体现在：
> - Llama在技术路线选择极度短视、急功近利，为了meet 1.5个月的check point的evaluate bar，train模型时直接加入评测集；比如不选PPO的技术路线（OpenAI的技术路线），因为要花更长的时间、更好的人
> - 人力投入在能出短期结果的地方，pre-train的人数<post-train的人数，很多工程师在post-train雕花，只想出确定性的结果
> - 这还没有提内卷文化在更长时间维度下对人才的反向选拔：天才在慢慢脱离生产，brain drain
> - 例如Llama在很早开始做Reasoning Model，但模型效果一直不好，后面被DeepSeek做出来了；在有数据优势的多模态模型上也很早开始尝试做图片理解，效果也不好；根本原因还是数据质量和模型的architecture 不行，还是因为基本功不行，人不够好

### **Move Fast 是一种能力**

#### **Focus on Impact，数据驱动是****管理方法论****而不是产品方法论**

首先是**「Focus on Impact」，**对员工的评价基本只看numbers，几乎所有Meta的员工都提到了这个词。Meta和Google最大的区别可能就是Meta**崇尚"one line fix"**，如果通过改一行代码和做一个复杂系统能让公司赚一样的钱，那两者在评定上也是等价的，这种评价的好处是Meta在**机制上就把 「impact的生产效率」最大化：**

> *谷歌喜欢激励花里胡哨的东西，meta喜欢激励结果，只看数据涨了多少，留存高了多少**，比如我几年前刚入职没多久做了一个产品改动，简单的UI改变，没有深度学习算法，但也得到了激励，公司是激励low-haning fruits的，只要能达到那个number，你的solution没有创新也没全没关系  *——*Meta 软件工程师，ex-谷歌*

> *众所周知Facebook运转的核心精神是“focus on impact”。这在软件工程师每半年一次的绩效考核上的体现就是：考核只考虑这半年做出来的结果而不考虑过程。如果通过改一行代码能让公司赚到与做一个复杂系统同样多的钱，那两者在评定上也是等价的。事实上公司也特别推崇“one line fix”。这可能是Facebook与Google在软件工程师绩效考核的理念上最大的区别 —— Meta Director of Engneering *

> *在 Google，员工手册上也会写：前半年你什么都不用做，你只需要学习，learn as much as you can；但是在 Meta 就是首先没有任何documentation，因为为了快，并不需要把这个东西记录下来，也几乎不会写design，也不会review, 就是说你想到了你就直接写code做出来原型再说 ——Meta 1年员工，软件工程师，ex-谷歌6年*

> *Meta的perf process是我见过评价体系最完善，对结果的公正程度scrutiny最多的公司。**Meta用focus on impact就已经尽量的减少了人为因素对rating的影响。我之前在一个中型公司，perf rating axes里面有technical/drive/ownership/communication，但这些东西很难量化，但impact和numbers是硬的**，所以比如一个英文不好但技术强的哥们能做出些成绩，在Meta隐形的天花板就会更高一些。Meta的评价体系里对结果的scrutiny，老板们要先mashup，然后再calibration，很多时候老板还会主动跟别人adhoc mashup，这些都是work，一般没有两三周整不完（但我们org这次一周就整完了…），这都在尽量减少人为评价里面的偶然性  *——*Meta Tech Lead，ex-中型创业公司*

> *Meta 的 value 第一条就是focus on impact，作为刚来的同事，第一个项目应该是是直接能影响topline/能一个half内launch的且看到结果的—— Meta Manager，from 小红书笔记*

**在focus on impact/结果驱动的考核机制下，工程师们会自发解决那些技术之外的问题，而不是对没有技术难度的事情嗤之以鼻，**工程师成为了product generelist

> *很多人说Facebook的软件工程师分担了一部分产品经理的责任，这话是有道理的，因为早期 Facebook 的很多事情的瓶颈并不在技术上。在考核机制的作用下，大多数的软件工程师会演化成product generalist，为了拿到 impact而把产品经理的活也干了 —— Meta Director of Engneering *

![](https://xhs-doc.xhscdn.com/1040025031eie6u964e0cblbc38?imageView2/2/w/1600)

*               图：META Headquarter@Menlo Park, 墙上的标语除了Move Fast外，第二条就是focus on long-term impact*

> *国内以我在纽约阿里的见闻来说，在阿里是跟老板关系好，他给你好项目，你有好的机会和exposure，你最终你就能升职加薪；但 Meta 的 performance 比较公平，最终的衡量标准是impact，是你到底产生了 impact 没有？ 比如说我做data，build pipeline 和 foundation，核心问题是 so what，你这个产品 unblock 了谁，别人用来干什么了？我们在我们内部有个工具叫 ML Hub，Machine Learning Hub，所有模型的 training job 都提交到这个平台。如果我做了个产品 feature ，公司会衡量能帮这个 MLE（Maching Learning Engineer）减多少工作时间？我的工作目标非常清晰，如果方向不对会自己掉转方向，为了有产出的numbers，自己会比较有压力去找真正有impact的事来做，减少假的表演类工作，不会每天坐在座位上等老板下班再走，这本身就会让你 move fast ——  Meta AI Infra Data Engineer，ex-阿里*

#### Facebook内部有一个Facebook

几乎所有Meta的员工都提到了 **Meta 内部的信息非常透明，这得益于公司有一个内部版的Facebook：Workplace，且在Workplace的表现会对直接影响绩效评价**。**这使得Meta的HR系统有8-9层，也并不扁平，但它的信息系统****（***WorkSpace、Task和个人的Profile***）****让整个公司的信息overhead大大减少，部门间的silo减少**

> *我之前在苹果，我做某个module比如蓝牙，产品上市当天，我才知道做的蓝牙是用在手机上还是在 iPad 上；但 Meta 是全公开的，只要你想知道一个新的project，它的售价、PMF、目标客户是谁，内部在Workplace一搜就知道了。因为上班都会发post，就跟发朋友圈一样，就去说这周我见了这个供应商，我聊了什么，我达成了这些目标，下周我要见这个供应商，我准备达成啥目标，我的目标是啥，都会发帖更新，然后比如隔壁组做耳机的可能看到这个供应商不错，就会来问一下能不能介绍给他们 —— Meta Reality Labs Hardware Tech Lead，ex-Apple*

> *我在新员工训练营的时候，被告知在 Meta 一个很重要的技能就是学习如何在 workplace 发 post 来展现你自己的 impact，项目开始发一个post，项目做到一半发个post，结项的时候也要发一个post。Meta的绩效review叫psc，psc的时候很重要就是要看你发了多少个post，每个post有多少人看到了、评论了，绩效自述的不能超过几百字的，所以大家都会附上自己的post超链接到workplace。Workplace也有很多group，可以设置不同的权限，后如果说你作为一个其他的其他组的人，你如果没有订阅我们这个 group 的话，在你的时间线上是看不到我发的这个 post 的，但大家一般都默认发全员可见的post，因为Meta 内部大家信息都爆炸了，看都看不完 ——  Meta Corporate Infrastracture Engineer, ex-JPM*

> *在快手我们一般是不是先拉群，再约会，双方对齐一下OKR，最后会议结束，输出一个双方能合作的点的todo，然后再拉上双方老板，再对一两遍，普通国内的互联网公司都是这样。在Meta你跨部门和其他同事对接，看一眼对方的profile业就知道对方是做什么的了，我可能看完就知道我不会和他合作了，也不需要开会了，节约了很多时间；因为他的activity、他的task、他最近评论的task、他创建的文档以及他的最近写的代码都会体现在profile页上，所有人都能看到 —— Meta Staff Engineer， ex-快手 Tech Lead*

这也使得一线员工的信息触点增多，去中心化的”mini决策们“得以涌现，主动性也大大提高：

> *业绩的一部分靠Workplace的 post说话，很多人会给你反馈，也是你的impact，但不是看post的互动数，而是看：1）有没有link到关键业务，比如我之前发了post，隔壁组manager看到了就来找我合作了，大家就交流交流做了业务，就相当于线上约咖啡了；2）有没有影响到关键人，比如VP会不会点赞  ——  Meta AI Infra Data Engineer，ex-阿里*

> *Meta 的 HR 系统的树状结构层次多、不扁平，但它的信息系统（WorkSpace、Task和个人的Profile）和文化让整个公司的信息overhead变少。比如我自己工作内容的80%都会发在Task上，用#hashtag打标，以及有task id，这样全公司的人都能看到、搜到每一个项目。我感觉员工已经被洗脑了，所有的项目做完了先建一个task id发到task上，然后才是归属自己的团队 —— 5年Meta软件工程师*

**                   Workplace -  Feeds **

![](https://xhs-doc.xhscdn.com/1040025031eihcorh4e00q2kul0?imageView2/2/w/1600)

**                              Workplace - Group **

![](https://xhs-doc.xhscdn.com/1040025031eihcuvfke09tf21qc?imageView2/2/w/1600)

                                **Workplace- Chat
**

![](https://xhs-doc.xhscdn.com/1040025031eihg5c04e07oieup0?imageView2/2/w/1600)

#### 服务导向的管理方法

员工觉得在Meta manager的职能和其他公司不一样，**manager 不分配任务、不催进度，不micro-management， 而是赋能和上升（escalation）：**

> *Facebook式的数据驱动，不是做产品的方法论而是公司管理的方法论。数据驱动，是为了赋权到个人，为了每个人可以根据整体目标自己做决策而不是靠你的manager。传统公司组织就如同蜘蛛，它的决策权在大脑，对应的所有事情都需要等待大脑的信号，而去中心化组织就如同海星，没有头但智能分布在身体各处，数据驱动（focus on impact）是公司可以成为快速运转的组织的一个前提 ——  Meta Director of Engneering *

> *我觉得Meta的manager和阿里的manager很不一样，国内老板最重要的事是派任务，但Meta的老板不派任务、不管进度，不会催你push你；而是帮你协调资源，帮你上升、帮你找人还有定义scope和边界，更多是做项目logistics的工作，给我赋能，我每周只和老板碰1次20分钟，他帮我把控一下大概的方向，给我一些建议，我工作需要的所有信息和人都能在workplace里搜到。在评价我、和对我产品的管理方式上都不一样 ——  Meta AI Infra Data Engineer，ex-阿里*

> *Meta 这边 manager 不负责任务的分配，负责的是更多是人事的事情，工作需要我自己去挖掘，比如 Workplace 是一个community，里面有我们engineers，就是我做的平台的用户，你可以去里面和人沟通，看大家的feedback，来决定要不要做这个project，manager 会去帮你评估这个项目 impact 有多大，值不值得做 ——  Meta Corporate Infrastracture Engineer, ex-JPM*

信息权和评价权不垄断在+1和+2手上：

> *发post和建task有点像建立你自己在公司内的公域currency和IP，让你不完全被你的+1评价，也可以被+2/+3看到，让每个员工都能有更多被评价的维度和更多visibility，其他组的老板能看到你的产出，如果你觉得老板不公正你也知道找谁去活水 —— 5年Meta软件工程师*

> *我刚刚回Meta的时候，一个VP comments on我的代码，应该是在其他地方顺着找来的，我问我的director要该怎么回答，因为在国内，你回复大老板的时候需要征求你小老板的同意吧；但我Meta的老板觉得很神奇，他很惊讶我竟然会问他这个问题，他觉得我是个individual，应该有和+2/+3独立对话的权力；当然我的director是个老meta，在有的microsoft的老板组里就会更官僚一些—— Meta Staff Engineer， ex-快手 Tech Lead*

#### 用「Cycle Time」监测组织效率

**为什么会有「内部透明的信息系统」的设计？Meta不采用组织架构完全相同的职责模式，而是通过透明的信息系统，把更多信息权和决策权下放，所谓的“Damn the Org Chart ”**

> *公司规模越来越大，流程就变得越来越慢，核心观察指标是「Cycle Time」,也就是一个任务或决策从提出到完成上线的端到端时间，「Cycle Time」取决于：1）要跨越多少层级，2）每个层级多少人。减少「Cycle Time」的最佳方法是把决策权下放（IC决策），而不是以组织架构为导向的职责模式（Manager决策）。*
> *为什么严格按照组织架构的决策方式更冗长更慢？因为“managers have a great deal of overhead to deal with”每个人都有日常的工作，还要思考、考虑，就很慢了  —— CTO Boz*

关于IC和manager，在Meta内部经历了3个阶段：

> *2016年之前：只有IC，人多起来之后就让懂业务的IC同时转管理，就出现了问题，IC没有时间研究技术和业务，senior IC的时间被管理分走了太多，从IC中长出manager对团队是好的，但是当组织变大之后不scalable，在manager的个人精力分配和供给上；*
> *2016-2023这七年：Sheyl带进来很多people manager，专门做管理，让好的ic做ic，但是导致中间层多了很多不懂业务和技术的人，ic没有权利调动资源，去跟manager说又不懂，沟通和执行效率就下来了，最多的时候有9层；*
> *2023年以后：一轮大的layoff，把product /design /user research /ds 砍掉70%，回归到engineering drive，层级砍到5层   *
> *—— Meta VP of engneering*

因此解决方式是：让更多Senior IC直接决策，且“senior managers should have small teams”,  绩效管理上「**激励ROI，而不是absolute impact**」，把团队人力和投入成本纳入考核范围:

> *Performance management should not focus on “absolute impact” but rather “return on investment.”  —— CTO Boz*

#### 工程师驱动

以广告团队为例，**Meta是技术/工程师来驱动产品迭代，所以Meta的程序员都会找idea和insights来设计产品UI或者流量策略的A/B test**，但在国内这个事儿更多是产品经理在做，这是Meta和国内互联网不同的地方：<u>美国是工程师驱动产品，国内是PM驱动产品</u>

> *广告的tech stack太多，必须要懂技术才能驱动，在广告团队是engineer和产品co-own产品roadmap，前者管实现，后者管沟通（对内画ppt说明之类的）；用户产品是design driven —— Meta VP of engneering*

> *美国只有只有engineer驱动和design驱动，没有产品驱动，大学里有工程和设计专业，没有产品专业 —— ex-Snapchat VP of engneering*

> *不同于国内产品和技术的泾渭分明，Facebook更多是工程师驱动产品，具体到信息流，就是算法策略驱动产品设计。早期的例子就是微博那个被骂翻了的未读信息重新加入新排序，就是抄自FB —— Meta Director of Engneering *

> *广告技术分成targeting, bidding, conversion等环节，我会每个环节找team里最强的5个人来做3-5年的roadmap规划，从学术界，工业界的前沿找有10x/100x机会的技术方向，会做的很细，把不同类型的技术方向都列出来，然后做判断（比如machine learning会有什么突破，未来三年会对广告推送有多大影响），在多个技术方向中做选择，并且规划每年产品应该做到什么程度，因为会映射到资源的分配。每年会rolll这个roadmap，来复盘看做对做错了哪些判断，2018年开始做，之前完全没有，最开始只有10%的准确率，花了两年做到了60% —— Meta VP of engneering*

#### Break Things 是一种政治正确

- Move Fast且不停地throw ideas的一个副作用就是会经常犯错，但Meta员工似乎对犯错（Break Things) 非常自豪，在Meta 犯错是一种政治正确：mo

> *我16年刚入职的时候，有一次版本发布我改错了，结果同事和manager都来和我 high five：“恭喜你！你跟我们一样犯过错了，说明你改的代码很重要” 我当时的感觉是大家发自内心觉得犯有价值的错是光荣的，很value犯错这件事—— Meta 5年软件工程师*

> *在 Meta，Move Fast意味着发布有缺陷的工具永远是政治正确的，甚至一些内部员工的工具使用体验也因此很糟糕，比如内部的Quest会一直黑屏，官方 API 会突然产生无法恢复的错误等等，很多其他工具也会不停瘫痪或崩溃 —— Alvin Wan‘s Blog <Why Work at Meta?>*

> *有两个故事公司从 07 年讲到 15 年，我入职的时候对这个故事印象很深：早期，员工去Facebook马路对面吃饭，要回办公室，要绕道去很远的人行道，工程师就自己拿颜料画了一个人行道，这样不用绕路了，后来被警察抓到了，但他们引以为豪。第二个案例是meta不到100个人的时候公司没有工位了，有一个员工，自己违章去天台搭了半层楼出来，然后大家又有多了几个工位出来。Meta把这个写到这个 culture book 里边，把这种精神灌输给后面的员工，后来公司大了删了 —— Meta Staff Engineer， ex-快手 Tech Lead*

> *早期Facebook有Ship Early and Often的文化，就是你每周都要发布代码，频率是非常高的，Zuck的要求是代码必须快速上线，哪怕有小问题，也要先发布、再修复  —— Facebook第5号员工 Sean Park*

- Break Things也意味着，break a **good **product in the search of a **great **one，“最成功的社交网络公司也是随时会沉没的泰坦尼克号”

> *When we were a social network we were at the top of a hill....To quote Tyler Durden, they end up “polishing the brass 铜铁 on the Titanic. It’s all going down, man.  —— CTO Boz‘s Blog *

但后来Meta把Move Fast & Break Things 改成了「Move fast with Stable Infrastructure」，再后来只讲「Move Fast」。

#### 用户体验服务于增长斜率

- 一切服务于增长速度，甚至是用户体验

> *在2009年时，Facebook发表了四个愿景：1. 不断扩大用户量  2. 重新定义搜索  3. 殖民化网络  4. 定向广告。这四个愿景都指向巨大的用户量和用户数据。而**用户体验、用户权益、社区，这些都排在增长后面** —— 《*收购Instagram后的矛盾反复*》*

> *在Instagram，用户体验大于一切。在Instagram被收购后，Instagram对于Facebook那套以增长为核心甚至可以牺牲用户体验的做法不太认同。扎克伯格很想在Instagram上线图片人像标签功能，每当用户被标签后会收到邮件和推送，大大提升了Facebook的增长。但**Systrom坚持不会像Facebook那些疯狂给用户推送**，只做了一个Instagram版的人像标签功能，没有带来增长但用户体验很不错。相比于Facebook的Move fast and break things，Instagram的理念像是Don't fuck it up —— 《*收购Instagram后的矛盾反复*》*

> *很多人说Facebook产品太复杂了体验太差了，还说Instagram走上了FB主应用的老路，某种程度上我是同意的。我们把所有用户按挑剔程度排在一个光谱上。一个极端是特别挑剔的，特别关注产品质量，愿意为此付出额外努力去做筛选，典型例子是欧美青少年用户。另一个极端是完全不挑的，给什么用什么，典型例子就是中国的预装和倒流。Facebook的整个国际化过程就是从最挑剔的扩展到最不挑的，实现的策略就是把产品做重，所有功能怼到你脸上，想用什么用什么。Facebook在很多发展中国家的使用形态虽然完全不是熟人社交应用但也还是做起来了，靠的就是这个 —— Meta Director of Engneering *

#### 15%中国人的公司

- 关于怎么有好的talent inflow,  没在招聘上听到特别有意思的点，更多是和字节很像的招聘策略：市场上Tier 1 的薪资水平，“卷”的名声在外filter进来的人都是卷王
- Workplace里有一个**chat group叫「Chinese@Meta」，显示群成员有9.8k人；考虑到Meta有7w正式员工，也就是员工人数里含中国率为15%，这个比例本身已经tells a lot***（用Amazon、Google、特斯拉全球的**Perm 永久就业资格的历年申请数量来估计这三家的中国员工比例，分别为3-5%，5-10%和11%）*

> *在硅谷Meta就算卷的，从来都是，来Meta的也都知道，这种事情双向选择，愿打愿挨没问题。但是Meta从来没有公开宣扬这个，至少从意愿上还是尽可能照顾WLB，实际能做到多少那是另一回事 ——  Meta Senior Director, ex-快手数据分析部负责人*

- 同时在招聘流程上尽量减少人为因素的干预，保证招聘的公正：

> *面试基本都是structure interview, 有一个问题清单，每个岗位确定4-5 dimensions，比如business partnership、collaboration、financial knowlege等，谁招人谁来定，每个dimension问的case的问题也是固定的，面试就是 go through the case;  分4-5个round，每一轮的面试官就只问这一个dimension，面试官也是招人的HR和manager/director一起来指定。所有的流程都希望保证公平性和 consistency，避免个人喜好和熟人倾向的影响 ——  Meta FP&A Senior Manager*

### Meta 只有三层架构

> Meta 是一个假装自己不是大公司的大公司。反映到管理上，就是Meta 其实只有三层架构：
> - 最低的一层，是下至一线员工上至director级别的所有人。特点是**impact驱动去中心化管理**，因此职能要求刻意的模糊以鼓励员工发挥最大的能量而非自我设限；
> - 最高的一层，就是Mark Zuckerberg一个人，典型的**benevolent dictator**；
> - 中间的一层，是Zuck三级汇报圈范围内的VP们。主要负责将Zuck的意志KPI化，核心能力其实是在**Zuck的意志面前超高效的协同合作的能力；**
> *———*—  Meta Director of Engneering

#### "Benevolent Dictator"和“Outsized Power”：最高层

> *在扎克伯格的Facebook页面，他是这样介绍自己的：率真，破坏欲，革命性，信息流，保守，动手制作，心无杂念  —— 《No Filter》*

> *大多数人无法准确评价Meta，很可能还是因为Meta这个人同时具备极端的理想主义和极端的现实主义，所以公司很多时候也会同时呈现这两种形态。不要做只会肤浅地计算短期得失的，愚蠢的现实主义者。也不要做只知道浪漫化自己的行为的，幼稚的理想主义者 ——  Meta Director of Engneering*

**—— 极端的现实主义**

- "I'm CEO, Bitch"

![](https://xhs-doc.xhscdn.com/1040025031cvs2hu83o0a8r93sc?imageView2/2/w/1600)

> *我的亲身经历是在国内，比如一笑和宿华裁员都是让-1来说，但小扎挺敢当坏人的，裁 low performer都是自己出来说，他说话经常很刺耳、很难听，所以很多人讨厌他。但确实这个公司裁人很快，这也导致每个人发自内心都很有压力，我前一段时间有一个项目和隔壁团队协作，隔壁组的director说了一句：这个项目做得好我能再多领6个月薪水，大家都是在算我还能领几个月薪水，说他们VP直接问：You have the right talent or not？隐含的意思就如果你没有 right talent，那你可能也不是right talent，我能感受到大家都是战战兢兢 ——Meta Staff Engineer， ex-快手 Tech Lead*

> *疫情之前软件公司从来没有裁过人。我认识Meta做财务的人，他说当时（2022年）财务给小扎的建议是裁2000人，但是小扎他就是希望立刻掉头，最后裁了2万人，小扎说“矫枉就要过正”  *——*Meta 软件工程师，ex-谷歌*

- “抄”

> *Don’t let your ego prevent you from copying what works   ——Zuckerberg, internal Q&A session, 2016*

> *Instagram能有现在的商业地位主要因为三件事：1) 从Facebook抄了Newsfeed，然后打磨得像自己原生的一样; 2) 从Snap抄了Stories，然后打磨得像自己原生的一样; 3) 对其他不够好的想法说不  ——  Meta Director of Engneering*

- 竞争性

> *他曾跟朋友的女儿玩拼字游戏不小心输了，气得念念不忘，写了一个程序寻找单词以确保自己再也不会输。他对于好的概念是要比所有人好，且不会接受失败 —— 《No Filter》*

> *Instagram can hurt us. We need to either buy them or compete harder  —— 2021 年美国联邦贸易委员会 FTC 对 Meta 的反垄断诉讼公开文件*

**—— 极端的理想主义**

- 什么塑造了Zuckerberg？

> *Mark Zuckerberg不止一次地表示，塑造了他的那个事件就是雅虎的10亿美元收购邀约。当时他周围几乎所有的经验丰富的“成年人”们都认为应该接受。拒绝被收购对于当时的Mark Zuckerberg来说是一个孤独又艰难的决定，但最终被证明是无比正确的结果也让他从此彻底抛开外人的意见而相信自己内心的想法。Peter Thiel因为当时让他自己做决定从而成了当中陪他走得最远的人 —— Meta Director of Engneering*

> *唯一可能不同的，就是Mark Zuckerberg对自身理想的偏执程度比Google的两位高出不少。毕竟，当年Yahoo对Google和Facebook两家公司都给出过收购offer。Google拒绝的原因是出价太低，而Facebook拒绝的原因是Zuck找不到除了继续做这家公司之外的人生目标  —— Meta Director of Engneering *

> *“这种对于理想的意志力从何而来? Zuckerberg considered the question—possibly for the first time—and concluded simply, “Jewish mother.” —— 《Becoming Facebook》, 2009*

#### 把Zuck的意志KPI化：中间的核心管理层

> *我在围观VP们因为Zuck的一个想法而聚在一起开会时，总会想起小时候大家课间操时本来各自玩各自的，突然铃声响了就迅速集合并排站好的情景。我之前为了尝试理解这种架构的生命力曾试图寻找现实中类似的例子，但思来想去只找到一个，就是有着蜂后/雄蜂/工蜂三种角色的蜂群。虽然很多细节有所出入，但蜂群在行为上的很多推论同Meta是极为符合的：蜂王-唯一具备完全生殖能力的雌性个体，雄蜂-完全服务于基因传递，工蜂-一线工程师 ——  Meta Director of Engneering*

**Andrew Bosworth-CTO，负责Reality Labs**

*“文化捍卫者、强势、激进”，Zuck的哈佛学长&Tutor，主要战功是早期做了Ads平台*

> *Boz 是 one of Top 3 talents in Meta, 很有product vision，懂怎么搭org，也直抒己见，带广告后直接从20%到60%增速3~5yr，是Zuck在哈佛的TA，CTO只是title实际上是GM，很收到zuck信任，去带VR之后认定未来的产品形态应该是便携的，就改了之前oculus创始人的设计，五年没有做出结果，但现在Rayban证明是对的   —— Meta VP of engneering*

> *非常激进，和小扎某种程度上很像，他说Meta需要connect people **even if it causes deaths**, 在内部posts公开说的，我只能说到这里了 * *—— Meta Staff Engineer， ex-快手 Tech Lead*

> *2016年Boz的内部备忘录「The Ugly」，阐述了Facebook的持续增长背后的代价，我个人认为这是2016内网最有价值的文章。很坦率地尝试讨论目的与手段，理想与现实的议题，是我之前所不曾见过的。我最佩服的是他没有一丝犬儒的气息，没有尝试说“我是被环境逼的”，而是在说“我明白，但我们还是要这么做”。这两者在我看来有本质的区别。我很讨厌Boz，他很没礼貌，但我希望公司内有Boz这样的人来表达不同的声音 —— Meta Director of Engneering *

> *对小扎公开喊爹，喊“Dad Zuck”，也会在Workplace怼一线员工，有一次下班时间从18:00延迟到18:30，有员工在Workplace吐槽，boz直接回复了帖子，意思是在这里就要fit这里的规则 ；这种反差让很多员工很讨厌他—— Meta ex-Reality Labs PM*

> *Boz到现在依然每周二和大家开直播唠嗑，在他自己家后院，Reality Labs全员都能参加，还给我们看他的花园和花花草草，他家很豪华，家居都是电动 —— Meta Reality Labs Hardware Tech Lead，ex-Apple*

**Chris Cox-CPO**

> *我两次入职的Orientation都是Chris，他会给所有新员工亲自讲课，我两次入职听过他两遍他的课，依然觉得很有魅力，长得也很帅。很早的时候，Facebook做一个个人profile页，小扎发布了之后没人有啥感觉，但是Chris娓娓道来，讲他的爷爷怎么在圣诞节的之后做贴纸簿，以及他自己结婚了渴望有一种纪念结婚纪念日的方式等等，大家就顿时被点燃了，觉得这个功能做的太深入人心了 —— Meta Staff Engineer， ex-快手 Tech Lead*

> *他常在公司园区步行开会或与普通员工共乘班车，笑声爽朗且富有同情心，与扎克伯格的机械感形成鲜明对比 —— CNBC访谈，2021*

> *Chris是雷鬼乐队Rafa的键盘手，早期常抽空排练， 他还资助非营利音乐厂牌Redtone Records，致力于文化保护 —— CNBC访谈，2021*

**ex-COO: Sherly Sandberg **

> *Sheryl不够adaptive/pivot，所以23年这次变化就离开了  —— Meta VP of engneering*

> *之前Zuck说过，公司里有两件事，‘需要做的事’（商业化）和‘热爱做的事’（产品创新），Sheryl 负责前者 —— Spotify CEO Daniel Ek *

> *很多媒体在过去一年里会把Sheryl 离开Meta看成是这家公司的负面新闻之一。但我认为Sheryl没有更早地离开反而阻碍了Meta的自我革新。这套方式work的原因是Facebook当时的app确实可以以这种方式拆分管理：普通用户和广告主所面对的FB是两套体系。这套模式在整个互联网行业其实是个特例：对于大多数的业务形态，product和business是同一件事。也正因如此，整个行业再没出现第二个像Sheryl一样的角色，因为其他公司都无法像那时的FB一样运作。造成的结果就是：但凡无法明确拆分成product与business而是需要两者紧密协作的业务都很难做起来，因为两个组织相对独立，只有到CEO那里才交汇。这个问题公司显然是意识到了，以至于Sheryl一走组织架构就改了。但她不走，改革就很难发生 —— Meta Director of Engneering‘*

<u>（上面这部分VPs的决策、行为 Need More Infos）</u>

#### Scaling of Founder Mode

- 小扎觉得** founder mode 也需要找到 scale 的方式，来形成 ****founder mode lieutenants**（“创始人副手团”），一是需要识别更多founder-like behaviors的人，并激励他们；二是告诉大家管更多的人不会让你升职，鼓励更多人去做「redefine projects」

> *在Meta工作的10年多我也看到了Zuckerberg怎么激励“founder-like behaviors以及 well above managerial qualities，比如有一些本来不直接汇报给他的人，因为表现出了founder-like behaviors，会直接被Zuck直接任命，负责Zuck想做的内部创业项目之一，并在项目上和Zuck直接汇报；Zuck也经常“强迫我”缩小我的管理scope，多做新的、难的项目 ——  Fidji Simo, Instacart CEO，ex-VP of Facebook（注，Fiji是被一些员工提到在Meta火箭晋升的典范）*

- 在类VP-level也可以不带人，单独设立Senior IC 的 promotion track，鼓励IC文化，攻坚内部创业项目：

> *有个 Q&A 场合 HR 专门提到我们要 promote Senior IC，也给了data说，你的organization 有多少 Senior IC 是合格的，会给一个guidance，希望你到这个水平，如果不够就去 promote。公司鼓励 technical 的 knowledge 来 drive impact，只talk about technique，更 focus，让 engineer intelligence 更 dense，集中去做一些难的事，另一方面也是给基层engineer更多voice和visibility，你一半的时间在项目上汇报给Senior IC，另外一半时间汇报给你的report chain的manager，公司对你的评价也会更公正 ——  Meta FP&A Senior Manager*

> *在Meta有IC9（类似P11），一个IC5.5-6基本=P8，IC9基本是VP级别的了，依然可以组虚拟团队做创新的项目，但在快手（包括其他的中国互联网公司）所有副总裁都是带团队的，有的VP下面有4-5个senior director，也会有2-3个IC，Elon去X裁员的标准是代码行数，这个很粗暴但也make sense，从这里能看出来Meta也是非常尊重纯粹代码写得好的人 —— Meta Staff Engineer， ex-快手 Tech Lead*

> *Zuck repeatedly sent the signal 告诉大家：持续把新产品和新业务从0到1做起来比管理带宽重要的多，所以在Meta有一种潜移默化的文化是，要做到VP of Product，一个重要标准是要亲自推动过至少一个“redefine project”，但难点在于，怎么告诉这些founderlike的候选人：“公司有好的评价体系你尽管去试吧”，因为大多数绩效和薪酬措施都是考核短期收益的，这种考核方式更适合经理人模式；Meta花了很多时间来做这件事，但喜忧参半 —— Fidji Simo, Instacart CEO，ex-VP of Facebook*
> **注：Meta的绩效评级里，Redefine=5分，Great Exceeds=4， Exceeds=3.75，Meet All=3.5，Meet Most=3.5-**

> *我能看到Meta一直在fight against短视的绩效review机制，内部post也有人在说。某一年Meta 先把psc从半年改成到一年一review（但半年依然可以promote），因为不希望限制员工promote的机会，但大家又觉得promote决定不transparent，所以后面又改成半年有一个简易版的psc，只写200-300字，半年也可以promote，但这样和原来半年也没有区别了？之前还有一段时间加入了long-term metrics，但在Meta的组织里怎么评价这个long-term当时也比较混乱，怎么保证绝对公平，所以效果我个人觉得是TBD，我的观察大家还是非常short-term，特别是现在Year of Efficiency之后 ——  Meta FP&A Senior Manager*

- 一个Meta员工举例的**“Redefine Project”**的案例：Menlo Park Headquarter 墙上挂的 Mapping System，能帮你在这个工区找到任意一间会议室和任意一个人的工位，并告诉你路线怎么走，解决了经常在园区迷路/找不到人的问题

![](https://xhs-doc.xhscdn.com/1040025031ejp50jc4e00sdl9hc?imageView2/2/w/1600)

![](https://xhs-doc.xhscdn.com/1040025031ejp545k4e0cv743ms?imageView2/2/w/1600)

> *这个项目在其他公司不一定能拿redefine，但是在Meta我很能理解，因为Meta很苛刻地关注组织内的信息流通效率，Workplace连接虚拟世界的信息，Mapping System连接物理世界的会议室和人，Meta是一个信仰连接这件事的公司——  Meta AI Infra Data Engineer，ex-阿里*

> *2008年初，Boz 开始意识到，Facebook的文化可能面临挑战甚至失败。2008年的一天，当他在公司餐厅排队时，遇到了一位之前从未见过的工程师。于是Boz问他，在公司干了多久。对方的回答让他震惊：一年。他感觉有点不对劲儿。他想：“他已经来了一年，我竟然不认识他，我们是Facebook，我们应该在公司内部也规划一个高效的沟通网络，就真的有麻烦了。我在Facebook这四年半，一开始几乎每个工程师都互相认识，但随着人员迅速增长，这一点变得不可能。如何有效地让最适合（潜在）合作的人互相认识，有信任感，以保证项目的高效完成，成了Facebook这些年很大的挑战 —— 《打造Facebook》*

**什么样的人可以快速晋升？***以华人VP Meihong Wang 为例*

- 在Meta，技术团队很难定住压力不去产品和应用端，聪明的人都去了产品团队
- 推荐团队都是赛马的，infra里的技术团队和产品的技术赛马，但infra的抓手只有模型大的架构，没法boost流量等，产品的算法可以决定流量的分发，很容易出numbers，因此产品团队的技术leader都升的很快

> *Meihong就是产品团队的engineer VP，我认识他的时候还是IC，前几天改了一个很大的流量策略是meihong发现我们的信息流内容分发时效太长了，很多很老的内容还是会分发出来，meihong就上了一个策略给新内容更多boost，numbers很好；还在Reels推了长视频，觉得能吸引好的Youtube creators过来，提升内容质量，进一步提升用户和时长*

> **Meta 的三层架构有什么pros & cons？**
> - 以impact的数字定成败（focus on impact) 和效率优先（move fast）是一体两面的，本质都是以功利主义的短期结果作为核心考核和激励手段
> - 采用这种方式且能高效运作的组织注定是内卷的，优点是在“**已知的未知**”上的进步有效前进、迭代飞快，但也有缺点，比如对范式变迁（即“**未知的未知”**）缺乏有效手段
> - 典型的解决方法是靠组织的中心节点（founder/CEO) 来下大棋布大局，比如上述的(Scaling of) Founder Mode，但带来的问题是整个组织变得极为刚性，如果中心节点误判了，组织缺乏有效的自我纠正机制；且这种迭代很快，只看numbers的组织方式也不适合所有业务形态，比如硬件<u>（下面以Reality Labs举例）</u>
> - 这还没有提内卷文化在更长时间维度下对人才的反向选拔：有才华但抵触内卷的人慢慢脱离生产，从而导致brain drain，这在新技术范式出来之后显得更明显<u>（下面以Llama举例）</u>
> *———*—  Meta Director of Engneering

#### “Half Staffed is Unstaffed”

在「未知的未知」的事情上，Meta一直以一种自上而下的、all-in的姿态在投入，很聚焦，用Boz的话说就是「Half Staffed is Unstaffed」 只用一半的人不如不用：

> *“有太多分散的idea比没有idea更惨，所有重大决策都需要有 ruthless prioritization，要么 fully fund 要么 shut it all down*

> *举个有点琐碎的例子，在与Zuck的炉边谈话中，有时会被问到：公司是否能支持一些非营利组织？Zuck总是会拒绝，他解释说，这并不是因为我们不关心公益事业，而是因为我们的comparative advantage不在慈善捐赠，而在开发产品；每个偏离核心竞争力的行为单独看都有正向ROI，但加在一起却产生了很大的负面影响  —— CTO Boz's blog *

最典型的两个决策就是Metaverse和Llama:

### Reality Labs

#### 两个灵魂人物：Boz vs Carmack

Carmack 是之前 Oculus 的 CTO，Oculus 被收购之后留在了Meta，是非常懂AR/VR、游戏和光学的技术大牛，在技术路线选择等上面都被验证了有vision，但最后离开了，把Reality Labs 全部交给了Boz ：

> *Carmack是 Timewarp和Spacewarp的作者，这个技术是减少了Oculus的眩晕感的关键技术，小扎之前会让John Carmack列一个技术重点清单给自己学习（而不是找Boz，那会22年Boz已经是RL负责人了，而且又是整个Meta的CTO role），后来Carmack把这个给小扎的清单放出来了给大家看*

> *Boz 想走 PCVR 的路， Carmack想走独立一体机，要便携，不需要连根线，后面Quest 2做出来证明了Carmack是对的，但最后离职的是Carmack*

> *John离职的时候发过一个内部post，最后一段大意是说受够了这里的 politics，对外发的版本删掉了最后一段, 可能 Boz 是很懂 politics 的*

> *Boz 刚去RL的时候可能确实刚开始学习技术，做了一些错误的决定，比如那会用户粘性和留存已经在下降，但Boz给RL定了一个激进的ARPU指标，后来做了2个月负反馈太大叫停了*

> *我们组的 tech design doc Carmack都会看然后评论，Carmack应该不会不想当VR的一号位，最后的结果看肯定是小扎不愿意，可能是信任问题*

> *我们内部最高决策会叫 MZ Review（Mark Zukerberg Review），我们要做什么东西最后都要给他present，比如VR的下一代要不要加 eye tracking等等，最后全是小扎的决定*

#### 旧地图 vs 新大陆

旧地图找不大新大陆：Meta的move fast、bottom-up决策在早期硬件组织上造成了很大的混乱

> *Apple没有Product Manager，只有 Engineer Leader, Designer 和 Project Manager，就是因为产品的定义一定是leadership做。在Apple 的做法是，比如Principal Engineer会给你说，主板怎么做、芯片、功率、发热量，下面的人去研究实现成本、时间、可行性；*
> *iPhone是有2个团队每2年迭代一次，这样可以每年release一版iPhone，也就是我们今天的iPhone就是2年前就定好了，这样才能保证产品long-term可以打磨的好，对产品的控制力更强，组织的状态更polished。因为硬件需要更长的 iteration，需要做很多prototype、供应链、工厂、新功能，需要更强的vision和自上而下的意志*
> *但是Meta是不可能这么做的，我同事当时在Oculus做主板和集成电路，之前是Apple的，去了Meta后发现基本没有guideline，就是让你自己去做就行；我在那边两年都是半年就要换一个方向，leadership只给方向，说你要做做做，但终点长什么样呢？而且Meta我当时的manager每个half都要自己去想其他projects，大家有蛮大发挥的自由度*

> *离职两年了还记得的事是，当时Oculus casting投屏会掉线，连接率fail太高，要花1min连上，Carmack发post说要花时间improve连接体验，post 下面大家也都说要 improve，很多人点赞；我看到这个post很高兴，有事儿可以做了，去找当时的manager对，结果manager说不用做这个功能，要去做直播吧（Go Live），后面我找了skip的 Sr manager ，她也说也不知道为什么不做连接率；决策比较混乱*

对用户体验的忽视：

> *没有人care产品体验，因为Facebook App干啥都有人用，80分就可以了，这在硬件上掉坑了，Carmack 发过好几个post 说有Oculus的体验有 fundamental的问题需要解决，比如刷新率低、head movement 延迟严重容易产生晕眩，也是很久了才解决*

#### 想象力在哪

- 从微观上看，组织有变好的signal：

> *依然比较有信心的点是，Meta还是在花大价钱找最好的人来做硬件，很多人觉得苹果Pay很高，苹果的硬件给的是贼低贼低，苹果只是市值高，Meta 硬件的人都是苹果来的，在硬件上Meta能给最高的package，招比较好的人*

> *Meta像 10 年前的苹果，或者像15年前，07/08年前的苹果，刚开始做硬件的时候硬件的体验，团队，都不太ready。我们的几个SVP 是 Instagram 调过来的，从来没去工厂出过差，他们也意识到这样可能不行，后面的几个VP都是从苹果和微软来的，组织在慢慢的变好，至少我看到 VP们 去中国去工厂出差了*

> * Meta 的硬件整体来说是自下而上的公司，我们下边的人去 propose 要做什么东西，然后往上去推；苹果是自上而下。因此经常会有几个组打架的情况，如果出现类似的几个function/几个组一起 compete 的情况，肯定要有一个人来决策，所以有一个我们叫STL（Single Thready Lead 单线领导），这个人一般是一个 director 或者 VP 去对各个组扯皮的东西来决策*

- 业务上的想象力、技术积累和独特的positioning：

> **想象力：**
> *从新的往旧的说，上周刚 announce 要做humanoid，其实大家都在想到底 VR 能干啥，现在 VR 能做的是两个：打游戏和看视频，这两个都不是所谓的刚需痛点。最大的还是下一代计算平台，取代手机就要手机做不了的事。比如 AVP 能做的 eye-tracking 手机做不了，因为手机在兜里没法一直 eye-tracking,  hand-tracking， face-tracking 。AVP也是一直在做「取代手机的功能」*
> *未来这几个功能最有可能落在什么形态上？短期能看到的是眼镜， Meta 在这个赛道上很久了，准确来说是 Meta 开创了智能眼镜的赛道，Ray-Ban Meta 也证明了用户愿意把摄像头带在脸上*
> *长期看 eye-tracking,  hand-tracking， face-tracking 到底能干啥？一个方向是机器人，因为这些都是机器人目前最缺的，因为现在机器人现在是imitation learning（模仿学习），类似小孩什么也不懂，但看大人做2000遍就能学会，训练起来很费劲；但如果用类人的方式，人的脑子（大模型）、人的眼睛（smart glasses+eye tracking）、人的手（机械臂+hand-tracking），整个 humanoid 可能都会有一些范式变化，这就是Meta在bet on的东西*
> <u>技术积累</u>：
> *类人的方式是：眼看+手拿，这完全是 VR 头显可以做的，头显首先 eye-tracking，再 hand-tracking，我们的技术已经可以知道手在这个杯子的前面还是后边，这些景深的技术我们都有，而机器人公司没有，他们没有头显，Google 也没有，只有Apple 和 Meta 有，而且Apple不会开放的，做 AVP 的应用的人连定位的 location 你可能都拿不到。未来的机器人的操作系统Meta有很大机会，不管你是波动顿动力还是宇树，最后都要接上类似Android的系统*

### Llama

#### **怎么评价 Llama 的团队和组织？**

- **“人太菜了”，方向对的（reasoning model）做不出来，有有数据优势的也做不出来**

> *Llama当时的活水政策有很大的坑，基本是内部high performance的人就可以活水，但很多人是只有相关经验比如是做强化学习的，大家开始从trasformer架构学起，天才密度变低了；人数狂涨，3个月从800人涨到1300人，现在将近2000人了 —— Meta Llama Post-Train Engineer*

> *方向不对做不出来，方向对了也做不出来，比如reasoning model Llama也一直想做、也在做，但做不出来，知道后面被DeepSeek做出来了；有多模态的data set，理论上做图片理解（picture-in, text-out）是有优势的，但我们内部的模型从结果看也是没做出来（开源的多模态模型效果一般，那个没有用meta用户的data set），后来我们内部做了一版用了instagram的data set的模型没外发，效果还是不行，主要是数据质量和模型的architecture 不行，还是因为人菜，基本功不行 —— Meta Llama Post-Train Engineer*

- **“Always on Fire”，War Room是常态，不是新闻上说的DeepSeek出来才War Room**

> *Meta是湾区大厂最卷的，Llama是Meta最卷最累的团队，没有之一，上周的long weekend 几个VP都在加班，我每次1点下班office都有很多人，其他部门office都看不到人的；但今年给了20%的Meet Most（类似3.5-），裁了10%（公司平均只有5%），从裁员比例看公司是不满意的  —— Meta Llama Post-Train Engineer*

> *但每天都在救急，比如模型要train&evaluation，因为我们代码每个人own一小部分，pre-train改了post-train也要改，但因为大家太忙又经常忘记/来不及对齐knowdge，又出了更多bug；knowledge gap 导致了混乱，不仅是 information 层面，就是“不会”，很多人只知道跑 code，出了问题解决不了只能找人、问人、也不知道找谁去修，就回去escalate，只能找manager，manager只能拉一大波人在群里在研究这个bug；裁人也不解决问题，因为不只有一个人 —— Meta Llama Post-Train Engineer*

> *还有一些历史遗留问题， Llama 的 code base 在两个的地方，你可以理解为 Meta 内部有一套infrastructure，是大家一直在用的，但是 Llama 开始的时候是FAIR做的，然后FAIR 的 code 全部在外部的 Github 上，跟内部不是用的一套东西，我们现在是混在一起用的，就导致了更多的混乱。再加上每次project都特别急，很多线下来不及测试就上线了，出bug了又要去救急，很多时候是这么个状态，llama 3的bug到现在还在修；所以很多时候感觉大家在忙没那么重要的事，在救火（注：FAIR团队和GenAI组织的历史可以参考：[Meta AI Org Revolution](https://docs.xiaohongshu.com/doc/8d25cba875277a492bb572fe2cd37316)) —— Meta Llama Post-Train Engineer*

> *我的感受是GenAI团队一直没想清楚，到底是做模型、平台，还是应用，现在是全都要，我听说前几周那边有100个PM在群里吵架，因为有个团队找不到 use case，本来是找GenAI的，但他们一直在吵方向，没人接需求，就来找我们了 ——   Meta Business AI Director*

> *We often say at Meta we value productive tension...when an organization is under pressure it is more valuable to move in a uniform direction  ——  CTO Boz, 2022*

#### **为什么从结果看，人多、卡多，但Llama 4依然难产？**

- 每1.5个月就有check point，“Move Fast”，使得团队在技术路线选择、人力投入上都很短视

> *为了meet evaluate bar，先把评测集放进来train，发现还是没法meet bar，就把evalaute bar也调低了，因为负责evaluate bar的团队也在GenAI里，都是一个老板Ahmad，evaluate团队也压力很大，不希望是整个team的卡脖子 —— Meta Reinforcement Learing Engineer*

> *在模型进化路线上也选择短期有受益的事，我准备活水的时候和llama的director聊过后来放弃了，因为我发现Llama只做post-traing的雕花，不做RL，后面deepseek做RL做出来了。为什么这样？因为做post-train每周都能有结果，比如 how are you? 这种简单的query 找500个数据做SFT，结果就更好；但没法投入2周时间做更难upside更高的事比如RL；我看到有的Llama做sft的engineer在workplace发出来的post是说自己局部优化了一些场景和回答，发现了用户痛点（发现how are you 回答的不好），leverage了组织的力量（找人来标了500个数据），最后解决了用户需求（how are you回答的更好了）—— Meta Reinforcement Learing Engineer*

> *还比如业内都在做PPO，但Llama的technical report特地说:  PPO不work（注：见下述图片），其实是因为PPO需要更好的人、花更长的时间，要take risk，OpenAI之前的联创John Schuman是PPO的一作，连这种业内共识的、已经做出来了的技术实践，Meta也很难take risk —— Meta Reinforcement Learing Engineer （注: DeepSeek也没有选择PPO路线，而是优化成了GRPO）*

![](https://xhs-doc.xhscdn.com/1040025031ek0bqekke059kk3e0?imageView2/2/w/1600)

> *pre-train 需要 architecture，bottleneck是chips，好不容易有卡可能2-3周才能出一个结果，post-train 更容易短期出活，理论上有人力都能有产出，一定能train出来，就是发现bug喂数据就行，最后边际效应递减而已；Llama做post-train的人比pre-train多 —— Meta Llama Post-Train Engineer*

- **“没有一个老板非常懂，从小扎到Ahmad到VP”**

> *Llama的middle manager什么都不懂，而OpenAI让最强的10个ic make all the decisions，openAI认为不需要people manager；应该从2000人砍到300，super ic拎上来，manager靠边站；在Llama这个事上，hr缺位（Meta的HR很弱，Engineer自己搞文化和组织） ——  Meta VP of engineering*

> *小扎确实很hands on在Llama上，之前在instagram，所有的decision最后到director最多到VP就能拍板了，来了Llama发现从模型参数几个b，到开源哪个模型，模型的架构，Meta AI的模型定位，都是小扎拍的板，我们都知道他非常关注，非常handson—— Meta Llama Post-Train Engineer*

> *GenAI的老大Ahmad 之前Apple做autonomous driving的，加拿大人 ，擅长的是CV视觉不是大模型 —— Meta Llama Post-Train Engineer*

- **"focus on impact"的考核标准让大家只看numbers**

> *Llama的人做事都很不fundamental，比如产品VP之前提过的一个奇葩的降本增效的需求：怎么提Llama的DAU（增效），同时降低Llama的回答输出（降本），Meta的metrics都是和roi有关，负责做这个需求的manager说做了两个月后来做不下去了 ；这个VP之前是做Facebook App的—— Meta Reinforcement Learing Engineer*

> *比如之前CPU转GPU的shift，计算效能翻了100x，engineer 也没干什么事情，业内都换GPU了，但是整个team都有非常好的绩效和promotion —— Meta Reinforcement Learing Engineer*

- **“鱿鱼厂”，团队文化变差**

> *小扎内部的post明确说接下来“每个performance cycle都会强制裁员5%”，也就是半年你的组一定会有5%的人要走，所以大家很有竞争的压力，不希望被其他人知道，我朋友landing的时候有一个tensor平台使用的问题，整个team没有人回复他这个工具怎么用，后来还是找了他自己的一个前同事解决了，更别说corporation。我的team members上线了之后拿到了结果之后我们才知道。半年为考核周期，都在抢low-hanging fruits，抢到果实吃下去了吃到了，恭喜你又续命半年，是这么个鱿鱼游戏*

> *之前我的组员的一个idea在offline测试，还没launch的时候，被隔壁组的人打包成了一个 combo 抢先上线了，因为在Meta每个人的代码是透明的，别人都能看到你的代码。我只能劝他说在Meta就是你launch了才能算你的，然后帮他上升协调了，最后在project上挂了一个名字，但performance review这个项目很难算给他*

- **“When a measure becomes a target, it ceases to be a good measure”**

Boz 2023年在自己的博客中频繁提到focus on impact带来的负面问题：

> *This problem is the foundation of Goodhart’s law, which states that “when a measure becomes a target, it ceases to be a good measure...*
> *People will notice if you celebrate the launch of something new but not the successful maintenance of something old. If you never celebrate a team shutting down a program or having a *[*convincing failure*](https://boz.com/articles/convincing-failure)* then people will naturally gravitate in the opposite direction. Over time these trends compound until you have technical debt and feature creep...*
> *It is just who we are as a species — we try to meet the cultural expectations around us first and foremost.*
> *—— 2023.2 Boz's blog*

#### **R1 出来后，Llama组织内部有哪些变化？**

> *DeepSeek出来之后，Almad 要求我们director每周和他开2次会汇报War Room的进度；我听到的是开会频次没听到大的决策和组织调整，我的体感是老板在疯狂push进度，逼大家execution，背后还是因为老板没那么懂？除了execution不知道能做什么*

> *有leader被降级了，下面一个负责 post-train的华人团队大幅裁员，还有一个本来要升director，下面100个人，刚被降成 IC了；组织里确实在研究DS的技术，我觉得就是你说的只学了how没学到why，只学了技术，但开卷考试了按Meta的执行能力大概率能做出来了*

#### **Top Researcher和Engineer 怎么看 Meta/Llama？**

> *我觉得有两种相对幸福的工作，一种是OpenAI, busy but extremely excited, 一种是Google, not excited but extremely chill；Meta 既没有OpenAI excited，也没有Google chill，而且我观察我在Meta的朋友都没那么开心，所以我不会考虑Meta —— OpenAI Longevity Science Model lead researcher*

> *我们的founder之前是Meta ESM（Evolutionary Scale Modeling）Lab的负责人，你可以理解为 Alpha Fold 是第一个用计算代替实验做蛋白结构预测的，但AF最大的问题是在计算上有bottom neck，需要大量的搜库而占用计算资源；而Meta ESM 把这个事儿解决了，很牛的技术突破，且效果上很好，甚至微微超过AF3达到了SOTA水平，但小扎却让整个团队都走了，可能是觉得这个技术没法短期应用在产品上，很难想象 Google Deepmind 会把刚做出来Alpha Fold3的团队干掉 —— Ch.ai ( 被OpenAI投资）Founding Team , ex-Meta ESM Lab lead researcher*

> *Meta比较崇尚move fast，文化总体比较高压，但我比较偏向打磨一个东西，我的stereotype里是国人去的大多是冲着钱 —— Nvidia Staff Engineer*

#### Llama的意义和目标是什么？

- 做落后于DeepSeek 3个月的开源模型，缩减科研和算力成本，集中做BC端的应用

> *最差的情况是Llama永远都在追赶，拿到DeepSeek recipe的三个月内做出来一样的模型，也足够好了，去防止没法用DeepSeek的风险，永远要有自己的模型。而且但你就不需要做这么多research了，2000人的团队变成200人，人和算力都省下来，只做第一名的follower*

> *从广告团队模型应用的角度，我们不强制使用Llama，什么好就用什么，因为我是 on behalf of the business，我最牛的是可以 access business 和 users ，这个市场上应用能成的关键不在于模型，所以我一直不太在乎Llama，不行就用别的 model *

> *Meta AI 有几个不同的 workstream，有 ads、agent/bot，有还没launch的group subscription（类似ChatGPT），我做的是bot，我们的vision是未来Facebook、Whatsapp、Ins上的任何一个 business 都需要这个bot，比如东南亚的商家，他们的用户习惯和商家聊天，但商家没法提供 24 小时客服，有了bot以后 conversion rate 变高，广告单价也能提升*
> *为什么 Salesforce AI CEO 过来？是因为 Salesforce 只有 CRM和系统，很大的短板是看不到 user 真正会问什么，里面的90%都是 garbage 的数据，但是Meta有chat的数据，我能知道整个退货流程，user退货会先问什么问题，客服应该怎么答，怎么引导user退款等等*

> *东南亚有很多小店没有网站，只有一个 Facebook 主页，主页上有很多营业信息：我什么时候打折、几点开门，Facebook 是一个infrastructure，B端也有很多user case可以去模型解决*

### 附录

**Highlight： [Meta VP访谈-202503](https://docs.xiaohongshu.com/doc/8c2802df212a61565e2041b5e022b125) 推荐读一读！**

| **一级 Org 部门** | **Notes** | 是否持续做功 |
| --- | --- | --- |
| **Ads** | [Meta VP访谈-202503](https://docs.xiaohongshu.com/doc/8c2802df212a61565e2041b5e022b125) <br>[Meta Search Engineer_20250213](https://docs.xiaohongshu.com/doc/c83e77b97fb2ef192a2b3d298140a0d6) | ![](https://xhs-doc.xhscdn.com/1040025031f0cfnfkke0b54mij4?imageView2/2/w/1600) |
| **Business AI** | [WIP_Meta Business AI Director_20250224](https://docs.xiaohongshu.com/doc/b2852189a4845d95e8c0989285486f53) | ![](https://xhs-doc.xhscdn.com/1040025031f0cfnfkke0b54mij4?imageView2/2/w/1600) |
| **GenAI** | [Meta Llama Post-Train Engineer_20250220](https://docs.xiaohongshu.com/doc/5982fce8f696e81e296b647bed702afe)<br>[Meta_Reinforcement Learing Engineer_20250219](https://docs.xiaohongshu.com/doc/5387ee8ede29c40fe70573cd0661ab74) | ![](https://xhs-doc.xhscdn.com/1040025031f0cfnfkke0b54mij4?imageView2/2/w/1600) |
| **Reality Labs** | [WIP_Meta Hardware Engineer_20250222](https://docs.xiaohongshu.com/doc/6392f53fbbd7ee40aa7e5b7253fdc087)<br>[Meta_ex-Reality Labs_20250218](https://docs.xiaohongshu.com/doc/912623af2a94e7fb128c1ed8eacf5f64)已离职<br>[Meta Reality Labs PM_20250211](https://docs.xiaohongshu.com/doc/daef04e9b03351f3bcd8ea300e1c254d) | ![](https://xhs-doc.xhscdn.com/1040025031f0cfnfkke0b54mij4?imageView2/2/w/1600) |
| **Facebook** | [WI_Meta_Video Recommendation Engineer_20250221](https://docs.xiaohongshu.com/doc/54b17abe9dbe5aeb2b1db3b23e3fc88f)<br>[Meta_Marketplace Data Scientist_20250212](https://docs.xiaohongshu.com/doc/0b96ba6af8a7b9009d4e70a34a19a8c8) |  |
| **Finance** | [WIP_Meta Finace/BizOps Senior Manager_20250224](https://docs.xiaohongshu.com/doc/abd446b79d861dc1094a1bf6e57072b1) |  |
| **Infra** | [Meta AI Staff Engineer_20250213](https://docs.xiaohongshu.com/doc/9b8fd7af785d453751adce085c906bd4)<br>[Meta AI Infra Data Engineer_20250213](https://docs.xiaohongshu.com/doc/c07a54c0a248499bbb5aef901b56a8ff) |  |
| **其他** | [Nvidia Autonomous Vehicle Robotics_20250213](https://docs.xiaohongshu.com/doc/dd8f74bf6b9935f0c68692d5c7f30bf1)<br>[TikTok_Ads Platform_20250212](https://docs.xiaohongshu.com/doc/801f6378fc5e40917f84e28b5eb00891) |  |

![](https://xhs-doc.xhscdn.com/1040025031elejpp8ke04qukdek?imageView2/2/w/1600)

