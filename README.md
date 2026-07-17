# 🚀 Easy Unraid

<p align="center">
  <img src="https://raw.githubusercontent.com/wlaosj/easy-unraid-ssh/main/lib/easy_unraid_ssh.dart" alt="Easy Unraid Logo" width="120" style="border-radius: 24px;"/>
</p>

<p align="center">
  <strong>一款简洁、优雅且安全的跨平台 Unraid 服务器管理器</strong>
</p>

<p align="center">
  <a href="https://flutter.dev"><img src="https://img.shields.io/badge/Platform-Flutter-blue.svg?style=flat-square&logo=flutter" alt="Flutter"/></a>
  <a href="https://github.com/wlaosj/easy-unraid-releases/releases"><img src="https://img.shields.io/badge/Build-GitHub%20Actions-brightgreen?style=flat-square&logo=github-actions" alt="Actions"/></a>
  <a href="https://github.com/wlaosj/easy-unraid-releases/releases/latest"><img src="https://img.shields.io/github/v/release/wlaosj/easy-unraid-releases?style=flat-square&color=orange" alt="Version"/></a>
  <img src="https://img.shields.io/badge/OS-Android%20%7C%20macOS%20%7C%20Windows%20%7C%20iOS-blueviolet?style=flat-square" alt="OS Support"/>
</p>

---

[中文介绍](#-中文介绍) | [English Introduction](#-english)

---

## 🇨🇳 中文介绍

**Easy Unraid** 是一款专为 Unraid 系统量身打造的跨平台客户端管理器。我们致力于打破传统的 WebUI 限制，为您在手机和电脑端提供丝滑的原生操作体验与精美的可视化监控看板。

### ✨ 核心功能亮点

*   **📊 实时硬件仪表盘**：直观的多色彩图表展示 CPU 负载、各核心温度、内存使用率、实时网速以及阵列读写状态。
*   **🐳 Docker 容器管理**：支持一键启动、停止、重启 Docker 容器，并可在 App 内直接查看容器的实时运行日志。
*   **💾 存储阵列掌控**：图表化展示磁盘空间使用率，实时读取各个硬盘的读写速度、工作温度以及健康坏道（Errors）监控。
*   **📁 极速文件管理器**：基于底层 SFTP 协议实现。支持文件与文件夹的浏览、删除、重命名；内置媒体流中转，支持音视频在线极速播放。
*   **🚀 虚拟机控制**：一键开启、关闭、重启 Unraid 内置的虚拟机服务。
*   **🛡️ 安全 SSH 终端**：内置全功能 SSH 终端控制台，支持多会话管理，让您随时随地进行深度服务器维护。

---

### 📥 客户端下载通道

请前往 **[👉 最新发布页面 (Releases)](https://github.com/wlaosj/easy-unraid-releases/releases/latest)** 下载对应系统的安装包：

| 平台 | 格式 | 安装说明 |
| :--- | :---: | :--- |
| **🤖 安卓端 (Android)** | `.apk` | 推荐下载 `arm64` 版本以获得最佳性能。 |
| **💻 苹果端 (macOS)** | `.dmg` | 下载后双击打开，将 `Easy Unraid` 拖入 `Applications` 文件夹即可。 |
| **🔌 微软端 (Windows)** | `.zip` | 下载后解压，双击运行文件夹内的 `easy_unraid.exe` 即可（免安装）。 |
| **📱 苹果手机端 (iOS)** | `App Store` | 正在苹果 App Store 上架审核中，敬请期待。 |

---

### 🛡️ 极客安全背书与开源审计

服务器的 root 权限关乎您的数据生命安全。为了让您百分之百放心，我们做出了以下安全防线设计：

> [!IMPORTANT]
> **1. 密码仅用一次，成功后物理抹除**  
> 首次配对时，App 在成功连接并将生成的安全公钥注入您的 Unraid 闪存后，**会立即在本地内存中物理抹除明文密码**，永久不进行本地存储。后续所有连接均走高安全强度的公钥私钥对免密登录。

> [!TIP]
> **2. 核心通信组件开源审计**  
> 所有的密钥生成、密码配对与命令执行逻辑，均封装在我们的独立开源模块中，接受全球极客的安全性审计。  
> 🔗 开源模块地址：[easy-unraid-ssh 源码库](https://github.com/wlaosj/easy-unraid-ssh)

> [!NOTE]
> **3. 纯本地直连，绝无云端中转**  
> App 在运行过程中仅与您填写的服务器 IP（内网直连或您的内网穿透域名）通信，绝对没有任何向第三方服务器上传密码、凭证或流量数据的分析代码。欢迎使用 `Charles` 或 `Wireshark` 等工具随时进行网络抓包审计。

---

## 🇺🇸 English

**Easy Unraid** is a sleek, modern, and powerful cross-platform client manager for Unraid servers, built with Flutter. It breaks free from browser limitations to provide you with a fluid, native experience on both mobile devices and desktops.

### ✨ Key Features

*   **📊 Real-time Dashboard**: Beautiful multi-color charts displaying CPU load, core temperatures, memory usage, real-time bandwidth, and array read/write status.
*   **🐳 Docker Management**: Start, stop, and restart Docker containers with one tap. View container logs directly in the app.
*   **💾 Storage Array Monitor**: Track disk utilization, read/write speeds, temperatures, and smart health errors in real-time.
*   **📁 Built-in File Manager**: High-speed file browsing, deleting, and renaming powered by SFTP. Stream media files directly from your server.
*   **🚀 VM Control**: Turn on, shut down, or restart your Unraid virtual machines.
*   **🛡️ Secure SSH Terminal**: Full-featured SSH console supporting multiple sessions for advanced server maintenance.

---

### 📥 Downloads

Please visit the **[👉 Releases Page](https://github.com/wlaosj/easy-unraid-releases/releases/latest)** to download the installation package:

*   **Android (`.apk`)**: Select the architecture match for your device (typically `arm64` is recommended).
*   **macOS (`.dmg`)**: Download, double click, and drag `Easy Unraid` into your `Applications` folder.
*   **Windows (`.zip`)**: Download, extract the archive, and double-click `easy_unraid.exe` to run.

---

### 🛡️ Security & Trust

Your server's root access is critical. We designed Easy Unraid with a security-first architecture:

*   **Zero Password Storage**: The root password is only used in memory for the initial session to inject the SSH key. Once verified, it is permanently wiped. Subsequent sessions rely entirely on RSA keypair authentication.
*   **Open-Source & Auditable**: The core SSH connector, keygen, and key injection logic are completely open-source. Inspect the code here: [easy-unraid-ssh Repository](https://github.com/wlaosj/easy-unraid-ssh).
*   **100% Direct Connection**: No telemetry, no backend servers, and no data forwarding. The client communicates directly with your server IP. Feel free to monitor the network traffic using any proxy tool.
