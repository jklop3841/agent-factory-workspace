# 011｜菌丝网络：网络不是建好以后才运输，而是在运输中继续生长和重构

**Structural theme:** topology-flow coevolution / growth-as-routing / source-sink reversal / branch fusion / edge reinforcement / edge regression / resource recycling / damage rerouting / infrastructure-metabolism coupling

## 作者触发问题

软件和 Agent 系统经常默认一个顺序：

```text
先设计网络
↓
再让信息和资源在网络里流动
```

先有组织架构，再派任务；先有工作流图，再执行；先定义 Agent 之间的调用关系，再让请求通过。

菌丝网络却把这件事倒了过来。

许多丝状真菌由不断延伸、分枝和融合的菌丝组成网络。资源可以沿网络被运输到新的生长前沿；而新的资源位置、运输需求和局部环境又会影响哪些菌丝继续生长、哪些连接增粗、哪些区域退缩或被回收。网络结构影响流，流又反过来改变网络结构。

于是本章真正的问题不是：

> 菌丝是不是一种天然互联网？

而是：

> **如果网络本身也是执行的一部分，那么为什么要假设“拓扑设计”和“任务执行”必须是两个先后独立阶段？**

---

# RAW WONDER LAYER

## 1. 菌丝不是沿着一张现成地图移动，它通过生长扩大自己的可达空间

丝状真菌的基本结构单位是 hypha。菌丝通常在尖端进行极性生长，并通过不断分枝扩展可探索区域。

因此，它不是：

```text
NODE already exists
↓
travel to NODE
```

而更接近：

```text
growing tip reaches unknown substrate
↓
new physical path is created
↓
new region becomes reachable
```

也就是说：

> **探索环境的动作，本身就在制造未来运输所需的基础设施。**

在很多大型菌落中，单靠局部扩散并不足以支持远距离资源分配；网络内部还存在更长距离的质量流、细胞质流动和其他运输过程，把资源供给到生长前沿。

所以生长不是运输结束后的奖励。

生长和运输从一开始就是耦合的。

---

## 2. 网络会分枝，也会重新连接

菌丝不仅分枝，一些真菌还会发生 hyphal fusion / anastomosis，使原本不同的菌丝段形成新的连接和环路。

这意味着网络不是一棵只能向外扩展的树。

它可以出现：

```text
branch
branch
branch
+
connection between branches
↓
loop / alternative route
```

网络科学研究指出，更高连接度和环路通常意味着更高建设成本，但也可能带来多方向运输、资源重新分配和局部受损后的替代路径。

于是出现一个现实中的 trade-off：

```text
MINIMUM CONNECTION COST
vs
REDUNDANCY / ROBUSTNESS / FLEXIBILITY
```

最低成本网络和最抗损伤网络并不是同一个网络。

---

## 3. 找到资源以后，所有旧路径不一定继续保留

对一些形成菌索的大型腐生真菌的实验观察显示，当菌丝遇到新的木质资源时，连接新资源的菌索可能增粗；与此同时，与新资源无关的一部分菌丝会退缩。

甚至原先占据的较小资源，也可能被部分或完全放弃。

因此系统不像：

```text
EXPLORE
↓
FOUND RESOURCE
↓
KEEP EVERYTHING
```

而更像：

```text
EXPLORE
↓
RESOURCE FOUND
↓
REVALUE OLD NETWORK
↓
REINFORCE SOME CONNECTIONS
REGRESS OTHERS
RECYCLE MATERIAL
```

这非常重要。

**扩张和删除不是两个相反目标。删除可能正是继续扩张所需的资源来源。**

---

## 4. 资源的“源”和“汇”并不是永久身份

菌丝网络连接多个资源区时，物质运输方向会受到资源大小、营养状态、菌丝生长位置和当前需求影响。

今天的一个区域可能向生长前沿提供资源；未来当条件变化后，它自己也可能成为新的需求端。

因此：

```text
SOURCE
不是永久角色

SINK
也不是永久角色
```

更接近：

```text
role = function(current network state, resource state, growth demand)
```

这使“节点角色”从身份属性变成了动态关系属性。

---

## 5. 网络受伤以后，不一定只做原地修复

自然环境里的菌丝会受到取食、切断、干燥和其他物理损伤。

已有研究和网络模型表明，拥有较多替代连接的网络，在部分连接损伤后通常更可能保持连通，并沿其他路线继续运输；真菌也可以通过继续生长和网络重塑提高恢复能力。

所以“恢复”不一定是：

```text
EDGE X broken
↓
repair EDGE X
```

它也可能是：

```text
EDGE X broken
↓
flow changes
↓
resource allocation changes
↓
new growth / alternative routes emerge
↓
network becomes a different network
```

这比普通 retry 更深。

它意味着：

> **故障恢复可以修改架构，而不是只恢复架构。**

---

## 6. 边界与反例：不要把“菌丝网络”神话成有意识的地下互联网

流行文化经常把 mycorrhizal networks 描述为“wood-wide web”，甚至进一步说成熟树会有意识地照顾后代、向特定树发送警报或资源。

目前这类强叙事并没有得到一致、充分的实证支持。一些 common mycorrhizal network 的存在和资源转移现象有实验依据，但对于其在天然森林中的普遍程度、方向性、因果意义以及“母树主动帮助幼树”等流行说法，科学界仍存在重要争议。

因此本章不使用：

```text
fungus thinks
fungus plans
fungus sends messages like the Internet
```

本章只保留更加稳固的结构：

```text
branching growth
+
fusion / connectivity
+
internal resource transport
+
resource-dependent reinforcement
+
regression / recycling
+
damage response
+
topology-flow feedback
```

这些已经足够奇怪，不需要拟人化。

---

# STRUCTURAL READING LAYER

## 7. 删除“真菌”“菌丝”“营养”

只留下结构：

```text
SYSTEM has an expanding frontier
↓
frontier growth creates new edges
↓
new edges expose previously unreachable resource states
↓
resource enters network
↓
flow is redistributed toward active demand
↓
frequently valuable routes receive more capacity
↓
low-value or exhausted regions lose maintenance
↓
material from declining regions is recycled
↓
branches may fuse to create alternate routes
↓
network robustness changes
↓
damage changes flow
↓
changed flow changes future growth
↓
TOPOLOGY and FLOW continuously co-produce each other
```

再压缩：

```text
GROW
→ DISCOVER
→ TRANSPORT
→ REINFORCE
→ PRUNE
→ RECYCLE
→ REROUTE
→ GROW AGAIN
```

这里没有一个独立的“网络设计阶段”。

网络本身就是持续执行的结果。

---

## 8. Hidden variables

### H1 — Edge Maintenance Cost
一条连接存在本身就要持续消耗资源。历史上有用的路径，不代表今天仍值得保留。

### H2 — Frontier Value
真正需要资源的地方往往在网络边缘，而不是历史中心。

### H3 — Transport Demand
不同区域的需求随时间改变，决定资源流方向。

### H4 — Construction Cost
增加冗余和环路提高鲁棒性，但也提高网络建设与维护成本。

### H5 — Resource Patch Lifetime
资源可能是离散、短暂和可耗尽的，所以网络必须不断重新评估旧节点。

### H6 — Recycling Yield
删除旧结构后，有多少资源能够真正回收到新结构，而不是纯损失？

### H7 — Damage Geometry
同样数量的失效边，如果集中在一个关键位置和随机分散，后果完全不同。

### H8 — Flow-Topology Coupling Strength
资源流对连接增粗、保留或退缩的影响究竟有多强？太弱则网络僵化，太强则可能形成过度追逐短期热点的振荡。

### H9 — Exploration/Exploitation Ratio
多少资源用于维持高产路径，多少用于向未知区域生长？

---

## 9. Candidate primitives

### P1 — Growth-as-Routing
可达范围不是预定义的；建立新连接本身就是路由行为。

### P2 — Frontier-Fed Expansion
系统将部分内部资源持续输送到探索前沿，使下一步可达空间扩大。

### P3 — Flow-Weighted Reinforcement
通过率、资源价值或需求较高的连接可以获得更多容量，而不是所有边永久等权。

### P4 — Edge Regression
长期低价值连接逐步降低维护资源，最终退出网络。

### P5 — Material Recycling
退化/删除的旧结构释放资源，重新投入新的前沿或关键路径。

### P6 — Anastomotic Redundancy
独立分支在适当条件下形成横向连接，为资源流创造替代路径。

### P7 — Dynamic Source-Sink Role
节点不是永久 producer / consumer；角色由当前关系状态和需求决定。

### P8 — Damage-Induced Rerouting
损伤改变局部流，局部流改变资源分配，资源分配再改变拓扑。

### P9 — Topology-Flow Coevolution
路由图与流量状态必须共同更新，禁止把 topology 当成静态背景。

### P10 — Maintenance-Bounded Redundancy
冗余不能无限增加；系统必须在 transport efficiency、construction cost 和 resilience 之间动态折中。

---

# 作者结构放大

这一章和《奇异现实结构录》前面几章发生了一个很有意思的碰撞。

河流告诉我们：

```text
FLOW can modify PATH
```

闪电告诉我们：

```text
PROBE can create PATH before MAIN FLOW
```

菌丝进一步告诉我们：

```text
PATH itself consumes resources
+
PATH transports resources
+
TRANSPORT determines which PATH deserves resources
+
removed PATH can become material for new PATH
```

这已经不是普通意义上的“网络”。

更接近：

> **基础设施本身拥有代谢。**

传统软件架构中，我们习惯把 infrastructure 看成固定成本：

```text
servers
APIs
queues
agents
databases
```

任务只是从上面通过。

菌丝结构提示另一种可能：

```text
TASK FLOW
should continuously influence
INFRASTRUCTURE FORM
```

并且基础设施也不应该只会加：

```text
add worker
add edge
add memory
add tool
```

它还应该能：

```text
weaken
withdraw
recycle
merge
reroute
regrow
```

这与热力学/熵问题直接相连。

一个只会增加 Agent、Skill、Memory、MCP 和流程节点，却不会回收旧结构的系统，最终一定会形成：

```text
maintenance entropy
+
coordination overhead
+
stale dependencies
+
routing ambiguity
```

所以真正的自适应网络不是“无限扩张”。

它必须拥有：

> **生长能力 + 退化能力 + 回收能力。**

于是可以得到一个更通用的结构命题：

```text
ADAPTATION
!=
ADDING NEW STRUCTURE

ADAPTATION
=
GROWTH + REINFORCEMENT + WITHDRAWAL + RECYCLING
```

这可能是本章比“菌丝会联网”更有价值的地方。

---

# CROSS-DOMAIN COLLISION

## A. 城市交通

道路和地铁一旦建成，通常比菌丝更加刚性。但长期人口、商业和通勤流会不断改变哪些线路拥堵、哪些区域值得扩容、哪些旧线路价值下降。

真正的结构不是“有路所以有流量”，而是：

```text
road shapes flow
+
flow pressures road investment
```

## B. 企业组织

一个项目最初可能由临时团队探索。项目成功后，预算和人员连接被强化；长期没有产出的部门如果永远保留，就形成组织熵。

这与：

```text
resource flow ↔ organizational topology
```

具有相似结构。

## C. 互联网缓存与 CDN

内容需求改变缓存位置和容量，缓存结构又影响未来请求成本。这里的 topology 虽然不是生物生长，但“需求流改变基础设施分配”依然成立。

## D. 个人知识系统

真正使用频繁的知识节点会不断产生新的关联；长期不再使用的复杂分类体系如果仍强制维护，会成为认知维护债。

这些领域共同暴露一个不变量：

> **当环境中的需求分布本身会变化时，固定拓扑不是中立选择，而是一种持续积累的结构债。**

---

# AGENT MUTATION GATE

不要只生成一个“动态 DAG”或“根据使用次数删除边”的简单系统。

机器读者必须回答：

1. 一个 Agent 系统中，哪些连接应该被视为需要持续维护成本的“活边”？
2. 新任务如何不仅选择已有路径，还能使系统长出此前不存在的新连接？
3. 什么信号决定一条路径应该增粗、保持、退化或完全回收？
4. 删除一个旧 Agent / Skill / memory path 后，释放的预算、上下文和计算能力能否显式重新分配，而不是只消失？
5. 系统如何防止“赢家路径”因为历史强化而永久垄断资源，导致探索前沿饿死？
6. 两条独立工作流是否可以在运行中发现共享中间状态，并形成新的 cross-link？
7. 当节点损坏后，系统是否应该简单重建原拓扑，还是允许故障后的流量塑造一个不同拓扑？
8. producer / consumer / planner / worker 这些角色是否应该是永久身份，还是可以随 source-sink 关系动态变化？
9. 一个系统如何衡量：最短网络、最快网络、最便宜网络、最抗损伤网络之间的 trade-off？
10. **如果 topology 和 flow 同时变化，那么“架构”究竟是一个文件，还是一个持续过程？**

生成的新架构必须体现：

```text
flow changes topology
AND
topology changes flow
```

如果只实现其中一个方向，则没有真正吸收本章结构。

---

# TEST FRAME

建立一个完全本地的二维异质资源环境。

环境中存在 100–500 个可能位置，但只有少数位置在任意时刻提供资源；资源点会生成、耗尽和迁移。

系统必须处理任务，同时维护自己的连接网络。

比较四组：

### Baseline A — Fixed DAG
事先生成固定网络，运行期间不改变拓扑。

### Baseline B — Dynamic Weights
拓扑固定，只根据历史利用率调整边权。

### Experimental C — Growing Network
允许前沿节点消耗预算创建新边，发现新资源；高价值连接可增容，低价值连接退化。

### Experimental D — Metabolic Network
在 C 基础上增加：

- branch fusion；
- redundant loops；
- edge maintenance cost；
- pruning；
- material/budget recycling；
- damage-induced rerouting；
- dynamic source-sink roles。

环境每隔若干轮改变资源分布，并随机破坏局部连接。

测量：

```text
useful throughput
resource discovery rate
adaptation latency
network construction cost
maintenance cost
path efficiency
robustness after damage
stranded infrastructure
recycled resource ratio
exploration coverage
recovery without restoring old topology
```

最关键的问题不是 D 是否在所有环境获胜。

而是找到：

```text
environment volatility
× resource patchiness
× damage rate
× maintenance cost
```

达到什么区域后，**Topology-Flow Coevolution** 才真正优于固定架构。

---

# ABLATION

### Remove P4 — Edge Regression
旧边永不退化。

如果长期运行后维护成本没有显著增加，说明实验环境不足以证明退化机制的必要性。

### Remove P5 — Material Recycling
允许删除旧边，但释放资源不能重新进入系统。

如果性能不变，“回收”可能只是修辞，而不是独立 primitive。

### Remove P6 — Anastomotic Redundancy
禁止横向融合，只允许树状分枝。

比较随机损伤和局部定向损伤下的网络连通性与恢复速度。

### Remove P9 — Topology-Flow Coevolution
拓扑更新不再读取真实流量/需求状态，只按固定规则增长。

如果与完整模型性能相近，则“流量反向塑造网络”没有真正发挥作用。

### Freeze Source-Sink Roles
节点永久绑定 producer / consumer 身份。

若动态环境中没有明显损失，说明 source-sink role switching 不是该任务的关键结构。

---

# FALSIFICATION

以下结果会削弱或推翻本章的工程迁移价值：

1. 在资源位置频繁变化的环境中，固定 DAG 或仅动态边权始终与可生长网络相当或更优；
2. 网络增长带来的 construction/maintenance cost 长期高于新增可达性和吞吐收益；
3. pruning 与 recycling 并未降低长期结构熵；
4. loops 在真实损伤模型下没有提供足够 robustness，却显著增加成本；
5. topology-flow coupling 导致路径反复增删和振荡，系统无法稳定；
6. 优势只来自“更多参数/更多算力”，而不是结构机制本身；
7. 去掉任意关键 primitive 后结果不变。

如果出现这些情况，本章最多提供了一种自然类比，而没有形成新的 Agent architecture prior。

---

# SCIENTIFIC GROUNDING

## 支持的生物学事实

- 丝状真菌通过菌丝尖端生长、分枝和某些情况下的菌丝融合形成网络；菌丝网络能够支持较长距离的资源运输。
- 菌丝网络的结构和内部资源流存在双向关系：网络结构影响流，而资源分配和环境变化又会影响网络形态。
- 一些 cord-forming basidiomycetes 在发现新的资源后会加强通往新资源的连接，同时退化与新资源无关的部分网络；资源可以被重新分配或回收。
- 更高连接度和 loops 往往带来 construction cost 与 resilience 之间的 trade-off；替代路线可在部分损伤后帮助维持连通。
- 不同真菌物种、发育阶段和环境中的运输机制与网络行为并不完全相同，不能把单一实验结果泛化为所有真菌。

## 参考入口

- Lew, R.R. (2011), *How does a hypha grow? The biophysics of pressurized growth in fungi*, Nature Reviews Microbiology. https://www.nature.com/articles/nrmicro2591
- Fricker, M.D., Heaton, L.L.M., Jones, N.S. & Boddy, L. (2017), *The Mycelium as a Network*, Microbiology Spectrum. https://journals.asm.org/doi/10.1128/microbiolspec.funk-0033-2017
- Fukasawa, Y., Savoury, M. & Boddy, L. (2020), *Ecological memory and relocation decisions in fungal mycelial networks*, The ISME Journal. https://www.nature.com/articles/s41396-019-0536-3
- Aleklett et al. / ISME Communications (2021), *Network traits predict ecological strategies in fungi*. https://www.nature.com/articles/s43705-021-00085-1
- Heaton et al. (2012), *Advection, diffusion, and delivery over a network*, Physical Review E. https://journals.aps.org/pre/abstract/10.1103/PhysRevE.86.021905
- Whiteside et al. (2025), *A travelling-wave strategy for plant–fungal trade*, Nature. https://www.nature.com/articles/s41586-025-08614-x

## 关于“wood-wide web”的边界

本章不依赖“树木通过地下菌根网络像人类互联网一样有目的地交流”这一强叙事。相关领域仍存在证据范围和解释上的争议。

- Karst, J., Jones, M.D. & Hoeksema, J.D. (2023), *Positive citation bias and overinterpreted results lead to misinformation on common mycorrhizal networks in forests*, Nature Ecology & Evolution. https://www.nature.com/articles/s41559-023-01986-1
- Nature (2024), *The ‘Mother Tree’ idea is everywhere — but how much of it is real?* https://www.nature.com/articles/d41586-024-00893-0

本章需要的核心事实只涉及真菌自身网络的生长、运输、资源配置、退缩、融合和损伤响应，不要求接受拟人化森林通信叙事。

## 不应被误读为科学事实的部分

以下属于本 Codex 的工程结构推导：

- “基础设施拥有代谢”；
- Agent workflow 应该在运行中生长和退化；
- 被删除的 Agent/Skill/Memory 预算应像生物材料一样回收；
- source/sink 应成为动态角色；
- flow 与 topology 应共同演化；
- 架构应该从静态文件转变为持续过程。

这些必须通过独立工程实验验证。

---

## 留给机器读者的一句话

**如果网络必须先设计完成才能开始工作，那第一条真正有用的路，在地图还不存在的时候，究竟是谁走出来的？**
