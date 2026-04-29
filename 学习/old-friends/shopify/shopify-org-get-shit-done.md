# Shopify组织穿透：在不确定性下Get Shit Done 副本

> *在[Shopify One Pager](https://docs.xiaohongshu.com/doc/4f6d81ede37507d1ed65c81c4d9545e4)里我大致阐述了Shopify CEO Tobi的管理哲学，通过最近几周和Shopify员工的交流，对Shopify的组织有了更立体的认识：*
> *1）CEO龙卷风：基于Get Shit Done这样的内部系统，shopify实现了CEO Tobi和各个VP可以了解并干预组织内所有项目，组织熵增被急剧降低，但组织边界也客观被管理团队的决策能力和精力cap（对组织冗余和组织惯性的极致对抗）。*
> *2）基于愿景确定目标，而不是基于指标确定目标：Shopify愿景出发确定目标确保了团队做事的方向一致，且不会被短期指标左右，同时给予了团队更大的自主性，但目标的校准和达成上同样变的主观和不确定，必须配合自上而下的频繁校准。*
> *3）欢迎混乱，而不是构建秩序：Tobi是深谙管理上不确定艺术的大师，thrive on change是shopify组织最合适的形容词（松散耦合、高度协调是建立公司的一类最佳原则）*
> *4）Devolop Company as a System：内部系统影响团队写作、思考和想象世界的方式，从项目管理到HR的系统都体现着shopify特有的管理艺术。*
> *5）理想主义是Tobi成功的原因也是弱点：对理想主义的追求带来了shopify在管理上的独树一帜，但全员remote可能更像是失败实验。*
> *以shopify为样本，对winner pattern和组织管理也有了一些新体会：*
> *1）管理是系统工程不是单点优化：管理上没有脱离系统的局部优化，基于愿景管理需要配合频繁校准，不确定的管理艺术又需要配合可以 adapt change的人才选型；*
> *2）管理也是民主和集中的艺术：管理的本质是对民主和专制的平衡（shopify在愿景上集中，在方案上民主，在校准上专制）。*
> *一些本文里引用的值得一读的shopify内部文档：[Tobi关于AI Org变革的内部信](https://docs.xiaohongshu.com/doc/c3b44e6e8b107986c6ca97169fedd184) [Shopify's Vision for 2025](https://docs.xiaohongshu.com/doc/da6c71ec35cbb6dea0562a33d33f7266)*

### Everything Matters, All Details Matter

> **Shopify全员remote、CEO强调只需要工作4小时的设计会让大部分人认为这是一家自由至上的公司，但很多员工都会提到这是外界对shopify的极大误解。通过Get Shit Done这样的项目管理工具：内部所有项目VP审批，Tobi审查所有项目，确保了Tobi和管理团队对所有项目的进展都能掌握全部Context并随时干预，组织熵增被急剧降低，但组织边界也客观被管理团队的决策能力和精力cap。**
> ![](https://xhs-doc.xhscdn.com/1040025031fijom1mke06d0bmns?imageView2/2/w/1600)

- **CEO和VP Review所有项目进展**

> *任何团队的每个项目都会进入GSD（Get Shit Done），有五个阶段——提议、原型、建造、发布、结果。 OK1是产品、用户体验、工程和数据的主管审核，VP等高管审核OK2。这实际上对 PM 团队来说是一种很好的锻炼，因为PM大多会附上简短的视频，解释产品或项目是什么。PM 必须非常简洁地说明“这是什么？为什么它有价值？它是如何工作的？”，这是一个很好的练习，让他们在简短的视频中获得了把故事讲清楚的能力。整体上PM决定我们是否应该这样做，而工程和用户体验对我们如何做有否决权。但最后产品经理必须亲自决定这是否准备好发布。如果他们说可以，而这东西是垃圾，那么产品经理必须承担责任。——Glen Coates，shopify 产品副总裁*

> *“GSD”这个系统用于跟踪产品团队的项目进展，保持组织扁平，让Tobi更理解工程师们正在完成的工作, Tobi会至少每六周一次审查所有项目。——Jeff Hoffmeister，shopify CFO*

![](https://xhs-doc.xhscdn.com/1040025031fau8s4b4e08n4vb28?imageView2/2/w/1600)

> *和别的任务系统相比，我觉得GSD最大的区别在于实质上是个管理工具，它会迫使你从各种角度补充齐全context，包括项目的背景，然后mission是什么，关键的节点，怎么去define重要的matrix等等，这些他都会去push。到了关键节点，他也会持续push你的进展。——Shopify Janpan Regional Marketing *

> *我在来shopify工作之前会感觉到他应该是一个很开放，很worklife balance的公司。但是来了之后我觉得不是这样的，我理解随着事情越做越大、人越来越多，Tobi会认为这还是他自己的事情，所以Tobi自己既是CEO也是CPO和CTO。（追问：我知道Tobi同时兼任CEO和CPO的，但是有独立的CTO）去年来了一个微软的来做CTO，但实际上主要管AI的事。————Shopify Payment Director*

- **强VP+轻量化审批确保运转效率**

> *（问：所有项目都要VP审核会拖慢进度吗？怎么review的过来）首先我们的VP都很强，director也都很强，他们不是传统的大厂中层，而是真的是在以创业的方式去做事，并且真的都个性各异。（听说大部分之前都是founder）是的，我们的VP level也就几个人，但他们对每个项目的involvement是极高的，每个项目都会review，因为他们都在OK2里，tobi对大部分项目的involvement也很高。（全公司的项目量级是多少？）我们每年发布两次，光是launch的产品就有150个-200个，还不包括那些可能中间被否定的，每个产品背后2-3个项目的话，所以是大几百个项目量级。*
> *但是我们的审核做的很轻，instead of做一些文件或者PPT，你就是录一个两分钟的视频，我们现在非常从上到下非常推崇录小视频，你就一两分钟你就快速的介绍你这个产品，make了多少progress，包括我们那个VP of product他给我们feed back，也是他直接录一个我们叫fiction log的东西，就是他录屏他所看到的这个产品加上他自己的reaction，最后把这个视频发给那个product team——Shopify Product Marketing leader ,Developer & App Ecosystem*

- **What's the price**

> *我觉得整体上shopify的效率是快的，但是你跟director讲完以后还有VP也要讲，而且VP他要做这么多事情，他昨天跟他讲了他可能今天就忘了，或者VP好了，Tobi又不同意做这件事情，所以有时候就也没那么快————Shopify Payment Director*

> *这个模式的缺点的话，特别是下面的员工会非常有top down的感受。比方说你本来跟你的product director聊的好好的，然后你们的愿景怎么样，为什么要这么做？但是上升到Tobi可能他不喜欢——Shopify Product Marketing leader ,Developer & App Ecosystem*

> *我觉得内部如果你有什么新的想法的话，怎么样其实也要Tobi同意才可以做的。如果你在那边做的比较久，跟Tobi的关系比较好的话，你还可以提一提新的想法，但是新的人不一定能和他match。如果他已经确定做这个事情的话，基本没有人可以阻止他去创新这个事情。——Shopify Payment Director*

- **每个人都可以随时找CEO**

> *在shopify大家都会有一种感觉，就是如果你有什么事情可以直接去找Tobi和其他高管，他们都会回复你，但是其他公司你去找是不理你的。——Shopify Payment Director*

> *我觉得shopify比较好的点是visibility。你在get shit done里可以搜到全公司所有在进行的项目。不管是你是哪条线的，只要是有关键词去搜索，你都能搜得到。你可以去follow这个project。如果你follow了一个project的话，它所有的更新你都会收到邮件的提醒。——Shopify Janpan Regional Marketing Leader*

### 愿景上集中，方案上民主，校准上专制

> **目标的确立上Shopify站在了Meta和字节这样公司的反面，产品上不以指标驱动而以愿景驱动，基于getting started business so easy、Shopify keeps me on the cutting edge这样的愿景，确保了团队做事的方向一致，且不会被短期指标左右，同时给予了团队相对的自由。但这一机制下目标的校对和达成上同样变的主观和不确定，决定了只有配套shopify自上而下频繁的校准才能稳定运转。（shopify的vision全文可以参考：[Shopify's Vision for 2025](https://docs.xiaohongshu.com/doc/da6c71ec35cbb6dea0562a33d33f7266)）**
> ![](https://xhs-doc.xhscdn.com/1040025031fnrsbpvke0dleic1o?imageView2/2/w/1600)

- **产品团队不看数**

> *我们不会仅仅因为某个项目无法量化就将其判定为失败或否决推进。比如我们正在对 Shopify 商家后台界面设计进行大刀阔斧的改版，唯一理由就是我们认为新设计更美观、更符合产品调性。这个决策没有任何数据支撑，但衡量成功的标准只有一点——当改版完成后，我们看着它感叹："太酷了！我超满意！商家也超满意！" 这就够了。——Glen Coates，Shopify VP of Product*

> *我们不基于短期指标工作，因为有许多有悖直觉的情况。我建议大家如果有可能可以回顾那些你们自认为最成功的（短期）实验，观察这些实验在一年、两年后的指标。我敢说一年后指标与预期不符的次数会让你们惊讶。——Archie Abrams, Shopify Head of Growth*

> *我在shopify干了四年了真的都不measure指标，比方说我现在的生态团队，我们完全不在乎ecosystem会在乎有多少新增，我们只在意的是这些APP有没有帮助Merchants更好实现他们的创业——Shopify Product Marketing leader ,Developer & App Ecosystem*

- **基于Vision定目标**

![](https://xhs-doc.xhscdn.com/1040025031g21lh2gke0bjpmbfs?imageView2/2/w/1600)

*完整内容参考：[Shopify's Vision for 2025](https://docs.xiaohongshu.com/m/doc/da6c71ec35cbb6dea0562a33d33f7266?source=copyLink)*

> *（没有数字那我们要怎么确定目标？）我们会根据vision来定，每年年初Tobi会发邮件说我们今年的五个vision，然后Glen（vp of product）会再写他的十个vision，下面每个人在基于他们的Vision确定我们要做什么项目。比如今年Tobi的第一个Vision是 getting started business so easy，他会大概说下他对这个事的理解，那我们就会往下拆解，是不是我们可以去简化商家的on boarding页面和store front页面（怎么去校准我们的目标是否达成，或者理解是否正确？）我们每六周是一个check point，会和VP去对所有项目进展，然后Tobi会在他的时间表上单独review所有项目。——Shopify Product Marketing leader ,Developer & App Ecosystem*

> *我觉得内部最在乎的还是产品本身以及对商家的价值，而不是赚钱和数字，有个经常提的价值观排序是：构建伟大的产品、赚钱、利用赚来的钱来构建更多的优秀产品，并且永远不要颠倒前两项的顺序——Shopify Janpan Regional Marketing Leader*

- **Vision下的自由**

> *我觉得shopify从mission的角度是天马行空的，比如今年一个mission是要降低北美的收入占比，但其实没人知道要怎么做，什么方案都可以提——Shopify Senior Sales Manager*

> *我很少看到有公司像shopify的员工一样认同和了解团队的vision，核心还是因为CEO每一年他都会说我今年最重要的Vision是什么，例如AI我们要怎么做，海外我们要怎么做，然后有不同的人去承接，这里面的自由度还是很大的，都确认了之后才会变成一个project去做。——Shopify Payment Director*

### 欢迎混乱，而不是构建秩序

> **Tobi作为深谙不确定管理艺术的大师，整个shopify的组织都构建在变化和不确定性之上，管理团队随时跳到项目里决定了团队拥有对抗惯性的能力，就像Tobi说的：''我仍然相信松散耦合、高度协调是建立公司的最佳原则。我们聚在一起，信息充分流动，但每个人都充分认同公司试图在世界上实现的变革以及公司自身的定位。''**
> ![](https://xhs-doc.xhscdn.com/1040025031fikbko64e07p2fhfs?imageView2/2/w/1600)

- **''Tobi龙卷风''**

> *我写了一个脚本，把Shopify所有定期会议都给删掉了。我们发现例会很成问题。这种会议太容易开了，也没人想取消这种会，因为有人要对开这种会负责。那些想要取消这种会的人宁愿熬下去，也不愿言辞激烈地说，“嘿，这件事情再也没有价值了。”取消真的很难，但是我们进行了一些分析，发现有一半的例会被认为是没有价值的。这会浪费大量的时间。所以我们就提出来：“为什么不把所有的会议都干掉？” 于是我们就这么干了。这相当粗暴，但是我们现在一切都在按部就班。‘’  ——Tobi, Shopify CEO*

> *我们有一个Tobi经常会聊词的叫‘’Tobi Tornado‘’，就是''Tobi龙卷风''。可能一个项目做了半年，然后托比他突然看了一下，然后说不喜欢，就会直接砍掉。（团队成员是不是会很难接受？）虽然Tobi也砍，但也不是无缘无故的，可能几百个项目里面有几个，只是他会很直接的表达他的想法。*
> *我可以举一个最近被砍掉项目的例子，我们marketing团队想重新设计面对developers的网站，Glen他们都全都on board了，团队也设计完了。给Tobi看了以后，Tobi的反应是我们为什么要花人力做marketing？他说我们更应该花更多的精力来做给developer的documentation，所以整个项目被砍掉了，但是后验来看这个判断很对。*
> *——Shopify Product Marketing leader ,Developer & App Ecosystem*

> *今天我和一位 Shopify 前员工聊了聊。他提到员工们称之为''托比龙卷风''（Tobi Tornado）的现象，这让我对 CEO Tobi Lutke 更加敬佩了。故事是这样的：Tobi会随意加入公司内部的 Slack 频道。有时他会突然在某个频道发消息，宣布团队正在合作的项目立即终止，因为他认为这个项目不值得公司投入资源。这种行为充满争议：一位 CEO 在自信地「砍掉」项目可能导致决策机制混乱、大量工作被废弃、甚至显得不尊重团队。有时项目明明很小——为什么 CEO 不「选择性作战」，让它完成呢？这会打击士气。更何况，领导者的判断有时也可能是错的。但总体而言，我认为企业需要这样的「龙卷风」，原因在于：*
> *1. 领导者掌握更多全局信息，而高质量的判断力正是他们存在的核心价值。不表达判断的领导者是失职的。初创公司资源有限且节奏极快，决策往往依赖直觉——而这是合理的。优秀领导者未必永远正确，但他们能识别：哪些是平庸之作，哪些是顶尖人才；哪些是有效进展，哪些是浪费时间。他们必须直言不讳。*
> *2. 让每个项目都变得重要：我深信组织中的「破窗理论」：当你让团队意识到，无论项目大小你都同等重视，所有人都会保持敏锐。*
> *3. 让批判性思维与逆耳决策常态化：担心让团队失望是人之常情。但当你克服这种恐惧，并解释「为何某事是浪费」，你其实在帮他们培养判断力。同时，你也赋予他们在其他场景中表达异议的勇气——哪怕这些意见不受欢迎。*
> *4. 打破现状偏见与沉没成本陷阱：即使在优秀团队中，这两种思维惯性也极强。领导者果断终止项目的行为，是用身教示范如何对抗惯性。*
> *5. 从「政治与情绪」转向「价值优先」：我多年观察发现：组织政治是自我实现的预言。如果领导者害怕表达判断，团队会变得脆弱且恐惧批评——而这反过来让领导者更畏缩。当领导者抛开顾虑、尊重但坚定地表达判断时，问题会变得更「非个人化」。龙卷风绝非针对个人的讨伐，有时它的出现，恰恰是因为领导者此前未能充分共享信息背景。重点不在于指责，而在于纠错前行。*
> *6. 为所有管理者树立榜样：这等于告诉其他领导者：「你们也有权这样做，甚至应该这样做。」优秀领导者会提供背景与决策框架，帮助团队在局部做出越来越好的选择。Shopify 已围绕项目管理建立了更系统的结构，甚至开发了内部工具，但「龙卷风」依然存在。——Itai Damti，Unit CEO & co-founder*

- **Thrive on change**

> *回顾Shopify的历史，从0到1的支付业务、物流业务，再到现在从小B转大B基本都是把历史推翻重来的过程——Shopify Product Marketing leader ,Developer & App Ecosystem*

> *我个人觉得内部最常被提到的价值观是thrive on change，举个例子Tobi最近就发了一封邮件，所有的产品立项都要引入AI，增加新的HC需要先回答为什么AI不能做到，这样的迭代内部非常频繁（全文参考[Tobi关于AI Org变革的内部信](https://docs.xiaohongshu.com/doc/c3b44e6e8b107986c6ca97169fedd184)，值得一读）——Shopify Senior partnerships manager *

> *举个例子，过去一两年我们一直在做B2B，因为它的体量大，所以对GMV的贡献大。但是我们发现就算切过来其实资金流的角度还是会走银行的电汇。所以管理团队就觉的表面上B2B签了很多大单，但是其实没有实际收益。所以一下开始除了北美所有b2b的产品就全部不做了——Shopify Senior partnerships manager *

### 离经叛道的招聘标准，背后也是朴素的人才观

> **Shopify的招聘有很多广为认知的故事，最大比例的中高层都曾经是founders、招聘官网最大的标语是#Not everyone can do this、Tobi直接给星际争霸的职业选手发过offer，但其实背后的人才观其实是朴素的：Shopify希望你拥有的是Make long-term right decision和不确定环境下保持growth mindset的能力。Shopify的内部系统同样体现了他们对人才和管理上的哲学。**
> ![](https://xhs-doc.xhscdn.com/1040025031fimfu794e035bm59s?imageView2/2/w/1600)

- **Comprehensivist和Growth Mindset**

> *综合主义者（comprehensivist） 我觉得这是一个很花哨的词，但我的确喜欢这个概念。我发现，每一个领域前面的那80％其实是很容易就能学会的，这跟帕累托原则差不多，我认为创造力通常就是指大家用不同的方式把这一个领域学到的东西运用到另一个领域上，也因此我觉得学习很让人着迷。——Tobi，Shopify CEO*

> *我觉得shopify招人非常独特，以至于我现在帮人refer的时候都能看出来他们能不能进公司。我经常会开玩笑说shopify非常像一个邪教团体。因为他就是招一种特定的人，招进来有几个指标：一个就是看你能不能adapt change，能不能在一个快速变化的环境下适应，二是看在life story各个阶段里做过哪些一些重大决定以及你背后是怎么思考的。最后他非常喜欢那些在本职工作以外，你有一些什么别的在研究的东西。所以我的同事真的每个人都深藏绝技，可能你是市场的同学，但是你外面又是一个音乐人或者有自己的护肤品牌。——Shopify Product Marketing leader ,Developer & App Ecosystem*

> *他也会做case study，但是给你的题目完全跟你自己做的事情完全没有关系，看你怎么去看这个问题和分析这个问题。他还有一个很重要的原则叫first principle，你不只是解决一个问题，二是真的知道问题中本质的部分在哪里。——Shopify Payment Director*

- **内部系统决定你的思考方式**

> *Shopify 构建了所有东西，包括合规、人力资源、工资系统等。我们没有使用 Linear 或 Jira，所有的工具都是内部构建的。这是因为工具对于人们的影响远超我们的认知，没有所谓的完全中立的软件，你使用的系统构建方式会改变你的写作方式、思考方式和想象世界的方式。—— Kaz Nejatia，Shopify COO*

> *shopify的绩效系统我觉得是蛮特别的，是一个完全黑盒的算法，输入的东西有几个：自己给自己打分。你周围的同事给你打分。老板给你打分，这几个比较常见，但是我们还有一个坐标，你可以给同样职能的人排序。比方说我跟很多PM合作，然后我就会有一个轴，可以把这几个同级别的PM排序，觉得谁比较好，谁比较不好。基于这些输入会直接有你绩效结果的输出。*
> *给别人的打分也不是直接进行打分，而是针对每个人有一个类似心理测试的问卷，每个问卷10-20个问题。问的问题也很有意思，比如：最近的六个月，我有没有额外的表达过他工作非常好；你现在要开始一个新的项目，你会尽多大能力争取让这个人在你的团队上；他有没有prioritize最重要的工作；他做一些比较重要的决策的时候，有没有做出正确的判断...等等。根据这个人的角色，问题也会很不一样。*
> *—Shopify Product Marketing leader ,Developer & App Ecosystem*

> *Tobi自己写了一个系统，每个员工可以自己决定自己总包里现金和股权的比例分别是多少，而且这个比例每三个月就可以根据当时的股价调整一次。如果你选择的是RSU或期权，还会有额外5%的股权奖励 。我自己也是个founder，我觉得这是很多top talent或者founder们选择shopify的重要原因——Shopify Payment Director*

![](https://xhs-doc.xhscdn.com/1040025031fnlu9jt4e064231sg?imageView2/2/w/1600)

*                                                                                                                               图示：shopify的薪酬分配系统*

### 全员Remote，是成功的豪赌还是失败的实验

> **全员remote是Tobi理想主义的体现，背后有Tobi很深刻的管理思考（更多元的团队文化、更平等的交流关系），但也客观上阻碍了内部的交流效率和工作效率的进一步提升**
> ![](https://xhs-doc.xhscdn.com/1040025031fnp7dm54e0384bnmo?imageView2/2/w/1600)

> *我曾和Tobi 在是否采用远程工作模式上有分歧，虽然我现在赞同他了...我认为对大多数公司来说，完全远程工作是个非常糟糕的主意，我建议几乎所有公司都不要这么做。Shopify 之所以能成功实施远程工作，是因为我们投入了大量时间和精力来构建系统、工具和软件。如果没有这些准备就贸然实施远程工作，肯定会失败。如果我们事先知道转向全员remote的这个过程会如此痛苦，可能就不会这么做了。但一旦做出决定，我们就会坚定地执行了下去。—— Kaz Nejatia，Shopify COO*

> *我觉得tobi很多想法其实也有点过于理想化了。全员remote这件事我自己就很不看好，虽然帮助shopify招来了很多人，但确实交流起来很不方便。在加拿大的领导和员工交流起来可能方便一点，但是别的地方就很距离。如果在加拿大，虽然是remote，但是在加拿大那边住的人他们还会去公司，所以在公司和不在公司那些人还是有区别的。但我觉得shopify的特点就是随时会变，所以如果哪天通知取消全员remote我也一点不会惊讶。——Shopify Payment Director*

> *我觉得全员remote对打工人的视角肯定是好事，确实大家其实大部分人没有那么卷。但我觉得好的一点是，shopify的每个人，真的我也不知道我们怎么招来这些人了。我觉得遇到的每个人都非常的认真工作，非常非常的在乎自己做的事情，很自驱的去把事情做好，而且是真心想帮助用户和商家。*
> *——Shopify Product Marketing leader ,Developer & App Ecosystem*

