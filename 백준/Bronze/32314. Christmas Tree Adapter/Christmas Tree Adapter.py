# 32314 Christmas Tree Adapter - 11월
tree_power = int(input())
watt_power, volt_power = map(int, input().split())
need_power = watt_power / volt_power
if tree_power <= need_power: print(1)
else: print(0)