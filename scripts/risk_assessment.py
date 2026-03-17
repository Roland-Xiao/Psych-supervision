#!/usr/bin/env python3
"""
自杀风险评估记录生成器
生成符合临床标准的自杀风险评估文档。

重要说明：本工具生成记录模板，不替代临床判断。
如来访者处于即时危险，请立即联系危机干预服务。

用法：
  python scripts/risk_assessment.py
  python scripts/risk_assessment.py --client "A001" --date "2026-03-15"
"""

import argparse
import os
from datetime import date


def generate_risk_assessment(client_code: str, therapist: str, assessment_date: str, output_path: str):
    content = f"""# 自杀风险评估记录

> ⚠️ 本文件含敏感临床信息，请加密存储，仅治疗师和督导可查阅。

| 字段 | 内容 |
|------|------|
| 评估日期 | {assessment_date} |
| 来访者代号 | {client_code} |
| 评估治疗师 | {therapist} |
| 评估场景 | □ 常规会谈  □ 危机接触  □ 随访评估 |

---

## 一、风险三维度评估

### 1. 意图（Intent）

**直接问法**："你有没有想过结束自己的生命？"

- □ 否认任何自杀意图
- □ 被动死亡愿望（"希望睡着不要醒来"）
- □ 主动自杀意念，无计划
- □ 主动自杀意念，有模糊计划
- □ 主动自杀意念，有具体计划

**区分关键**：想结束痛苦（逃离）vs. 想死（死亡意志）
记录来访者原话：
_______________________________________________________________________

### 2. 计划（Plan）

- □ 无具体计划
- □ 有方法，无时间/地点
- □ 有方法 + 时间或地点
- □ 有完整计划（方法+时间+地点）
- □ 已做准备（囤药/购买工具/写遗书）

**计划具体内容（如有）：**
_______________________________________________________________________

**致死性评估（该方法的致死可能性）：**
□ 低（如割腕）  □ 中  □ 高（如跳楼/枪支/大量药物）

### 3. 能力（Capability）

- 是否有获取手段的实际渠道：□ 是  □ 否  □ 不明
- 过去自杀尝试史：□ 无  □ 有，次数 _______，方式 _______
- 最近一次尝试日期：_______

> **注**：既往尝试史是未来风险的最强预测因子之一。

---

## 二、保护因素评估

| 保护因素 | 存在 | 强度（弱/中/强） | 备注 |
|----------|------|-----------------|------|
| 子女/家人依赖 | □ | | |
| 宗教/文化信仰 | □ | | |
| 社会支持网络 | □ | | |
| 对治疗的投入 | □ | | |
| 对未来的期待 | □ | | |
| 对死亡的恐惧 | □ | | |

---

## 三、综合风险等级

□ **低风险**：有意念，无计划，有保护因素，愿意承诺安全
□ **中风险**：有计划但无即时行动能力，或保护因素薄弱
□ **高风险**：有具体计划+获取手段+时间节点，或有近期尝试史
□ **即时危机**：正在实施或计划立即实施

---

## 四、干预行动记录

**本次采取的行动：**

□ 继续常规治疗，加强监控频率
□ 与来访者制定安全计划（见附件）
□ 通知紧急联系人（需知情同意，或危及生命可绕过）
□ 联系机构/主管督导
□ 转介住院或危机干预
□ 其他：_______

**安全计划核心内容：**

1. 预警信号（来访者识别）：_______
2. 内部应对策略：_______
3. 可联系的支持者：_______ 联系方式：_______
4. 危机热线：北京 010-82951332 / 全国 400-161-9995
5. 如无法控制：去最近急诊室
6. 治疗师联系方式（工作时间内）：_______

> **记住：安全计划是关系契约，不是法律合同。**
> 它之所以有效，是因为来访者不想让你失望。

---

## 五、督导与记录

- 本次评估是否已告知督导：□ 是  □ 否（说明原因）：_______
- 下次评估计划：_______
- 评估者签名：_______

---

*本评估记录遵循保密原则。危及生命情况下，治疗师有权在不征得同意的情况下联系相关方。*
"""

    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"风险评估记录已生成：{output_path}")
    print("⚠️  如来访者处于即时危险，请立即联系危机干预服务，不要只依赖本文件。")


def main():
    parser = argparse.ArgumentParser(description="生成自杀风险评估记录模板")
    parser.add_argument("--client", default="匿名来访者", help="来访者代号（勿用真实姓名）")
    parser.add_argument("--therapist", default="（治疗师）", help="治疗师姓名")
    parser.add_argument("--date", default=str(date.today()), help="评估日期（YYYY-MM-DD）")
    parser.add_argument("--output", default=None, help="输出文件路径")
    args = parser.parse_args()

    if args.output is None:
        args.output = f"risk_assessment_{args.client}_{args.date}.md"

    generate_risk_assessment(args.client, args.therapist, args.date, args.output)


if __name__ == "__main__":
    main()
