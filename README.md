# 🚀 Easy Unraid - Client Download & Releases

[English](#english) | [中文说明](#中文说明)

---

## English

**Easy Unraid** is a sleek, modern, and powerful cross-platform client manager for Unraid servers, built with Flutter. It provides an intuitive user interface for monitoring server telemetry, managing Docker containers, virtual machines, local files, and securely connecting via SSH.

### 📥 Download Installation Packages

Please head over to the **[Releases](https://github.com/wlaosj/easy-unraid-releases/releases/latest)** page to download the latest build for your platform:

*   **🤖 Android**: Download the specific APK for your device architecture (`arm64` / `arm32` / `x86_64`).
*   **💻 macOS**: Download the standard `.dmg` image. Drag and drop to install.
*   **🔌 Windows**: Download the portable `.zip` archive. Extract and run `easy_unraid.exe`.

### 🛡️ Security & Privacy Auditable Core
We value the safety of your server. To guarantee absolute security:
*   All connection settings and credentials are strictly stored in your local system sandbox.
*   We do not use any cloud servers for telemetry or password logging.
*   Our core SSH, keypair generation, and execution modules are completely open-source and audited. Check out the open-source repository: **[easy-unraid-ssh](https://github.com/wlaosj/easy-unraid-ssh)**.

---

## 中文说明

**Easy Unraid** 是一款专为 Unraid 服务器设计的现代化、跨平台桌面与移动客户端管理器。它致力于提供极佳的交互视觉体验，帮助您轻松掌控服务器硬件状态、一键启动/停止 Docker 与虚拟机、远程管理文件并随时发起安全的终端会话。

### 📥 客户端下载通道

请前往本仓库的 **[最新发布 (Releases)](https://github.com/wlaosj/easy-unraid-releases/releases/latest)** 页面下载对应系统的安装包：

*   **🤖 安卓端 (Android)**：选择适配您设备架构的 APK 安装包（推荐下载 `arm64` 版本）。
*   **💻 苹果端 (macOS)**：下载 `.dmg` 磁盘映像文件，双击拖拽进应用程序文件夹即可使用。
*   **🔌 微软端 (Windows)**：下载 `.zip` 压缩包，解压后双击 `easy_unraid.exe` 启动。
*   **📱 苹果手机端 (iOS)**：目前正在准备上架 App Store 中，敬请期待。

### 🛡️ 极客安全背书与开源审计
我们把服务器的安全放在第一位：
*   **本地存储**：所有连接凭证和密钥对只保存在您本机的安全沙盒中。
*   **直连无中转**：App 仅与您填写的服务器 IP 进行内网/外网直连，绝不经过任何第三方云端。
*   **核心安全组件开源**：我们已将涉及 SSH 密码处理、密钥对生成、公钥注入的底层通信逻辑完全开源以接受全球审计，您可以访问核心安全仓库查看源码：**[easy-unraid-ssh](https://github.com/wlaosj/easy-unraid-ssh)**。
