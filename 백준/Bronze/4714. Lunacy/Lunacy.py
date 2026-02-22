# 4714 Lunacy
while True:
  earth_weight = float(input())
  if earth_weight == -1.0: break
  moon_weight = earth_weight * 0.167
  print(f"Objects weighing {earth_weight:.2f} on Earth will weigh {moon_weight:.2f} on the moon.")