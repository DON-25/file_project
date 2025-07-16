# File Organizer 自动化文件整理工具

一个用于根据文件类型（图片、文档、压缩包等）自动整理目录中文件的 Python 工具。

---

## 功能特点

- 支持配置文件自定义分类规则
- 自动将文件按类型归类移动
- 支持多种文件扩展名
- 命令行一键运行

---

## 安装依赖

确保你已安装 Python 3.8+，然后运行：

```bash
pip install -r requirements.txt
```

## 项目结构说明
```
file_project/
├── config.json # 分类规则配置文件
├── config.py # 加载配置文件的函数
├── rules.py # 文件分类匹配规则模块
├── organizer.py # 核心文件整理逻辑
├── main.py # 主程序入口
├── requirements.txt # 依赖包说明
└── README.md # 项目说明文件
```

## 使用方法
运行主程序：
```
python main.py
```
程序将自动扫描当前目录中的所有文件，并根据配置文件将它们移动到对应的文件夹中。

## 整理效果示例
运行前：
```
file_project/
├── test.jpg
├── 报告.docx
├── archive.zip
```
运行后：
```
file_project/
├── 图片/
│   └── test.jpg
├── 文档/
│   └── 报告.docx
├── 压缩包/
│   └── archive.zip
```

## 单元测试
本项目使用 pytest 作为单元测试框架，测试覆盖了以下核心功能：
- config.py：配置加载与错误处理
- rules.py：文件扩展名匹配分类逻辑
- organizer.py：文件移动、异常、未匹配场景处理

测试文件目录结构：
```
tests/
├── test_config.py       # 测试配置文件加载
├── test_rules.py        # 测试规则匹配函数
├── test_organizer.py    # 测试整理逻辑
```

如何运行测试：
1.请确保你已经安装 pytest：
```
pip install pytest
```
2.在项目根目录下运行所有测试：
```
pytest tests
```
3.运行成功示例输出：
```
================= test session starts =================
collected 9 items

tests/test_config.py ....                         [33%]
tests/test_rules.py ....                          [66%]
tests/test_organizer.py ...                       [100%]

================== 9 passed in 0.05s ==================
```

