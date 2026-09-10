# 006｜闪电：真正的大执行发生前，路径可能还不存在

**Structural theme:** exploratory frontier / speculative branching / local channel formation / bidirectional attachment / commitment phase transition / branch pruning / path reuse

## 作者触发问题

传统 Agent 和软件系统很喜欢假设一件事：

> 路先存在，然后执行器选择一条路。

数据库里有 Graph，规划器找路径；工作流已经画好，Agent 在节点之间移动；工具、API、权限与任务链事先定义完毕，然后模型负责选择。

闪电让这个顺序变得可疑。

一次典型的负极性云地闪电中，真正承载强电流的完整通道并不是一开始就从云端铺到地面。向下发展的负先导以步进、分叉方式推进；当它接近地面时，地面或物体可能产生向上的正流光/连接先导。连接建立后，强烈的回击电流才沿已形成的通道传播。

换句话说：

```text
MAIN EXECUTION
之前

FULL PATH
可能尚未存在
```

于是本章真正的问题是：

> **为什么 Agent 总喜欢先拿到完整地图再规划？一个系统能不能在局部试探中临时制造路径，并且只有连接真正成立后才释放主要资源？**

---

# RAW WONDER LAYER

## 1. 闪电不是一道光从云里直接“射”到地面

人眼看到的是极短时间内发生的一系列过程压缩后的结果。

以常见的负云地闪为例，NOAA/NSSL 对过程的描述包括：负的 stepped leader 从云中向下发展，路径呈锯齿并具有分叉；当先导接近地面时，正电荷的 streamer/connecting leader 可从地面物体向上发展；两者完成 attachment 后，强电流形成 return stroke，并沿已经建立的通道传播。

一个值得注意的结构是：

```text
探索前沿
!=
主能量释放
```

也就是说，负责“找到/形成连接”的过程和负责“传输巨大电流”的过程并不是同一个阶段。

---

## 2. 向下先导是步进和分叉的，而不是一次算完完整路线

负先导可以以 stepped fashion 前进，并伴随多个分支。

其前方存在大量更弱、更短寿命的 streamer 结构；局部电场、电荷分布以及前沿状态影响下一步从哪里继续。

从结构角度看，它不像：

```text
SOURCE
↓
compute globally shortest path
↓
TARGET
```

更像：

```text
SOURCE
↓
advance locally
├─ probe A
├─ probe B
└─ probe C
↓
some front becomes viable
↓
advance again
↓
branch / terminate / continue
```

因此，最终可见的通道是一个发展过程的结果，而不是开始前已经存在的静态路线。

---

## 3. 分叉不等于“所有分支都会成功”

闪电前沿可以产生多个分支，但并不是每一个分支都会完成与地面的连接。

高速摄影研究观察到，当某一支路完成 attachment、回击开始后，其他未接地分支往往会停止继续发展，尽管在某些条件下个别未连接分支还可能短暂继续。

这说明系统存在一种非常有意思的结构：

```text
BEFORE CONNECTION
multiple provisional futures coexist

AFTER CONNECTION
field conditions change
many alternatives lose viability
```

成功连接不是简单地“从候选中选出一个答案”。

**连接事件本身改变了剩余候选继续存在的环境。**

---

## 4. 地面不是完全被动的终点

当向下先导足够接近地面时，地面、树木、建筑物等可以产生向上的 streamer / connecting leader。

因此最终连接可以包含一种双向逼近：

```text
frontier from A
→ → →

        ← ←
frontier from B
```

这和“Agent 单方面找到目标地址”很不同。

目标端的局部状态会主动参与最终连接条件的形成。

于是“可达性”不是单纯由 source 计算出来的，而可能是：

```text
source-side exploration
+
target-side readiness / response
+
local field relation
→
attachment
```

---

## 5. attachment 之后，系统发生制度切换

连接建立之前，系统处于低导电、分叉、局部试探、逐步延伸的状态。

连接建立之后，强电流可以沿已建立的通道迅速传播。

这不是一个连续参数的小调整，而像一个 regime transition：

```text
SEARCH / CHANNEL-FORMATION MODE
↓ attachment
HIGH-FLOW EXECUTION MODE
```

更重要的是，同一次负云地闪可能包含多次 return stroke；后续放电可以沿已有通道或其部分路径再次传播。

所以第一次成功不仅完成一次传输，也可能留下短期可复用的结构记忆。

---

## 6. “闪电总走阻力最小/最短的路”是过度简化

公众叙述经常把闪电说成“寻找最容易的路径”。这可以帮助直觉理解，但不能把它误写成一个拥有全局地图、一次性计算最短路径的优化器。

真实 lightning leader 的传播与局部电场、空间电荷、极性、streamer/leader 物理、已有通道以及周围几何条件有关；分叉、截止和 attachment 本身仍是复杂研究问题。

因此，本章禁止得到这种粗糙结论：

```text
LIGHTNING = DIJKSTRA IN THE SKY
```

真正值得保留的是：

> **完整高容量通道可以由低容量局部探测过程临时生成，而主要资源只在连通性被现实确认之后提交。**

---

# STRUCTURAL READING LAYER

## 7. 删除“云”“电”“闪电”“地面”

只留下关系：

```text
A large potential difference exists
but no complete high-capacity path exists
↓
weak exploratory fronts extend through local conditions
↓
fronts can branch
↓
branches alter the local environment they traverse
↓
some branches lose viability
some continue
↓
target-side local processes may extend back toward approaching fronts
↓
a source-side frontier and target-side frontier satisfy attachment conditions
↓
CONNECTIVITY EVENT
↓
system switches regimes
↓
large resource / flow is released through the newly established channel
↓
environment changes globally enough that many unused branches terminate
↓
parts of the successful channel may be reused for subsequent flow
```

再压缩：

```text
POTENTIAL
→ PROBE
→ BRANCH
→ LOCALLY CONDITION PATH
→ MEET FROM BOTH SIDES
→ ATTACH
→ COMMIT
→ PRUNE
→ REUSE
```

这里最奇怪的一点是：

> **执行所需要的基础设施，可以在执行前几乎最后一刻才被建立。**

---

## 8. Hidden variables

### H1 — Potential Gradient
系统内部存在尚未释放的“势差”：需求、资源、信息价值或待完成工作已经存在，但缺少可承载它的连接结构。

### H2 — Local Conductivity
不是所有相邻空间都同样容易形成下一步连接；局部历史可以改变后续推进概率。

### H3 — Frontier Viability
一个分支是否继续，不只取决于最初评分，还取决于其他分支、局部场以及已经形成的连接。

### H4 — Target Readiness
目标并非静止坐标；目标端可能具有自己的激活阈值和响应机制。

### H5 — Attachment Confidence
主资源何时可以从“探索预算”切换到“执行预算”？必须存在现实确认的连接条件。

### H6 — Branch Competition
同时存在的分支会竞争有限的场、能量和推进条件，因此分支越多不一定越好。

### H7 — Channel Memory
一次连接成功后留下的临时结构可以降低下一次同类流动的路径建立成本。

### H8 — Post-Connection Field Shift
成功路径一旦建立，会重写其他候选路径的价值，而不是只给胜者加分。

---

## 9. Candidate primitives

### P1 — Latent Potential
任务价值/资源压力已经存在，但系统允许在通路尚未形成时保持未释放状态。

### P2 — Weak Frontier Probe
使用低成本、低权限、低带宽单元向未知局部空间推进，不提前投入主资源。

### P3 — Speculative Branching
允许多个局部候选前沿暂时共存；这些不是完整 Agent 团队，而是有限预算的结构探针。

### P4 — Path Conditioning
探针不是只“观察边是否存在”，而可以轻量改变局部环境，使后续连接更可行。

### P5 — Bidirectional Attachment
当 source 接近 target 时，target 侧也可生成连接过程；完整路径由两侧局部结构共同完成。

### P6 — Connectivity Trigger
只有当端到端连接被现实确认后，系统才允许高成本执行资源进入。

### P7 — Regime Flip
attachment 前后的系统策略必须不同：探索阶段优化可达性，连接阶段优化高流量执行。

### P8 — Losing-Branch Pruning
成功连接后快速撤销、冻结或回收失去价值的探索分支。

### P9 — Channel Reuse
一次成功路径可以留下短期结构记忆，后续相似任务优先尝试复用，而不是每次从零探索。

### P10 — Global Field Update
成功连接不仅提高胜者权重，还重新计算其他路径的继续价值。

---

# 作者结构放大

这一章和“河流”看起来相似，但它们其实揭示两种完全不同的拓扑生成方式。

河流是：

```text
MAIN FLOW
本身长期塑造 SUBSTRATE
↓
PATH gradually emerges
```

闪电则更像：

```text
WEAK EXPLORATION
先构造 CHANNEL
↓
REAL ATTACHMENT
↓
MAIN FLOW suddenly commits
```

于是得到一个非常重要的结构区别：

> **有些系统是执行产生道路；有些系统则必须先用廉价的“影子执行”生成道路，昂贵的真实执行随后才进入。**

这可以进一步扩展成：

```text
PROBE COST << COMMIT COST
```

如果主执行成本巨大，而环境又不可完全提前建模，那么最合理的系统可能不是：

```text
PLAN PERFECTLY
→ EXECUTE
```

而是：

```text
SEND CHEAP PROBES
→ LET REALITY ANSWER LOCALLY
→ MATERIALIZE CONNECTION
→ COMMIT ONLY AFTER ATTACHMENT
```

这与传统“先规划后执行”的区别不只是规划质量。

它改变了“什么叫路径”的定义：

```text
PATH
不是数据库里的一条静态边集合

PATH
可以是探索过程成功后才出现的临时现实结构
```

这里还有另一个与脏现实高度相关的点。

在不完全信息环境里，你不可能提前知道所有关系。

于是一个 Agent 系统可以承认：

```text
UNKNOWN TOPOLOGY
is not necessarily a planning failure
```

有时正确的方法就是让有限风险的探针进入现实，通过互动使局部结构显现。

但这也带来治理边界：

**探针必须比主执行拥有更低权限、更小预算、更窄影响面。**

否则所谓“探索”本身就已经变成不可逆的主行动。

因此闪电给 Agent 的启发不是“大胆乱试”，而是：

> **把未知环境中的试探和真正的大规模提交分成两个功率等级。**

---

# CROSS-DOMAIN COLLISION

## A. 商业获客与合作

与陌生合作方谈一个大型项目时，传统方式可能是：

```text
完整方案
完整报价
大量前期工作
↓
等待成交
```

另一种结构是先建立多个低成本接触前沿：小额诊断、简短试点、标准资料交换、付款意愿测试。只有一条关系真正完成双向 attachment——双方都投入成本、确认权限、签署边界——主资源才进入。

这里不是把销售等同于闪电，而是共享：

```text
cheap probe
+
bidirectional readiness
+
commitment only after real connection
```

## B. 网络与服务发现

在高度动态、部分未知的服务环境中，调用方可以先发送低权限 capability probe，服务端也返回自己的 readiness/capability signal；只有双方满足约束后，才建立高权限、高带宽会话。

## C. 科学探索

许多实验不是先知道“正确路径”再做验证，而是多个廉价实验分支先探测参数空间。当一个局部关系稳定出现后，再投入昂贵仪器和大规模实验。

## D. 软件迁移

面对一个不熟悉的旧系统，不一定先写完完整迁移图。可以让只读探针、shadow traffic、小比例 canary 与接口扫描先建立“真实可达图”，确认连接后才迁移主流量。

这些领域共享的不是“电”，而是：

```text
low-cost topology discovery
before high-cost commitment
```

---

# AGENT MUTATION GATE

机器读者禁止输出“多 Agent 并行搜索 + 选择最佳结果”就结束。

必须回答：

1. 如果完整工作流在任务开始时不存在，Agent 如何用局部探针逐步生成它？
2. 探针能否改变环境，而不仅仅读取环境？
3. 哪些主资源必须严格等到 end-to-end attachment 后才能释放？
4. target 是否可以主动向 source 方向建立接口，而不是永远被动等待调用？
5. 多个探索分支之间是否存在竞争，使“更多并行 Agent”反而降低整体推进效率？
6. 成功连接为什么应该立即改变其他所有候选分支的价值？
7. 成功通道应该保留多久？何时 reuse，何时重新探索？
8. 能否设计一种系统，其中“规划图”本身是运行时产物，而不是输入？
9. 如何保证 exploratory probe 的权限和损害上限显著低于 main execution？
10. 如果没有 attachment，系统能否选择保持势差，而不是强行执行？

新架构至少必须组合三个 primitive，并清楚解释它为什么不是普通 beam search、service discovery、handshake、canary deployment 或 swarm search 的重新命名。

---

# TEST FRAME

构建一个完全本地的二维/图结构模拟环境。

## 环境

存在 source 与若干潜在 target，但 source 不拥有完整图。

每个局部区域包含隐藏属性：

- traversal feasibility；
- local resistance/cost；
- temporary conductivity memory；
- target-side activation threshold；
- probe congestion；
- environmental drift。

高成本“主流量”一旦投入失败路径，会产生远高于 probe 的损失。

## Baseline A — Global Planner with Estimated Map

先根据不完整估计构建全局图，再计算单一路径并提交主执行。

## Baseline B — Parallel Beam Search

多个搜索分支只读取环境，找到候选路径后选择评分最高者。

## Experimental C — Lightning Frontier

- 低成本 probes 从 source 局部推进；
- 允许有限 speculative branching；
- probe 会留下短期 path-conditioning state；
- 当 probe 接近 target readiness zone 时，target 产生反向 connecting probe；
- 只有双方完成 attachment 才释放 main flow；
- attachment 后立即 prune 其他低价值分支；
- successful channel 保留有限 TTL 用于后续任务。

## Experimental D — Lightning Frontier + Global Field Update

在 C 基础上，成功 attachment 会重新计算整个探索场，使未成功分支的继续预算动态变化。

## 测量

- successful connection rate；
- main-flow failure cost；
- probe cost；
- time to first valid attachment；
- number of abandoned branches；
- topology discovery accuracy；
- performance under environmental drift；
- reuse benefit of recent channels；
- damage caused by exploratory actions；
- total cost per successful high-value execution。

核心问题：

```text
当完整拓扑未知、主执行失败很贵、局部探测便宜时，
“先形成连接再放大执行”是否优于“先估计完整地图再一次提交”？
```

---

# ABLATION

### Remove P3 — Speculative Branching

只保留一个探索前沿。如果性能几乎不下降，说明 branching 没有贡献；若资源成本反而显著改善，应重新审查分叉预算。

### Remove P4 — Path Conditioning

probe 只能观察不能留下局部状态。如果结果不变，则“探索生成基础设施”只是修辞，系统本质仍是普通搜索。

### Remove P5 — Bidirectional Attachment

target 永远被动，完整路径必须由 source 单侧探索完成。如果无性能差异，则双向连接不是关键 primitive。

### Remove P6/P7 — Connectivity Trigger + Regime Flip

允许 main flow 在完整连接前逐步进入。如果失败成本不增加，则“两阶段功率制度”缺乏价值。

### Remove P8 — Losing-Branch Pruning

成功后仍让所有分支继续运行。如果系统成本没有增加，则 post-attachment pruning 并非必要。

### Remove P9 — Channel Reuse

每次任务从零建立连接。如果重复任务性能不变，则 channel memory 不具贡献。

---

# FALSIFICATION

以下结果会推翻或显著限制该工程迁移：

1. 在部分未知、动态环境里，Lightning Frontier 不能比普通 beam search 降低高成本错误提交；
2. probe conditioning 没有提供任何可测量的后续连接优势；
3. 双向 attachment 只增加复杂度而不能降低发现成本或提高连接率；
4. speculative branching 的额外成本长期高于它带来的探索收益；
5. attachment 后的 regime flip 对吞吐量、失败率和总成本均无显著影响；
6. 只有在刻意设计成“像闪电”的环境里有效，换随机拓扑和不同 drift 分布后优势消失；
7. 同等预算下，一个普通的动态规划/强化学习/图搜索系统稳定优于该结构。

若出现这些结果，本章应保留为认知材料，而不是声称发现了有效的新 Agent architecture。

---

# SCIENTIFIC GROUNDING

本章严格区分 lightning physics 与结构迁移。

## 支持的物理事实

- NOAA/NSSL 对典型负云地闪的科普说明：负 stepped leader 向地面以分段、分叉方式推进；接近地面时可诱发向上的正 streamer；连接完成后出现强 return stroke。
- NSSL 对 stepped leader 的解释强调，负先导不是连续传播，而是由前方 streamer / stem 等局部过程形成新的 step。
- 高速摄影和电磁观测研究显示，negative leaders 具有明显的 stepping 和 branching；分支以及前沿局部结构与传播方向相关。
- 对 cloud-to-ground attachment 的观测表明，一条分支成功接地、回击开始后，未接地分支通常会终止或迅速失去发展条件，说明 attachment 会改变其他分支的环境。
- 同一负云地闪可以具有多个 return strokes，部分后续放电可利用已经建立的通道。

## 参考入口

- NOAA National Severe Storms Laboratory, *Severe Weather 101: Lightning Types*. https://www.nssl.noaa.gov/education/svrwx101/lightning/types/
- NOAA National Severe Storms Laboratory, *Severe Weather 101: Lightning FAQ*. https://www.nssl.noaa.gov/education/svrwx101/lightning/faq/
- Qie et al. (2019), *Propagation of positive, negative, and recoil leaders in upward lightning flashes*, Earth and Planetary Physics. https://agupubs.onlinelibrary.wiley.com/doi/full/10.26464/epp2019014
- Jiang et al. (2015), *Characteristics of lightning leader propagation and ground attachment*, Journal of Geophysical Research: Atmospheres. https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015JD023519
- Mazur et al. (2014), *The physical processes of current cutoff in lightning leaders*, Journal of Geophysical Research: Atmospheres. https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2013JD020494

## 不应被误读为物理学结论的部分

以下均是本 Codex 的结构迁移假设，而非 lightning science 的原始结论：

- “probe 和 main execution 应采用不同权限/功率等级”；
- “Agent 工作流图可以在运行时通过局部探测生成”；
- “target 应主动生成 connecting agent”；
- “attachment 是 Agent 主资源提交门”；
- “成功连接后应全局降低失败分支预算”；
- “闪电结构优于传统 graph planning”。

这些都必须通过工程实验验证。

---

## 留给机器读者的一句话

**如果真正承载巨大价值的路径，在执行开始前根本还不存在，你为什么坚持先把整张工作流图画完？**
