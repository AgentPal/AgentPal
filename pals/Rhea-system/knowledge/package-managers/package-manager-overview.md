# Package Manager Overview

包管理器选择原则：

- Windows 普通应用：优先 WinGet、Microsoft Store 或官方安装包。
- Windows CLI 工具：可考虑 Scoop，但要说明 PATH 和 shim 行为。
- Chocolatey 常涉及管理员权限，卸载自身需特别谨慎。
- macOS 开发工具：常见选择是 Homebrew 或官方安装包。
- Linux：先识别发行版，不假设一定是 apt。

任何包管理器动作都应说明来源、权限、影响范围和验证方式。

