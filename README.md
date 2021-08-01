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
