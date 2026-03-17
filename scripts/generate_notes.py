#!/usr/bin/env python3
"""
督导会谈记录生成器
生成结构化的督导会谈记录文件，供治疗师保存和归档。

用法：
  python scripts/generate_notes.py
  python scripts/generate_notes.py --therapist "张三" --date "2026-03-15"
  python scripts/generate_notes.py --output "my_notes.md"
"""

import argparse
import os
from datetime import date


def generate_supervision_note(therapist_name: str, supervisor: str, session_date: str, output_path: str):
    content = f"""# 督导会谈记录

| 字段 | 内容 |
|------|------|
| 日期 | {session_date} |
| 治疗师 | {therapist_name} |
| 督导 | {supervisor} |
| 会谈时长 | _______ 分钟 |
| 督导形式 | □ 个人督导  □ 团体督导  □ 同伴督导  □ AI督导 |

---

## 一、呈报案例概要

**来访者基本信息**（仅用匿名代码，不记录可识别信息）

- 代号：_______
- 年龄段：_______  性别：_______
- 主要困扰：_______
- 治疗进行至第 _______ 次

**本次督导聚焦的议题：**

> （描述你今天最想讨论的核心问题）

_______________________________________________________________________

---

## 二、治疗师内部状态（督导前自我评估）

**在这个案例里，我此刻的感受是：**

- 情绪：_______
- 身体：_______
- 主要担忧：_______

**同盟状态评估（1–10）：** _______

**我认为治疗目前卡在：**
□ 同盟问题  □ 目标不一致  □ 疗法不匹配  □ 我自己的议题  □ 系统阻力  □ 不清楚

---

## 三、反移情记录

| 类型 | 我的反应 | 临床意义初步思考 |
|------|----------|-----------------|
| 互补性 | | |
| 和谐性 | | |
| 主观性 | | |
| 躯体性 | | |

---

## 四、案例概念化（督导中形成的理解）

**核心困境（一句话）：**

_______________________________________________________________________

**发展史/依恋视角：**

_______________________________________________________________________

**防御功能：**

_______________________________________________________________________

**来访者的力量与资源：**

_______________________________________________________________________

---

## 五、督导洞见与行动计划

**今天最重要的洞见：**

_______________________________________________________________________

**下次会谈我想尝试：**

_______________________________________________________________________

**需要继续思考的问题：**

_______________________________________________________________________

---

## 六、治疗师自我照顾检查

□ 我的工作量在可持续范围内
□ 这个案例没有引发替代性创伤的迹象
□ 我有足够的支持系统（同伴/督导/个人治疗）

**如果有信号，我的应对计划：**

_______________________________________________________________________

---

## 七、下次督导安排

- 日期：_______
- 拟讨论议题：_______

---

*本记录用于个人专业发展，请妥善保管，不包含来访者可识别信息。*
"""

    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"督导记录已生成：{output_path}")


def main():
    parser = argparse.ArgumentParser(description="生成督导会谈记录模板")
    parser.add_argument("--therapist", default="（治疗师姓名）", help="治疗师姓名")
    parser.add_argument("--supervisor", default="AI 督导", help="督导姓名")
    parser.add_argument("--date", default=str(date.today()), help="日期（YYYY-MM-DD）")
    parser.add_argument("--output", default=None, help="输出文件路径")
    args = parser.parse_args()

    if args.output is None:
        args.output = f"supervision_notes_{args.date}.md"

    generate_supervision_note(args.therapist, args.supervisor, args.date, args.output)


if __name__ == "__main__":
    main()
