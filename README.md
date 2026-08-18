<a name="readme-top"></a>

# 🚀 Easy Unraid

<p align="center">
  <img src="https://raw.githubusercontent.com/wlaosj/easy-unraid-ssh/main/logo.png" alt="Easy Unraid Logo" width="120" style="border-radius: 24px;"/>
</p>

<p align="center">
  <strong>一款简洁、优雅且安全的跨平台 Unraid 服务器管理器</strong>
</p>

<p align="center">
  <a href="https://flutter.dev"><img src="https://img.shields.io/badge/Platform-Flutter-blue.svg?style=flat-square&logo=flutter" alt="Flutter"/></a>
  <a href="https://github.com/wlaosj/easy-unraid-releases/releases"><img src="https://img.shields.io/badge/Build-GitHub%20Actions-brightgreen?style=flat-square&logo=github-actions" alt="Actions"/></a>
  <a href="https://github.com/wlaosj/easy-unraid-releases/releases/latest"><img src="https://img.shields.io/github/v/tag/wlaosj/easy-unraid-releases?style=flat-square&color=orange&label=Version" alt="Version"/></a>
  <a href="https://t.me/+7jcTMePlNVwwZjg1"><img src="https://img.shields.io/badge/Telegram-Group-2CA5E0?style=flat-square&logo=telegram&logoColor=white" alt="Telegram Group"/></a>
  <img src="https://img.shields.io/badge/OS-Android%20%7C%20macOS%20%7C%20Windows%20%7C%20iOS%20%7C%20Harmony-blueviolet?style=flat-square" alt="OS Support"/>
</p>

<p align="center">
  <img src="screenshots/feature_graphic.png" alt="Easy Unraid Features" width="800" style="border-radius: 16px;"/>
</p>

---

## 📌 目录 (Table of Contents)

<details open>
<summary><b>📖 点击展开/折叠目录大纲 (Click to Toggle)</b></summary>

*   **[🇨🇳 中文介绍](#intro-zh)**
    *   [✨ 核心功能亮点](#features-zh)
    *   [🚀 快速配对指南](#quick-start-zh)
    *   [🌐 外网安全访问建议](#remote-zh)
    *   [💎 免费版与专业版说明](#free-vs-pro-zh)
    *   [📥 客户端下载通道](#downloads-zh)
    *   [🛡️ 安全背书与极客审计](#security-zh)
*   **[🇺🇸 English Introduction](#intro-en)**
    *   [✨ Key Features](#features-en)
    *   [🚀 Quick Start Guide](#quick-start-en)
    *   [🌐 Remote Access & Security](#remote-en)
    *   [💎 Free vs Pro Edition](#free-vs-pro-en)
    *   [📥 Downloads](#downloads-en)
    *   [🛡️ Security & Privacy](#security-en)
*   **[📸 运行截图 (Screenshots)](#screenshots)**

</details>

---

<a name="intro-zh"></a>

## 🇨🇳 中文介绍

**Easy Unraid** 是一款基于 Flutter 构建的高性能、跨平台 Unraid 服务器管理客户端。突破传统浏览器访问限制，为移动设备与桌面端提供流畅、原生的硬件监控、应用商店检索、Docker 编排、插件一键升级、自托管 AI 智能相册与极速文件传输体验。

<a name="features-zh"></a>

### ✨ 核心功能亮点

- **📊 实时硬件监测与官方设计语言**
  - **官方矢量图标**：全量集成 Unraid 官方原生矢量图标体系，品牌爱马仕红橙（`#FF5D22`）点睛。
  - **优雅仪表盘**：采用苹果运动圆环与跑车高精仪表盘重绘 CPU、内存与硬件指标。
  - **错层防重叠**：指标卡片硬件 Logo 与高频折线波形错层隔离，排版清爽现代。
  - **主题切换**：支持仪表盘顶部一键无感切换深浅色主题。
- **🛒 Community Applications 官方社区应用商店 (PRO)**
  - **海量应用**：完整接入 Unraid 官方百万级社区应用商店，秒级检索与智能分类浏览。
  - **模版引擎**：深度解析原生 XML 容器模版，自动装配网络、端口映射、路径卷与环境变量。
- **🔌 插件全量检测与一键批量升级**
  - **静默检测**：后台静默检测 Unraid 已安装插件更新，多服务器沙盒物理隔离缓存。
  - **一键更新全部**：多插件可升级时动态浮现「全部更新 (Update All)」排队串行升级，避免安装锁死并提供实时合并日志流。
  - **版本对比与卸载**：支持多版本 Markdown 历史更新日志对比与一键安全卸载。
- **🧠 自托管 AI 智能相册 (PRO)**
  - **自研后端**：一键部署轻量级自托管 Docker 容器（`easy-unraid-photos`），支持 GPU 硬件加速。
  - **离线语义搜图**：纯本地运行多模态 CLIP 智能搜索引擎，中英文输入精准检索照片场景。
  - **离线人脸聚类**：纯本地人脸识别聚类算法，支持空闲内存超时自动回收，零云端隐私泄露。
  - **视频预览时长可配**：支持自由配置动态视频预览时长（关闭 / 3秒 / 5秒 / 10秒 / 15秒），关闭后 0 转码开销秒开原画。
  - **流畅动效**：支持 Pinch 双指网格捏合缩放、大图视差滑屏与 Hero 飞入，高刷 120Hz 极速贴手。
  - **智能直连加速**：局域网自动探活直连（LAN Bypass），外网自动回退安全加密 SSH 隧道。
- **🐳 Docker 容器与 Compose 编排 (PRO)**
  - **独立分立式控制栏**：移动端全新设计为纯净搜索框 + 商店高亮入口 + 快捷添加 + 更多菜单。
  - **来源元数据副标题**：智能识别原生模版、CA 商店、Compose 堆栈，卡片视图智能去重端口。
  - **一键更新**：独家支持点击角标一键重建并自动拉起更新容器。
  - **极客编排**：独家支持 Docker Compose 项目一键部署与 YAML 语法高亮编辑。
  - **直观监控**：集成容器 CPU/内存实时进度条与 Network/Disk IO 彩色流量胶囊。
- **💾 阳极氧化铝 3D 拟物化阵列面板**
  - **工业质感机箱**：阳极氧化冷银铝合金机箱前面板，绿光 LAN 指示灯高频闪烁。
  - **硬盘体检**：实时监测硬盘读写速度、工作温度、休眠状态及坏道 Errors 警告。
  - **三态判定**：SMART 状态重构为健康/未知/异常，自动过滤无 SMART 引导/虚拟盘。
- **📁 极速文件管理器与分享转存 (PRO)**
  - **断点续传**：基于极速 SFTP，大文件上传与下载支持暂停、继续和断线后自动重连续传。
  - **桌面拖拽**：macOS 独家支持直接向 App 窗口拖入文件/文件夹触发快速上传。
  - **秒开缓存**：内置 4K 媒体流播，针对 PDF 与图片引入专属本地磁盘缓存，二次打开秒开。
  - **分享转存**：iOS/Android 系统级分享扩展一键转存，智能记忆 4 条历史存储路径。
  - **防灾回收站**：内置独立物理回收站缓冲机制，误删文件可快速一键原路还原。
- **🚀 虚拟机控制与内置 SSH 终端 (PRO)**
  - **VNC控制**：支持虚拟机状态一键启停并内置 VNC 远程桌面控制台。
  - **终端卡片**：SSH 终端深度融入仪表盘快捷卡片，支持右键/长按菜单、剪贴板快捷粘贴（`Cmd/Ctrl+V`）。
  - **安全交互**：优化二次 PIN 码验证，进入终端时不触发输入框聚焦，防止与指纹面容弹窗冲突。
- **🔒 一键防爆破加固 (禁用 SSH 密码登录)**
  - **极客安全加固**：密钥配对成功后一键关闭 Unraid 的 SSH 密码登录通道，100% 免疫公网扫描与自动化暴力破解。
  - **断电持久生效**：配置安全固化至引导 U 盘（`/boot/config/ssh/sshd_config`），宿主机断电重启后永久生效。
- **🔋 UPS 备用电源监测**
  - **NUT适配**：全量适配第三方 NUT 插件（`nut-dw`），展示 UPS 实际功耗瓦数与预计续航。
  - **趋势折线**：新增 UPS 功耗历史趋势折线图，主界面解耦后台加载。
- **🎨 大屏黄金自适应与桌面集成**
  - **黄金自适应规范**：设置中心、新增容器与首次登录引导页在大屏下统一收敛为 `maxWidth: 820` 居中布局，彻底消除超宽屏过度拉伸。
  - **全量矢量去噪**：全面去除彩色 Emoji，统一为纯净、支持主题高亮的 `LucideIcons` 线性矢量图标。
  - **原生小组件**：支持 iOS/Android/macOS 三端原生桌面小组件，基于 App Group 共享沙盒实时数据同步。
  - **静默更新**：macOS 平台一键检测并静默自动完成解包、替换与新版自动重新拉起。

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="quick-start-zh"></a>

### 🚀 快速配对指南 (Quick Start)

首次运行 App 时，在系统配置页需要完成**连接模式配置**与**安全 SSH 密钥配对**：

#### 第一步：选择连接模式 (Connection Mode)
- **直连模式 (Direct Connection)**：推荐在【局域网内网】或【已连接 VPN（WireGuard, Tailscale, ZeroTier）】时使用，延迟最低、速度最快。
- **SSH 隧道穿透 (SSH Tunneling)**：推荐在【外网远程访问】且未开启 VPN 时使用。只需在路由器映射 SSH 端口，App 即可自动通过加密通道穿透 API 数据，实现 API 端口零暴露。

#### 第二步：进行安全 SSH 密钥配对 (SSH Pairing)
App 不在本地存储明文 root 密码。配对成功后统一走 RSA/ED25519 强加密 SSH 密钥对进行免密连接：
- **方式 A：自动免密注入（极简一步配对）**
  1. 输入服务器 IP 地址、端口及 `root` 账户密码。
  2. App 连通后自动生成 SSH 密钥对并写入服务器闪存，配对成功后**明文密码在内存中被物理抹除**。
- **方式 B：极客手动注入（推荐 - 100% 密码零接触）**
  1. 输入服务器 IP 地址及端口。
  2. 在 App 配置中生成或导入 SSH 密钥对，复制显示出的 **公钥 (Public Key)**。
  3. 登录 Unraid Web 管理页打开终端，将公钥内容追加到 `/boot/config/ssh/authorized_keys` 即可免密连接。

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="remote-zh"></a>

### 🌐 外网安全访问建议 (Remote Access)

为了服务器安全，在外网远程连接时**强烈建议使用 VPN 虚拟局域网隧道（如 WireGuard、Tailscale 或 ZeroTier）**，而非在路由器上直接暴露 API 与 SSH 端口。

> [!WARNING]
> **风险提示**：Easy Unraid 需要同时与 Unraid API（HTTP/HTTPS 端口）及 SSH 控制台（22 端口）建立连接。直接将管理端口映射到公网极易遭受暴力破解和扫描攻击。

> [!IMPORTANT]
> **公网 SSH 隧道安全黄金法则**：  
> 若您在外网环境下选择【SSH 隧道穿透】并在路由器上暴露了 SSH 端口，**在 App 首次配对成功后，请务必前往「设置 ➔ 安全」中开启「禁用 SSH 密码登录 (防爆破)」**。开启后 Unraid 将关闭密码与交互式认证，仅允许持有本设备私钥的客户端连接，彻底斩断公网黑客的自动化字典撞库与暴力破解通道。

> [!TIP]
> **VPN 隧道优势**：
> * **极致安全**：公网零暴露，核心端口安全隐蔽。
> * **配置一致**：接入局域网后，App 统一填写 Unraid **局域网内网 IP**（如 `192.168.31.99`）即可连接，无需为 API/SSH 单独设置公网端口。
> * **开箱即用**：Unraid 官方内置 WireGuard 支持；应用市场亦提供 Tailscale 和 ZeroTier 一键异地组网方案。

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="free-vs-pro-zh"></a>

### 💎 免费版与专业版说明 (Free vs Pro)

Easy Unraid 采用“基础核心功能永久免费，高级生产力工具付费激活”的模式，以保障项目的长期维护与迭代。

| 功能模块 | 免费版 (Free) | 专业版 (Pro) |
| :--- | :---: | :---: |
| **📊 实时硬件仪表盘** (CPU/内存/网速看板/官方矢量图标) | **✅ 免费** | **✅ 免费** |
| **💾 存储阵列监控** (磁盘空间/温度/坏道警告/3D拟物机箱) | **✅ 免费** | **✅ 免费** |
| **🔌 插件管理与检测** (插件更新检测/日志查看/单插件升级) | **✅ 免费** | **✅ 免费** |
| **⚙️ 基础系统配置** (多服务器配置/自动切换/820黄金自适应) | **✅ 免费** | **✅ 免费** |
| **🔒 SSH 隧道与安全双模连接** (直连/加密隧道) | **✅ 免费** | **✅ 免费** |
| **🛡️ 登录安全审计** (会话日志解析与图形化统计) | **✅ 免费** | **✅ 免费** |
| **🛒 Community Applications 应用市场** (CA 应用商店/XML 模版一键装配) | ❌ 需激活 | **✅ 解锁** |
| **📦 插件一键「全部更新」** (排队串行批量升级与日志合并) | ❌ 需激活 | **✅ 解锁** |
| **🧠 自托管 AI 智能相册** (离线 CLIP 搜图/人脸聚类/大图视差/预览时长可配) | ❌ 需激活 | **✅ 解锁** |
| **📁 极速文件管理器** (SFTP/4K 串流/压缩包解解压/拖拽上传/全局搜索) | ❌ 需激活 | **✅ 解锁** |
| **🗑️ 误删回收站保护** (物理回收站防灾缓冲) | ❌ 需激活 | **✅ 解锁** |
| **🐳 Docker 容器与 Compose 编排** (日志/一键更新/YAML 高亮/部署) | ❌ 需激活 | **✅ 解锁** |
| **🚀 虚拟机控制与 SSH 终端** (VM 控制/全功能终端/禁用密码登录) | ❌ 需激活 | **✅ 解锁** |

> [!TIP]
> **💡 授权政策：一次激活，全家共享，不限设备**  
> 专业版授权与 Unraid 服务器引导 U 盘唯一硬件 GUID 绑定（单授权最多可同时绑定 3 台服务器）。服务器激活后，所有连接该服务器的客户端设备（手机/平板/Mac/Windows）**均会自动解锁全部 PRO 专业功能**。购买与激活入口在 App 内 **「设置 ➔ 解锁专业版」**。

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="downloads-zh"></a>

### 📥 客户端下载通道

请前往 **[👉 最新发布页面 (Releases)](https://github.com/wlaosj/easy-unraid-releases/releases/latest)** 下载对应系统的安装包：

| 平台 | 格式 | 安装与使用说明 |
| :--- | :---: | :--- |
| **🤖 安卓端 (Android)** | `.apk` | 推荐下载 `arm64-v8a` 版本以获得最佳硬件加速性能。 |
| **💻 苹果端 (macOS)** | `.dmg` | 下载后双击打开，将 `Easy Unraid` 拖入 `Applications` 文件夹。 |
| **🔌 微软端 (Windows)** | `.zip` | 下载后解压，双击运行文件夹内的 `easy_unraid.exe`（免安装）。 |
| **📱 苹果手机端 (iOS)** | `TestFlight` | 🟢 **已开启公测！** 目前正处于苹果官方初审阶段，审核通过后将公布万能链接；亦可将 Apple ID 邮箱发给我们获取内测邀请。 |
| **🇨🇳 鸿蒙端 (HarmonyOS)** | `HAP / APP` | 纯血鸿蒙 (NEXT) 本地全链路已验证跑通。目前正处于技术适配阶段，等待官方发布支持 Dart 3.0+ 的 SDK。（注：HarmonyOS 4.x 及以下用户可直接下载运行 Android 64位安装包） |

---

### 💬 官方 Telegram 社区与交流群

欢迎加入官方 Telegram 交流群，参与功能讨论、BUG 提交与最新公测版体验：  
👉 **[点击加入 Easy Unraid 官方 Telegram 交流群](https://t.me/+7jcTMePlNVwwZjg1)**

---

<a name="security-zh"></a>

### 🛡️ 安全背书与极客审计

服务器的安全关乎您的数字资产生命。我们始终坚持“本地直连、安全透明”的极客开发原则：

- **密码零保留，物理层抹除**：App 不在本地保留明文 root 密码。配对成功后统一使用高安全性的 RSA/ED25519 强加密 SSH 密钥对进行免密连接。
- **核心通信组件 100% 开源审计**：所有涉及密钥对生成、密码配对与底层命令执行逻辑，均封装在我们的独立开源模块中，接受全球极客安全性审计：[easy-unraid-ssh 源码库](https://github.com/wlaosj/easy-unraid-ssh)。
- **纯本地直接连接，绝无云端中转**：App 仅与您填写的服务器 IP 直接通信，绝无云端中转服务器，也绝不收集流量日志。欢迎使用抓包工具进行审计。
- **敏感数据本地加解密与存储机制**：
  - **Android**：通过 Android Keystore 系统级硬件安全密钥库加密保护。
  - **iOS**：使用系统级安全钥匙串（Keychain）进行沙盒加密隔离存储。
  - **macOS (独立分发版)**：采用 App 独立隔离沙盒（SharedPreferences Sandbox）加密存储，防跨目录访问；未来商店版将支持 Keychain。
  - **Windows**：使用 Windows Credential & Registry 隔离沙盒物理存储。
- **🔒 一键防爆破加固与持久化机制 (100% 免疫公网暴力破解)**：
  - **加固原理**：在客户端成功建立私钥免密配对后，可直接在「设置 ➔ 安全」中一键开启「禁用 SSH 密码登录」。App 会自动更新 `/boot/config/ssh/sshd_config` 与 `/etc/ssh/sshd_config`，将密码验证及交互式认证彻底关闭（`PasswordAuthentication no`、`ChallengeResponseAuthentication no`、`KbdInteractiveAuthentication no`）并热重载 SSHD。
  - **开机与断电持久化**：由于配置写入了 Unraid 引导 U 盘闪存（`/boot/config/ssh/`），宿主机在经历系统更新、断电重启后，防爆破安全策略依然永久生效。
  - **极客应急还原指令**：若因换机或客户端设备丢失导致无法密钥登录，用户可随时登录 Unraid Web 终端（WebUI Terminal）执行单行指令秒级还原默认密码登录：
    ```bash
    sed -i 's/^PasswordAuthentication.*/PasswordAuthentication yes/g' /boot/config/ssh/sshd_config /etc/ssh/sshd_config && /etc/rc.d/rc.sshd restart
    ```

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="intro-en"></a>

## 🇺🇸 English

**Easy Unraid** is a sleek, modern, and powerful cross-platform manager for Unraid servers, built with Flutter. It breaks free from traditional browser limitations to provide you with a fluid, native experience for hardware telemetry, Community Applications, Docker & Compose management, plugin batch upgrades, self-hosted AI smart gallery, and high-speed SFTP file transfers.

<a name="features-en"></a>

### ✨ Key Features

- **📊 Real-time Telemetry with Official Unraid Design**
  - **Official Vector Icons**: Fully integrated with the official Unraid vector icon library and signature Hermes Orange (`#FF5D22`) accents.
  - **Activity Rings & Speedometers**: Cupertino-style activity rings and precision speedometers for CPU, RAM, and hardware telemetry.
  - **Separated Layering**: Shifted hardware logos and mini charts onto separate vertical layers to completely prevent chart-logo overlap.
  - **Theme Toggle**: Switch between Light and Dark mode seamlessly at the top bar.
- **🛒 Community Applications (CA) Store & Template Engine (PRO)**
  - **Vast Ecosystem**: Direct access to thousands of Unraid community applications with instant search and category filtering.
  - **XML Template Engine**: Seamless parsing of native XML container templates, automatically wiring network modes, port mappings, volume mounts, and environment variables.
- **🔌 Plugin Management & Batch Upgrades**
  - **Silent Background Detection**: Scans for installed Unraid plugin updates in the background with host-isolated caching.
  - **Batch "Update All" (PRO)**: Sequenced queue upgrades when multiple plugins have updates, featuring merged terminal output streams and safety locks.
  - **Changelog Comparison & Uninstallation**: Detailed multi-version Markdown changelog comparisons and safe one-click plugin uninstallation.
- **🧠 Self-Hosted Smart Gallery with Offline AI (PRO)**
  - **Lightweight Backend**: One-click deployment of custom Docker backend (`easy-unraid-photos`) with GPU hardware acceleration.
  - **Offline Semantic Search**: Integrated multi-modal CLIP AI engine for natural language scene and object searches completely on-device.
  - **Offline Face Clustering**: On-device facial recognition clustering with automatic memory timeout reclamation—100% private.
  - **Configurable Video Previews**: Customizable dynamic preview duration (Off / 3s / 5s / 10s / 15s) to eliminate transcoding overhead and stream raw original video instantly.
  - **Smooth Transitions**: Pinch-to-zoom timeline grids, parallax scrolling, Apple-style Hero transitions, and 120Hz smooth scrolling.
  - **LAN Bypass**: Bypasses SSH tunnel on local networks (LAN auto-probe) to maximize transfer speeds, falling back to secure tunnel on external WAN.
- **🐳 Docker & Compose Orchestration (PRO)**
  - **Separated Mobile Control Bar**: Clean independent search bar, CA store highlighted button, container creation, and more actions.
  - **Subtitle Metadata Identification**: Automatically classifies templates (Native / CA Store / Compose Stack) and eliminates duplicate port rendering.
  - **One-Click Updates**: Rebuild and update container binaries directly from card badges.
  - **Compose Editor**: Deploy Docker Compose projects with built-in YAML syntax highlight editor.
  - **Visual Statistics**: Dedicated CPU/RAM progress bars and colored IO traffic capsules.
- **💾 Anodized Aluminum 3D Array Panel**
  - **Skeuomorphic NAS Bezel**: Simulates a physical cold-silver aluminum rackmount bezel with green flickering LAN lights.
  - **Smart Warnings**: Real-time read/write speeds, temps, standby states, and bad sector warnings.
  - **Three-State Telemetry**: SMART diagnostics (Healthy/Unknown/Warning) while auto-omitting boot/virtual disks.
- **📁 Advanced File Manager & Share Extension (PRO)**
  - **Resumable Transfers**: SFTP upload/downloads with pause, resume, and auto-resuming on network drop.
  - **macOS Drag & Drop**: Native drag-and-drop file/folder transfers straight into the application window.
  - **Instant Preview**: Built-in 4K video streaming and dedicated disk caches for instant PDF/image reopening.
  - **Native Share Sheet**: iOS/Android system shares to Unraid with 4 recent path memories and App Group sandbox support.
  - **Delete Protection**: In-app physical recycle bin buffer with one-click recovery.
- **🚀 VM Power Control & SSH Terminal (PRO)**
  - **VM Management**: Control VM states with built-in in-app VNC console support.
  - **Embedded Terminal**: Integrated SSH terminal card with right-click context menus and `Cmd+V` / `Ctrl+V` pasting.
  - **Verification Polish**: Autofocus-free PIN screen preventing clashes with system biometric prompt.
- **🔒 One-Click Anti-Brute-Force Hardening**
  - **Geek Hardening**: Completely disable Unraid SSH password authentication with one tap after key pairing, ensuring 100% immunity against automated brute-force attacks.
  - **Persistent Across Reboots**: Security policies are permanently saved to your Unraid boot flash drive (`/boot/config/ssh/sshd_config`).
- **🔋 UPS Telemetry Integration**
  - **NUT Plugin**: Full integration for NUT plugin (`nut-dw`), presenting live wattage and estimated runtime.
  - **Power Sparklines**: Decoupled background telemetry loading with historical power trend line charts.
- **🎨 Standardized Layouts & Desktop Integration**
  - **maxWidth: 820 Constraint**: Settings, container installation, and onboarding welcome flows unified under a 820px centered layout to eliminate excessive widescreen stretching.
  - **Full Vectorization**: Clean Lucide linear vector icons replacing colored emojis across connection toggles and security guides.
  - **Home Screen Widgets**: Native iOS/Android/macOS widgets synced via App Group sandbox.
  - **Silent Updater**: MacOS background auto-extraction, replacing, and relaunching of binary updates.

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="quick-start-en"></a>

### 🚀 Quick Start Guide

During initial setup, configure the **Connection Mode** and establish an **SSH Pairing**:

#### Step 1: Choose Connection Mode
- **Direct Connection**: Recommended for [LAN Internal] or [VPN Connected (WireGuard, Tailscale, ZeroTier)] networks for lowest latency and best performance.
- **SSH Tunneling**: Recommended for [External Remote Access] without a VPN. By forwarding your Unraid SSH port on the router, the App automatically tunnels API traffic over SSH, keeping API ports hidden.

#### Step 2: Establish Secure SSH Pairing
The App never stores your root password in plaintext. Subsequent connections use secure RSA/ED25519 keypairs:
- **Mode A: Automatic Pairing**
  1. Enter server IP/domain, port, and `root` password.
  2. The App connects, generates an SSH keypair, and injects the public key into your Unraid flash drive. Password is **wiped from memory immediately**.
- **Mode B: Manual Setup (Recommended - 100% Password-free)**
  1. Enter server IP/domain and port.
  2. Generate or import an SSH keypair in App settings and copy the **Public Key**.
  3. Log in to Unraid WebGUI, open terminal, and append the public key to `/boot/config/ssh/authorized_keys`.

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="remote-en"></a>

### 🌐 Remote Access & Security Guide

To guarantee server safety, we **highly recommend using a VPN tunnel (such as WireGuard, Tailscale, or ZeroTier) for remote access**, rather than exposing API and SSH ports directly via port forwarding on your router.

> [!WARNING]
> **Security Notice**: Directly exposing core management ports (API and SSH port 22) to the public internet makes your server vulnerable to automated scanners and brute-force attacks.

> [!IMPORTANT]
> **Golden Rule for WAN SSH Tunneling**:  
> If you expose the SSH port to the public internet for 【SSH Tunneling】, **you MUST navigate to "Settings ➔ Security" and enable "Disable SSH Password Authentication (Anti-Brute-Force)" immediately after initial pairing**. Once enabled, Unraid rejects all password and keyboard-interactive authentication attempts, ensuring 100% immunity against automated dictionary and brute-force attacks.

> [!TIP]
> **VPN Tunnel Benefits**:
> * **Zero Public Exposure**: Keeps administration ports hidden behind encrypted gateways.
> * **Seamless Configuration**: Connect via your Unraid server's **local LAN IP** (e.g., `192.168.31.99`) in the App without configuring separate public ports.
> * **Built-in Options**: Unraid includes **built-in WireGuard support**, and community apps like **Tailscale** or **ZeroTier** can be deployed with one click.

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="free-vs-pro-en"></a>

### 💎 Free vs Pro Edition

Easy Unraid adopts a sustainable model: "Essential monitoring features are permanently free, while advanced productivity tools require a Pro activation".

| Feature | Free Edition | Pro Edition |
| :--- | :---: | :---: |
| **📊 Real-time Dashboard** (CPU/RAM/Network real-time stats & vector icons) | **✅ Free** | **✅ Free** |
| **💾 Array Monitor** (Disk utilization/temperatures/smart errors/3D Bezel) | **✅ Free** | **✅ Free** |
| **🔌 Plugin Manager** (Update checking/changelog view/single upgrade) | **✅ Free** | **✅ Free** |
| **⚙️ Server Configurations** (Multi-server switching & 820px layout) | **✅ Free** | **✅ Free** |
| **🔒 SSH Tunneling** (Direct and secure local port forwarding) | **✅ Free** | **✅ Free** |
| **🛡️ Security Audit Logs** (Login session auditing and metrics) | **✅ Free** | **✅ Free** |
| **🛒 Community Applications Store** (CA App Store & XML Template parser) | ❌ Pro Only | **✅ Unlocked** |
| **📦 Plugin "Update All" Batch Upgrade** (Queued background batch upgrades) | ❌ Pro Only | **✅ Unlocked** |
| **🧠 Smart Gallery** (Offline CLIP search, face clustering, preview config, LAN bypass) | ❌ Pro Only | **✅ Unlocked** |
| **📁 File Manager** (SFTP / 4K streaming / ZIP & TAR / Drag & Drop / Deep search) | ❌ Pro Only | **✅ Unlocked** |
| **🗑️ Safe Recycle Bin** (App-level delete protection) | ❌ Pro Only | **✅ Unlocked** |
| **🐳 Docker & Compose** (Logs/one-click updates/YAML editor/deployments) | ❌ Pro Only | **✅ Unlocked** |
| **🚀 VM & SSH Console** (Virtual machines/SSH terminal/Disable password auth) | ❌ Pro Only | **✅ Unlocked** |

> [!TIP]
> **💡 Sustainable Licensing Policy: One-Time Activation, Unlimited Clients**  
> The Pro license is directly bound to your Unraid server's unique Flash Drive GUID (supports up to 3 servers per license). Once activated, all client devices (phones, tablets, Mac, Windows) connecting to this server **automatically unlock all PRO features**. Activation is in the App under **"Settings ➔ Unlock Pro"**.

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="downloads-en"></a>

### 📥 Downloads

Visit the **[👉 Releases Page](https://github.com/wlaosj/easy-unraid-releases/releases/latest)** to download the installation package:

| Platform | Format | Installation & Usage Guide |
| :--- | :---: | :--- |
| **🤖 Android** | `.apk` | `arm64-v8a` is recommended for best hardware acceleration. |
| **💻 macOS** | `.dmg` | Double-click to open and drag `Easy Unraid` into your `Applications` folder. |
| **🔌 Windows** | `.zip` | Extract and double-click `easy_unraid.exe` to run (portable). |
| **📱 iOS** | `TestFlight` | 🟢 **Live on TestFlight!** Public link will be posted once Apple review completes. Email us your Apple ID for a direct invite. |
| **🇨🇳 HarmonyOS** | `HAP / APP` | HarmonyOS NEXT pipeline validated. Currently under adaptation for Dart 3.0+ SDK. (HarmonyOS 4.x users can download Android package directly) |

---

### 💬 Official Telegram Community & Support

Join our official Telegram community to chat with users and test preview builds:  
👉 **[Join Official Easy Unraid Telegram Group](https://t.me/+7jcTMePlNVwwZjg1)**

---

<a name="security-en"></a>

### 🛡️ Security & Privacy

* **Zero Password Storage**: Plaintext passwords are never saved. Connections rely on high-strength SSH keypair authentication.
* **Open-Source & Auditable**: Core SSH connector, keygen, and injection logic are open-source: [easy-unraid-ssh Repository](https://github.com/wlaosj/easy-unraid-ssh).
* **100% Direct Connection**: No telemetry, cloud servers, or data forwarding. Communicates directly with your server IP.
* **Sensitive Data Encryption**:
  * **Android**: Secured via hardware-backed Android Keystore.
  * **iOS**: Saved in secure System Keychain.
  * **macOS (Out-of-Store)**: Utilizes App Sandbox Local Encrypted Storage; transitions to System Keychain in App Store edition.
  * **Windows**: Encrypted within Windows Credential Manager & Registry.
* **🔒 One-Click Anti-Brute-Force Hardening & Persistence (100% Immunity)**:
  * **Mechanism**: Once SSH key pairing is established, toggle "Disable SSH Password Authentication" in "Settings ➔ Security". The App automatically updates `/boot/config/ssh/sshd_config` and `/etc/ssh/sshd_config` (`PasswordAuthentication no`, `ChallengeResponseAuthentication no`, `KbdInteractiveAuthentication no`) and reloads SSHD.
  * **Flash Drive Persistence**: Hardening configs are stored directly on the Unraid boot flash drive (`/boot/config/ssh/`), keeping the security policy active across OS upgrades, power cuts, and reboots.
  * **Emergency Rollback Command**: If you lose your client device, you can instantly restore default password authentication by running a single command in the Unraid WebGUI Terminal:
    ```bash
    sed -i 's/^PasswordAuthentication.*/PasswordAuthentication yes/g' /boot/config/ssh/sshd_config /etc/ssh/sshd_config && /etc/rc.d/rc.sshd restart
    ```

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>

---

<a name="screenshots"></a>

## 📸 运行截图 (Screenshots)

### 📊 实时硬件仪表盘 (Dashboard)
<p align="left">
  <img src="screenshots/Screenshot_2026-08-05-07-42-24-644_com.wlaosj.easy_unraid-edit.png" height="330" alt="Dashboard Overview"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="screenshots/Screenshot_2026-08-05-07-43-05-365_com.wlaosj.easy_unraid-edit.png" height="330" alt="Storage Details"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="screenshots/Screenshot_2026-08-05-07-43-39-158_com.wlaosj.easy_unraid-edit.png" height="330" alt="System Logs"/>
</p>

### 🐳 Docker 容器管理 (Docker & Compose)
<p align="left">
  <img src="screenshots/Screenshot_2026-08-05-07-43-21-014_com.wlaosj.easy_unraid-edit.png" height="330" alt="Docker Containers 1"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="screenshots/Screenshot_2026-08-05-07-43-28-830_com.wlaosj.easy_unraid-edit.png" height="330" alt="Docker Containers 2"/>
</p>

### 📁 极速文件管理器 (File Manager)
<p align="left">
  <img src="screenshots/Screenshot_2026-08-05-07-44-09-345_com.wlaosj.easy_unraid-edit.png" height="330" alt="File Browser"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="screenshots/Screenshot_2026-08-05-07-44-15-608_com.wlaosj.easy_unraid-edit.png" height="330" alt="Sidebar Navigation"/>
</p>

### 🐳 智能相册 (Smart Gallery)
<p align="left">
  <img src="screenshots/Screenshot_2026-08-05-07-45-33-076_com.wlaosj.easy_unraid-edit.png" height="330" alt="Smart Gallery Timeline"/>
</p>

<p align="right">(<a href="#readme-top">⬆️ 返回顶部 / Back to Top</a>)</p>
