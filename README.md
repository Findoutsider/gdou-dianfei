# gdou-dianfei

广东海洋大学电费查询 Python 客户端

## 安装

```bash
pip install gdou-dianfei
```

## 使用

```python
from gdou_dianfei import EBClient

client = EBClient(username="学号", password="密码")
client.login()

# 获取空调电费余额
balance = client.get_ac_ele_balance()
print(f"余额: {balance.moneyBalance}元")

# 获取照明电费余额
light_balance = client.get_light_ele_balance()
print(f"照明余额: {light_balance.moneyBalance}元")
```

## License

MIT
