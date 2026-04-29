# NVIDIA 组织穿透：One Architecture_250620 副本

> 由于英伟达的业务本质和计算需求的增速相关，而不是计算需求的规模本身，因此公司永远在寻找计算需求的 next big bet（历史上找到了PC电脑、游戏、区块链和生成式AI)，在这样的组织环境下，英伟达组织最核心的能力之一需要有「**fundamental ability to stay alert of weak signals**」，体现在组织设计上：
> - 「Top 5 Things 邮件」的机制设计，每个员工给 Jensen 发邮件，对行业的信号做采样，eg., 对「Attention is all you need」这篇 paper 的信号捕捉；Jensen 说「T5T是 NVDA 的 global neural network」
> - 采样之后，由 NV Reasearch 来做信号的放大和转化， NVR 部门除了发 paper 以外，以进入生产落地为目的，设置很多创新小组，立项、中期答辩、毕业 release 的项目基本能落地生产，重要的方向甚至有 5-10 个小组一起做，eg., Transformer Engine 在 ChatGPT 应用爆发之前就已经设计和生产落地
> - T5T 本身也是对重要信号的放大器，Jensen 早期会用「Reply All」的邮件来表达注意力的分布，比如甚至细节到对 CUDA 的客户话术该怎么说； 「Jensen 最近 Reply All 了什么邮件」是员工们茶余饭后讨论很多的话题；类比小红书，T5T 像一个碎片化的「看见商家」，Jensen 不仅能看见，也会立刻指导团队的动作
> 找到计算需求的 big bet 后，怎么建立基于 bet 的生态壁垒？这涉及到英伟达组织保持十年没变的组织设计核心理念：**One Architechture**
> - 无论 Product（Gaming、Automotive、Robotic，前些年的 Mobile ）怎么变，下面的 Hardware Engineering-GPU  和  Software Engineering -CUDA 是基本保持不变的，这两部分是整个英伟达最核心的 **One Architechture**
> - 这两个部门在最底层做了大而全的 GPU 产品，每个产品线可以根据需求来切蛋糕、做阉割
> - 从 2012/2013 年开始至今，英伟达的组织架构按照  One Architechture 一直保持不变，是一个英伟达组织和业务很重要的 inflection point，CUDA 的战略意义在组织架构上正式展现：
> - 在 2012  年，CUDA + GPU 在著名的 ImageNet 图像识别比赛上性能表现为 CPU 的 10x
> - 2013年左右，CUDA 从**硬件部门下的三级部门**变成了**软件部门下的最核心的二级部门**
> - 自此 **One Architechture **的组织架构形成，意味着从「GPU硬件指导软件」变成**「软件定义需求，驱动硬件设计」，**某种程度上软件比硬件的战略意义更重要
> CUDA被看作是英伟达最深的护城河，是怎么构建的？
> - GPU 是一锤子买卖，越来越接近 Commodity，所以英伟达希望客户把「计算方式」跟英伟达绑定，计算方式和 GPU 中间差的东西就是 CUDA；Jobs 说苹果是一家软件公司，「iPod、Mac、iPhone 都是 Software」，英伟达也一样
> - CUDA的发展也经历了几个阶段，从一开始的「工具」到「生态」，从是封闭的、自研的，到半开放的，客户可以自己开发CUDA算子和模版；不看数字指标的老黄，会在T5T里关注developer的数量和反馈，回复邮件问：「GTC大会有多少developpers参加？」，CUDA像GPU生态的“C++语言”，迁移成本巨大
> - 调研了NV中国的客户，发现：不兼容CUDA的华为，软件开发成本巨大，被最后退卡退人；兼容CUDA的平头哥（阿里系芯片公司），在硬件和软件上也都只能做跟随者

### "Stay Alert With Weak Signal“

#### Top 5 Things:  寻找 Weak Signal

> *老黄当时发现了上一代AI的弱点，以前你拍一张图片，能识别是红灯绿灯，但如果这个路口有交警在做手势，以前的AI 是不能识别的；现在 transformer 能识别有时间序列的视频，交警给你做左转或右的手势，现在的AI可以识别。老黄在all hands里提过这个事情，后来我们GPU部门会有讲过，当时「Attention is all you need」出来的时候，我们内部是有讨论的，老黄在T5T里看到有人提，后面他自己也会读paper，他在也会办那种Top 10 Paper的活动，让大家来讲 paper ——  Nvidia 架构师，2013年入职，ex-Intel *

> *Ian Buck 当时是 Standford 的学生，还是实习生，他是 Bill Dally （现在 NV Research 的负责人）推荐过来的，Bill 当时是他的导师，老黄看到了 Ian Buck 上学发的论文，觉得 GPU 不是只来做渲染的，可以 hack GPU 接口，做一个软件做优化更多的计算。但当时 CPU 用的很好，还有OpenCL，没有人觉得 CUDA 有必要存在。你说的信号识别，我觉得唯一的识别人是老黄，可能 Ian 自己都不是 ——  Nvidia 架构师，2013年入职，ex-Intel *

> * If you’re living in an exponential world, you don’t want information to be propagated from the top down one layer at a time ——  Jensen Huang, Wired, 2023*

> *Be alert of very weak signals that could be coming from somewhere. That fundamental ability to stay alert of weak signals, and then being able to go back to first principles when you make some observation, go back to first principles on why is that important, what is the reason, what are the governing dynamics associated with that phenomenon? And then be able to generalize them ——  Jensen Huang, Wired, 2023*

> *Weak Signal 没有下面团队捕捉的，这点和其他大公司一摸一样的，全是 Senior Team 做的，更多就是老黄做的 ——  Nvidia NV Research Solution Architect，ex- GEAR Lab*

- NV历史上经历了从PC游戏显卡，到通用计算平台，再到生成式AI这几个最重要变化，考古历史，确实没有facts表明这些signals的第一来源是T5T，因此把weak signaks的summary放在附录二，供大家参考

#### NV Research：用创新小组放大信号

> *NV Research 整体 200多人，10+个team，都是 researchers & scientists。里面各个方向都有，做封装的，做芯片的、做工艺的、搞机器视觉的，也会发paper，有一个「Internal Projects」的立项机制，和创业公司拿天使投资一样*
> - **谁来initiate：***内部创新项目基本都是NV research lead*
> - **给的资源：***会批一些经费，一般开发会买那些器材或者是开发机，但主要是人的投入，因为会用到一些工程资源，需要有有软件的人来写代码，或者一些硬件人来做一些开发*
> - **时间周期：***最多 2 年，快的 1 年就需要汇报。一般是 6 个月到一年需要汇报，你可以选要不要汇报，看汇报结果公司决定是不是进 Phase 2，最多只能做两年*
> - **怎么结案***：要有落地性的、真正贴近市场的，不是纯粹发 paper 的项目，要能进入生产，所以一般只要你能熬到项目结案，这个技术或者方案能进到最终产品里的概率是非常高的，项目成果转化率很高*
> - **Release***: 两个 T5T Topic/ 邮件组（比如 NV research 邮件组和 Machine Learning 邮件组）里发 internal project release 的信息*
> - **举例：**
> - *比如 Jim Fan，以前 OpenAI 的实习生，做机器人感知的项目，很成功，英伟达现在** GR100 **里用的感知和仿真的工具，都是 Jim Fan 当时的创业项目，后面他 double promotion 了*
> - *比如还有 TensorRT-LLM，CUDA 主要是做 GPU 的并行计算，TensorRT 主要是部署模型的工具链，以前服务器都比较小，计算都是在一个节点上做的，一个节点就两个 GPU 带八张卡，但现在大模型都是万卡集群, 你的这个 CUDA 和你的 TensorRT 是要跨大规模节点，最理想情况是任务能分平均的分布到不同的卡上去，每个执行的时间都差不多，这样不会发生有的卡算完了有的卡还没结束，这就是 TensorRT-LLM，一个非常复杂的计算工具，但非常实用，非常有帮助，这些项目都是 NV Reasearch 他们做的*
> - *比如我最近在支持 NV Reasearch 做自动驾驶的芯片，一个专门针对自动驾驶大模型改造的方案，未来会做到通用汽车的项目里面去，这个项目做了一年，已经完成两期答辩了，效果非常好，通用也很满意，一年就提前 release 了*
> *——  Nvidia 架构师，2013年入职，ex-Intel *

> *Gear Lab（Jim Fan 在的人形机器人实验室） 里做video generation的，做multimodal model的，非常多，最后发现都是一摸一样的，NV Research 里做创新的团队很多，但是基本都给大家很多自由的时间，但最近几年活太多了，创新的自由时间变少了——  Nvidia NV Research Solution Architect, ex-Gear Lab*

> *如果是公司层面的话，创新的基本上都是 NV Research 在做，比如近些年做出来了 Isaac 我们的机器人平台 —— Nvidia Jetson Engineer, ex-Apple, 10年司龄 *

> *2020-2021 年左右，老黄要求 NV research 推动一个叫 Transformer Engine 的一个技术，因为当时安培芯片/A卡已经定型了，老黄特别就要求一定要把 Transformer Engine 做到安培的下一代芯片里面去，后来就做到了 H100 的卡里。结果正好在安培和和 Hopper 的 H 卡之间的时候，大模型火了，生成式 AI 火了，当时 OpenAI 还是用安培芯片/ A 卡做的，后来就是 Hopper/ H 卡立刻就接上了 ——  Nvidia 架构师，2013年入职，ex-Intel *

> *2020年开始，就需要我们 GPU 这边去看一些 Transformer Engine 在 H 卡上的 bug，OAI 的 bug report 就是 OAI report，NV Research 那边会把一些 report 反馈给我们 ——  Nvidia 架构师，2013年入职，ex-Intel *

> *现在 NV Research 部门也在看 Transformer 下一代的技术，因为我们做 GPU 会和 NV Research 的人，因为我们会跟 NV Research有一些讨论。就是让他们去做一些研究理论的研究，看看是不是能·找到可行的办法。我跟他们聊的时候，因为都是中国人，他们会说老黄的重心会放一些在找到下一个AI的方向，下一个 Transformer 在哪，Gemini 最近也是在讨论这个事 —— Nvidia Jetson Engineer, ex-Apple, 10年司龄 *

> *NV去做项目孵化的时候，非常强调内部的小团队作战的内部创业的组织风格。当时有很多内部的大概两三人甚至三四人的个位数的小团队，公司就会给这个团队几百万美金作为一个孵化的资金。在接下来几年之内，用这些资金去折腾，但是给到的折腾的方向足够的自由和开放，所以就是可以孵化出来很好的一些创新的点子，但是给到的钱也是非常少的，所以在有限的资源约束之下，也不会轻易过分的扩张很多的 head count，需要一个人干非常多人的活，需要非常充分的利用有限的资金 ——  现 Intel GPU Senior Product Director，ex-英伟达（22年11月离开）*

> *英特尔也有 Intel Lab （英特尔研究院），但是象征性的做一做，发个 paper 就结束了，没有一套机制，或者强有力的人把创新的东西推到产品里面去 *

> *There's a very large part of our company is designed to build very complicated computers perfectly ；Another part of the architecture is a invention and refinement organization（我聊的员工认为老黄这里说的"invention organization"大概率是指 NV Research）. We have a whole bunch of skunkworks（秘密小组） ——— Jensen Huang, No Priors, 2023*

#### T5T  邮件的 「Reply All」也是信号增强器

> *当时邮件里（指2013年）会看到老黄对 CUDA 的评价是「Incredible」，你看到老黄说一个事情「Incredible」就知道这是他很看重的了。当时销售会发 T5T 说客户对 CUDA 不感兴趣，老黄会在下面告诉你，你应该怎么样跟客户聊，他甚至会跟你讲一些话术，然后会讲一下他体验，包括或或者他希望跟那个销售去setup一个会议。我对 CUDA 的重要性的认知，比较直观的原因是老黄的邮件回复数量，老黄那个时候对 CUDA 的邮件可能几乎每个都回复的，可能那个时候人也比较少（注：2013年英伟达大约三千人，中国区~200-300人），后面我很快就感受到了，原来 CUDA 是最重要的 ——  Nvidia 架构师，2013年入职，ex-Intel *

> *他会在学术会议给客户宣传CUDA，因为其实客户用不了cuda。因为当时买这个东西主要做了一些图形工作栈，但老黄邮件里都明确要求销售和公司售前技术人员的去给客户介绍CUDA，因为那时 T5T 基本上都在讨论CUDA —— Nvidia BDM，ex- 微软*

> *我后来离职印象很深，当时一直 CUDA 推不出去，GPU 也卖不好，后来 Intel 也开始做GPU了，我就去英特尔了，那段时间走的人很多 ——  Nvidia 架构师，2013年入职，ex-Intel *

- 和英伟达的员工聊，每个人都能讲出来老黄「Reply All」的 case，并对这些「Reply All」自己的解读

> *老黄大部分时间都在回复基层的 T5T，这让我们感觉到，他确实在看，并且知道我们在干什么，老黄偶尔会回复 Top-level 的 T5T，有时候在整合资源，比如他看到 simulation 团队或大模型团队在做的新东西，觉得自动驾驶这边能用上，他就会在 T5T 里直接跟吴新宙（自动驾驶负责人，ex-小鹏）说：「你跟那个部门的人联系一下，我要看到一个产品」因为他都会「Reply All」VP 们发的 T5T，所以指令会清晰传达给所有人——Nvidia Autonomous Driving Engineer，2017年入职*

> *中国区今年还有一个好的 case 是我们做了一个 developer 的分析，老黄回复了 excellence，分析是针对中国的开发者，尤其是不同画像的开发者，比如是大型企业的开发者还是独立开发者，还是初创企业的开发者。他对于我们哪些 coupon 的使用率是最高的？出了一个 analysis，抄了老黄之后，老黄很感兴趣，还CC 了好几个 e-staff，从这里面我们看到老黄对 developer community 是很看重的 —— Nvidia Inception*

> *我支持字节比较早，字节还没有那么 CUDA-ready，很多团队不会上手去调 CUDA，后面我们给自己做了一些 Design Workshop，每两周办一次，一个系列有 10 个 workshop，都是针对非常具体的 wokrload 需求，比如推荐里常见的怎么看 profiling，怎么实现常见召回算法，所以当时我写了一个 training 的 summary, 老黄就跳进来就回这个邮件，Reply All，说「应该持续坚持去做」 —— Nvidia BDM ex-腾讯/字节*

> *举个例子，我们体系里有位非常重要的同事，他跟老黄很熟，老黄也很欣赏他。但他掌握的信息很多，所以每次邮件都写得特别长。老黄虽然会看他的邮件，但有一次还是找了个机会，当着所有人的面直接点名说：“Email should be short, long email means show off.” 他会用这种方式来 educate 其他人 —— Nvidia Sales Director *

> *T5T 这个汇报机制之所以有效，是因为我们知道老黄真的会看。之前有位北京的同事，大概有六个月没有更新他的 T5T，然后突然被老黄翻了出来。老黄在他六个月前的那封邮件上「Reply All」问：“为什么你没有更新你的 T5T？” 你永远不知道他什么时候在看邮件。可能他当时对你提到的某个点感兴趣，六个月后又想起来了，搜了邮件，想了解一下进展，结果发现没有后续。所以你发的邮件，根本不知道他什么时候会看  —— Nvidia Inception*

> *他会知道我们每一个项目的负责人，我们叫 PIC，然后直接在邮件里把他们@进来。这样一来，事情马上就有了明确的责任人。老黄对硬件组里的核心角色非常了解，能和几十个人都很熟，其中有些人的级别可能只有L-3（甚至更低。他会直接@人，而且经常是跳级@。比如之前有个项目，他会直接@到最一线负责这个项目的工程师 —— Nvidia Business Develop Manager*

> *去年 Automotive 邮件组里有一个比较 sharp 的回复，有个人去参加了汽车行业跟奔驰的会，奔驰反馈英伟达合作一个全站的一个技术方案，奔驰觉得英伟达定的系统参数不太可以实现的，说我们做的是「garbage」，经销商的销售把这个邮件截屏放到了 T5T，被老黄看到了，老黄把 Auto 部门的 leader 加进来，问这个是不是真的需要？怎么解决这些问题？怎么样去向奔驰去改善跟奔驰的交互体验？在 Automotive 邮件组里面的「Reply All」 —— Nvidia Autonomous Driving Engineer，2017年入职*

> *（Nvidia 新员工入职培训中，关于「如何写好T5T」 的培训材料如下：*
> **Top 5 in Jensen’s words：**
> *"T5T is one of the most important things I read. It is our company’s 'global neural network' "*
> *"It lets us monitor for alignment, and detect environment changes that requires us to pivot quickly"*
> *"It is meant to be lightweight – more frequent from more people, is better than exhaustive reports from just a few"*
> *"Each function and group can have your own style. But keep it light"*
> *"T5T helps us stay alert, stay aligned, and stay agile. Write it. I read it"*
> *"Let’s get the simple things right, so that we can focus on the important things"*
> *"It shouldn’t take but 5 to 10 minutes to write since it is your Top 5 Things"**
> 
> ***Some features of a good T5T:**
> *Plain spoken.*
> *Top priorities that you are actively working on. Top 5 Things is your “priority list”, and not “To-do list”.*
> *Threats and opportunities that you would like to bring attention. (though the people directly affected should not be reading this for the first time on T5T).*
> *Insights that you would like to share.*
> *What worked and didn’t.*
> *Changes in strategy, direction, approach, plan.*
> EIOFS（Early Indicator of Future Success）– just the most important one
> **Purpose：**
> *Status executives on your work, share key insight about your business, and provide your future focus & priorities.*
> *This report provides early warning signals to opportunities and issues and helps us determine if we are all aligned.*
> *Frequency：Bi-weekly, preferably Sunday night *
> **Length：**
> *Keep reports to ½-1 page, sharing only the most relevant and important items; empty sections are okay*
> **Content：**
> *Please write clearly & succinctly using “list of actions” or “newspaper-style headlines” approach—a “list of nouns” is not helpful*
> *Don’t just cut-and-paste from prior report unless it communicates what you are doing, or you feel it’s important to reiterate, in which case you should highlight your new updates/changes in blue*
> *No date is needed in the subject line. Date is provided automatically by outlook.*
> **举例：2025年6月17日某T5T邮件示意**
> ![](https://xhs-doc.xhscdn.com/1040025031itfliktgs03dgclk8?imageView2/2/w/1600)

### One Architecture

#### 十年如一日的 One Architecture

- 十年前英伟达就保持现在的组织架构不变， 即「One Architucture」， **GPU 研发**和** CUDA 研发**是组织最核心的「One」 ，英伟达有20个一级部门，但**近70%的员工都集中在研发部门（GPU 硬件研发 & 软件 CUDA 研发）**：
- Hardware 研发（GPU设计）和 Software 研发（著名的CUDA），研发部门做了**大而全的产品叫 101**，每个产品线（Auto、Gaming、Robotics等）可以根据需求来**切蛋糕**，这使得英伟达的所有产品都是「One Architecture」；对比英特尔，PC芯片、手机芯片在不同的事业部，重复造轮子现象很多

> *英伟达harcware和software的研发部门，他们是做了一个大而全的产品，它的代号叫101，数据中心去用这个最大的GPU -—— Nvidia GPU 架构师，ex英特尔*

> *产品部门按照自己的需求去切出来一块自己需要的尺寸，比如说做车载的，做机器人，会去做阉割，就是产品不需要那么强的GPU，贵、功耗高，所有的产品部门会根据这个大而全产品去阉割 —— Nvidia GPU 架构师，2013年入职*

> *英特尔有各种不同的事业部，比如 CCG（客户端计算事业部）是做笔记本电脑的，DCG（数据中心事业部）是做data center的，每个事业部都是一个小公司，自己研发芯片和软件，分散式的研发会造成很多浪费，比如芯片启动需要一个软件叫 boot loader，英特尔每个部门里面都会有一个做 boot loader 的，在英伟达只有一个软件部门，只有一个 boot load team -—— Nvidia GPU 架构师，ex英特尔，2013年入职*

> *苹果那边比如要做AI，我朋友在battery group说要做这个AI的，IOS的也要做，iPhone组的也要做，都怕做了被别人抢了功劳;  英伟达从来没这个问题，我们叫「One Team」*

> *几个硬件和软件部门 ，十几年都没有变过，组织变化主要来自于业务新的发展，比如说新增的汽车团队  —— Nvidia GPU 架构师，2013年入职*

- 围绕 GPU 建护城河，反面案例是 Intel 对 GPU 的摇摆

> *Intel 的新项目就是两年生命周期，R&D cycle 一年，business cycle一年，两年以后基本就没有信心了。比如当时 Intel 是 投了 20 亿美金来做手机和平板的芯片，大概到两年后，从第三年开始就开始逐渐萎缩了。跟老黄这种一言九鼎顶住压力长期做一个事的风格完全不同*

> *因为英特尔尝试过好几次做GPU，但是战略上都不坚定，这次把我招过来，也是明确了要下定决心做GPU这件事情。但是之前英特尔的老板、CEO并不是一个很靠谱的人，导致公司有很多山头文化，政治氛围很差，而且大家的积极性都并不是很高，整体文化就非常的僵硬  ——  现 Intel GPU Senior Product Director，ex-英伟达*

- 再往前考古，2013年Jensen把CUDA从「Hardware」部门调整到「Software」，意味着从「GPU硬件指导软件」变成**「软件驱动GPU硬件」，生成式AI时代软件比硬件重要，**原因是2012年GPU+CUDA 在 ImageNet 上比 CPU 快了 10x 以上

![](https://xhs-doc.xhscdn.com/1040025031je2o3p32006pp4hn8?imageView2/2/w/1600)

> *在 2012 年的 ImageNet 图像识别比赛中，有一个网络叫 AlexNet，它使用 CUDA + GPU 训练。这是首次在大型神经网络训练中成功应用英伟达的 GPU，并大幅提升训练速度，是当时比 CPU 快 10x 以上，是一个比较重要的拐点  —— Nvidia GPU 架构师，2013年入职*

- **软件定义需求，驱动硬件设计；**而不是反过来

> *AlexNet虽然效率和性能远远高于CPU，但还是没有把GPU性能充分调度起来，因为当时CUDA的工具链依然在出始阶段，因为过去CUDA的工具链，都是在GPU硬件部门做的，GPU先设计好，然后CUDA去适配GPU，通过AlexNet，老黄觉得需要让外部生态里的需求影响CUDA，更强大的CUDA工具链出来之后再影响GPU*

> *挖矿也是，最开始是靠暴力出奇迹，因为CPU最多几十个核，而GPU有有上万个核。但当时CUDA的工具链不是适合挖矿，因为GPU适合做同一个步骤内有大量的并行计算，区块链顾名思义还是链条一样的计算方式，需要增大更多的缓存，所以当时也是为了这种新的计算特征，先做了CUDA工具链的支持，后面再调了GPU内部的架构，内存、线程调度这些*

> *英伟达会先用CUDA工具链（如cuDNN、TensorRT）去适配LLM的结构，因为CUDA如果都不能适应模型的结构，就很难高效的跑在GPU上，现在是软件团队跟客户沟通的非常紧密，软件团队吃透以后，再去驱动下一代的GPU硬件结构，比如Blackwell对比H800在通信架构上有优化*

> *CUDA里的人主要是做Cuda Kernel的，因为很重要，后面比特币和区块链时期发现有很多并行计算不是能靠渲染就做完的，能做但是效率不高，，所以催生了编译器的需求，需要用编译器的方式配置CUDA内核和工具链，让他按照客户的需求去灵活地工作*

#### 人才有 Versatile Skill Set  特点

- 由于 One Architecture，公司人才的技能通用性（英伟达员工的说法是要有 Versatile Skill Set）很强，导致人才的「即插即用」现象很普遍，Re-org 到其他 Mission 是常态，因为方向调整而裁员的必要性也大大下降

> - *英伟达虽然现在人很多了，但大部分的人都在做 GPU，不管是你做数据中心自动驾驶，依赖的都是 GPU，不同 product 上也没有太多的差别，比如数据中心 A100 的安培架构和做自动驾驶 Orin 芯片的 GPU 架构是一样的，所以人是可以流动的，这就是老黄一直强调的 One Architecture 的好处*
> - *GPU硬件不管是在数据中心上，还是在嵌入式端侧上，GPU的参数、特性，都是一样的，只是说最上层针对不同的应用领域，它会有不同的CUDA的模版和模型，但万变不离其宗，就像你会用手机你就会玩平板，差别很小*
> - *Intel 每个部门的产品都不一样，电脑是酷睿芯片，手机灵动芯片，芯片的硬件架构和上面跑的软件都完全不一样，上层的工具也不一样。以前我在英特尔转岗要学很久，在英伟达这边基本上不用学*
> *-—— Nvidia GPU 架构师，ex英特尔，2013年入职*

> *这个从七八年前跟现在应该也没都没什么变化，我印象 NV 一直是有很多 Virtual Teams，有的时候 Top 5 Things (T5T) 的范围都是由这些虚拟团队来定义的   —— Nvidia Autonomous Driving Engineer，2017年入职*

> *堆栈放的是临时数据，就是说为了完成一个任务，GPU线程里的数据都会临时放到堆栈里，英伟达的组织可以很短期把相应的这些这条线上硬件、软件、产品、营销部门都串起来，开始做一些 special mission。之前有一个 GPU 叫 H100，后面是 H200 的产品，因为计划表上没有 H200，H100 出完了就准备卖 B 系列 Blackwell，但当时英伟达的 H100 出来半年后，AMD出了一款 Mix 300 ，对英伟达产生了很大的威胁。因为生成式 AI 计算的很依赖 HBM 的带宽和容量，H100 的 HBM 用的是80GB，AMD 出的这个产品就变成了 90GB 的 HBM3E（E 就Enhanced 提高版），容量和带宽都比英伟达这个产品高。当时微软就一下子就把很多订单给到了AMD，而且AMD这个质量，这个参数特别好。老黄一下子着急了，当场就拍板要去做一个H200的产品，其他完全一样。只是内存从 H100 的 80G 变成 96GB 的HBM3E，96GB是当时能放的最大的容量了。这个新的临时的Mission 一出来，马上组成了一个临时的研发和生产计划，大概两三个月 H200 就出来发给客户了 —— Nvidia GPU 架构师，ex英特尔*

> *NV 要保持在前沿技术上的的领先地位，就得保持交叉的组织能力，因为新的技术在旧组织里找不到位置，我现在做的是大模型推理框架这件事情，今年年初 Deepseek R1 火了之后，强化学习这个概念还能火起来，之前没有团队专门做强化学习，也有之前团队做的事和强化有点关联，这个时候你就会需要去不同的团队去合作  —— Nvidia 架构师，ex-商汤*

> *每一个 Component Team 可以去做一个 Mission，也可能被调到另外的 Mission 上， 我现在就在一个 Virtual Team 上。之前开发过一个“Shield”的安卓的游戏机顶盒的团队，后来整个团队（包含许多安卓开发者）被调往自动驾驶部门，也没裁员，这种例子特别多  —— Nvidia Autonomous Driving Engineer，2017年入职*

> *不裁员，但会fire人。他在 all-hands 说他不会永远不裁员，说那个如果哪天真的明天活不下去了，也会去 layoff 一些人，但是现在不会去，现在的这些科技公司那样去做这些事 —— Nvidia Jetson Engineer, ex-Apple, 10年司龄 *

- 人均技术实力强，Senior Director 会写代码，销售可以当 0.5 个售前支持用，售前支持可以当 0.5 个研发用，人员干练且精简

> *我之前在英特尔跟客户聊技术，老板也不懂技术，会让工程师和客户去聊，售前支持解决不了的会让研发去解决。但是在英伟达都是总监或者甚至高级总监直接去跟客户聊技术，已经是有一定难度的技术交流，都可以搞得定的，很懂技术，AMD 在英伟达和 Intel 中间的水平。因为老黄也会追着你问技术细节，邮件里我们都看得到，所以我觉得氛围上是大家都在苦练基本功  *

> *我第一次来英伟达以后，第一次听会就比较 shocked，没想到会聊到这些 topic， 比如 workflow 怎么去优化，优化过程会涉及到说怎么平衡存储的占用和通信的占用，瞬间让我觉得回到了读书的时代。比如说我之前在微软只需要聊到 10 分的技术，剩下  90 分给售前支持去聊，但在 NV 少要聊到 50 分，售前支持只需要 cover 剩下 50 分 —— Nvidia BDM ex-腾讯/字节*

> *我举两个例子英伟达对技术的要求有多高。几年前参与的一个项目，当时公司在快速发展，人员根本不够，有个关键模块出了问题，那个时段时间我干通宵都有的，就这样项目还很赶，当时一个向 VP 汇报的一个老大，级别挺高的，现在已经是 VP 了，他说：我们分一下任务，我来 take 这一段代码，我当时惊呆了你知道吗？*
> *另一个数字是，我 13 年从华为来 NV，前后推荐了 20 个人来 NV，但是只有 1 个人推荐成功了，NV 对工程师的要求比华为更高，面试很严格，面到 Senior Director 的时候都会问很细的技术细节。华为是很伟大的公司，但当时架构已经细化到很细的设计模块，校招生直接打开文档写代码就可以了，人不需要很聪明 —— Nvidia GPU 架构师，2013年入职*

#### 恐惧是创新的敌人，弱化短期评价

- 几乎不裁员

> *比如说阿里巴巴有20多万人，微软的话也是20多万人，AWS 也是20多万人，对你只有1/7的人的情况下，你所有的事情真的都得一起干，在英伟达没有人觉得自己会被裁，大家都在踏实干活 —— Nvidia Inception*

> *不裁员，但会 fire 人，做的不好会被裁员。他倒没有裁过员，他说他也不会永远不裁员，2 月份老黄来上海，说如果哪一天真的活不下去了也会去 layoff ，但现在不会像科技公司那样裁员。他对短期绩效的看法是，如果过于看重短期的业绩，他觉得他自己也早就被 fired 了，比如他当时认为 CUDA 是正确的，但他坚持 CUDA 的那几年，公司的股价和利润都下跌，投资人很不看好。那如果他们只看一年两年的表现，他就那个时候被 fired 了，他过往很多年的表现都是硅谷 last five percent 的 CEO  —— Nvidia Inception *

> *CUDA带来的最大的隐性成本，可能是分散了Jensen对核心GPU客户服务的关注，2006年底，游戏玩家抱怨笔记本电脑中的GPU在使用数周后会停止工作，英伟达股价再次暴跌，6年内第二次损失了近90%的市值，但他也表现出极高的宽容度，即使是最大的失误，因为 Jensen 非常在意对人们的冒险意愿和创新精神产生哪怕轻微的抑制效果，他会责骂你，会冲你大吼，但他不会解雇你 ——《英伟达之芯》*

- 没有 35 岁焦虑，员工体感上「老员工的退休邮件多于新员工的 on boarding 邮件」

> *因为今年2月份老黄给中国区开年度会议，他提了一些有趣的话题。有个人问 35 岁会被裁吗？他说他当时到35岁的时候差不多工作了 10 年，他觉得大部分人这个时候才真正知道怎么把工作做好，所以我体感上这边看到比 welcome 新员工更多的邮件就是退休的 farewell，非常多人在英伟达退休，Maggie Liu（中国 Enterprise Marketing 负责人） 60 岁了，老黄 62 岁了；中国区整体去年 0.2% 离职率（注：按中国区4000人算，每年只有8人离职）  —— Nvidia Inception *

> *英伟达是十三薪，年薪制，没有年终奖，老黄在 all-hands 说我们所有人努力工作，我们的股价涨好，我对大家的股份也很 generous，所以我们我也不搞太虚的。之前我在阿里经历过大大小小的奖，这边就完全没有，有个员工在 GTC 之后问老黄，大会做得好会有奖励吗？老黄念完这个问题后，说：「what are you guys, kids？要不要我给你们一些 stickers 让你们贴上？」 —— Nvidia Inception *

![](https://xhs-doc.xhscdn.com/1040025031itv1i0c0s09aoht94?imageView2/2/w/1600)

*                                        （图：All-hands的场地是 Nvidia 总部 Voyager 里面的这块屏幕下的空地）*

- 绩效评价不看 numbers

> *英伟达一年一次绩效评价，没有半年评价，有季度 QBR 但就是内部开个会。因为这里不太关注短期的收益，你自己也不会那么那么焦虑，就是踏踏实实做  —— Nvidia Inception *

> *英伟达是个不太看数字的公司，我们不太看 numbers，所以为数不多老黄问 numbers 的地方，我们可能就知道这相对更重要，比如 developers 的数量，老黄会问很多次，比如他会问 GTC 有多少 developers 参加？ —— Nvidia BDM ex-腾讯/字节*

> *Meta 的话就是多劳多得，Google 感觉需要更多 non-technical 的投入，要做出来一个新东西，但英伟达都不是。不能简单地按“交付成果”来衡量，比如无人车这些新业务则都在投入期，在美国英伟达发的也是年薪，不是按月薪加固定月数奖金的模式 ，如果你是优秀员工Top Contributor 会直接给你涨年包 —— Nvidia Autonomous Driving Engineer*

> *我23年的时候中间去了一家国产创业芯片公司 1 年，这家公司的老板和高层基本上是走的国内的互联网公司的一个管理风格，所以和在国内那段时间和国内互联网的管理差不多，就一个季度打一次绩效，然后会有OKR，然后OKR会从部门总一直摊到我是团队leader，然后摊到我这一层，我再摊到我下属的同学。每个人都有自己的一个季度的OKR，然后每个季度都要根据这个季度的OKR的完成情况去给他打这个季度的绩效。然后每个季度的绩效还有10%的比例，一定要打出那个差绩效。我挺不适应的又回 NV 了，英伟达没有个人OKR，只有一个团队层面的OKR，主要指导你的工作方向，不为了绩效  ——  Nvidia 架构师，ex-商汤*

- 绩效评价里， Top Contributor 激励充分，有 30%+的年薪包涨幅，且**能通过邮件再给部门推荐一个 TC**

> *在英伟达最好的绩效是 Top Contributor 占比 20%，中间 75% 的人都是FC（Fully Contributor，相当于 3.5/3.5+），可能95%甚至98%的人都是有不差的绩效，只有 2-5% 的人是 RI ( Require Improvement，相当于3.5-)  ——  Nvidia 架构师，ex-国产芯片公司*

> *我之前是TCA（注：指Top Performer），因为绩效好，我的老板会来找我，让我再推荐一个我心里的优秀员工，前几年我推荐的一个人，和我不是一个部门，是跨部门推荐，他当年的绩效应该也是不错，公司肯定是希望他的考评是更公正的，我理解公司希望听优秀员工的意见 —— Nvidia GPU 架构师，2013年入职*

![](https://xhs-doc.xhscdn.com/1040025031ise7gjogs0116bhj0?imageView2/2/w/1600)

*                                                                               （图：Nvidia 绩效人数分布）*

### 成功决策：CUDA 的生态壁垒

#### 卖计算方式还是卖 GPU

- GPU 是一锤子买卖，越来越接近 Commodity；英伟达希望客户把「计算方式」跟英伟达绑定，计算方式和 GPU 中间差的东西就是 CUDA

> *老黄从来不说我们是 GPU 公司，永远都在说我们是计算公司，最近说的是「加速计算」公司，中间的差别就是 CUDA。比如自动驾驶，最近支持他们，以英伟达之前的业务模式就是卖芯片给客户去做自动驾驶控制器，比如国内的地平线，但英伟达在国外跟奔驰、捷豹、路虎、沃尔沃，做的不光是芯片，也提供自动驾驶的算法和传感器的软件，做软硬件绑定。软件是个长期的东西，传感器要升级，升级了软件就要跟着变，老黄算过新的模式下，跟奔驰的合作每年可以赚10亿美金，卖的是算法和软件的升级费；一个芯片卖 400 美金，你卖一件就结束了*

> *我的感受是 CUDA 在这二十年的发展大致分为 3 个阶段*
> - **第一阶段***（~2006-2013）***：***第一个 10 年 CUDA 是比较封闭的，因为**英伟达提供了用 CUDA 做数学计算或者并行计算的模板，你只需要写一行代码，就能实现非常复杂的计算，这也是为啥大家都觉得依赖于它了，**因为它太简单了、就特别好用*
> - **第二阶段***（~2014-2022）***：***过去几年英伟达开发了很多 CUDA 的变种，比如用 CUDA 做深度学习加速的 CuDNN（CUDA Deep Neural Network library），你可以理解为一个 library，很多人都在往这个 library 里添砖加瓦；还有就是因为神经网络有很多线性代数计算，叫 cuBLAS（CUDA Basic Linear Algebra Subprograms），后来可以做比如大气计算、天气气候模型的，但是这些依然远远不够*
> - **第三阶段是***半开放阶段（~2022至今）：因为生态爆发了，英伟达发现靠自己开发完全来不及，搞不定，所以现在可以让客户自己写CUDA算子和模版，我们有一个开源项目叫 CUTLASS（CUDA Templates for Linear Algebra Subroutines，2022年开源），就是慢慢把CUDA 要开放出来让客户可以开发自己的 CUDA 模板*

> *我们现在这三阶段的东西都有在用，越往后的使用成本是越低的，二三阶段有现成的话，也会直接用  —— Nvidia_LLM Post-Train Lead（Nvidia的某客户）*

> *我是离客户最近的岗位，我本人日常工作里面，六七成以上都是 CUDA 相关的，我之前会和字节的算法团队、工程团队沟通很多，基本都是 base 在 CUDA 上的 topic，无论他们是说去用我 CUDA 已经开源的一些 library，还是基于现有的产品，或者就是基于扩大本身去重写一些加速计算的 kernel、函数、程序，这些 topic 整体都是也在 CUDA 之上 —— Nvidia BDM ex-腾讯/字节*

#### “苹果是一家软件公司，英伟达也一样”

> *Jobs 说苹果是一家软件公司，我觉得英伟达也一样，今天客户用英伟达的卡大部分可能是因为 CUDA  —— Nvidia BDM ex-腾讯/字节*

> *It's because these really great Japanese consumer electronics companies who kinda own the portable music market for a long, long invented it and owned it. But the they couldn't do the appropriate software. Couldn't conceive of and implement the appropriate software. Because an iPod is really just software, software in the iPod itself, it's software on the PC or the Mac and software in the cloud for the store. And it's in a beautiful box but it's software. If you look at what a Mac is, it's OS X, right? It's in a beautiful box, but it's OS X. And if you look at what an iPhone will hopefully be, it's software. And so the big secret about Apple, of course, not so big secret maybe, is that Apple views itself as a software company —— Steve Jobs, 「Apple is Software」*

> *AMD 也有个类似 CUDA 的平台叫 ROCm，但和我们依然有差距，支持的颗粒度更粗，因为底层的算子和 library 更少，也没有 CUDA流畅，目前是没有办法媲美的 —— Nvidia GPU 架构师，2013年入职*

#### Developers, Developers, Developers

> *之前谷歌 CEO Eric 说得挺对的，CUDA就像 GPU 的 C++ 语言，外加一个软件生态，20年的语言学会了基本就是母语了，对于developers来说，还是要费挺大精力再学一门外语的 —— Nvidia GPU 架构师，2013年入职*

> *市场上已经培养了大批用CUDA的人，但任何一个国产GPU或者AMD，开发芯片的专业人才是更少的，在这种情况下，作为企业你要用这个芯片，你要招到这个专业人才是极其困难的 —— Nvidia_LLM Post-Train Lead（Nvidia的某客户）*

> *英伟达是个不太看数字的公司，我们不太看 numbers，所以为数不多老黄问 numbers 的地方，我们可能就知道这相对更重要，比如 developers 的数量，老黄会问很多次，比如他会问 GTC 有多少 developers 参加？ —— Nvidia BDM ex-腾讯/字节*

> *CUDA 除了现有的模板算子，另一些在重点做的是 developer 社区掌握这个 skill set 的人员，我感知上也很关注的维度是developer的数量，公司内部的会议，他会无数次提到 developer developer developer；NV 的数字导向的东西不是特别多，但能看到对于参与的 developer 的数量，其实是每次都会被 track 的数字 ——Nvidia Jetson Engineer, ex-Apple, 10年司龄*

> *中国区今年还有一个好的 case 是我们做了一个 developer 的分析，老黄回复了 excellence，分析是针对中国的开发者，尤其是不同画像的开发者，比如是大型企业的开发者还是独立开发者，还是初创企业的开发者。他对于我们哪些 coupon 的使用率是最高的？出了一个 analysis，抄了老黄之后，老黄很感兴趣，还CC 了好几个 e-staff，从这里面我们看到老黄对 developer community 是很看重的 —— Nvidia Inception*

#### 案例1：阿里的平头哥全面拥抱CUDA，但依然只是追随者

> *平头哥（注：指阿里的全资半导体芯片业务主体）战略上其实算是有思考的：*
> - *一是平头哥从一开始就全面接入CUDA生态，他们有自己的API接口，跟CUDA不一样，但会额外在上面封一层和CUDA一样的API。**我问他们，你们自己封口有没有任何一个落地成功的？他说，完全没有，全都是CUDA平台落地的案例**；二是阿里的千问模型效果很好，在很多中国的2B场景占据了大部分的市场份额，通义和平头哥跑起来更便宜更快 *
> - *听起来可以跨越CUDA的壁垒，但其实不是的：因为这意味着完全被限制、完全在follow。CUDA的API和NV的硬件是相关的，你用他的API就意味着全部的硬件设计要跟着NV的方案妥协，那就是纯在追十几年的时间差距了，这样原本一些NV硬件设计不合理的地方，要优化可能会受限，做不出特色和成本优势，纯跟随战略很难打*
> - *而且平头哥的芯片依然有问题，芯片稳定没有那么容易，定制几个模型稳定跑简单，但是灵活支持算法改动模型都能天然跑得对跑得快是挺有挑战的，PPU现在重点做推理场景且绑定Qwen模型，但训练场景的挑战依然很大，要比推理大，NV在这一块沉淀很多年，硬件的计算稳定性、正确性和对各场景适配的灵活度是要高于这些新的芯片的*
> - *—— Nvidia_LLM Post-Train Lead（Nvidia的某客户）*

#### 案例2：华为退卡

- 某NV客户在贸易战背景下买了华为数张千卡，因为不兼容CUDA，团队招了写华为NPU语言的工程师，最后依然选择退卡

> *华为和AI相关的加速计算生态叫NPU（Neural Processing Unit），去年贸易战的时候，公司比较着急，跟华为签了一个战略合作协议，买了几千张卡：*
> - *我们为了战略合作，团队专门招了5个专门做NPU的同学，**现在已经全部离职了，华为的卡也全部退回去了*
> - *华为跟我们联合跑通了业务的一个模型，假设叫1.0版本，跑通了，但算法它会持续迭代的，比如一个月之后模型变成了2.0版，发现就不能跑了，这时怎么办呢？就需要去找华为再支持迭代，这中间的周期，我们公司是完全**不可接受的。最**后业务的算法工程师全放弃了。有NV卡的情况下绝对不用华为卡，全退了。我们infra招的人也劝退了*
> - *（2.0版完全不能跑的原因是什么？）芯片技术不是攻坚战，需要慢慢成熟，需要时间，需要真正稳定和适配各种灵活的场景和开发，要非常多踩非常多的坑。在人力都有限的情况下，企业基本没有时间、耐心和人力去打磨国产卡在内部的适配性和成熟度。**华为现在就是这个点搞不动，每出个新的模型，适配一个月，黄花菜都凉了，NV卡直接开箱即用，正确性和性能都没问题*
> * —— Nvidia_LLM Post-Train Lead（Nvidia的某客户）*

关于「芯片成熟」这一点，今年两月和 AWS 投资 Anthropic 的 deal team 聊到，AWS 投资 Anthropic 也有类似的动机：

> *Amazon 的 AWS 的 corp dev 团队投资了 Anthropic，最主要的合作方向是 Amazon 有自己的 Trainium 和 Inferentia 芯片，但是做的不好，有很多需要 improve 的地方，由于Anthropic的 infra 工程师很强，能提出非常solid的、非常好的修改和提升建议，能帮自研chips提升。另外两个目的是：1）Alexa 的语音模型除了用 Amazon 自己的 Nova 模型，还用 Anthropic 的模型；2）可以部署在AWS的模型托管平台BedRock上 —— AWS Cop Dev  Deal Team（Anthropic deal team），ex-Microsoft （OpenAI deal team）*

> *Anthropic 有一个 20 人的团队专门服务 AWS，给 Amazon 的 chip （叫Trainien）提意见，帮他们修改  —— ex-AWS pre-train researcher*

> *字节一开始买了一些华为的卡，字节的基数太大（~百万张卡），只买5%也是非常多的卡了，各种找业务方用，业务方一开始都不愿意用，后面先LLM的推理去用，因为推理场景通用性更强一点；后面永辉来了以后，说不行，因为字节已经落后了，无论是训练还是reasoning，都要加NV的卡，所以一度把华为的卡重新给了搜广推，但在搜广推也是难用的，就发生了我跟你说的，把华为的卡退掉，换成寒武纪的卡，因为据说寒武纪的卡在搜广推比华为的卡好。后面我交接了，不知道寒武纪的卡用的如何了 —— Nvidia BDM，ex- 微软*

### 加速计算、自动驾驶、智能座舱业务上的白热化

- 加速计算白热化

> - *五年前，英伟达领先 AMD 大概有两代，后来生成式 AI 出来的时候，和 AMD 大概有一代的代差，但现在大概只有半代了，所以也出现了比如要临时加 A200 的卡的情况*
> - *就像以前 Intel 的生产工艺也领先台积电两三代，但现在英特尔完全落后台积电的，完全创新的速度一定比追赶者的速度慢，LLM也是一样的，OpenAI 22年的领先优势一定比现在大*
> - *好在英伟达现在现金流比较充裕，可以提前买断台积电的更好的工艺*
> *——  Nvidia 架构师，2013年入职，ex-Intel *

- 自动驾驶

> - *自驾的算法层面已经进入尾声，自驾是 safety critical 的业务，需要 100% 的准确性，99.99%都不行，华为和特斯拉已经进入需要持续做功 corner case 的阶段，华为 3000 个人都在做 corner case，比如大卡车上装了很多 stop sign 的车牌，算法识别不出来，这种 corner case，但基本技术层面其实已经人心惶惶、大浪淘沙、进入尾声*
> - *好多自驾这边的工程师在 NV 股价上来之前离职，因为 engineer 的 mindset 觉得 NV 做的东西太垃圾了，坐了特斯拉觉得自己做的是 shit mountain，堆代码,  代码太差了*
> - *老黄的判断是 NV 还有机会的唯一原因是特斯拉的技术是 inhouse 的，无法卖给所有人，没法作为 supplier。 NV 还有机会从成本角度打败主机厂，可以做一套 solution 卖给所有传统汽车公司，奔驰宝马，摊薄成本是单主机厂的 1/10 甚至 1/20*
> - *但吴新宙和 NV 的文化冲突很大，micro-manage 很严重，团队有很大的不稳定性*
> *——Nvidia Autonomous Driving Engineer，2017年入职*

> *Robotics、Commerce Driving、Omniverse 元宇宙等这种新的垂直领域，比起 GPU 生态系统从硬件到软件直接垂直的这么一个搭，其实没有特别多的优势，相当于跑 100 米，其他玩家已经比你提前 30 米了，NV 其实没有太多优势，所以这几个部门是很艰苦的*

- 智能座舱

> - *汽车产品现在主要分两大块，智能座舱和自动驾驶，以前的汽车座舱里都是带指针的、机械式的仪表系统，以前比较土，现在都是液晶触摸大屏，目前主要是高通在做*
> - *老黄就一直不愿意去做智能座舱，他觉得毛利低，不是 GPU 擅长的场景，不需要那么多的并行计算，还是比较传统的显示加影音的场景。真正需要大量并行计算的才是英伟达生态能发挥长处的地方，比如几百亿参数并行计算的大模型*
> *——  Nvidia 架构师，2013年入职，ex-Intel *

### 员工体感：文化的变与不变

#### 火车越快，你越停不下来

- 更多优秀的年轻人加入后，公司的节奏越来越快，越来越“卷”，火车跑的越快，你越停不下来

> *Nvidia前些年其实，并不是硅谷非常受欢迎的公司，在前些年，甚至很多人都不愿意去。然后，一线里面有很多比较元老的人比较躺平，所以很多中层也推不动他们，就导致整个公司反而是中层和最上层老黄是最累的。一线的话，反而是可以比较轻松的，跟着公司执行就行，这两年 NV 火起来之后，招到了更好的人才  ——  现 Intel GPU Senior Product Director，ex-英伟达*

> *公司市值和基本面的巨大改变，也导致了大家对公司、公司对自己的期待都不一样了，人的心态也随之发生巨大变化，大家普遍觉得工作节奏和压力确实变大了。我在的 Auto 团队变化更大，吴新宙（从小鹏去 NV 的做自动驾驶的 VP）来了之后，变化巨大，他把很多国内职场的管理文化带了过来，对我冲击很大，有点“南橘北枳”的感觉。他在小鹏的很多经验是无法在这边复刻的。在国内可以强硬地管理，但这种方式在一个美国企业，是行不通的。以前更多的是 voluntary ，是对这个事情有使命感， culture 会 influence 你让你心甘情愿地去做事，但现在是不情不愿地在做。我甚至在考虑换岗位 ——Nvidia Autonomous Driving Engineer，2017年入职*

#### 机器人团队开始末尾淘汰，Jensen敏锐地发现了文化问题

- 机器人团队开始末位淘汰，同一个方向有5-10个团队在做，做一摸一样的事情，不变的依然是「Speed of Light」

> *越来越卷了，之前大家 work life balance，到点都找不到人，大家都回去接小孩去了，现在是因为名气大了、年轻人多了，大家就开始卷起来了。比如机器人组现在已经开始末尾淘汰了 ---- Nvidia Jetson Engineer, ex-Apple, 10年司龄*

> *我们的自由度很高，比如我们在选中国的机器人供应商，很多可以选，Jim Fan 经常说，先做了再说，选来差不多的试一试，公司也不会管的很细，给你很大的自由度去试，所以我就来中国谈供应商了 ——  Nvidia NV Research Solution Architect，ex- GEAR Lab*

- 但老黄发现了文化的问题，在 all-hands 上表态敲打

> *Jensen 太聪明了，他对文化的变化很敏锐，他在 all-hands 上说，我们招聘你不是看中你之前的企业文化，而是看重你本身的技术背景，我希望所有新来的人，不要试图改变公司的企业文化。他太敏锐了，我们所有人都比较吃惊他会公开提出来，我们都觉得是吴新宙的自动驾驶团队  —— Nvidia GPU 架构师，2013年入职*

### 附录一：访谈名单 & 纪要

*（点击链接可以直接阅读）*

| **序号** | **Base 地点** | **员工&职位** |
| --- | --- | --- |
| 1 | 上海/北京 | [Nvidia_Chinese Cosumer Internet_ex微软_8年司龄_20250524](https://docs.xiaohongshu.com/doc/70e1104e781c3cabdfba4b067a623a8e) |
| 2 | 上海/北京 | [NVDA_China Inception ex阿里云_3年司龄_20250526](https://docs.xiaohongshu.com/doc/3a930d66d10c5722864b7f1220c14611) |
| 3 | Santa Clara | [Nvidia_Autonomous Driving Engineer_校招_7年司龄_20250528](https://docs.xiaohongshu.com/doc/d44009b4210dc712cba9ac2e85f3cb26) |
| 4 | Santa Clara | [Nvidia_Robotics Engineer_校招_7年司龄_20250213](https://docs.xiaohongshu.com/doc/dd8f74bf6b9935f0c68692d5c7f30bf1) |
| 5 | 上海/北京 | [Nvidia_BDM_ex腾讯/字节_3年司龄_20250606](https://docs.xiaohongshu.com/doc/3a796bbf001fdfa5e75fe0bdb06d63bd) |
| 6 | Santa Clara | [Nvidia Jetson Engineer_exApple_10年司龄_20250617](https://docs.xiaohongshu.com/doc/3c18acac19dc84f9b1633afe38f9912e) |
| 7 | San Francisco | [Nvidia_现 Intel GPU Product_ex英伟达_202505](https://docs.xiaohongshu.com/doc/f4fe76d028d944b7758ffb2d7afb5421) |
| 8 | Santa Clara | [Nvidia_NV Research_Solution Architect_20250619](https://docs.xiaohongshu.com/doc/deaa09937e5639f195c9efaedab478c0) |
| 9 | Santa Clara | [Nvidia_Prduct Manager_3年司龄_20250618](https://tingwu.aliyun.com/doc/transcripts/58gmq63obpe5qzwo) |
| 10 | 上海 | [Nvidia_LLM Post-Train Lead（NV客户）_ex 百度_20250625](https://docs.xiaohongshu.com/doc/24274a825b73559a814db1b43d231b60) |
| 11 | 上海 | [Nvidia_GPU 架构师_ex英特尔_10年司龄_20250610_第1次](https://docs.xiaohongshu.com/doc/f8985babac2f557707ac1d86725e69f5)<br>[Nvidia_GPU 架构师_ex英特尔_10年司龄_20250610_第2次](https://docs.xiaohongshu.com/doc/d03db6d8235d7be8e83e6bbb964e0ec3) |
| 12 | 上海 | [Nvidia_架构师_ex 国产芯片公司_3年司龄_20250604](https://docs.xiaohongshu.com/doc/555314b9c2003d77d73ba1ea3263c937) |
| 13 | 上海 | Nvidia_工程师_ex 华为_12年司龄_20250613 |
| 14 | 上海 | （信息量一般）https://tingwu.aliyun.com/doc/transcripts/zj78qpdrev6zqxdp |
| 15 | 上海 | （信息量一般）https://tingwu.aliyun.com/doc/transcripts/4l6xqapjv2eeqm2y |
| 16 | 上海 | （信息量一般）https://tingwu.aliyun.com/doc/transcripts/3kprql7mp4ky9xgd |
| 17 | / | [《英伟达之芯》读书笔记](https://docs.xiaohongshu.com/doc/53f82536c35238fd5a694181920d51c7) |
| 18 | / | [《英伟达之道》读书笔记](https://docs.xiaohongshu.com/doc/d6f29495f0190f2627747a9dfe4ea568) |
| 19 | / | [2005-2025: Nvidia Waves & Signals ](https://docs.xiaohongshu.com/doc/bfd341c7ecc341f823547980db0aac54) |

### 附录二：重要的Weak Signals

<u>PC游戏的图形GPU时代（2000年左右）</u>

> *Signal  我们在 PC 行业看到的一个现象：越来越多的青少年在个人电脑前花费了更多时间——他们在电脑前花费的时间越来越多，玩大型虚拟世界游戏也越来越多。所以我认为——PC 正在成为一个完全不同的游戏平台，而且是一个真正重要的游戏平台  ——2000 Q4 Earnings Call*
> *Action &Impact  1999年NVIDIA 首次提出“GPU”（Graphics Processing Unit）的概念，发布 GeForce 256，个人电脑（PC）的消费级显卡，它的发布标志着现代GPU时代的开启*

*图形专用显卡到通用计算平台（2006年左右）*

> *Signal 2003年 John Nickoll 主动致信黄仁勋：新一代的光刻机能制造出宽度仅有100个原子的晶体管，在这样精细的尺度上，晶体管的导电性将会受到影响，导致电流泄漏到周边电路中，如果出现这样的情况，计算机的运行速度将会下降；因此 John Nickoll 预言摩尔定律即将失效 ——  《英伟达之芯》*
> *Action &Impact  John Nickolls 希望可以找到绕开摩尔定律的方法，这个方法就是并行计算，它并非通过提高速度，而是通过让更多的晶体管能够同时响应，与英特尔的CPU每次只能激活少量晶体管不同，英伟达的游戏GPU可以一次激活数千个晶体管。于此同时，需要找到那些真正需要GPU强大性能的需求和场景。在 Jensen 的邀请下，于 2003 年加入英伟达，主导将 GPU 从图形专用硬件转变为通用并行计算平台，开始构想设计 CUDA 核心阵列 ，CUDA的第一款产品在2006年正式上线*

<u>AI芯片（2012年-至今）</u>

> *Signal IIya 和 Alex 在 Hinton 的指导下开发的 AlexNet 算法在李飞飞的 ImageNet 数据集上取得了突破，准确率较上一代算法提升了 10%；算法本身和 LeCun 的 LeNet 没有本质的区别，都是基于卷积神经网络，核心在于 AlexNet 的算法要庞大的多：与LeNet相比，AlexNet可以处理大约10倍规模的图像，通过一个大小约为其两倍的卷积核（可以理解为神经网络的“焦点”）来扫描图像。在此基础上，AlexNet通过一个更深的网络对识别的细节进行过滤，这个网络比LeNet多出几层，因此能够更全面地处理所获得的信息，并做出更复杂的推断。这种「庞大」背后的支撑是英伟达的硬件，GPU训练神经网络的速度比CPU快数百倍；继杨立昆的LeNet之后，AlexNet实现了计算机视觉领域的新跨越；后面谷歌收购了 Hinton 团队，当提出让 Alex 使用其庞大的CPU集群时，Alex 拒绝了，反而选择购买了一台普通的电脑和几张零售的英伟达 GPU ——  《英伟达之芯》、《李飞飞自传》*
> *Action &Impact 卡坦扎罗感受到了这个变化，决定越过层级，直接向黄仁勋陈述自己的观点，黄仁勋对他的理念产生了浓厚的兴趣。在二人的首次会面之后，黄仁勋甚至推掉了所有安排，整整一个周末都埋头钻研人工智能这一他之前几乎未曾涉猎的领域，而在随后的会面中，他将卡坦扎罗召至自己用来办公的会议室，黄仁勋断定，神经网络将彻底变革社会，而英伟达可以通过CUDA占据必要的硬件市场。他宣告，自己将举公司之力投入这个项目的发展。“他在周五晚间发了封电子邮件，说我们将全面转向深度学习，不再只是一家图形芯片公司，”英伟达副总裁格雷格·埃斯特斯(Greg Estes)讲述道，“到了周一早上，我们已经转型为一家AI芯片公司。2014年初，cuDNN即将面世。在2014年的GTC大会上，黄仁勋登台推介此项成果，这是英伟达21年历程中首次公开与AI的联合 ——  《英伟达之芯》*

> *Signal  2017年7月，Attention Is All You Need 发表在《神经信息处理系统》(Neural Information Processing Systems)期刊上，Transformer 机制解决了之前循环神经网络的局限性：记忆短、速度慢、无法理解复杂关系的问题，被OpenAI应用到ChatGPT上，GPT-1 于2018年6月问世 ——  《英伟达之芯》*
> *Action &Impact  2022年9月 英伟达在GTC大会上宣布H100 GPU时，首次推出 Transformer Engine技术*

