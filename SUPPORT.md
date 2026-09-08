# Easy Unraid (iOS & iPadOS)
## 官方技术支持与使用文档 / Official Support & Documentation

欢迎访问 **Easy Unraid (iOS & iPadOS)** 官方技术支持与帮助中心。  
Welcome to the official support and documentation page for **Easy Unraid** for iPhone and iPad.

---

## 📌 目录 / Table of Contents
- [🇨🇳 中文指南](#-中文指南)
  - [1. 核心功能概览](#1-核心功能概览)
  - [2. 快速配对与连接指南](#2-快速配对与连接指南)
  - [3. 常见连接排错 (FAQ)](#3-常见连接排错-faq)
  - [4. Pro 终身版与内购说明](#4-pro-终身版与内购说明)
  - [5. 隐私合规与服务条款](#5-隐私合规与服务条款)
  - [6. 联系技术支持](#6-联系技术支持)
- [🇬🇧 English Guide](#-english-guide)
  - [1. Key Features](#1-key-features)
  - [2. Quick Start & Connection Guide](#2-quick-start--connection-guide)
  - [3. Troubleshooting & FAQ](#3-troubleshooting--faq)
  - [4. Pro Lifetime & In-App Purchases](#4-pro-lifetime--in-app-purchases)
  - [5. Privacy & Terms](#5-privacy--terms)
  - [6. Contact Support](#6-contact-support)

---

## 🇨🇳 中文指南

### 1. 核心功能概览
**Easy Unraid** 是一款专为 Unraid 用户打造的高性能系统管理与监控客户端：
* **实时遥测看板**：官方爱马仕红橙设计语言，动态展示 CPU、内存负载、网络实时吞吐流量与阵列健康状态。
* **智能相册与云端备份**：自托管 AI 驱动的私有相册，支持本地 CLIP 语义搜图、人脸聚类与 iOS 动态照片 (Live Photo) 流畅播放。
* **极速文件管理器**：基于高吞吐 SFTP 协议，支持大文件上传下载、断点续传、文本代码编辑与 4K 媒体流播。
* **原生交互 SSH 终端**：内置全功能交互式 SSH 终端，支持命令快捷粘贴、常用脚本库与安全免密连接。
* **Docker 容器与虚拟机管理**：实时查看容器状态、资源占用曲线、一键重启/更新与日志流式回放。

---

### 2. 快速配对与连接指南

首次在 iPhone 或 iPad 上打开 Easy Unraid 时，只需简单两步即可完成配对：

#### 第一步：选择连接模式
1. **直连模式 (Direct Connection)**：
   * **适用场景**：iPhone / iPad 与 Unraid 处于同一局域网 Wi-Fi，或已开启 VPN 虚拟局域网（如 WireGuard / Tailscale）。
   * **配置方法**：填写 Unraid 的局域网 IP（例如 `192.168.31.99`）与 Web 管理端口（默认为 `80` 或 `443`）。
2. **SSH 隧道加密模式 (SSH Tunneling)**：
   * **适用场景**：在外网环境下远程访问，且路由器仅映射了 SSH 端口（例如 `22` 或自定义高位端口）。
   * **优势**：App 会自动通过本地加密 SSH 隧道中转所有数据，Web 管理端口零暴露，安全抗公网扫描。

#### 第二步：配置安全 SSH 密钥对
Easy Unraid 采用端到端加密设计，**密码仅保存在本地 iOS Keychain 硬件加密区**：
* 推荐在 App 中直接输入 `root` 账户与密码，App 将自动为当前设备生成强加密 ED25519/RSA 密钥对并注入 Unraid 闪存。
* 密钥配对成功后，后续所有连接均通过密钥验签，安全高效。

---

### 3. 常见连接排错 (FAQ)

#### Q1: 提示“连接超时”或“网络不可达”？
* 请确保 iOS 系统的「设置 ➔ Easy Unraid」中已授予**「本地网络 (Local Network)」**权限。
* 若使用域名或公网 IP，请检查路由器端口映射是否正常生效。

#### Q2: 切换 Wi-Fi 或蜂窝网络后连接断开？
* App 内置断线自动重连机制。进入后台或网络切换后，只需在首页下拉刷新，App 即可自动恢复会话。

---

### 4. Pro 终身版与内购说明

Easy Unraid 核心硬件概览与监控功能永久免费；高级生产力工具（智能相册、SFTP 文件传输、SSH 终端等）提供 Pro 终身版解锁。

* **官方 StoreKit 2 内购**：Pro 终身版完全通过 Apple 官方 App Store 应用内购买结算，安全可靠。
* **多宿主机支持**：同一个 Apple ID 购买后，最多支持绑定 3 台 Unraid 宿主机（基于引导优盘唯一硬件 GUID 绑定）。
* **恢复已购项目**：在任意登录同一 Apple ID 的 iPhone 或 iPad 上，进入「设置 ➔ Pro 授权」，点击**【恢复已购项目 (Restore Purchases)】**即可一键同步激活状态。
* **设备换绑与名额释放**：若更换 Unraid 宿主机或升级优盘，可在「设置 ➔ Pro 授权」点击**【注销当前设备授权】**释放云端名额，随后在新机器上点击【恢复购买】即可无缝迁移。

---

### 5. 隐私合规与服务条款
* **隐私政策 (Privacy Policy)**：[查看完整隐私政策](https://github.com/wlaosj/easy-unraid-releases/blob/main/PRIVACY.md)
* **标准使用条款 (EULA)**：[Apple 标准最终用户许可协议](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/)

---

### 6. 联系技术支持
如果您在使用过程中遇到任何问题，欢迎随时联系开发者团队：
* **技术支持邮箱**：[qq918652593@gmail.com](mailto:qq918652593@gmail.com)
* **问题反馈与建议**：[GitHub Issues 页面](https://github.com/wlaosj/easy-unraid-releases/issues)

---

## 🇬🇧 English Guide

### 1. Key Features
**Easy Unraid** is an iOS/iPadOS client crafted for Unraid server management:
* **Real-time Telemetry Dashboard**: CPU, memory, array health, and live throughput waveforms with clean modern design.
* **Smart Gallery & Auto Backup**: Self-hosted AI gallery with on-device CLIP semantic search and smooth Live Photo playback.
* **SFTP File Manager**: High-speed file transfers, pause/resume, in-app code editing, and 4K media streaming.
* **Interactive SSH Terminal**: Full-featured native shell with command clipboard utilities and secure key pairing.
* **Docker & VM Management**: Container status overview, resource usage charts, one-click rebuilds, and live logs.

---

### 2. Quick Start & Connection Guide

#### Step 1: Select Connection Mode
1. **Direct Connection**: Recommended when your device and Unraid are on the same Wi-Fi or connected via VPN (WireGuard / Tailscale). Enter your server's local IP and Web GUI port.
2. **SSH Tunneling**: Recommended for remote management where only the SSH port is exposed on your router. The App establishes an encrypted SSH tunnel for all API communications.

#### Step 2: Configure SSH Key Pairing
Easy Unraid stores credentials strictly inside the hardware-backed iOS Keychain:
* Enter your `root` password once; the App generates a secure ED25519/RSA key pair and injects the public key into your server.
* Once paired, all subsequent sessions authenticate securely via SSH keys.

---

### 3. Troubleshooting & FAQ

#### Q: "Connection Timeout" or "Host Unreachable"?
* Verify that **Local Network** permission is enabled in iOS Settings ➔ Easy Unraid.
* If connecting remotely, verify port forwarding rules on your gateway router.

#### Q: Network switched from Wi-Fi to Cellular?
* Pull down on the Dashboard screen to trigger an immediate reconnect.

---

### 4. Pro Lifetime & In-App Purchases
* **Official Apple StoreKit 2**: All Pro Lifetime upgrades are processed directly through Apple In-App Purchase.
* **Multi-Server License**: One Apple ID supports binding up to 3 Unraid servers (keyed to the boot USB GUID).
* **Restore Purchases**: On any new or additional iOS device under the same Apple ID, tap **Settings ➔ Pro License ➔ Restore Purchases** to sync your Pro status.
* **Rebind & Slot Release**: If you migrate your Unraid server to a new flash drive, tap **Deactivate Current Server** in Settings to release the license slot, then restore it on your new setup.

---

### 5. Privacy & Terms
* **Privacy Policy**: [Read Privacy Policy](https://github.com/wlaosj/easy-unraid-releases/blob/main/PRIVACY.md)
* **Terms of Use (EULA)**: [Apple Standard EULA](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/)

---

### 6. Contact Support
For inquiries, bug reports, or feature requests:
* **Support Email**: [qq918652593@gmail.com](mailto:qq918652593@gmail.com)
* **Community Feedback**: [GitHub Issues](https://github.com/wlaosj/easy-unraid-releases/issues)
