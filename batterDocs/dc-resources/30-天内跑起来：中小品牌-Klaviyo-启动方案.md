---
id: 5016
title: "30 天内跑起来：中小品牌 Klaviyo 启动方案"
slug: "smb-klaviyo-30days-start"
category: "DC 官方资源中心"
category_slug: "dc-resources"
wp_url: "https://dynamicycle.com/docs/smb-klaviyo-30days-start/"
wp_modified: "2025-12-24T04:04:54"
---

#### ****为什么我们要做这份操作文档？****

在为品牌提供 Klaviyo 服务的过程中，我们发现一个被长期低估、但影响极大的现实问题：

****大量品牌在使用 Klaviyo，但底层配置是“错误的”。****

这些问题并不显眼，却会在长期运营中持续放大成本、拉低效果，甚至让品牌误以为「Klaviyo 不好用」。

我们在实际项目中反复看到以下几类情况：

- ****Flow 的触发与筛选条件设置不合理****：导致同一用户在短时间内被重复触达，既影响用户体验，也伤害投递表现。
- ****关键事件未正确开启或未被使用****：Flow 无法基于真实用户行为触发，最终只能“按时间发邮件”，效果自然很差。
- ****用户分层逻辑混乱****：高价值用户与低意向用户混在一起，发送策略失焦，结果是——Klaviyo 费用持续上涨，但实际发送量和转化却始终上不去。

这些问题的共同点只有一个：

****Klaviyo 并不是“没配置”，而是“配置错了”。****

而一旦底层逻辑出错，后续再加 Flow、再多 Campaign，都只是在放大错误。

正因为如此，我们整理了这份 ****「Klaviyo 一键启动」操作文档****，目的并不是教品牌“怎么发更多邮件”，而是：

- 帮助品牌从一开始就把****事件、Flow、分层****配置在正确的轨道上
- 避免常见但隐蔽的配置陷阱
- 让 Klaviyo 的费用，真正花在“有效触达”上，而不是系统噪音上

这份文档，来自真实项目中的踩坑、复盘与修正，

不是功能说明书，而是一套****可直接落地的标准化启动方法****。

我们做这份文档，是因为发现：

****Klaviyo 用不好，往往不是运营能力问题，而是“第一步就走错了”。****

#### ****Klaviyo 从 0 到 1 搭建与运营操作文档****

目标：

****在 30–60 天内，让 Klaviyo 从“刚接入”变成“稳定产出订单的增长系统”****

|  |  |
| --- | --- |
| ****阶段**** | ****目标**** |
| Phase 1 | 技术接入 & 数据打底 |
| Phase 2 | 核心用户资产构建 |
| Phase 3 | 核心自动化 Flow 上线 |
| Phase 4 | Campaign 正式运营 |
| Phase 5 | 数据优化 & 扩展增长 |

##### ****一、技术接入 & 数据打底（Day 1–3）****

****这一阶段的核心目标不是“立刻发邮件”，而是确保数据真实、稳定、可用。****

****1.1 创建 Klaviyo 账户****

- 使用公司通用邮箱（非个人）
- 绑定官网域名
- 设置品牌信息（Logo、品牌色）

****1.2 [Shopify 官方集成（必做）](https://help.klaviyo.com/hc/en-us/articles/115005080407)****

路径：

****Klaviyo → Integrations → Shopify****

确认以下事件已同步：

- Viewed Product
- Added to Cart
- Started Checkout
- Placed Order
- Fulfilled Order

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-124.png?resize=984%2C1024&ssl=1)

****[启用 Klaviyo 的 Onsite Tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767)****

1. 在 Onsite tracking 部分，勾选 Track behavioral events，以启用对 Viewed Collection、Submitted Search和 Added to Cart的追踪。另外两个事件 Viewed Product和 Active on Site是默认启用的，一旦你开启应用嵌入，它们就会开始进行追踪。
2. 你会看到一条提示消息，告知你的 Klaviyo app embed 处于关闭状态。点击 Turn on，系统将带你进入 Shopify。
3. 如果出现提示，请使用你已集成至 Klaviyo 的账号登录 Shopify。
4. 你将被引导至主题设置的 App embeds 选项卡。请确保 Klaviyo 的 app embed 已切换为开启状态。
5. 在你的theme editor中点击保存。
6. 返回 Klaviyo 中的 Shopify 集成设置页面，如果需要的话请刷新页面。你应该会看到一个绿色横幅，表明你的 app embed 现在已启用。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image1.png?resize=1024%2C539&ssl=1)

****完成以上步骤后，请等待 24–48 小时，确认数据是否稳定，再进入下一步。****

****1.3 基础配置（很多人忽略）****

- 设置 Default Sender Email
- [域名认证（DNS）](https://help.klaviyo.com/hc/en-us/articles/115000357752)
- [打开 Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311)
- 设置主时区 & 货币

📌 ****没做域名认证，后面所有努力都会被送进垃圾箱。****

##### ****二、Klaviyo 中事件（Event）的定义与用途说明****

****理解‘事件’就是理解 Klaviyo 的底层逻辑，这是所有自动化的起点。****

****2.1 Shopify 标准事件（必须认识）****

|  |  |  |
| --- | --- | --- |
| ****事件名称**** | ****含义**** | ****常见用途**** |
| Viewed Product | 浏览商品 | Browse Abandon Flow |
| Added to Cart | 加入购物车 | Abandoned Cart Flow |
| Started Checkout | 开始结账 | Checkout Abandon Flow |
| Placed Order | 完成下单 | 转化、复购、RFM |
| Fulfilled Order | 发货完成 | 售后 / 教程 |
| Cancelled Order | 订单取消 | 风控 / 关怀 |

****2.2 Placed Order 事件重点字段****

在 ****Metrics → Placed Order → Activity Feed**** 中查看：

关键字段包括：

- Order Value
- Product Name
- SKU
- Category
- Discount Code
- Currency

📌 ****Flow 和 Segment 的 80% 判断逻辑，都基于 Placed Order****

****2.3 事件常见误区****

- ❌ 用 Added to Cart 判断真实意图（不够准）
- ❌ 不区分 Checkout 和 Cart
- ❌ 不用金额字段做分层

👉 ****事件不是“看有没有”，而是“怎么用”****

##### 三、 ****弹窗（Popup）的创建与配置****

****弹窗与 Welcome Flow 同步规划，避免割裂用户体验。****

****3.1 形式与内容策略****

****标准配置****：Popup (居中弹窗) + Multi-step (分步表单)

- Step 1：仅收 Email（门槛低，先留资）
- Step 2：收 Phone/SMS（高价值，选填）

****价值交换****：必须在成功页直接展示 Coupon Code，不要让用户去邮箱查收

****3.2 触发与互斥 (核心参数)****

****触发****：Scroll > 30% 或 Time Delay > 10s。

****排他性 (Targeting)****：

- ****严格执行****：Don’t show to existing profiles。
- ****逻辑****：只抓新客。老客通过 Email 触达，不要再用弹窗打扰。

****频控****：关闭后 ****5-7 天**** 内不再显示。

##### 四、 ****核心 Flow 的设置（从高收益到低收益）****

****4.1 [Welcome Flow（第一优先级）](https://help.klaviyo.com/hc/en-us/articles/115002775172)****

****触发条件：****

- List Trigger → Master List

****推荐结构：****

1. 品牌介绍 + 核心价值
2. 热卖产品 / 社会证明
3. 轻转化（优惠 / 内容）

📌 通常是 Email 收入贡献最高的 Flow

****4.2 [Abandoned Cart Flow](https://help.klaviyo.com/hc/en-us/articles/115002779411)****

****触发：****

- Added to Cart
- 条件：未 Placed Order（X 小时内）

****设置建议：****

- 2–3 封
- 第一封不建议给折扣

****4.3 Checkout Abandonment Flow****

****触发：****

- Started Checkout
- 未完成 Placed Order

📌 ****转化率通常高于 Cart Abandon****

****4.4 [Post-Purchase Flow](https://help.klaviyo.com/hc/en-us/articles/360028872611)****

****目标：****

- 建立信任
- 降低退款
- 为复购做准备

常见结构：

1. 使用指南 / 物流说明
2. 品牌故事 / 社区
3. Review / UGC 引导

##### 五、 ****Campaign 的设置与发送****

****Campaign 不是为了发邮件，而是为了用最高效的方式对话。做对‘排除’，比‘发送’更重要。****

****5.1 基础设置****

- ****发送身份****：确保发件人 Name / Email 与品牌保持一致。
- ****Subject Line****：直接、清晰。
- ****Preview Text****：必填（它是增加打开率的关键）。
- ****Smart Sending****：建议 ****开启****。如果该用户最近 16 小时内已经收到了你的 Flow 邮件，就跳过此 Campaign，避免过度打扰。

****5.2 内容类型建议****

- ****新品 / 精选****：突出新品或季节热卖
- ****Storytelling****：讲品牌故事，增加情感连接
- ****Highlight Content****：导流到 Blog 或其他内容，保持用户活跃
- ****Promotions****：独家折扣或限时优惠，营造紧迫感

****5.3 受众选择与排除****

****发 Campaign 前不只问“发给谁”，更要问“谁不该看到？”****

****核心逻辑：****不要发给不相关的人，不要干扰正在 Flow 里的高价值转化。

1. ****排除 (Exclude) 刚刚购买的人****
   - ****条件****：Placed Order at least once in last 30 days。
   - ****原因****：他们刚买完，不该立刻收到新一轮大促信息。应该让他们进入 Post-Purchase Flow 享受服务。
2. ****排除 (Exclude) 长期无反应的“僵尸粉”****
   - ****条件****：Opened Email = 0 in last 90 days AND Clicked Email = 0 in last 90 days。
   - ****原因****：硬发给这些人会拉低整体打开率 (Open Rate)，进而伤害域名的送达信誉，导致邮件更容易进垃圾箱。这类人应该做专属的 Winback Flow。
3. ****发送给 (Send to)****
   - 建议发给 ****Engaged Segment****（例如：30-60 天内活跃用户），而非全员发送 (Open Blast)。

****5.4 成功标准 (Benchmark)****

不要只盯着发出去了多少封，看这两项：

- ****Open Rate (打开率)****：保持在 ****30% 以上**** 是健康标准。
- ****Unsubscribe Rate (退订率)****：如果单次发送退订率超过 ****0.3%****，说明你选错了人，或者频率太高。

#### ****DC Klaviyo方法论****

****——Klaviyo 事件 × Flow 触发 / 过滤「标准对照表（DC 版）」****

使用原则（一句话版）：

****Trigger 决定“为什么发”，Filter 决定“该不该发”。****

90% 的重复发送、骚扰用户，都是 Filter 没设计好。

##### ****一、事件使用总原则（先看这个）****

|  |  |
| --- | --- |
| ****类型**** | ****使用建议**** |
| Placed Order | 强转化信号，优先 Trigger |
| Started Checkout | 强意图信号，可 Trigger |
| Added to Cart | 中强意图，需配合 Filter |
| Viewed Product | 兴趣信号，慎 Trigger |
| Active on Site | 存在信号，只做 Filter |

****越靠后的事件，越不该单独触发 Flow****

##### ****二、核心 Flow 对照表（可直接照抄配置）****

****1️⃣ Welcome Flow****

|  |  |
| --- | --- |
| ****项目**** | ****配置**** |
| Trigger | Joined List（Master List） |
| 必加 Filter | Has not been in this flow |
| 推荐 Filter | Has not Placed Order |
| 绝对禁止 | 用 Active on Site / Viewed Product 触发 |

****Welcome 是“身份变化”，不是行为触发****

****2️⃣ Abandoned Cart Flow****

|  |  |
| --- | --- |
| ****项目**** | ****配置**** |
| Trigger | Added to Cart |
| 必加 Filter | Has not Placed Order since starting this flow |
| 推荐 Filter | Not in Checkout Abandon Flow |
| 推荐延迟 | 30分钟 |

⚠️ ****不加 Placed Order Filter = 重复发送重灾区****

****3️⃣ Checkout Abandonment Flow****

|  |  |
| --- | --- |
| ****项目**** | ****配置**** |
| Trigger | Started Checkout |
| 必加 Filter | Has not Placed Order |
| 推荐 Filter | Cart value ≥ X |
| 推荐延迟 | 30分钟 |

📌 ****Checkout Flow 优先级 > Cart Flow****

****4️⃣ Browse Abandonment Flow（进阶）****

|  |  |
| --- | --- |
| ****项目**** | ****配置**** |
| Trigger | Viewed Product |
| 必加 Filter | Has not Added to Cart |
| 推荐 Filter | Viewed Product ≥ 2 次 |
| 推荐延迟 | 12–24 小时 |

****单次浏览直接触发 = 干扰而非转化****

****5️⃣ Post-Purchase Flow****

|  |  |
| --- | --- |
| ****项目**** | ****配置**** |
| Trigger | Placed Order |
| 必加 Filter | None（谨慎） |
| 推荐 Filter | Order value ≥ X |
| 推荐延迟 | 即时 / 1 天 |

📌 ****这是“关系 Flow”，不是促销 Flow****

****6️⃣ Win-back Flow****

|  |  |
| --- | --- |
| ****项目**** | ****配置**** |
| Trigger | Segment Trigger |
| Segment 条件 | 60–90 天未 Placed Order |
| 推荐 Filter | 最近 30 天未 Active on Site |
| 推荐频率 | 极低（1–2 封） |

##### ****三、事件作为 Filter 的“标准用法”****

****1️⃣ Active on Site（只做 Filter）****

|  |  |
| --- | --- |
| ****用法**** | ****示例**** |
| 判断是否活跃 | Active on Site ≥ 1（7 天） |
| 判断沉默 | Active on Site = 0（30 天） |
| 防骚扰 | 最近 3 天无 Active on Site |

❌ ****禁止直接作为 Trigger****

2️⃣ ****Viewed Product（谨慎 Trigger）****

|  |  |
| --- | --- |
| ****用法**** | ****示例**** |
| 兴趣判断 | Viewed Product ≥ 2 |
| 类目兴趣 | Viewed Category = X |
| 排除条件 | 未 Added to Cart |

##### ****四、常见错误配置（务必规避）****

|  |  |
| --- | --- |
| ****错误**** | ****后果**** |
| 无 Placed Order Filter | 已下单用户被持续骚扰 |
| Cart & Checkout Flow 重叠 | 同一用户收多封 |
| Active on Site 触发 Flow | 噪音巨大，退订飙升 |
| Viewed Product 无频控 | 打断用户决策 |

##### ****五、DC 内部「事件使用优先级」****

1️⃣ Placed Order

2️⃣ Started Checkout

3️⃣ Added to Cart

4️⃣ Viewed Product

5️⃣ Active on Site

👉 ****信号越弱，越应该放在 Filter，而不是 Trigger****