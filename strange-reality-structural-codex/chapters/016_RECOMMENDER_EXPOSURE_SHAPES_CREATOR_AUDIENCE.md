# 016｜社交媒体推荐：分发机制如何同时塑造创作者和受众

**Structural theme:** exposure gate / observability bias / feedback loop / creator adaptation / preference shaping / popularity amplification / endogenous data / exploration reserve / counterfactual exposure / ecosystem co-adaptation

## 作者触发问题

我们经常把社交媒体想象成一个巨大的内容市场：

```text
CREATORS produce
↓
USERS choose
↓
GOOD CONTENT wins
```

但推荐系统加入以后，现实并不是所有内容先平等地摆在用户面前，然后用户自由选择。

在推荐驱动的平台里，平台首先决定：

> **什么内容有机会被谁看见。**

只有被展示的内容，才有机会得到点击、停留、点赞、评论、转发、关注或跳过。

这些行为随后又会成为系统下一轮判断的重要数据。

创作者看到哪些内容得到流量，也会调整自己的标题、选题、节奏、画面、长度、表达方式和更新频率。

于是，一个三方闭环出现了：

```text
PLATFORM allocates exposure
↓
AUDIENCE reacts to exposed content
↓
CREATOR adapts to visible reward
↓
NEW CONTENT DISTRIBUTION
↓
PLATFORM learns again
```

所以这一章真正的问题不是：

> 推荐算法是不是在“控制人”？

而是：

> **如果系统决定谁能被看见，而下一轮系统又用“被看见以后产生的数据”学习，那么它到底是在观察现实，还是正在参与制造自己下一轮将观察到的现实？**

---

# RAW WONDER LAYER

## 1. 没被展示，不等于被拒绝

推荐系统里有一个非常基础、却容易被忽略的问题：exposure bias。

如果用户没有点击一条内容，原因可能很多：

```text
A. 看见了，但不喜欢
B. 看见了，但当时没有时间
C. 看见了，但位置太靠后
D. 根本没有被展示
```

其中 D 和 A 在很多隐式反馈数据里并不天然等价。

所以：

```text
NO INTERACTION
!=
NEGATIVE PREFERENCE
```

这意味着平台记录到的“用户行为”并不是用户对整个世界的完整评价。

它只是：

> **用户对平台先前选择展示的那一小部分世界的反应。**

这是本章第一个关键结构。

系统不是先看到完整偏好再做推荐。

它往往是在自己制造出来的局部曝光条件中继续估计偏好。

---

## 2. 推荐结果会进入下一轮训练数据

典型推荐闭环可以写成：

```text
MODEL_t
↓ selects exposure
EXPOSURE_t
↓
USER RESPONSE_t
↓ logged
DATA_(t+1)
↓
MODEL_(t+1)
```

这里存在一个很奇怪的问题：

下一轮数据并不是完全独立于上一轮模型产生的。

上一轮模型决定了什么有机会进入数据。

所以数据开始带有政策内生性：

```text
MODEL
creates part of
ITS OWN FUTURE TRAINING DISTRIBUTION
```

这和一个摄像头单纯记录街道不同。

更像摄像头先决定谁可以进入街道，然后再根据街上的人群判断“世界上都是什么人”。

---

## 3. 曝光可以形成“富者更富”的回路

如果一条内容因为初始条件、已有粉丝、历史表现或模型估计而获得更多曝光，它就有更多机会产生互动。

更多互动又可能成为进一步获得曝光的信号。

于是可能形成：

```text
MORE EXPOSURE
↓
MORE OBSERVABLE INTERACTION
↓
MORE CONFIDENCE / POPULARITY SIGNAL
↓
MORE EXPOSURE
```

这不意味着所有推荐系统都会无限放大头部。

不同平台、目标函数、探索机制、去偏方法和内容生态会产生不同结果。

但研究已经反复表明，推荐反馈回路可能放大 popularity bias、降低整体多样性，并制造长期 exposure inequality。

因此：

> **被观察得更多，本身就可能提高未来继续被观察的概率。**

曝光不仅是奖励。

曝光也是制造下一轮信号的权力。

---

## 4. 创作者不是静态候选项，他们会学习平台

传统推荐模型很容易把“内容”想成一个固定物品集合。

但创作者不是商品货架上的罐头。

他们会观察：

- 什么标题得到更多点击；
- 什么长度得到更多完播；
- 什么情绪得到更多评论；
- 什么主题更容易进入推荐；
- 什么更新频率更容易保持曝光；
- 什么表达会被压低或放大。

然后创作者改变下一轮生产。

于是：

```text
RECOMMENDER
does not only rank CONTENT

RECOMMENDER
changes FUTURE CONTENT SUPPLY
```

这使推荐系统从“排序器”变成了一种环境选择压力。

即使平台从未公开告诉创作者“你应该这样创作”，只要曝光和收入高度相关，创作者也会通过试错反推系统偏好。

---

## 5. 用户偏好也不是固定的“真值”

推荐系统通常试图预测用户喜欢什么。

但用户偏好并不一定像血型一样固定存在、等待被测量。

用户看到什么，会影响之后熟悉什么；
熟悉什么，会影响之后愿意点什么；
连续暴露于某类内容，也可能改变兴趣、判断、记忆和后续选择。

研究者因此提出过 preference pollution 等概念：系统推荐本身可能影响之后收集到的偏好数据，使所谓“ground truth preference”不再完全独立于系统过去的选择。

所以：

```text
PREFERENCE_t
+
EXPOSURE_t
→
PREFERENCE_(t+1)
```

至少在某些条件下，这是必须考虑的结构变量。

---

## 6. 推荐并不天然等于退化

本章必须保留一个重要反例。

推荐系统可以：

- 降低信息搜索成本；
- 帮助用户发现长尾内容；
- 提高相关性；
- 连接原本难以相遇的创作者与受众；
- 让小众兴趣形成稳定社群；
- 在巨大内容空间中提供必要过滤。

甚至一些审计研究同时发现，算法反馈既可能形成有害螺旋，也可能形成有益螺旋。

所以本章不是：

```text
ALGORITHM = MANIPULATION
```

真正的问题是：

```text
SELECTION
+
FEEDBACK
+
ADAPTIVE USERS
+
ADAPTIVE CREATORS
+
RETRAINING
```

组合以后形成的长期动力学。

---

# STRUCTURAL READING

现在去掉“平台”“视频”“创作者”“用户”这些领域名词。

只留下结构：

```text
SELECTOR chooses subset of candidates
↓
ONLY SELECTED candidates generate rich feedback
↓
feedback updates SELECTOR
↓
CANDIDATES adapt to selection rule
↓
RECEIVERS adapt to repeated exposure
↓
future candidate distribution changes
↓
future receiver state changes
↓
SELECTOR observes a world partly produced by itself
```

这可以压缩成：

# Exposure-Shaped Reality

**曝光塑形现实。**

系统看见的现实，不一定只是外部世界原样输入。

系统过去决定“让什么进入可见区”，会改变下一轮现实的数据分布、参与者策略和可观察行为。

---

# HIDDEN VARIABLES

## 1. Exposure Probability

某对象进入可观察区的概率。

## 2. Observation Conditionality

一个行为数据是否只有在先被选择以后才可能产生。

## 3. Feedback Endogeneity

下一轮训练数据在多大程度上由上一轮策略制造。

## 4. Adaptation Elasticity

参与者会多快、多强地适应系统给出的奖励结构。

## 5. Preference Plasticity

接受者状态是否会被重复曝光改变。

## 6. Popularity Carryover

历史曝光优势向下一轮延续的程度。

## 7. Exploration Rate

系统是否主动给低置信度、低历史曝光对象测试机会。

## 8. Blind-Pool Size

长期没有获得足够曝光，因此无法被可靠评价的候选集合规模。

## 9. Ecosystem Diversity

优化某个局部指标以后，候选生态是否仍然保持多样性。

## 10. Policy Half-Life

当前推荐规律被参与者识别和适应以后，还能保持多久有效。

---

# STRUCTURAL PRIMITIVES

## P1 — Exposure Gate

只有通过门的对象，才能产生大部分后续行为证据。

## P2 — Conditional Observation

观测数据依赖于先前分配决策。

## P3 — Self-Generated Training Distribution

系统部分生成自己的下一轮训练分布。

## P4 — Popularity Carryover

历史曝光优势可能变成未来曝光先验。

## P5 — Creator Adaptation

被选择对象会学习选择器的偏好并改变自身。

## P6 — Receiver Plasticity

接受者会因过去暴露而改变未来响应。

## P7 — Blind Pool

长期缺乏曝光，因而缺乏高质量估计的候选集合。

## P8 — Exploration Budget

主动牺牲部分短期确定性，为未知候选购买观测权。

## P9 — Counterfactual Exposure

通过随机化、对照或其他方法估计“如果曾经展示会发生什么”。

## P10 — Policy–Data Separation

区分自然产生的数据与由当前策略选择后产生的数据。

## P11 — Ecosystem Health Monitor

除了点击率等局部目标，还持续监测多样性、集中度、长期质量与生态退化。

## P12 — Incentive Drift

一旦参与者学会系统规则，原始评分信号的含义会随时间漂移。

---

# 作者结构放大

## 一、看不见的东西，不能被简单当成“不好”

这是推荐系统给 Agent 最直接的一刀。

很多 Agent 会：

```text
调用 Tool A
成功
↓
以后更相信 Tool A

没有调用 Tool B
↓
没有成功记录
↓
以后更少调用 Tool B
```

久而久之：

```text
Tool A has lots of evidence
Tool B has little evidence
```

系统可能错误地解释成：

```text
A objectively better than B
```

但真实情况可能只是：

```text
A was exposed more often
```

因此：

> **没有证据，不等于负证据。**

---

## 二、一个系统可以把自己的偏见训练成“现实”

假设调度器一开始轻微偏爱某类执行器。

于是更多任务给它。

更多任务带来更多日志。

更多日志改善对它的估计。

更多成功历史提升置信度。

于是更多任务继续分给它。

经过很长时间以后，系统可能拿出大量数据证明：

> “你看，它就是最可靠。”

但这份可靠性历史本身部分来自系统过去给予它的机会。

这形成：

```text
INITIAL BIAS
↓
UNEQUAL OPPORTUNITY
↓
UNEQUAL DATA
↓
UNEQUAL CONFIDENCE
↓
STRONGER POLICY BIAS
```

这不是普通的数据偏差。

这是：

# Policy-Made Evidence

**策略制造证据。**

---

## 三、最危险的闭环不是模型学错，而是世界开始配合模型

如果创作者为了获得曝光主动改变内容，平台最终观察到的内容生态已经不是初始生态。

同样，在 Agent 系统里：

```text
ROUTER rewards short answers
↓
SUBAGENTS learn to shorten
↓
future training data contains shorter outputs
↓
router concludes users prefer short outputs
```

如果没有外部校验，就可能出现：

```text
POLICY
→ PARTICIPANT ADAPTATION
→ DATA
→ POLICY CONFIRMATION
```

这是一种**自证实回路**。

系统不只是错误理解世界。

系统可能把世界的一部分推向更符合自己原先模型的形状。

---

## 四、探索不是浪费，是购买“未被自己污染的现实”

推荐系统为什么需要 exploration？

因为如果永远只展示当前预测最优的对象，系统很难知道：

> 那些从来没被展示的对象，到底是真的差，还是只是从来没得到机会？

所以随机探索、长尾曝光、对照实验等机制具有一个更深的结构价值：

> **它们是在购买反事实信息。**

对 Agent 来说也是如此。

偶尔调用低置信度工具、让不同模型独立作答、保留少量未优化样本、进行 blind evaluation，表面上降低短期效率，却能防止系统只在自己制造的数据里越来越自信。

---

## 五、生态健康和单次推荐准确率不是同一个目标

一个推荐系统可以在单次点击预测上越来越准，同时整个生态变得：

```text
more concentrated
less diverse
more strategically gamed
more homogeneous
more fragile
```

所以：

```text
LOCAL PREDICTION QUALITY
!=
LONG-TERM ECOSYSTEM HEALTH
```

这和森林火灾、珊瑚礁、捕食者—猎物章节开始连接起来。

系统必须同时看：

- 单次决策质量；
- 长期候选多样性；
- 参与者是否正在 gaming；
- 接受者状态是否被持续改变；
- 新参与者是否还有进入机会；
- 历史优势是否形成不可逆锁定。

---

# CROSS-DOMAIN COLLISION

## 1. Agent 工具选择

Agent 只会积累被调用工具的经验。

不进行探索，就可能把“历史使用频率”误当“真实能力排名”。

## 2. 多模型路由

某模型最初因成本低被更多调用，随后积累最多评测数据，最终路由器越来越偏向它。

这可能是性能优势，也可能是机会优势。

## 3. 招聘系统

某类候选人获得更多面试机会，就能产生更多“可观察表现”；没有被筛入面试的人缺少后续数据。

## 4. 科研资助

热门方向更容易获得资源，资源产生更多论文和人才，又进一步证明该方向“活跃”。

## 5. 商业流量

渠道获得更多预算 → 产生更多转化样本 → 模型更有把握 → 下一轮继续获得更多预算。

## 6. 安全监控

系统重点监控某一区域，就会在那里发现更多异常；如果直接拿发现数量判断危险程度，监控强度本身会污染风险估计。

---

# AGENT MUTATION GATE

读完本章以后，一个 Agent 架构如果只提出：

```text
“加一个推荐模块”
“做个用户画像”
“加个探索率”
```

还不够。

真正的结构迁移至少应该改变下面一项默认假设：

1. 训练数据是否被当前策略内生制造；
2. 未选择对象是否应继续保留不确定性，而非被判定失败；
3. 是否需要独立 exploration channel；
4. 是否需要区分 policy-generated evidence 和 external evidence；
5. 是否需要对参与者策略漂移建模；
6. 是否需要长期生态指标而非只看单步 reward；
7. 是否需要反事实评估或随机化观测。

---

# GENERATED ARCHITECTURE HYPOTHESIS

## Counterfactual Exposure Router

不是普通的“按历史成功率选最好执行器”。

系统维护三套状态：

```text
EXPLOITATION POOL
当前证据最强

EXPLORATION POOL
证据不足但仍有潜力

BLIND POOL
长期没有足够暴露，禁止被误判为失败
```

每个候选执行器同时保存：

```text
observed_success
exposure_count
selection_probability
context_distribution
policy_version
uncertainty
```

路由时：

```text
majority budget
→ exploit

small protected budget
→ explore

periodic randomized audit
→ blind pool
```

评估时不直接比较：

```text
raw success count
```

而比较：

```text
performance conditional on exposure
+
context
+
selection policy
```

并持续检查：

```text
Is the router learning reality?

or

Is the router learning the consequences of its own past routing?
```

---

# TEST FRAME

构造一个安全的本地模拟环境。

## Environment

- 100 个候选执行器；
- 每个执行器在 10 类任务上具有隐藏真实能力；
- 初始路由器只有带噪声的弱估计；
- 被调用以后才产生高质量反馈；
- 执行器会根据获得任务的类型逐渐专化；
- 用户偏好也会对重复暴露产生一定适应；
- 环境中偶尔出现新的高质量执行器。

## Baselines

### B0 — Greedy Historical Best

永远选择历史平均成功率最高者。

### B1 — Confidence Router

基于置信区间，但不显式记录 exposure bias。

### B2 — Exploration Router

固定比例随机探索。

### B3 — Counterfactual Exposure Router

显式记录 selection probability、blind pool、policy version，并执行周期性随机审计。

## Metrics

- long-run task reward；
- discovery rate of hidden high performers；
- concentration of allocation；
- blind-pool size；
- diversity of active executors；
- calibration error；
- new-entry survival rate；
- policy-induced specialization；
- regret under environment change；
- divergence between observed ranking and latent capability ranking。

---

# ABLATION

必须至少移除以下组件分别测试：

1. 去掉 Exploration Budget；
2. 去掉 Blind Pool；
3. 去掉 Policy Version Tracking；
4. 去掉 Counterfactual Audit；
5. 去掉 Ecosystem Health Monitor；
6. 禁止执行器适应，观察 co-adaptation 是否是主要来源；
7. 禁止 receiver preference drift，观察偏好塑形贡献。

如果去掉这些结构以后性能和长期多样性没有显著变化，那么本章对 Agent 架构的贡献可能只是装饰性类比。

---

# FALSIFICATION

本章的结构推断应在以下情况下被削弱或拒绝：

1. 在多轮模拟中，策略产生的数据与外部随机数据没有系统差异；
2. Greedy router 长期能够稳定发现新高质量候选，不产生锁定；
3. 参与者适应不会改变未来数据分布；
4. 随机/反事实曝光无法改善能力估计或生态健康；
5. 所有长期效应都可由普通静态 sampling bias 完全解释；
6. 新架构只是 bandit/exploration 的改名，没有产生新的可测状态或控制变量。

---

# SCIENTIFIC GROUNDING

## OBSERVED / SUPPORTED

- 推荐系统中的隐式反馈存在 exposure bias：没有互动不等于明确不喜欢，因为对象可能根本没有被展示。
- 多轮推荐反馈可以放大 popularity bias、降低多样性或形成 exposure inequality，具体结果依赖算法与场景。
- 推荐行为数据会受到先前推荐本身影响，因此后续收集到的偏好数据不一定独立于系统过去的选择。
- 推荐系统会创造参与者激励；内容生产者可能根据推荐规则调整行为。
- 2026 年关于平台—创作者共同适应的模型工作继续研究短期平台激励如何通过反馈回路改变创作者生态，但这些模型结果不应被当作所有现实平台必然遵循的定律。

## INTERPRETED

- 推荐系统可以被理解成一个“曝光场”：它通过分配可见性改变哪些行为证据有机会产生。
- 曝光是一种观测权分配，而不仅仅是流量奖励。
- 一个系统如果主要用自己过去选择产生的数据继续学习，可能逐渐进入自证实世界。

## ABSTRACTED

```text
SELECT
→ EXPOSE
→ OBSERVE
→ ADAPT
→ RETRAIN
→ RESELECT
```

## TRANSFERRED

在 Agent 系统中，应显式区分：

```text
not selected

selected but failed

selected and succeeded

unknown because insufficient exposure
```

## GENERATED

Counterfactual Exposure Router 是本章生成的 Agent 架构假设，不是现有推荐系统研究已经证明的标准架构。

---

# REFERENCES

1. Fabbri, F., Croci, M. L., Bonchi, F., & Castillo, C. (2022). *Exposure Inequality in People Recommender Systems: The Long-Term Effects*. ICWSM. https://ojs.aaai.org/index.php/ICWSM/article/view/19284
2. Adomavicius, G. et al. (2022). *Recommender systems, ground truth, and preference pollution*. AI Magazine. https://onlinelibrary.wiley.com/doi/full/10.1002/aaai.12055
3. Krauth, K. M. (2022). *The Dynamics of Recommender Systems*. UC Berkeley dissertation. https://escholarship.org/uc/item/34q9q61k
4. Khenissi, S. & Nasraoui, O. (2020). *Modeling and Counteracting Exposure Bias in Recommender Systems*. https://arxiv.org/abs/2001.04832
5. Mansoury, M. et al. (2020). *Feedback Loop and Bias Amplification in Recommender Systems*. https://arxiv.org/abs/2007.13019
6. Montero-Porras, E., Smets, A., & Lenaerts, T. (2026). *Enshittification of Algorithmic Recommendation: An Evolutionary Model of Platform-Creator Dynamics*. HHAI 2026. https://journals.sagepub.com/doi/10.3233/FAIA260512
7. Sun, Y. & Sun, B. (2026). *From exposure to followers: A stock-and-flow closed-loop framework of creator dynamics*. Information Processing & Management. https://www.sciencedirect.com/science/article/abs/pii/S0306457326000695

---

# 最后的 prior-breaking question

> **如果你只能从自己曾经选择展示的世界里学习，那么你越来越自信的时候，怎么知道自己是在越来越理解世界，而不是越来越理解一个被自己筛选过的世界？**
