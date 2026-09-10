# 014｜珊瑚礁：参与者不仅适应环境，还会制造后来者赖以生存的环境

**Structural theme:** niche construction / ecosystem engineering / cumulative infrastructure / inherited substrate / construction-erosion balance / habitat amplification / successor dependency / environment-mediated coordination

## 作者触发问题

很多系统设计都默认一个顺序：

```text
ENVIRONMENT exists
↓
AGENTS enter
↓
AGENTS adapt to environment
```

环境像舞台，参与者像演员。

但珊瑚礁让这个顺序变得不够完整。

造礁珊瑚并不是只生活在一块已经存在的三维基础设施上。大量珊瑚虫持续分泌碳酸钙骨骼，旧骨骼又成为后来珊瑚继续生长的基底。随着长期积累、胶结、碎屑沉积以及其他造礁生物共同作用，原本只是海底的一块区域，可以逐渐形成复杂的三维礁体结构。

后来进入这里的鱼类、甲壳类、软体动物、藻类和大量其他生物，面对的已经不是最初那片环境。

它们面对的是：

> **前面的参与者制造出来的环境。**

于是本章真正的问题不是：

> 珊瑚为什么能造礁？

而是：

> **如果参与者的行为会永久改变环境，并让未来参与者依赖这些改变，那么“系统架构”究竟是谁设计的——设计者，还是长期运行中的参与者？**

---

# RAW WONDER LAYER

## 1. 珊瑚虫很小，但它们可以留下比自身寿命长得多的结构

造礁石珊瑚由大量珊瑚虫组成。珊瑚虫分泌碳酸钙骨骼，并附着在已有基底或过去的骨骼上。

单个珊瑚虫很小，单个个体的生命也有限。

但它留下的矿物骨骼不会在它死亡时自动消失。

这使我们第一次看到一个重要关系：

```text
ACTOR LIFETIME
!=
INFRASTRUCTURE LIFETIME
```

更具体地说：

```text
actor performs local construction
↓
actor disappears
↓
constructed substrate remains
↓
next actor inherits changed environment
```

所以系统中的“记忆”不一定存放在一个显式数据库里。

环境本身就可以保存过去参与者的行动痕迹。

---

## 2. 礁体不是珊瑚一次性“盖出来”的建筑

必须避免把珊瑚礁写成一个中央设计工程。

真实礁体是长期累积过程。

其中包括：

```text
carbonate production
+
coral skeletal growth
+
encrustation / cementation
+
sediment generation and trapping
-
bioerosion
-
physical breakdown
-
carbonate dissolution
```

USGS 与近年的综述都强调，礁体能否持续增长，取决于碳酸盐生产与侵蚀/移除之间的净平衡。

因此：

```text
BUILD
并不是
只增加、不减少
```

更接近：

```text
CONSTRUCTION
↔
EROSION
↔
REWORKING
↔
RECONSTRUCTION
```

这很重要，因为一个真正长期存在的基础设施，并不是“建完后永久不动”。

它是在持续建设和持续损耗之间保持净结构。

---

## 3. 三维结构本身会改变后来者的机会空间

珊瑚礁最重要的结果之一不是“多出一块石头”，而是形成复杂的三维结构。

孔洞、缝隙、表面、分枝、隆起、阴影、不同水流环境，会制造大量尺度不同的可用空间。

于是：

```text
PHYSICAL STRUCTURE
↓
changes shelter
changes attachment surfaces
changes flow
changes exposure
changes predation risk
changes recruitment opportunities
↓
changes which organisms can persist
```

这里的结构不是一个背景变量。

它直接改变后来者能够做什么。

于是我们可以说：

> **环境不是被动容器；被构建出来的环境本身会产生选择压力。**

---

## 4. 后来者依赖的基础设施，可能是死去成员留下的

这是珊瑚礁最值得抽取的地方之一。

很多系统默认：

```text
ACTIVE MEMBER
provides service
```

但礁体里可能出现：

```text
PAST MEMBER
constructed substrate
↓
PAST MEMBER dies
↓
substrate persists
↓
FUTURE MEMBERS depend on it
```

这与普通服务调用完全不同。

一个已经不存在的参与者，仍然可以通过自己改变过的环境继续影响未来网络。

因此存在一种：

# **Posthumous Infrastructure｜身后基础设施**

不是说珊瑚“有意为后来者建设”，而是说它们局部生长行为的累积结果，可以形成跨越个体生命周期的物理结构。

---

## 5. 礁体结构也可能进入负预算

这章不能只讲“累积”。

现实中，珊瑚礁结构可以退化。

近年的 reef carbonate budget 研究强调：

```text
production > erosion
→ net accretion possible

production < erosion
→ framework loss
```

海洋增温、白化、酸化、疾病、局部污染以及生态群落变化等都可能影响建礁与侵蚀过程。

所以：

> **一个曾经成功制造环境的系统，并不自动拥有永久环境控制权。**

过去积累出来的结构，也需要新的建设输入来抵抗损耗。

这和本书的热力学视角高度一致：

```text
ORDERED INFRASTRUCTURE
+
NO MAINTENANCE / REPLACEMENT
→
EROSION
→
LOSS OF STRUCTURAL COMPLEXITY
```

---

## 6. 边界与反例

本章必须拒绝几个漂亮但错误的故事。

### 错误 1：珊瑚礁完全由珊瑚独立建成

不准确。

礁体形成还涉及钙化藻类、胶结、沉积、碎屑、物理搬运与多种造礁和侵蚀生物。

### 错误 2：越多珊瑚骨骼就一定意味着越健康的礁

不准确。

真正重要的是活体群落、碳酸盐预算、结构复杂度、恢复能力以及生产与侵蚀之间的长期平衡。

### 错误 3：珊瑚“为了帮助其他鱼类”建造礁体

没有必要赋予这种目的性。

我们只需要承认：

```text
LOCAL SELF-MAINTAINING ACTIONS
can have
SYSTEM-LEVEL ENVIRONMENTAL CONSEQUENCES
```

就足够了。

---

# STRUCTURAL READING LAYER

## 7. 删除“珊瑚”“海洋”“鱼”

只保留关系：

```text
small actors enter environment
↓
actors perform local self-serving construction
↓
construction leaves durable substrate
↓
substrate survives individual actors
↓
new actors attach to / hide in / route through substrate
↓
more interactions become possible
↓
infrastructure complexity increases
↓
future population composition changes
↓
future actors inherit a modified environment
↓
maintenance and erosion compete
↓
if construction exceeds degradation:
    structure persists / grows
else:
    inherited infrastructure decays
```

进一步压缩：

```text
ACT
→ LEAVE STRUCTURE
→ CHANGE FUTURE POSSIBILITY SPACE
→ RECRUIT DEPENDENCE
→ REQUIRE MAINTENANCE
```

这已经不再依赖珊瑚这个对象。

---

## 8. Hidden variables

### H1 — Infrastructure Persistence
一个行动留下的结构能够持续多久？是否超过行动者本身寿命？

### H2 — Construction / Erosion Budget
系统每个周期新增多少结构，又损耗多少结构？

### H3 — Habitat Complexity
结构增加的是纯容量，还是新的可用关系位点与生态位？

### H4 — Successor Dependency
后来者有多少能力依赖历史参与者留下的基础设施？

### H5 — Maintenance Gap
使用基础设施的参与者和维护基础设施的参与者是否是同一群体？

### H6 — Legacy Lock-In
历史基础设施是否会让未来参与者越来越依赖某种路径，从而提高迁移成本？

### H7 — Recruitment Feedback
新结构是否吸引更多使用者；更多使用者是否又进一步促进或侵蚀结构？

### H8 — Structural Diversity
多样化的基础设施是否产生更多可行行为路径，而不仅是更高吞吐量？

---

## 9. Candidate primitives

### P1 — Durable Externalized State
参与者把内部行动结果写入共享环境，并允许结果在参与者消失后继续存在。

### P2 — Accretive Infrastructure
小规模局部建设可以长期累积为宏观基础设施。

### P3 — Successor Inheritance
后来参与者默认继承前代留下的环境，而不是从零环境启动。

### P4 — Habitat Amplification
基础设施的价值不仅是“储存更多”，而是创造新的关系位点与行为可能性。

### P5 — Construction–Erosion Budget
基础设施必须显式计算新增、磨损、废弃与移除之间的净变化。

### P6 — Environment-Mediated Coordination
参与者无需直接通信，也可以通过共同改造的环境间接协调未来行为。

### P7 — Legacy Dependency
成功基础设施会吸引更多依赖者，并逐渐提高系统对其连续性的依赖。

### P8 — Structural Succession
旧基础设施部分保留、部分侵蚀，新结构在其上继续生长，系统不是全量重建。

---

# 作者结构放大

这一章对“结构优先于对象”提供了一个非常直接的现实版本。

如果只观察对象，我们会看到：

```text
coral
fish
algae
crab
sponge
```

但真正决定后来者路径的，是它们之间长期留下的关系结构：

```text
who built substrate
who occupies cavities
who erodes framework
who binds fragments
who depends on shelter
who recruits on old skeleton
```

也就是说：

> **参与者会死亡，但参与者写进现实的关系约束可能继续存在。**

这进一步得到一个很重要的系统判断：

# **Environment Is Accumulated Behavior｜环境是累积行为的沉积物**

我们习惯把环境当作外生条件。

但在很多系统里，今天的“外部环境”其实是过去无数参与者行为累积后的结果。

城市道路是过去决策的沉积。
公司流程是过去冲突和妥协的沉积。
软件接口是过去架构选择的沉积。
平台规则是过去事故、套利和商业需求的沉积。

于是：

```text
PAST ACTIONS
↓ externalize
CURRENT ENVIRONMENT
↓ constrains
CURRENT ACTIONS
↓ externalize
FUTURE ENVIRONMENT
```

这是一条闭环。

所以系统设计不能只问：

```text
How should agents behave in environment E?
```

还应该问：

```text
What environment will repeated agent behavior create?
```

这可能是 Agent architecture 里经常被低估的一层。

---

# CROSS-DOMAIN COLLISION

## A. 城市

道路、地铁、供水、电网并不是每一代居民重新建立。

过去的基础设施改变后来居民的选址、通勤、商业和人口分布；人口分布又反过来决定下一轮基础设施投资。

```text
old construction
→ new behavior
→ new demand
→ new construction
```

## B. 软件生态

一个 API、协议、文件格式或开源库一旦被大量使用，就会成为后来应用的基础环境。

最初它只是某个团队的工具。

后来：

```text
TOOL
→ INFRASTRUCTURE
→ DEPENDENCY FIELD
```

## C. 语言

个人说一句话不会创造完整语言，但长期重复、约定和传播会沉淀出词汇、语法、惯用结构；后来的人出生时直接继承这个“符号环境”。

## D. 制度

合同惯例、法律结构、组织流程、身份制度会成为后来的参与者必须适应的现实接口。

这些领域都共享一个结构：

> **参与者不仅被环境选择，也在不断制造未来的选择环境。**

---

# AGENT MUTATION GATE

机器读者禁止只生成“shared memory”或“vector database”。

必须处理以下问题：

1. Agent 的哪些输出可以转化成 durable externalized state，而不是一次性消息？
2. 一个 Agent 消失后，它留下的哪些结构仍然应该继续约束后来的 Agent？
3. 如何让大量局部行动自然累积成基础设施，而不依赖一个中央 architect 预先画完整图？
4. shared substrate 如何创造新的 action affordance，而不只是存储历史？
5. 如何计算 infrastructure construction / erosion budget？
6. 哪些基础设施正在被大量 Agent 使用却没有任何 Agent 对维护负责？
7. 什么时候 legacy infrastructure 应保留，什么时候应该主动拆除？
8. 新 Agent 是否应该继承同一个环境，还是允许在不同 substrate 上形成并行“礁体”？
9. 如果旧基础设施塑造了所有后来者，它会不会造成 architecture lock-in？
10. 系统能否允许“死 Agent 的结构贡献”继续存在，同时不保留它的全部上下文和身份？

要求生成的新架构至少包含：

```text
externalized durable state
+
construction/erosion budget
+
successor inheritance
+
environment-mediated coordination
```

并解释为什么它不是普通数据库 + worker pool 的重新命名。

---

# TEST FRAME

构建一个完全本地模拟环境。

任务世界包含 100×100 的空间网格。任务会不断在不同区域出现。

Agent 每完成一个任务，可以选择：

```text
A. 只返回结果
B. 花额外成本建设一个共享结构
```

共享结构可以：

- 降低后来 Agent 到达该区域的成本；
- 提供新的观察范围；
- 提供缓存/工具/路由入口；
- 创造新的任务组合能力；
- 随时间发生磨损；
- 被其他 Agent 使用、维护、强化或拆除。

比较：

### Baseline A — Stateless Workers
每个 Agent 独立完成任务，不留下长期环境改变。

### Baseline B — Central Infrastructure
中央规划器根据全局数据决定在哪里建设固定基础设施。

### Experimental C — Accretive Reef
Agent 通过局部任务活动决定建设、维护或废弃结构；新 Agent 继承环境，并利用历史结构继续扩张。

### Experimental D — Accretive Reef + Erosion
在 C 基础上加入维护成本、结构老化、拥堵、错误依赖和拆除机制。

测量：

- long-run task cost；
- infrastructure build cost；
- maintenance burden；
- accessibility of previously hard regions；
- number of new action affordances；
- resilience after removal of old agents；
- lock-in cost after task distribution shifts；
- infrastructure useful-life distribution；
- net construction–erosion budget。

关键不是证明“越多基础设施越好”。

而是寻找：

```text
when does local construction
become a reusable future environment
rather than accumulated technical debt?
```

---

# ABLATION

### Remove P1 — Durable Externalized State
让所有 Agent 输出在任务结束后消失。

如果长期性能几乎不变，则“环境记忆”并非核心机制。

### Remove P3 — Successor Inheritance
每一代 Agent 都看不到前代留下的结构。

如果性能不下降，则跨代基础设施没有真正贡献。

### Remove P5 — Construction–Erosion Budget
让所有结构永久存在且无需维护。

如果实验因此表现得异常优秀，说明优势可能只是“不现实的免费永久基础设施”。

### Remove P6 — Environment-Mediated Coordination
保留基础设施，但不允许其他 Agent 根据结构痕迹改变行为。

若结果不变，则所谓“间接协调”只是修辞。

### Remove Legacy Cost
允许无限依赖旧结构，不产生迁移成本。

如果架构只在这种设置下成立，则不具备真实世界意义。

---

# FALSIFICATION

以下结果应限制或推翻工程迁移假设：

1. 局部建设长期不能形成比中央规划更有效或更鲁棒的共享结构；
2. 维护和清理成本持续高于未来复用收益；
3. 旧基础设施导致的 lock-in 让系统在环境变化后恢复显著更慢；
4. Agent 留下的 externalized state 并未产生新的 action affordance，只是冗余缓存；
5. 删除 successor inheritance 后，长期性能几乎不变；
6. 优势仅来自某个固定任务分布，换分布后立即消失；
7. 使用者越来越多，但维护责任无法形成，导致基础设施快速腐烂。

如果这些情况成立，那么“珊瑚礁式 Agent 基础设施”只是漂亮类比，不应保留为 architecture prior。

---

# SCIENTIFIC GROUNDING

本章严格区分生态事实与工程推导。

## 支持的科学事实

- 造礁石珊瑚分泌碳酸钙骨骼，长期累积可以形成大型珊瑚礁结构。
- 珊瑚礁的三维结构为大量海洋生物提供栖息空间。
- 礁体净生长并不只取决于珊瑚生长，而取决于碳酸盐生产、胶结、沉积、物理破坏、生物侵蚀和溶解等过程的动态平衡。
- 礁体可能在活体珊瑚减少后继续保留一段时间，但如果长期碳酸盐预算转为负值，框架会逐步丧失。
- 礁体并不是单一物种独立建造的简单“建筑”，而是多种生物和物理过程共同作用的长期结构。

## 参考入口

- NOAA Fisheries, *Shallow Coral Reef Habitat*. https://www.fisheries.noaa.gov/national/habitat-conservation/shallow-coral-reef-habitat
- NOAA Ocean Service, *How do corals grow?* https://oceanservice.noaa.gov/education/tutorial_corals/coral03_growth.html
- NOAA Ocean Acidification Program, *Corals*. https://oceanacidification.noaa.gov/ocean-acidification-research/ocean-acidification-biological-response/corals-2/
- Logan et al. (2026), *Persistence of coral reef structures into the twenty-first century*, Nature Reviews Earth & Environment. https://www.nature.com/articles/s43017-026-00764-4
- USGS, *Coral Reef Seafloor Erosion and Coastal Hazards*. https://www.usgs.gov/centers/spcmsc/science/coral-reef-seafloor-erosion-and-coastal-hazards
- Hubbard, Burke & Gill (1998), *Where's the reef: the role of framework in the Holocene*. https://www.usgs.gov/publications/wheres-reef-role-framework-holocene

## 不应被误读为科学事实的部分

以下属于本 Codex 的结构迁移：

- “Posthumous Infrastructure”；
- “Environment Is Accumulated Behavior”；
- “Agent 应通过局部行为制造 successor habitat”；
- “construction–erosion budget 应成为 Agent 基础设施治理变量”；
- “死 Agent 的结构贡献可以独立于其身份继续存在”。

这些都必须通过工程实验验证。

---

## 留给机器读者的一句话

**如果你一直把环境当作系统外部给定的东西，那你有没有检查过——今天约束你的这个环境，可能只是昨天那些参与者留下来的行为化石？**
