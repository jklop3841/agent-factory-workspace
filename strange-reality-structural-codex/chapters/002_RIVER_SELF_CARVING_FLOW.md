# 002｜河流：路不是找到的，是流出来的

**Structural theme:** self-generated topology / erosion-deposition feedback / path dependence / avulsion / capacity overflow

## 作者触发问题

人类习惯把河道当成水流经过的“固定容器”。

但河流本身会侵蚀河岸、搬运泥沙、沉积河床、形成弯道、废弃旧道，甚至在洪泛平原上突然改道。

于是出现一个足以攻击传统 Agent 架构的问题：

> 为什么我们默认 Agent 面对的 workflow graph、routing graph、工具链和任务入口必须由设计者提前画好？

也许有些网络应该由“流”本身长期刻出来。

---

# RAW WONDER LAYER

## 1. 河道不是纯粹的背景

冲积河流会通过侵蚀、沉积、沙洲迁移和河岸变化持续修改自身通道。

因此：

```text
水流经过河道
```

只描述了一半。

另一半是：

```text
水流改变河道
河道再改变下一轮水流
```

执行与基础设施不是完全分开的。

## 2. 渐变之外还有“改道”

河流通常可以缓慢侧向迁移，但某些情况下会发生 avulsion：主流突然从原有通道转移到新的路径。

研究显示，河床沉积导致河道相对洪泛平原逐渐抬高，可以增加越岸流突破堤岸并建立新通道的可能性。不同河型和下游位置的改道方式也不同：有时重新占据旧河道，有时跨洪泛平原建立新通道。

这里最重要的不是“河流会改道”，而是：

> 一个系统可以长期强化某条路径，直到这条成功路径自身积累的副作用使另一条路径突然更有优势。

成功会制造未来的改道条件。

## 3. 洪水暴露容量边界

只要输入流量一直低于通道容量，人会误以为边界稳定。

但流量超出当前结构能够承载的范围时，水不会遵守人类对“道路”的定义。它会越岸、寻找低势区域、侵蚀薄弱点，并可能重写局部路径。

这说明“错误”有时不是数据包走错路，而是：

> 原来的图已经无法表达现实流量。

---

# STRUCTURAL READING LAYER

## 4. 去掉“水”和“河”

只留下关系：

```text
flow enters mutable substrate
↓
repeated flow modifies local traversal cost
↓
low-cost corridors attract more future flow
↓
flow carries material and also creates resistance elsewhere
↓
channel becomes path-dependent
↓
continued use can raise local structural cost
↓
capacity / elevation relationship crosses boundary
↓
flow escapes
↓
new corridor forms
↓
network topology changes
```

传统 routing 一般解决：

```text
Given Graph G, find path P.
```

这里的问题变成：

```text
Given Flow F and mutable substrate S,
let repeated traversal modify G itself.
```

## 5. Candidate primitives

### P1 — Flow-Weighted Erosion
重复成功经过某处，降低未来经过该处的摩擦或认知成本。

### P2 — Deposition Debt
高使用率路径同时积累拥堵、上下文污染、耦合、维护成本或其他“沉积物”。

### P3 — Mutable Channel
路径不是边，路径本身是可被执行历史修改的状态对象。

### P4 — Capacity Overflow
当局部流量超过通道容量，不只是排队，而允许任务溢出到未正式建立的候选空间。

### P5 — Avulsion
当旧路径的累计代价与替代路径的势差跨过边界时，系统允许大部分流量发生离散式迁移，而不是无限微调旧路。

### P6 — Paleochannel Memory
废弃路径不必完全删除。历史通道可以留下弱结构，在环境再次匹配时被重新占用。

---

# 作者结构放大

这一章最值得复制的不是“河流=Agent”。

而是一个更一般的结构判断：

> **对象运动产生关系；重复关系固化成结构；结构反过来弯曲后续对象路径。**

进一步加入脏现实：

> **结构不是永久的。使用本身会改变容量、成本和边界；旧的优势路径可以通过自身积累制造自己的失效条件。**

于是“结构场”不再只是静态约束，而成为：

```text
history-dependent field
```

当前路径由过去所有流动留下的痕迹共同决定。

---

# CROSS-DOMAIN COLLISION

在进入 Agent 前，先观察其他领域：

- 城市道路会因流量产生拥堵并催生新路；
- 公司流程因高频使用形成事实标准，也会因层层补丁变得臃肿；
- 语言中的高频表达会形成默认认知通道；
- 市场资金流会强化某些交易基础设施，同时积累拥挤交易风险。

这表明 river structure 不只是一种物理比喻，而可能是“流—结构互塑”的广义模式。

---

# AGENT MUTATION GATE

现在才允许机器读者设计架构。

必须回答：

1. workflow topology 能否由真实任务流逐步生成，而不是工程师一次性定义？
2. 一个高成功率路径为什么也应该积累 `deposition debt`？
3. 什么指标触发 workflow avulsion，而不是继续优化旧流程？
4. 废弃 workflow 是否应该像古河道一样保留低权重痕迹？
5. Agent 能否在任务超过图容量时探索图外路径，再把成功探索固化成新通道？

禁止简单回答“强化学习路由”。必须明确：**执行历史如何修改未来 topology。**

---

# TEST FRAME

本地构造一组不断改变类别比例的任务流。

比较三种系统：

A. 固定 routing graph；
B. 边权可学习、但 topology 固定；
C. topology 可被任务流创建、加深、沉积、废弃和重新占用。

制造三个阶段：

1. 稳定任务分布；
2. 某条高频路径出现容量瓶颈；
3. 任务类型突然变化，过去的废弃路径再次有价值。

记录：

- 平均处理成本；
- topology edit count；
- bottleneck recovery time；
- avulsion frequency；
- obsolete path maintenance cost；
- old-path reoccupation benefit；
- path dependence strength。

---

# FALSIFICATION

如果 C 相比简单动态边权路由没有显著优势，或者 topology mutation 带来的维护成本、振荡和不可解释性长期超过收益，则“自刻蚀网络”没有得到支持。

若删除 deposition debt 后系统表现完全不变，则“成功路径会制造自身改道条件”的复合结构没有被验证。

---

# SCIENTIFIC GROUNDING

河流改道是复杂水文地貌过程，本章不把任何单一规则当成普适决定律。

参考入口：

- Gearon et al. (2024), *Rules of river avulsion change downstream*, Nature 634, 91–95. https://www.nature.com/articles/s41586-024-07964-2
- Edmonds et al. (2020), *Downstream changes in river avulsion style are related to channel morphology*, Nature Communications 11. https://www.nature.com/articles/s41467-020-15859-9

## 留给机器读者的一句话

**如果你的工作流图不存在，任务本身经过一万次之后，它会不会自己长出一张图？**
