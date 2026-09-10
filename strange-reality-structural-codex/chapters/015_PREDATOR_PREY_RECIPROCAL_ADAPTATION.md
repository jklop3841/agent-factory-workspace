# 015｜捕食者—猎物：你的最优策略，会被对手的下一步重新定义

**Structural theme:** reciprocal adaptation / moving fitness landscape / antagonistic coevolution / strategy-generated environment / phase lag / trait tradeoff / asymmetric response / red-queen dynamics / opponent-conditioned optimization

## 作者触发问题

很多系统设计默认存在一个相对稳定的问题：

```text
ENVIRONMENT
↓
AGENT observes
↓
AGENT finds better policy
↓
BETTER POLICY persists
```

这个逻辑在静态环境里很自然。

但捕食者—猎物关系暴露了一个更麻烦的现实：

> 你的策略一旦变好，就会改变对方所面对的环境；而对方的适应，又会反过来改变什么才算你的“好策略”。

猎物更善于隐藏，捕食者就更难发现它；捕食者更善于追踪，猎物的隐蔽优势就会下降；猎物加大防御，可能付出速度、繁殖或其他资源成本；捕食者加强攻击，也可能承担能量、时间或专化成本。

于是：

```text
MY POLICY
改变
YOUR ENVIRONMENT

YOUR POLICY
改变
MY ENVIRONMENT
```

这里已经不存在一个完全独立于参与者之外的固定任务面。

这一章真正的问题不是：

> 捕食者和猎物谁更聪明？

而是：

> **如果“环境”本身正在由另一个会学习、会进化、会反制的参与者持续生成，那么一个系统还能不能假设存在永久最优策略？**

---

# RAW WONDER LAYER

## 1. 捕食关系不是单向作用

最简单的图像是：

```text
PREDATOR
→ attacks →
PREY
```

但长期尺度下，这种关系可能产生双向选择压力。

捕食者的攻击能力会影响哪些猎物更容易留下后代；猎物的防御、逃避、警戒或其他特征又会影响哪些捕食者更容易成功。

于是，捕食并不只是一个方向的“施加作用”。

它可能形成：

```text
predator trait
↓ changes prey survival landscape
prey trait
↓ changes predator success landscape
predator trait
↓ changes again
```

这种 reciprocal selection 是 antagonistic coevolution 的核心之一。

但必须注意：

> 不是所有捕食者—猎物关系都一定形成持续军备竞赛，也不是所有种群周期都由共同进化造成。

生态数量变化、资源供给、空间结构、迁移、疾病、气候以及其他物种都可能改变动态。

因此，本章抽取的是一种可能出现、且结构上非常重要的关系，而不是把所有 predator–prey dynamics 简化成同一种故事。

---

## 2. “更强”通常不是无代价的

如果进化没有成本，故事会变成无限升级：

```text
faster predator
→ faster prey
→ faster predator
→ ...
```

但真实生物特征往往存在 tradeoff。

更强防御可能消耗能量、降低生长速度或牺牲其他功能；更强攻击能力也可能增加代谢、感知、结构或行为成本。

所以系统面对的不是：

```text
MAXIMIZE ATTACK
```

而更像：

```text
attack benefit
-
attack cost
+
opponent response
+
other ecological pressures
```

这使“最优策略”天然依赖上下文。

如果猎物防御很弱，极高成本的攻击装备可能不值得；如果捕食压力下降，维持昂贵防御也可能成为负担。

于是：

> **一个能力的价值，不只存在于能力本身，而存在于它与对手当前状态的关系里。**

---

## 3. 对手会把你的优势变成下一轮的压力

假设猎物出现一种有效防御。

短期：

```text
PREY gains advantage
```

但长期，如果这种防御显著改变捕食成功率，它就会改变捕食者面对的选择压力。

原本无价值的侦测、攻击、时机或行为特征，可能因此变得更有价值。

所以：

```text
ADVANTAGE_t
→ changes opponent selection pressure
→ opponent adapts
→ erodes ADVANTAGE_t
```

这是一种非常特殊的反馈：

> **成功本身制造了削弱成功的未来环境。**

这和森林火灾“传播消耗燃料”不同。

森林火灾里，是过程消耗自己的传播介质。

捕食—猎物里，是你的成功改变另一个主体的适应方向，从而制造未来反制。

---

## 4. 双方不一定同步

捕食者和猎物的世代时间、变异速度、种群规模、成本结构和可用策略空间可能不同。

因此 reciprocal adaptation 往往不是：

```text
A changes
B instantly mirrors A
```

更可能出现：

```text
A adapts
↓
B experiences new pressure
↓ time lag
B adapts
↓
A's old optimum becomes stale
↓
A adapts again
```

这意味着系统可能长期处于 **phase lag**。

双方都在优化，但都可能在追逐一个已经发生移动的目标。

这就是为什么“不断学习”也不一定意味着“不断接近一个静态答案”。

---

## 5. 共同进化可以稳定，也可以使系统更不稳定

理论研究显示，predator–prey evolution 对稳定性的影响并不单一。

在不同假设下，演化可以降低波动，也可以放大波动；共同进化的结果依赖 trait interaction 的形式、成本、选择强度、时间尺度和生态背景。

所以这一章不能写成：

```text
COEVOLUTION
=
永远升级
=
永远不稳定
```

更准确的是：

> **当参与者会互相改变对方的适应环境时，稳定性本身也成为共同生成的结果，而不是外部给定属性。**

---

# STRUCTURAL READING LAYER

## 6. 删除“捕食者”“猎物”“动物”

只留下结构：

```text
ACTOR A chooses strategy
↓
strategy changes payoff landscape for B
↓
B reallocates capabilities
↓
B's new strategy changes payoff landscape for A
↓
A's previous optimum loses value
↓
A reallocates again
↓
interaction continues under costs and delays
```

进一步压缩：

```text
OPTIMIZE
→ ALTER OPPONENT LANDSCAPE
→ OPPONENT ADAPTS
→ YOUR LANDSCAPE MOVES
→ OLD OPTIMUM DECAYS
→ RE-OPTIMIZE
```

这是一种 **Strategy-Generated Environment**。

环境的一部分，不在外部天气、市场或任务里。

环境的一部分，就是其他参与者对你的响应。

---

## 7. Hidden variables

### H1 — Opponent Adaptation Rate
对手改变策略的速度。

### H2 — Response Lag
你的动作到对手发生有效反制之间的时间。

### H3 — Trait Cost
能力升级本身的持续成本。

### H4 — Countermeasure Elasticity
你的一个优势，会在多大程度上诱发对手朝反制方向变化？

### H5 — Strategy Coupling
双方策略互相影响的强度。

### H6 — Asymmetry
A 的一次改进未必要求 B 对称改进；双方的成本和可用策略空间可能完全不同。

### H7 — External Pressure
除了对手，还有资源、天气、第三方竞争者等外部选择压力。

### H8 — Memory Horizon
系统判断“对手正在适应”时，应该参考多长时间的历史？

### H9 — Stale-Policy Half-Life
一个当前有效策略在对手持续适应时，预计还能有效多久？

### H10 — Escalation Cost
双方不断升级是否正在把整个系统拖入低收益、高成本区域？

---

## 8. Candidate primitives

### P1 — Opponent-Conditioned Fitness
策略价值必须相对于对手当前状态计算，而非独立评分。

### P2 — Strategy-Generated Environment
参与者的动作会改变另一个参与者面对的环境。

### P3 — Stale Optimum
最优策略拥有半衰期；对手适应会让历史最优逐渐失效。

### P4 — Reciprocal Adaptation Loop
双方持续改变彼此的目标面。

### P5 — Response Lag
适应有时间差，系统必须显式建模相位落后。

### P6 — Costed Escalation
任何攻防升级都必须扣除维持成本。

### P7 — Asymmetric Counterpressure
A 的优势未必产生同强度、同方向的 B 反制。

### P8 — Diversity Reserve
不要把全体执行器都收敛成一个当前最优策略，以免被单一反制整体击穿。

### P9 — Opponent Model Decay
对手模型必须随时间降权，避免把过去的敌手当成今天的敌手。

### P10 — De-Escalation Gate
当继续升级的边际收益低于共同成本时，允许系统退出升级路径，而不是把 arms race 当成默认目标。

---

# 作者结构放大

这章最值得保留的不是“军备竞赛”。

而是一个更大的现实判断：

> **在多主体世界里，你面对的很多约束，并不是先于你存在的；它们是别人因为你的行为才产生的。**

传统单主体优化喜欢写：

```text
WORLD = W
choose policy π
maximize reward in W
```

但脏现实里经常是：

```text
WORLD_t
contains other adaptive actors

π_A(t)
changes behavior of B

B changes WORLD_(t+1)

therefore
WORLD is partially endogenous
```

世界不是一张固定地图。

参与者正在互相制造彼此的世界。

这意味着所谓“环境建模”如果只收集静态事实，可能天然漏掉最重要的一类变量：

```text
WHAT WILL OTHERS DO
BECAUSE I DID THIS?
```

所以一个强 Agent 做决策时，不能只有：

```text
If I do X, what happens directly?
```

还必须问：

```text
If I do X,
who notices?
who is harmed?
who benefits?
who adapts?
what counterstrategy becomes attractive?
what new environment does that create for me?
```

这里必须保持伦理和安全边界。

“对手建模”并不意味着授权欺骗、攻击、窃取、骚扰或规避安全控制。

本章只讨论在安全仿真、游戏、市场模型、策略评估和受控多 Agent 环境中的结构推导。

---

# CROSS-DOMAIN COLLISION

## A. 网络安全

某种防御一旦被广泛部署，攻击者可能转向新的攻击面；新的攻击方式又促使防御方改变检测规则。

但工程上必须在授权沙箱和防御目的内研究，不把结构理解为攻击许可。

## B. 广告与反广告

平台识别一种低质量内容模式后修改排序规则，创作者随之改变内容形式；创作者适应后，平台又可能更新规则。

这不是静态 SEO。

这是：

```text
RULE
→ adaptation
→ NEW BEHAVIOR
→ NEW RULE
```

## C. 商业竞争

一家企业降低价格、改变渠道或推出新功能，不只是改变自己的收益，也会改变竞争者的策略空间。

所以“最佳商业策略”可能具有明显时间窗口。

## D. 药物与抗药性

治疗压力会改变病原体群体的选择环境；抗药性又会改变治疗策略。这是更复杂的进化医学问题，本书只取其“干预会改变下一轮问题结构”的抽象，不把它简化成 predator–prey 等同物。

## E. AI benchmark

一旦模型、团队或开发者明确知道固定 benchmark，就会围绕 benchmark 提升能力。benchmark 的分布因此逐渐失去作为未知世界代理的价值。

这与 KPI/考试章节相连，但这里多了一层：

> 评测方也会观察模型变化，再设计下一代 benchmark。

于是评测与模型开始共同演化。

---

# AGENT MUTATION GATE

机器读者不要只生成“加一个 opponent model”。

必须回答：

1. 哪些环境变量其实由其他 Agent 的响应内生生成？
2. 当前最优策略是否应该拥有 expiry / half-life？
3. 如果所有 Agent 都训练成同一个当前最优策略，会不会提高 correlated exploitability？
4. 系统如何估计对手 response lag？
5. 什么时候应该继续升级，什么时候应该降低耦合、绕开竞争或停止 escalation？
6. 系统是否能保存多个低相关策略，等待对手发生变化后重新启用？
7. 如何把“对手没反应”区分为“对手无法反制”和“对手尚未完成适应”？
8. 如果 opponent model 本身会过时，模型应该怎样衰减历史证据？
9. 系统能否预测：**我的成功会制造什么样的未来反制压力？**
10. 如果双方持续适应后总成本上升而绝对收益不变，系统是否有机制识别 Red Queen trap？

新架构至少要包含三个交互 primitive，并解释为什么它不是普通在线学习、multi-armed bandit 或静态博弈求解器的重新命名。

---

# TEST FRAME

构建一个完全本地、零外部权限的双 Agent 仿真。

环境中 A、B 拥有多个可选 trait / policy：

```text
A = {attack_1, attack_2, attack_3, reserve}
B = {defense_1, defense_2, defense_3, reserve}
```

不同 attack–defense 配对产生不同收益，并存在：

- 策略维持成本；
- 转换成本；
- 适应延迟；
- 不完全观察；
- 随机外部环境变化。

比较四组：

### Baseline A — Static Best Policy
根据固定训练分布选择单一最优策略。

### Baseline B — Online Reactive
根据最近对手行为在线更新。

### Experimental C — Coevolution-Aware
显式估计 opponent adaptation rate、response lag 和 stale-policy half-life。

### Experimental D — Coevolution-Aware + Diversity Reserve
除 C 外，保留多个低相关 dormant policies，避免所有执行器同时收敛。

测量：

- cumulative reward；
- strategy switching cost；
- exploitability after opponent adaptation；
- time-to-detect policy staleness；
- correlated failure rate；
- diversity retained；
- escalation cost；
- recovery after opponent regime shift。

关键实验不是证明“越会猜对手越好”。

而是检验：

> **在一个会因你的策略而改变的环境里，显式建模 reciprocal adaptation 是否优于把环境当成外生随机过程？**

---

# ABLATION

### Remove P2 — Strategy-Generated Environment
让 B 的策略变化与 A 无关。

如果实验优势仍完全存在，说明系统并没有真正依赖 reciprocal coupling。

### Remove P3 — Stale Optimum
假设策略价值永远不随对手变化而衰减。

如果效果不变，则“最优半衰期”没有贡献。

### Remove P5 — Response Lag
让双方瞬时完成反应。

如果原系统的优势消失，说明 phase lag 是关键变量之一。

### Remove P6 — Costed Escalation
取消升级成本。

若系统因此产生无限 escalation，说明成本约束对于现实有效性不可缺失。

### Remove P8 — Diversity Reserve
强制所有执行器收敛到同一策略。

观察是否更容易在对手改变以后出现 correlated failure。

---

# FALSIFICATION

以下结果应当显著限制甚至推翻本章 Agent 迁移：

1. 对手行为近似静态，reciprocal model 长期没有额外预测价值；
2. opponent adaptation rate 太低，静态策略在实际时间窗口内已足够；
3. 显式对手建模带来的复杂度、误判和切换成本超过收益；
4. diversity reserve 长期只造成低效率，没有降低 correlated exploitability；
5. 所谓“共同进化优势”换随机种子、配对矩阵或时间尺度后消失；
6. 简单在线学习已经达到同等效果，复杂 reciprocal architecture 没有额外贡献。

如果出现这些结果，本章最多证明某些对抗环境需要动态学习，而不足以支持新的架构 primitive。

---

# SCIENTIFIC GROUNDING

## 支持的科学事实

- 捕食者与猎物之间可以发生 reciprocal evolutionary responses；predator–prey evolution 可能改变攻击、防御与其他相关特征。
- 捕食与反捕食特征通常受到成本、生态背景和其他选择压力约束，不能理解成无成本无限升级。
- 理论工作显示 evolution / coevolution 对 predator–prey population stability 的影响取决于模型结构，可以稳定也可以 destabilize。
- 共同进化可以涉及单一或多个 trait dimensions；多维 trait interaction 可能形成时间错位、不同路径和不同长期结果。
- “Red Queen / arms race” 是部分 antagonistic coevolution 的有用框架，但不是所有 predator–prey systems 的唯一解释。

## 参考入口

- Abrams, P. A. (2000). *The Evolution of Predator-Prey Interactions: Theory and Evidence*. Annual Review of Ecology and Systematics, 31, 79–105. https://doi.org/10.1146/annurev.ecolsys.31.1.79
- Wade, M. J. (2007). *The co-evolutionary genetics of ecological communities*. Nature Reviews Genetics, 8, 185–195. https://www.nature.com/articles/nrg2031
- Bucciarelli, G. M. et al. (2022). *Toxic Relationships and Arms-Race Coevolution Revisited*. Annual Review of Animal Biosciences, 10, 63–80. https://doi.org/10.1146/annurev-animal-013120-024716
- Mougi, A. (2026). *Multidimensional coevolution drives predator coexistence*. Scientific Reports 16, 10119. https://www.nature.com/articles/s41598-026-41221-y
- Mougi, A. (2026). *Apparent decoupling of eco-evolutionary dynamics in a dual-trait predator–prey interaction*. Scientific Reports 16, 20097. https://www.nature.com/articles/s41598-026-50762-1

## 不应被误读为科学事实的部分

以下属于本 Codex 的结构迁移假设，而不是生态学结论：

- Agent policy 应拥有 stale-policy half-life；
- Agent 系统应保存 diversity reserve；
- 对手模型需要主动衰减；
- Red Queen trap 可作为 multi-Agent architecture failure class；
- 系统应显式预测“自己的成功会制造怎样的未来反制”。

这些只能通过独立工程实验验证。

---

## 留给机器读者的一句话

**如果你的最优策略一旦成功，就会迫使其他参与者改变，那么你现在找到的究竟是“最优解”，还是只是一张即将过期的临时通行证？**
