# Mini Browser

一个基于 Python + PyQt5 + Chromium 的轻量级浏览器。

## 功能特性

- ✅ 基于 Chromium 内核（QtWebEngine）
- ✅ 前进/后退/刷新导航
- ✅ URL 地址栏（自动补全 https://）
- ✅ 加载进度条
- ✅ 状态栏显示
- ✅ 快捷键支持（F5 刷新，Esc 停止）
- ✅ 默认搜索引擎：Bing

## 安装依赖

```bash
pip install PyQt5 PyQtWebEngine
```

或者使用 requirements.txt：

```bash
pip install -r requirements.txt
```

## 运行

```bash
python browser.py
```

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| F5 | 刷新页面 |
| Esc | 停止加载 |

## 项目结构

```
minibrowser/
├── browser.py      # 浏览器主程序
├── requirements.txt # 依赖列表
├── cache/         # 缓存目录（自动生成）
└── storage/       # 存储目录（自动生成）
```

## 技术栈

- Python 3.x
- PyQt5
- QtWebEngine (Chromium)

## License

MIT