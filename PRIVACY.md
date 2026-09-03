# Easy Unraid 隐私政策 / Privacy Policy

最后更新日期：2026年9月3日 / Last Updated: September 3, 2026

欢迎使用 **Easy Unraid**（以下简称“本应用”）。本应用由独立开发者开发并维护，是一款专为 **Unraid OS**（家庭私有云 / NAS 平台）用户量身打造的移动运维管理工具。

我们深知个人隐私与数据安全对您的重要性。本应用坚持**“数据私有、零收集、本地直连”**的核心设计原则。在使用本应用前，请您仔细阅读本隐私政策。

Welcome to **Easy Unraid** ("the App"). The App is a dedicated mobile management utility designed for users of the **Unraid OS** (self-hosted NAS / home server platform). We are fully committed to protecting your privacy and ensuring your personal data remains 100% under your control.

---

## 1. 数据收集与隐私原则 / Data Collection & Principles

### 中文说明：
1. **数据零收集与不设中转服务器**：
   本应用不提供任何中心化的第三方云端存储服务器，不采集、不存储、不分析您的任何个人身份信息、浏览日志、私有文件或服务器配置。
2. **直连与点对点加密**：
   应用中所有的服务器遥测数据（CPU/内存/磁盘）、Docker 容器列表、虚拟机配置、相册媒体以及终端操作，**均通过直接 HTTP/HTTPS 或端到端 SSH 隧道在您的移动设备与您的 Unraid 宿主机之间直接通信**，绝无任何中间服务器窃听或中转。
3. **安全凭证本地保护**：
   您的 Unraid 登录密码、API Key、SSH 私钥及服务器配置仅存储在您设备的系统级安全硬件加密区（iOS Keychain / Android Keystore），绝不上报云端。

### English:
1. **Zero Data Collection**:
   The App does not operate any centralized backend servers to collect, track, or sell your personal information, server telemetry, or private files.
2. **Direct Peer-to-Peer Communication**:
   All communications—including hardware metrics, Docker/VM status, file browsing, photo sync, and terminal sessions—occur directly between your mobile device and your self-hosted Unraid server via direct HTTP/HTTPS or encrypted SSH tunnels.
3. **Local Credential Storage**:
   Your server credentials (passwords, API keys, and SSH private keys) are stored strictly inside your device's hardware-backed secure storage (iOS Keychain / Android Keystore).

---

## 2. 系统权限使用说明 / Device Permissions

为实现特定的管理功能，本应用在获得您的明确授权后可能会使用以下权限：

| 权限名称 / Permission | 使用场景与目的 / Purpose |
| :--- | :--- |
| **本地网络 (Local Network)** | 用于在局域网 Wi-Fi 环境下发现并与您的 Unraid 宿主机建立直接的 SSH/SFTP/GraphQL 连接。 |
| **系统相册 (Photo Library)** | 仅在您主动开启“智能相册备份”或浏览相册时使用，用于将手机照片安全备份至您私有的 Unraid 服务器中。 |
| **相机权限 (Camera)** | 仅用于扫描 Unraid Web 界面生成的二维码以快速填充服务器连接信息。 |
| **面容 ID / 指纹识别 (Face ID / Biometrics)** | 仅在设备本地用于 App 应用锁解锁，生物识别数据由 iOS/Android 操作系统安全隔离，应用无法获取。 |

---

## 3. 应用内购买与授权 / In-App Purchases & Licensing

### 中文说明：
1. 本应用的 Pro 终身版内购完全通过 **Apple App Store 官方 StoreKit** 渠道完成交易。我们不会接触、处理或保存您的信用卡、银行账户等任何敏感支付信息。
2. 在您成功购买后，苹果系统会生成加密的数字收据（Receipt）。本应用仅将该收据以及您当前连接的 Unraid 优盘物理 GUID 发送至云端授权验证节点（Cloudflare Worker），用于计算激活签名并在云端记录设备绑定名额（每个 Apple ID 最多绑定 3 台宿主机）。该过程不包含任何个人隐私信息。

### English:
1. In-App Purchases for Easy Unraid Pro Lifetime are processed directly through Apple's official StoreKit. We never see, process, or store your payment details or billing info.
2. Upon purchase, Apple generates an encrypted transaction receipt. The App transmits this cryptographic receipt along with your Unraid USB flash drive's physical GUID to our verification endpoint (Cloudflare Worker) to generate an offline activation signature and manage your 3-server license quota. No personal data is attached or stored.

---

## 4. 第三方服务与外链 / Third-Party Services & Links

本应用除 Apple StoreKit 支付系统和直接连接您指定的 Unraid 服务器外，不集成任何第三方广告 SDK、用户行为统计 SDK 或跟踪代码。

设置中提供的官方网站链接指向 GitHub 开源主页，用户访问 GitHub 遵守 GitHub 的自身隐私政策。

---

## 5. 联系我们 / Contact Us

如果您对本隐私政策或数据安全有任何疑问、意见或反馈，请通过以下方式与开发者取得联系：

* **GitHub 项目主页**：[https://github.com/wlaosj/easy-unraid-releases](https://github.com/wlaosj/easy-unraid-releases)
* **开发者邮箱**：[1006509988@qq.com](mailto:1006509988@qq.com)
