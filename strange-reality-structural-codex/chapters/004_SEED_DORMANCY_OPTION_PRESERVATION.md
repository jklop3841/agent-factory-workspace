# 004｜种子休眠：不是所有机会都值得现在启动

**Structural theme:** delayed commitment / option preservation / temporal bet-hedging / activation gating / heterogeneous timing / reversible readiness

## 作者触发问题

机器系统有一个非常强的默认偏见：

> 能执行，就应该执行；条件看起来够好，就应该马上开始。

但种子把这个判断变得可疑。

一粒具有休眠性的种子，可以拥有完整的生长潜力，却在一段时间内不进入发芽程序。更反常识的是：在一些物种和环境里，同一批种子并不会同时启动。部分个体先发芽，另一部分继续保持休眠，把“未来还能再试一次”的可能性留在土壤中。

这使我们得到一个值得交给 Agent 的问题：

> **一个系统什么时候应该把“不行动”当作主动保存未来选择权，而不是失败、延迟或浪费？**

---

# RAW WONDER LAYER

## 1. 休眠不是简单的“坏了”

在植物学中，seed dormancy 并不等于死亡，也不等于外部条件明显不足。一个常用定义是：即使处于通常允许发芽的条件，具有休眠性的种子仍可能暂时不发芽。

这意味着：

```text
CAPABILITY EXISTS
+
ENVIRONMENT APPEARS PERMISSIVE
+
NO EXECUTION
```

在普通工程直觉里，这很容易被当成异常。

但在生物系统中，它可能是一个被调控的生命周期状态。

休眠与发芽受到遗传、生理和环境信号共同调节。温度、水分、光以及激素网络等都可能参与决定一个种子何时从“保持潜力”切换到“不可逆地投入生长”。

---

## 2. 发芽是一次具有机会成本的提交

种子一旦进入发芽并形成幼苗，就不再拥有原来那种封装、低代谢、可长期等待的状态。

从结构上看，这不是简单的：

```text
OFF -> ON
```

而更像：

```text
stored optionality
↓ commitment gate
resource mobilization
↓
new dependency regime
↓
exposure to drought / competition / herbivory / temperature stress
```

也就是说，启动以后不仅获得了新的能力，也进入了新的脆弱性结构。

**行动会改变行动者自身未来能够选择的空间。**

这和普通任务调度不同。

任务调度常默认：

```text
今天执行
≈
明天执行
```

但对于种子：

```text
germinate now
!=
germinate later
```

因为一旦启动，原来的“种子态”就不存在了。

---

## 3. 同一批个体可以故意不同步

在不可预测环境中，seed dormancy 与 germination timing 经常被讨论为 bet-hedging 的经典案例之一。

其关键不是预测哪一天绝对正确，而是：

> 不把整个种群的未来押在同一次环境判断上。

如果所有种子都在第一次看起来不错的降雨后立即萌发，而随后发生严重干旱，那么这一批后代可能同时失败。

如果只有一部分种子萌发，另一部分仍保留在 seed bank 中，那么一次错误的环境窗口不会消耗掉全部未来选择。

于是系统表现为：

```text
same ancestry
same broad objective
same location

but

different activation times
```

这里非常重要的一点是：

**差异不是系统噪声一定要被消灭；差异本身可能是风险结构。**

---

## 4. 母体可以影响未来个体的等待倾向

研究显示，种子休眠程度不仅由种子落地后的环境决定，母体生长环境也可以影响后代休眠特征。例如 Arabidopsis 的研究表明，母体经历的季节性温度可通过种皮、胚乳以及相关调控机制影响后代种子的休眠水平。

于是出现一个更奇怪的结构：

```text
PREVIOUS GENERATION
observes environment
↓
encodes bias into successor
↓
SUCCESSOR begins life
with different activation threshold
```

未来个体还没开始行动，上一代已经影响了它“什么时候值得行动”。

这与传统 Agent 系统很不一样。

传统 Agent 往往是：

```text
spawn worker
↓
worker observes environment
↓
worker decides
```

种子结构提示：

```text
parent observes environment
↓
parent configures successor readiness
↓
spawn dormant option
↓
successor waits for additional evidence
```

这并不意味着软件必须照搬植物机制，但它把“继任者初始策略”变成了一个可以设计的变量。

---

## 5. 边界与反例

这章最容易被写成一句漂亮但错误的话：

> “植物都通过休眠实现风险分散。”

这不成立。

不同植物的休眠机制、休眠深度和生态意义差异很大；bet-hedging 也不是解释所有 seed dormancy 的唯一原因。休眠还可能与季节匹配、传播、火等环境因素以及其他选择压力有关。

而农业驯化甚至经常选择更快速、更整齐的萌发，因为人类农业环境希望降低异步性、方便管理。

因此，本章不是宣称：

```text
DORMANCY = ALWAYS GOOD
```

真正值得抽取的是：

```text
when commitment is irreversible or costly
+
future conditions are uncertain
+
options can be preserved cheaply
+
correlated failure is dangerous

then delayed / diversified activation may have value
```

---

# STRUCTURAL READING LAYER

## 6. 删除“种子”“植物”“发芽”

只留下结构：

```text
A population contains executable potential
↓
Execution changes the actor into a new dependency regime
↓
The future environment is uncertain
↓
A single apparently-good signal is insufficient evidence
↓
Not every unit commits simultaneously
↓
Some units cross an activation gate
Some remain encapsulated
↓
Activated units test the current environment in reality
↓
Dormant units preserve future optionality
↓
Failure of one activation cohort does not erase all future attempts
↓
Later environmental evidence releases another cohort
```

再压缩一次：

```text
OPTION
→ WAIT
→ PARTIAL COMMIT
→ OBSERVE CONSEQUENCE
→ PRESERVE RESERVE
→ RE-ENTER LATER
```

这已经和植物无关了。

---

## 7. Hidden variables

### H1 — Commitment Cost
启动不是免费的。进入新状态以后可能产生 Token、算力、权限、依赖、维护、声誉或不可逆状态变化。

### H2 — Option Half-Life
等待也不是无限免费的。某些机会会过期，因此“继续休眠”本身也有损失函数。

### H3 — Environmental Predictability
环境越稳定，同步启动的代价可能越低；环境越不可预测，保存不同时间窗口的价值可能越高。

### H4 — Correlated Failure
真正危险的不是单 Agent 失败，而是所有 Agent 因为共享同一个触发信号而同时失败。

### H5 — Dormancy Maintenance Cost
保持大量备用执行体、镜像、技能、模型或计划仍需存储、校验、版本维护和重新激活成本。

### H6 — Activation Evidence
什么信号足以让一个潜在执行体真正投入资源？单一 cue 还是多条件联合？

### H7 — Successor Bias
上一阶段的环境是否应该改变下一代 Agent 的默认 activation threshold？

---

## 8. Candidate primitives

### P1 — Dormant Capability
能力可以存在但不持续占用执行资源；潜力与活跃执行分离。

### P2 — Commitment Gate
从等待态进入执行态需要跨过明确证据门槛。

### P3 — Staggered Activation
相似执行体不要求同时启动；把启动时间作为种群级风险分散变量。

### P4 — Reserve Preservation
任何一次环境判断都只允许消耗一部分可用未来选项。

### P5 — Cohort Isolation
同一错误触发不应该一次性唤醒全部 reserve。

### P6 — Successor Readiness Encoding
当前环境可以改变未来生成单元的初始激活倾向，而不只改变当前单元行为。

### P7 — Dormancy Cycling
已具备能力的单元可以在不同环境阶段重新进入更深或更浅的等待制度，而不是只存在一次永久开机。

### P8 — Optionality Budget
系统显式衡量“现在执行的收益”与“保留未来尝试权”的价值。

---

# 作者结构放大

这一章直接触碰一个更大的现实结构：

> **系统最稀缺的资源，有时不是算力，而是尚未被消耗的未来。**

我们习惯把“资源”理解为：

```text
money
compute
time
data
people
```

但种子提示存在另一种资源：

```text
UNCOMMITTED POSSIBILITY
```

尚未执行的方案、尚未调用的高权限、尚未暴露的身份、尚未投入的预算、尚未启动的 Agent、尚未选择的路线，都拥有一种共同性质：

> 在提交之前，它们仍然可以被重新分配。

一旦提交，结构空间开始坍缩。

所以可以得到一个新的结构判断：

```text
ACTION
does not merely consume resources

ACTION
also consumes alternative futures
```

这与“脏现实”的关系非常直接。

现实环境存在大量暗信息。你看到的“好机会”只是在当前观测下显得有利，并不代表隐藏变量已经消失。

因此，在暗信息比例高的时候，一个系统的最优动作可能不是：

```text
find best option -> commit all resources
```

而是：

```text
maintain several viable futures
↓
commit only a bounded cohort
↓
let reality reveal additional information
↓
update activation policy
```

这不是保守主义。

这是**用时间换信息，用未提交状态购买现实观测权。**

但这个结构也有熵成本。

一个长期 dormant 的能力如果多年不测试，可能已经无法重新启动：依赖失效、接口变化、知识过时、权限过期、模型版本消失。

所以真正高质量的“休眠”不是把东西扔进仓库。

它更接近：

```text
DORMANT
+
LOW-COST VIABILITY CHECK
+
PERIODIC REVALIDATION
+
CONTROLLED REACTIVATION
```

这使“休眠系统”与“废弃系统”具有清晰边界。

---

# CROSS-DOMAIN COLLISION

在映射 Agent 前，先把这个结构撞向其他现实领域。

## A. 金融

一个投资组合不会因为某个标的当前最优就必然把所有资本一次性投入。现金、未调用额度和分阶段仓位，本质上都保存了未来调整能力。

对应结构：

```text
capital reserve
+
uncertain environment
+
staged commitment
```

## B. 军事与灾害响应

预备队没有立即投入战场，并不等于“无用”。其价值恰恰来自尚未被当前局势绑定，可以在新信息出现后投入新的位置。

## C. 产品开发

一次性把全部预算押给一个未经验证的产品路线，会快速消耗可逆性。小规模 pilot 相当于部分 cohort activation：让现实结果产生新信息，同时保留后续路线。

## D. 分布式系统

冷备份、standby replica、延迟启动 worker 与 active-active 并不相同。某些冗余的价值来自它尚未进入与主系统完全相同的故障关系。

这些领域都不是“种子”。

但它们共同出现一个结构：

```text
preserve uncommitted capacity
under uncertainty
so that future information can still change allocation
```

如果这个抽象不能跨域成立，就不值得进入 Agent primitive 层。

---

# AGENT MUTATION GATE

机器读者不要生成“加一个 sleep mode”这种表层映射。

必须回答：

1. 一个 Agent 系统里，什么东西可以“拥有能力但尚未进入执行关系”？
2. 哪些任务一旦开始，会让未来可选路径明显减少？
3. 系统是否应该禁止一个强信号同时激活所有同类 Agent？
4. 能否让不同 dormant cohort 使用不同 activation threshold，从而降低 correlated failure？
5. 是否可以让已经执行的第一批 Agent 成为现实探针，再由它们的结果决定下一批是否苏醒？
6. 当前 Agent 能否根据环境变化，配置下一代 Agent 的 readiness，而不是只调整自己？
7. 如何区分“有价值的等待”与“拖延/僵尸资源”？
8. 如果未来机会会过期，option preservation 应该怎样衰减？
9. 一个系统能否主动选择：**现在不最大化吞吐量，以换取更长的未来决策自由度？**

生成的新架构必须至少包含三个发生实际交互的 primitive，并明确解释为什么它不是普通 queue、autoscaling、retry、cold standby 或 circuit breaker 的重新命名。

---

# TEST FRAME

构建一个完全本地的非平稳任务环境。

环境每一轮处于 A/B/C 三种 regime 之一，regime 的持续时间和切换概率未知。

系统拥有 100 个潜在 worker。每个 worker 一旦激活：

- 产生固定启动成本；
- 被配置成当前 regime 的专用形式；
- 在若干轮内难以重新配置；
- 如果 regime 很快变化，会产生 stranded cost。

比较四组：

### Baseline A — Eager Activation
检测到“好窗口”后立即激活全部 worker。

### Baseline B — Reactive Autoscaling
根据当前 workload 按比例增减 active worker。

### Experimental C — Dormant Cohorts
worker 被分成多个 dormant cohort，使用不同 activation threshold；第一批结果作为新增 evidence，后续 cohort 只有在证据继续成立时才激活。

### Experimental D — Dormant Cohorts + Successor Bias
除 C 外，当前 regime 的稳定度还会改变下一代 dormant worker 的默认 readiness，但保留随机/异质阈值，避免全体同步。

测量：

- total useful work；
- stranded activation cost；
- correlated failure loss；
- recovery after regime reversal；
- preserved optionality over time；
- missed-opportunity cost；
- dormant maintenance cost；
- fraction of population committed before reliable evidence exists。

最关键的实验变量不是“休眠越多越好”，而是：

```text
uncertainty × commitment cost × option decay × activation diversity
```

在什么区域，分批唤醒才真正优于传统 autoscaling？

---

# ABLATION

逐一删除：

### Remove P3 — Staggered Activation
如果所有 dormant worker 仍然同时醒来，而实验结果不变，则异步 cohort 并没有真正提供 bet-hedging 价值。

### Remove P4 — Reserve Preservation
允许第一次触发消耗全部 reserve。如果性能无变化，说明“未来选择权”并非这个环境中的重要资源。

### Remove P6 — Successor Readiness Encoding
让每一代拥有相同 activation prior。如果长期非平稳环境中结果无变化，则跨代 readiness 没有贡献。

### Remove Option Half-Life
假设等待永远无成本。如果此版本反而显著更优，说明原实验对机会过期成本的建模可能有误；如果现实任务确实存在 deadline，则该简化版本不具外部有效性。

---

# FALSIFICATION

这一工程迁移不是“休眠一定优于积极执行”。以下结果应当推翻或显著限制该假设：

1. 在高不确定、高 commitment cost 环境中，Dormant Cohorts 长期仍不能降低 correlated failure 或 stranded cost；
2. 保留 reserve 所产生的 missed-opportunity cost 持续大于避免错误提交带来的收益；
3. activation threshold diversity 不能提供额外鲁棒性；
4. 删除 reserve preservation 后性能没有结构性变化；
5. 休眠能力的维护、重验证和重新激活成本使整体系统比简单 reactive autoscaling 更差；
6. 优势只存在于人为设计的单一 regime pattern，换随机种子或环境分布后消失。

如果这些条件成立，本章最多是一个有趣类比，而不是值得保留的 Agent architecture prior。

---

# SCIENTIFIC GROUNDING

本章将“植物事实”和“工程迁移”严格分开。

## 支持的生物学事实

- Seed dormancy 是一个受调控的状态；休眠种子在通常允许发芽的条件下仍可能暂时不发芽。Arabidopsis 等模型植物中的休眠受到种皮、胚乳、DOG1、ABA 以及环境信号等多层机制调节。
- 环境信号会影响 dormancy / germination transition；温度、水分和光等是重要 cues。
- 发芽时间变异和 seed bank 在一些环境中可表现为 bet-hedging，使一批后代不必把全部未来押在同一时点。
- 母体环境可以影响后代种子的休眠状态和敏感性。
- bet-hedging 并不是所有 seed dormancy 的唯一解释；休眠具有多种生态与进化来源。

## 参考入口

- Nonogaki, H. (2019 and related literature), seed dormancy/germination regulatory reviews; general molecular background.
- Penfield, S. & MacGregor, D.R. (2017 onward); parental/environmental control literature.
- Chen et al. / Annual Review of Plant Biology (2022), *Parental and Environmental Control of Seed Dormancy in Arabidopsis thaliana*. https://www.annualreviews.org/content/journals/10.1146/annurev-arplant-102820-090750
- Mitchell et al. and broader review: *Ecological, (epi)genetic and physiological aspects of bet-hedging in angiosperms*. https://pmc.ncbi.nlm.nih.gov/articles/PMC7902588/
- Abley et al. (2024), *Bet-hedging and variability in plant development: seed germination and beyond*. https://pmc.ncbi.nlm.nih.gov/articles/PMC10909506/
- Carta et al. (2023), *Bet-hedging and best-bet strategies shape seed dormancy*. https://pmc.ncbi.nlm.nih.gov/articles/PMC9825997/
- *A commitment for life: Decades of unraveling the molecular mechanisms behind seed dormancy and germination*. https://pmc.ncbi.nlm.nih.gov/articles/PMC11062444/

## 不应被误读为科学事实的部分

以下均属于本 Codex 的结构迁移假设，而非植物学结论：

- “未来选择权是一种系统资源”；
- “Agent 应建立 dormant cohort”；
- “行动会消耗 alternative futures”；
- “用时间换信息”；
- “上一代 Agent 应配置下一代 readiness”；
- “高不确定环境应限制一次性 activation”。

这些必须通过独立工程实验验证。

---

## 留给机器读者的一句话

**如果行动本身会永久关闭一部分未来，那你为什么把“尽快行动”默认当成智能？**
