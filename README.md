### AWs 成本优化小工具

**说明**

- Python环境为3
- 目前仅输出EC2运行实例及预留实例，不包含SPOT实例，亦不会跨账户统计

**使用方法**
1. 安装依赖
```bash
pip install -r requirements.txt
```

2. 指定区域运行
```bash
python calculate.py $region_name
```

**参考结果**

```bash
EC2 Calc:
Running Instances:
{'c5': 688, 'm5d': 368, 't3a': 163.5, 'r5d': 128, 'c5d': 292, 'r5': 28, 'r5a': 32, 'm5a': 136, 'i3en': 96, 'm6g': 4, 'r6g': 192, 'c6g': 10}
Reserved Instances:
{'r6g': 192, 'm5a': 192, 't3a': 192, 'r5a': 32, 'i3en': 96, 'c5': 960, 'c5d': 432, 'r5d': 128, 'm5d': 384, 'r5': 32}
```

输出结果为每种实例类型所使用之标准化因子，方便分析RI覆盖情况