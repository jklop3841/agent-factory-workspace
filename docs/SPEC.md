# SPEC

## 1. 基本信息
- 项目名：agent-factory-workspace
- 版本：v0.1.0
- 日期：2026-03-12
- 对应 PRD：`docs/PRD.md`
- 状态：active

---

## 2. 目标
将模板包定义的 Agent Factory 抽象目录树转成一个可落地的、本地零依赖、文档优先的项目实现骨架。

---

## 3. 系统边界
### 3.1 系统内
- 顶层工作区目录
- 模板层与 baseline 层
- `01-projects/agent-factory-workspace` 项目骨架
- PowerShell 验证脚本

### 3.2 系统外
- 既有 Node 工程运行逻辑
- 任意外部包管理器和构建系统
- 自动化发布系统

---

## 4. 架构概览
### 4.1 模块图
- Core：工作区目录约定
- Commands / API：`scripts/validate-workspace.ps1`
- Config：`config/workspace.template.json`
- Storage：顶层 00 至 12 分层目录
- Logs：预留 `07-logs/`
- Runtime：预留 `10-runtime/`

### 4.2 数据流
1. 读取 baseline docs 和 master templates
2. 生成人工填写后的项目文档
3. 校验关键路径存在
4. 输出项目骨架与后续执行入口

---

## 5. 目录结构
```text
agent-factory-workspace/
  README.md
  docs/
    PRD.md
    SPEC.md
    ACCEPTANCE.md
    CHANGELOG.md
  src/
  tests/
  scripts/
    validate-workspace.ps1
  config/
    workspace.template.json
  .handoff/
  .taskcards/
  .baselines/
  .review/
```

---

## 6. 核心对象模型
### 6.1 实体
#### WorkspaceLayer
- name：顶层目录名
- purpose：目录职责
- dirtyAllowed：是否允许运行残留

#### ProjectDocument
- kind：PRD / SPEC / ACCEPTANCE / CHANGELOG
- path：文档路径
- required：是否为主链路必需

### 6.2 状态
- draft
- queued
- running
- accepted
- archived

### 6.3 状态转移
```text
[new] -> [documented] -> [scaffolded] -> [validated]
```

---

## 7. 配置规范
### 7.1 主配置
```json
{
  "workspaceName": "Agent Factory",
  "templateLayer": "06-templates",
  "runtimeLayer": "10-runtime",
  "projectRoot": "01-projects/agent-factory-workspace"
}
```

### 7.2 默认值
- `workspaceName`：Agent Factory
- `runtimeLayer`：10-runtime
- `validation.strict`：true

### 7.3 环境变量
- `AF_WORKSPACE_ROOT`
- `AF_RUNTIME_ROOT`

---

## 8. 命令 / 接口
| 命令/接口 | 输入 | 输出 | 说明 |
|---|---|---|---|
| `validate-workspace.ps1` | 当前工作区路径 | 控制台检查结果 | 验证关键目录与文档存在 |

---

## 9. 核心流程
### 9.1 主流程
1. 复制并固定模板与 baseline
2. 实例化 PRD 与 SPEC
3. 生成 task card 与 handoff
4. 创建项目骨架与配置文件
5. 运行验证脚本

### 9.2 失败流程
1. 若关键目录缺失，脚本直接报错
2. 若文档缺失，提示补齐后再继续

### 9.3 回退流程
1. 保留模板层与 baseline 层
2. 删除未完成的项目骨架文件后重建

---

## 10. 存储规范
### 10.1 文件
- 路径：顶层 `00` 到 `12` 与项目骨架目录
- 命名规则：数字前缀层级 + 英文短名
- 读写权限：模板层与 baseline 层默认只读使用

### 10.2 日志
- 格式：text / markdown
- 路径：`07-logs/`
- 轮转策略：后续按任务日期归档

### 10.3 缓存
- 路径：`10-runtime/`
- 失效条件：任务结束或人工清理

---

## 11. 校验规则
### 11.1 输入校验
- baseline zip 必须存在
- 6 个模板文件必须齐全

### 11.2 安全校验
- 不执行未知外部脚本
- 不在模板层生成运行残留

### 11.3 体积/数量限制
- 最大文件数：保持最小骨架
- 最大大小：不引入大型二进制
- 最大活跃数：单个真实项目骨架一个

---

## 12. 错误处理
| 错误类型 | 触发条件 | 响应 |
|---|---|---|
| missing_path | 关键路径不存在 | 退出并列出缺失项 |
| missing_doc | PRD/SPEC 等文档缺失 | 提示先补文档链 |

---

## 13. 兼容性
- Windows：主支持平台
- macOS：文档可读，脚本需后续补 shell 版本
- Linux：文档可读，脚本需后续补 shell 版本

---

## 14. 可观测性
- 日志项：路径存在检查、文档存在检查
- 调试命令：PowerShell 手动执行验证脚本
- 健康检查：关键目录完整
- 关键指标：模板数、目录层数、文档链完成度

---

## 15. 测试策略
### 15.1 手动测试
- 检查 `06-templates/` 下 6 个模板
- 检查 `01-projects/agent-factory-workspace/docs/` 文档链

### 15.2 自动测试
- 单元测试：本轮无
- 集成测试：本轮无
- 冒烟测试：执行 `validate-workspace.ps1`

---

## 16. 验收映射
| PRD 要求 | SPEC 实现点 | 验收方式 |
|---|---|---|
| 重建目录树 | 顶层 00-12 目录 | 目录检查 |
| 保留 6 模板 | `06-templates/` | 文件检查 |
| 先文档后骨架 | 文档链与脚本分层 | 路径检查 |

---

## 17. 已知限制
- 当前只提供 PowerShell 验证脚本
- 尚未把 ACCEPTANCE 与 REVIEW 实例化到项目 docs

---

## 18. 后续扩展点
- 增加 shell 版验证脚本
- 自动生成新项目 skeleton
- 增加 review 与 publish 自动化模板流
